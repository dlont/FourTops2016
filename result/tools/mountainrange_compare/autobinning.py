import ROOT as rt
import numpy as np
import array as ar
"""
Class interface for automatic histogram binning
"""

def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.

    see https://stackoverflow.com/questions/2413522/weighted-standard-deviation-in-numpy
    """
    average = numpy.average(values, weights=weights)
    # Fast and numerically precise:
    variance = numpy.average((values-average)**2, weights=weights)
    return (average, math.sqrt(variance))

def weighted_quantile(values, quantiles, sample_weight=None, values_sorted=False, old_style=False):
    """ Very close to numpy.percentile, but supports weights.
    see https://stackoverflow.com/questions/21844024/weighted-percentile-using-numpy
    NOTE: quantiles should be in [0, 1]!
    :param values: numpy.array with data
    :param quantiles: array-like with many quantiles needed
    :param sample_weight: array-like of the same length as `array`
    :param values_sorted: bool, if True, then will avoid sorting of initial array
    :param old_style: if True, will correct output to be consistent with numpy.percentile.
    :return: numpy.array with computed quantiles.
    """
    values = numpy.array(values)
    quantiles = numpy.array(quantiles)
    if sample_weight is None:
        sample_weight = numpy.ones(len(values))
    sample_weight = numpy.array(sample_weight)
    assert numpy.all(quantiles >= 0) and numpy.all(quantiles <= 1), 'quantiles should be in [0, 1]'

    if not values_sorted:
        sorter = numpy.argsort(values)
        values = values[sorter]
        sample_weight = sample_weight[sorter]

    weighted_quantiles = numpy.cumsum(sample_weight) - 0.5 * sample_weight
    if old_style:
        # To be convenient with numpy.percentile
        weighted_quantiles -= weighted_quantiles[0]
        weighted_quantiles /= weighted_quantiles[-1]
    else:
        weighted_quantiles /= numpy.sum(sample_weight)
    return numpy.interp(quantiles, weighted_quantiles, values)


from abc import ABCMeta, abstractmethod
class HistogramBinning:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_histogram(self):
        pass

class UniformBinning1D(HistogramBinning):
    """
    Uniform binning provider
    """
    def __init__(self,nbins,xmin,xmax):
        self._nbins = nbins
        self._xmin = xmin
        self._xmax = xmax
    
    def binning(self,**kwargs):
        self._nbins = kwargs.get('nbins',self._nbins)
        self._xmin = kwargs.get('xmin',self._xmin)
        self._xmax = kwargs.get('xmax',self._xmax)

    def get_histogram(self):
        return rt.TH1D("sample_hist","",self._nbins,self._xmin,self._xmax)

class EquiProbableBinning(HistogramBinning):
    """
    Provider of binning with equal probability per bin.
    """
    def __init__(self,vec,vecw=None,xmin=None,xmax=None):
        self._bin_edges = []
        if vecw: self._vec = zip(vec,vecw).sort()
        else self._vec = zip(vec,[1.]*len(vec)).sort()
        self._nbins = None
        self._xmin = None
        self._xmax = None

    @property
    def nbins(self): return self._nbins
    @nbins.setter
    def nbins(self, nbins):
        self._nbins=nbins
    @property
    def xmin(self): return self._xmin
    @xmin.setter
    def xmin(self, xmin): self._xmin=xmin
    @property
    def xmax(self): return self._xmax
    @xmax.setter
    def xmax(self, xmax): self._xmax=xmax

    @property
    def vec(self):
        return self._vec

    def binning(self):
        n_entries = 0
        if _vecw: n_entries = np.sum(_vecw)
        else: n_entries = len(self._vec)
        n_entries_per_bin = int(n_entries/self._nbins)
        current_entry = 0
        bin_edges_set = set()
        if self._xmax: bin_edges_set.add(self._xmax)
        else: bin_edges_set.add(self._vec[-1]+self._vec[-1]*0.001)
        for el in reversed(self._vec):
            current_entry+=1
            if current_entry > n_entries_per_bin:
                bin_edges_set.add(el)
                current_entry=0
        if self._xmin: bin_edges_set.add(self._xmin)
        else: bin_edges_set.add(self._vec[0]-self._vec[0]*0.001)
        self._bin_edges = list(bin_edges_set)
        self._bin_edges.sort()
        print "bins:", self._bin_edges

    def get_histogram(self,name='sample_hist'):
        self.binning()
        bin_edges = ar.array('d',self._bin_edges)
        return rt.TH1D(name,"",len(self._bin_edges)-1,bin_edges)

class OprimizedBinning(HistogramBinning):
    """
    Optimized binning provider.
    Theory behind optimality of equiprobable binning can be found
    in F.James "Statistical Methods in Experimental Physics" 2nd ed.
    Sec. 11.2.3. number of bins is determined according to eq. 11.8
    Alternative binning schemes: Sturges, Scott 
    (see https://en.wikipedia.org/wiki/Histogram#Number_of_bins_and_width)
    """
    def __init__(self,vec,vecw=None,xmin=None,xmax=None):
        self._lowstat_algo = 'fd'
        self._lowstat_thresh = 20
        self._vec=vec
        self._vecw=vecw
        self._xmin=xmin
        self._xmax=xmax
        self._bin_edges = []
        # Normal distr. 1% alpha-point lambda(0.01)
        self._lambda_alpha = 2.33
        # Normal distr. (1-p0) alpha point, when p0=0.8. 
        # Prob to accept H0, when false is 1-p0
        self._lambda_false_positive = 0.84
        #b parameter can be between 2 and 4 (b=4 for simple hypothesis, i.e. no free parameters)
        self._b = 2

    @property
    def vec(self):
        return self._vec
    @vec.setter
    def vec(self, vec):
        self._vec=vec

    def get_n_bins_fd(self):
        self._lowstat_algo='fd'
        n_entries = 0
        if _vecw: n_entries = np.sum(_vecw)
        else: n_entries = len(self._vec)
        self._vec.sort()
        irq = np.subtract(*weighted_quantile(self._vec, [75, 25],vecw,False,True))
        min,max=self._vec[0][0],self._vec[-1][0]
        bin_width = 2.*irq/(n_entries)**(1./3.)
        nbins = (max - min)/bin_width
        print "FD: ", nbins
        return int(nbins)

    def get_n_bins_scott(self):
        self._lowstat_algo='scott'
        n_entries = 0
        if _vecw: n_entries = np.sum(_vecw)
        else: n_entries = len(self._vec)
        print self._vec
        self._vec.sort()
        sigma = weighted_avg_and_std(self._vec,self._vecw)
        min,max=self._vec[0][0],self._vec[-1][0]
        bin_width = 3.5*sigma/(n_entries)**(1./3.)
        print sigma,n_entries,self._vec
        nbins = (max - min)/bin_width
        print "Scott: ", nbins
        return int(nbins)

    def get_n_bins_sturges(self,n_entries):
        self._lowstat_algo='sturge'
        nbins = 1+rt.TMath.Log2(n_entries)
        print "Sturges: ", nbins
        return int(nbins)

    def get_n_bins_james(self,n_entries):
        self._lowstat_algo='james'
        #eq. 11.8 from F.James
        num = self._b*2.**0.5*(n_entries-1)**(2./5.)
        den = (self._lambda_alpha+self._lambda_false_positive)**(2./5.)
        nbins = int(num/den)
        print "James: ", nbins
        return nbins

    def get_histogram(self,name='sample_hist'):
        self.binning()
        bin_edges = ar.array('d',self._bin_edges)
        return rt.TH1D(name,"",len(self._bin_edges)-1,bin_edges)

    def binning(self,**kwargs):
        self._lowstat_algo = kwargs.get('lowstat_algo',self._lowstat_algo)
        self._lambda_alpha = kwargs.get('lambda_alpha',self._lambda_alpha)
        self._lambda_false_positive = kwargs.get('lambda_false_positive',self._lambda_false_positive)
        self._b = kwargs.get('b',self._b)
        
        #sort in ascending order for empirical cdf
        self._vec.sort()

        n_entries = 0
        if _vecw: n_entries = np.sum(_vecw)
        else: n_entries = len(self._vec)
        nbins = None
        if n_entries<self._lowstat_thresh:
            if self._lowstat_algo == 'sturge': nbins = self.get_n_bins_sturges(n_entries) 
            elif self._lowstat_algo == 'fd': nbins = self.get_n_bins_fd()
            elif self._lowstat_algo == 'scott': nbins = self.get_n_bins_scott()
            elif self._lowstat_algo == 'james': nbins = self.get_n_bins_james(n_entries)
            else: print "Error!"
        else:
            nbins = self.get_n_bins_james(n_entries)
        n_entries_per_bin = int(n_entries/nbins)
        current_entry = 0
        bin_edges_set = set()
        if self._xmax: bin_edges_set.add(self._xmax)
        else: bin_edges_set.add(self._vec[-1]+self._vec[-1]*0.01)
        for el in reversed(self._vec):
            current_entry+=1
            if current_entry > n_entries_per_bin:
                bin_edges_set.add(el)
                current_entry=0
        if self._xmin: bin_edges_set.add(self._xmin)
        else: bin_edges_set.add(self._vec[0])
        self._bin_edges = list(bin_edges_set)
        self._bin_edges.sort()
        print "bins:", self._bin_edges
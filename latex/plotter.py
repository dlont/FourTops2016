import logging

from ROOT import TFile
from ROOT import TCanvas
from ROOT import TPad
from ROOT import TH1
from ROOT import TObject
from ROOT import THStack
from ROOT import TLegend
from ROOT import TAxis

TH1.__init__._creates = False
THStack.__init__._creates = False
TPad.__init__._creates = False
TCanvas.__init__._creates = False
TLegend.__init__._creates = False

from pprint import pprint,pformat

from progress_bar import progress


class plotter:
	"""
	Binned comparison plotting tool
	"""	

	def __init__(self, **kwargs):
		self.infolder=kwargs['inputfolder']
		return

	def make_header(self,f):
		"""
		decorate_page
		"""
		
		header = "\\begin{figure}[htpb!]\n"
		f.write(header)
		return

	def make_footer(self,f):
		"""
		decorate_page
		"""

		footer = "\\end{figure}\n"
		f.write(footer)
		return

	def make_caption(self,f,caption,label):
		"""
		decorate_page
		"""

		cap = "\\caption{{{}}}\\label{{{}}}\n".format(caption, label)
		f.write(cap)
		return

	def decorate_pad(self, pad, stack, gPad):
		"""
		decorate_pad
		"""
		return

	def make_pad(self, plot):
		"""
		make_pad
		"""
		logging.debug(pformat(plot))
	      	#self.decorate_pad(pad_tup[1], st, gPad)
	      	return

	def make_pads(self,subfigs,nx,ny):
		"""
		make_pads
		"""
		result = "\\centering\n"
		for i,plot in enumerate(subfigs):
			widthfraction=1./float(nx)
			angle=None
			if plot['angle']: angle=plot['angle']
			plotwidth=1./float(nx)
			plotheight=None
			plotfile = self.infolder +"/"+ plot['file']
			plotparams = 'angle={}'.format(plot['angle'])
			if plotwidth: plotparams += ', width={}'.format(str(plotwidth)+'\\textwidth')
			if plotheight: plotparams += ', height={}'.format(str(plotheight)+'\\textwidth')
			result += "\subfloat[]{{ \includegraphics[{}]{{{}}} }}".format(plotparams,plotfile)
			result += "\n"
			if divmod(i+1, nx)[1]== 0 and i != len(subfigs)-1: result += "\\\\ \n"
		return result

	def make_pages(self,pages_config):
		"""
		make_page
		"""
		pages = pages_config['pages']
		i, total = (0, len(pages))
		for page in pages:
			##############################
			progress(i, total, 'Progress')
			i += 1
			#############################
			with open(page['name'],'w') as f:
				self.make_header(f)
				f.write(self.make_pads(page['subfloats'],page['nx'],page['ny']))
				self.make_caption(f, page['caption'], page['label'])
				self.make_footer(f)
	  		#self.decorate_page(root_canvas,c)
	  	return

	def make_stackplot(self, pad, gPad):
		"""
		make_stackplot
		"""

		return st

	def make_stackplot_ratio(self, pad, gPad):
		"""
		make_ratio_stackplot
		"""

		logging.debug(pformat(pad))
		return st

	def set_hist_style(self, hist, style):
		""" Set style """
		return


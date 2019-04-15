"""
Calculate systematic variation templates from reweighted events based on 
NNPDF replicas
"""

import argparse
import logging
import time
import sys
import imp
import ROOT as rt
from multiprocessing.dummy import Pool as ThreadPool

__version__ = "1.0"
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

rt.TCanvas.__init__._creates = False
rt.TFile.__init__._creates = False
rt.TH1.__init__._creates = False
rt.TH2.__init__._creates = False
rt.THStack.__init__._creates = False
rt.TGraph.__init__._creates = False
rt.TMultiGraph.__init__._creates = False
rt.TList.__init__._creates = False
rt.TCollection.__init__._creates = False
rt.TIter.__init__._creates = False

def cut_nnpdf(cut_string,search_scheme='9J3M,10J3M'):
	from centralweight import centralweight
	cut_baseline = [
	#PDF UP
	#("allSF_PDFUp", "inclusive",  "(1 {0})*{1}".format(cut_string,centralweight)),

	#("6J2M_PDFUp", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})".format(cut_string,centralweight)),
	#("6J3M_PDFUp", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})".format(cut_string,centralweight)),
	#("6J4M_PDFUp", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})".format(cut_string,centralweight)),
	("7J2M_PDFUp", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})".format(cut_string,centralweight)),
	("7J3M_PDFUp", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})".format(cut_string,centralweight)),
	#("7J4M_PDFUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})".format(cut_string,centralweight)),
	#("8J2M_PDFUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})".format(cut_string,centralweight)),
	#("8J3M_PDFUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})".format(cut_string,centralweight)),
	#("8J4M_PDFUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})".format(cut_string,centralweight)),
	#("9J2M_PDFUp", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})".format(cut_string,centralweight)),
	#("10J2M_PDFUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})".format(cut_string,centralweight)),
	#PDF DOWN
	#("allSF_PDFDown", "inclusive",  "(1 {0})*{1}".format(cut_string,centralweight)),

	#("6J2M_PDFDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	#("6J3M_PDFDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#("6J4M_PDFDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	("7J2M_PDFDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	("7J3M_PDFDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#("7J4M_PDFDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	#("8J2M_PDFDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	#("8J3M_PDFDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#("8J4M_PDFDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	#("9J2M_PDFDown", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	#("10J2M_PDFDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	]
	#if search_scheme == '9J3M,10J3M':
	#	cut_baseline += [
	#		("9J3M_PDFUp", "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
	#		("10J3M_PDFUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
	#		("9J3M_PDFDown", "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
	#		("10J3M_PDFDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
	#	]
	#elif search_scheme == '9J4M,10J4M':
	#	cut_baseline += [
	#		("9J3M_PDFUp", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#		("9J4M_PDFUp", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	#		("10J3M_PDFUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#		("10J4M_PDFUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	#		("9J3M_PDFDown", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#		("9J4M_PDFDown", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	#		("10J3M_PDFDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#		("10J4M_PDFDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	#	]
	return cut_baseline

def make_up_and_down_histograms_unpack(args):
	make_up_and_down_histograms(*args)

def make_up_and_down_histograms(config,histogram_draw_options,tree,output_file):

	if not output_file:
		raise RuntimeError("Output file is not ready")

	folder_name = histogram_draw_options[0]
	folder_title = histogram_draw_options[1]
	histogram_name = config.target
	histogram_baseline_cuts  = histogram_draw_options[2]
	histogram_template       = config.custom_binning[config.target][folder_name.split('_')[0]][0]

	output_file.cd(folder_name)
	print folder_name,histogram_name,output_file
	print histogram_baseline_cuts
	print histogram_template

	temp_hist_name = 'temp_central'
	temp_hist_central = histogram_template.Clone(temp_hist_name)
	tree.Draw(config.target+'>>'+temp_hist_name,histogram_baseline_cuts)
	temp_hist_name = 'temp_std'
	temp_hist_std = histogram_template.Clone(temp_hist_name)
	temp_hist_std.Reset()

	variations_histograms = []
	for ivar in range(0,101):
		nnpdfweight = 'pdf_nnpdf[{}]'.format(ivar)
		temp_hist_name = 'temp_'+nnpdfweight
		temp_hist = histogram_template.Clone(temp_hist_name)
		rt.SetOwnership(temp_hist,True)
		logging.debug(nnpdfweight)
		tree.Draw(config.target+'>>'+temp_hist_name,histogram_baseline_cuts+'*'+nnpdfweight,'goff')
		variations_histograms.append(temp_hist)

	for ibin in range(1,temp_hist_central.GetNbinsX()):
		std = 0.
		for h in variations_histograms:
			std = (temp_hist_central.GetBinContent(ibin) - h.GetBinContent(ibin))**2.
		std /= len(variations_histograms)-1.
		if 'Up' in folder_name: temp_hist_std.SetBinContent(ibin,temp_hist_central.GetBinContent(ibin)+std)
		if 'Down' in folder_name: temp_hist_std.SetBinContent(ibin,temp_hist_central.GetBinContent(ibin)-std)
	
	temp_hist_std.SetName('bdt')
	temp_hist_std.SetDirectory(dir)
	temp_hist_std.Write()

def main(arguments,config):
        # Disable garbage collection for this list of objects
        rt.TCanvas.__init__._creates = False
        rt.TFile.__init__._creates = False
	rt.TH1.__init__._creates = False
	rt.TH2.__init__._creates = False
        rt.THStack.__init__._creates = False
        rt.TGraph.__init__._creates = False
        rt.TMultiGraph.__init__._creates = False
        rt.TList.__init__._creates = False
        rt.TCollection.__init__._creates = False
	rt.TIter.__init__._creates = False

	root_file = rt.TFile.Open(config.inputfile)
	if not root_file:
		raise RuntimeError("Cannot open file: {}".format(config.inputfile))
	root_tree = root_file.Get(config.tree_name)
	if not root_tree:
		raise RuntimeError("Cannot retrieve tree: {} from file {}".format(config.tree_name,config.inputfile))
	
	root_output_file = rt.TFile.Open(config.output_filename,'RECREATE')

	list_of_cuts = cut_nnpdf('&&'+config.trigger_cuts,config.binning_option)
	root_output_file.cd()
	for cut in list_of_cuts:
		folder_name = cut[0]
		folder_title = cut[1]
		root_output_file.mkdir(folder_name,folder_title)

	list_of_arguments = []
	for item in list_of_cuts:
		list_item = [config,item,root_tree,root_output_file]
		list_of_arguments.append(tuple(list_item))
		print list_item

	threads = 2
	pool = ThreadPool(threads)
    	pool.map(make_up_and_down_histograms_unpack, list_of_arguments)
    	pool.close()
    	pool.join()

	root_output_file.Write()
	root_output_file.Close()	
	

if __name__ == '__main__':
        start_time = time.time()

        parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('config',help="tree2hist configuration file config_t2h.py")
	parser.add_argument('inputfile',help="Input craneen files")
	parser.add_argument('output_filename',help="Output histogram file")
	parser.add_argument('tree_name',help="Craneen tree name")
	parser.add_argument('scalefactor',help="Effective luminosity scale factor")
	parser.add_argument('systematic',help="Systematic source name")
	parser.add_argument('target',help="Observable for which histograms must be produced")
        parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
	parser.add_argument('-b', help="ROOT batch mode", dest='isBatch', action='store_true')
        #parser.add_argument('--no-batch', help="ROOT batch mode", dest='isBatch', action='store_false', default=True)
        parser.add_argument(
                        '-d', '--debug',
                        help="Print lots of debugging statements",
                        action="store_const", dest="loglevel", const=logging.DEBUG,
                        default=logging.WARNING,
                        )
        parser.add_argument(
                        '-v', '--verbose',
                        help="Be verbose",
                        action="store_const", dest="loglevel", const=logging.INFO,
                        )

        args = parser.parse_args(sys.argv[1:])
	
	sys.path.append('.')
	f, path, desc = imp.find_module(args.config.strip(".py"), ["."])
	configuration_module = imp.load_module("config", f, path, desc)

        print(args)

        logging.basicConfig(level=args.loglevel)

        logging.info( time.asctime() )
        exitcode = main(args,configuration_module)
        logging.info( time.asctime() )
        logging.info( 'TOTAL TIME IN MINUTES:' + str((time.time() - start_time) / 60.0))
	sys.exit(exitcode)



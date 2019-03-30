"""
Calculate systematic variation templates from reweighted events based on 
NNPDF replicas
"""

import argparse
import logging
import time
import sys
import imp

__version__ = "1.0"
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

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
	("7J4M_PDFUp", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})".format(cut_string,centralweight)),
	("8J2M_PDFUp", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})".format(cut_string,centralweight)),
	("8J3M_PDFUp", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})".format(cut_string,centralweight)),
	("8J4M_PDFUp", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})".format(cut_string,centralweight)),
	("9J2M_PDFUp", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})".format(cut_string,centralweight)),
	("10J2M_PDFUp", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})".format(cut_string,centralweight)),
	#PDF DOWN
	#("allSF_PDFDown", "inclusive",  "(1 {0})*{1}".format(cut_string,centralweight)),

	#("6J2M_PDFDown", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	#("6J3M_PDFDown", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#("6J4M_PDFDown", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	("7J2M_PDFDown", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	("7J3M_PDFDown", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	("7J4M_PDFDown", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	("8J2M_PDFDown", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	("8J3M_PDFDown", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	("8J4M_PDFDown", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	("9J2M_PDFDown", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	("10J2M_PDFDown", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_baseline += [
			("9J3M_PDFUp", "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
			("10J3M_PDFUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
			("9J3M_PDFDown", "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
			("10J3M_PDFDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_baseline += [
			("9J3M_PDFUp", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
			("9J4M_PDFUp", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
			("10J3M_PDFUp", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
			("10J4M_PDFUp", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
			("9J3M_PDFDown", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
			("9J4M_PDFDown", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
			("10J3M_PDFDown", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
			("10J4M_PDFDown", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
		]
	return cut_baseline

def make_up_and_down_histograms(config,histogram_draw_options,tree,output_file):
	folder_name = histogram_draw_options[0]
	histogram_name = config.target
	histogram_baseline_cuts  = histogram_draw_options[2]
	histogram_template       = config.custom_binning[config.target+'1'][folder_name.split('_')[0]][0]
	
	print folder_name,histogram_name,output_file
	print histogram_baseline_cuts
	print histogram_template

	temp_hist_name = 'temp_central'
	temp_hist = histogram_template.Clone(temp_hist_name)
	tree.Draw(config.target+'>>'+temp_hist_name,histogram_baseline_cuts+'*'+nnpdfweight)

	variations_histograms = []
	for ivar in range(0,101):
		nnpdfweight = 'pdf_nnpdf[{}]'.format(ivar)
		temp_hist_name = 'temp_'+nnpdfweight
		temp_hist = histogram_template.Clone(temp_hist_name)
		logging.debug(nnpdfweight)
		#tree.Draw(config.target+'>>'+temp_hist_name,histogram_baseline_cuts+'*'+nnpdfweight,'goff')
		tree.Draw(config.target+'>>'+temp_hist_name,histogram_baseline_cuts+'*'+nnpdfweight)
		variations_histograms.append(temp_hist)
		answer = raw_input("Do you want to continue [y/N]? ")
		if answer == 'y': pass
		elif answer == 'N': sys.exit(0)
	

def main(arguments,config):
	import ROOT as rt


	root_file = rt.TFile.Open(config.inputfile)
	if not root_file:
		raise RuntimeError("Cannot open file: {}".format(config.inputfile))
	root_tree = root_file.Get(config.tree_name)
	if not root_tree:
		raise RuntimeError("Cannot retrieve tree: {} from file {}".format(config.tree_name,config.inputfile))
	

	for item in cut_nnpdf('&&'+config.trigger_cuts,config.binning_option):
		make_up_and_down_histograms(config,item,root_tree,None)
		

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
        parser.add_argument('--no-batch', help="ROOT batch mode", dest='isBatch', action='store_false', default=True)
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



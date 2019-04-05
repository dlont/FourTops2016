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

def cut_nnpdf(cut_string,search_scheme='9J3M,10J3M'):
	from centralweight import centralweight
	cut_baseline = [
	#PDF UP
	#("allSF_TTJets_PDFUp", "inclusive",  "(1 {0})*{1}".format(cut_string,centralweight)),

	#("6J2M_TTJets_PDF", "Njet=6, nMtags=2",  "(nJets==6 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	#("6J3M_TTJets_PDF", "Njet=6, nMtags=3",  "(nJets==6 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	#("6J4M_TTJets_PDF", "Njet=6, nMtags=4",  "(nJets==6 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	("7J2M_TTJets_PDF", "Njet=7, nMtags=2",  "(nJets==7 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	("7J3M_TTJets_PDF", "Njet=7, nMtags=3",  "(nJets==7 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	("7J4M_TTJets_PDF", "Njet=7, nMtags=4",  "(nJets==7 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	("8J2M_TTJets_PDF", "Njet=8, nMtags=2",  "(nJets==8 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	("8J3M_TTJets_PDF", "Njet=8, nMtags=3",  "(nJets==8 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
	("8J4M_TTJets_PDF", "Njet=8, nMtags=4",  "(nJets==8 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
	("9J2M_TTJets_PDF", "Njet=9, nMtags=2",  "(nJets==9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	("10J2M_TTJets_PDF", "Njet=9+, nMtags=2", "(nJets>9 && nMtags==2 {0})*{1}".format(cut_string,centralweight)),
	]
	if search_scheme == '9J3M,10J3M':
		cut_baseline += [
			("9J3M_TTJets_PDF", "Njet=9, nMtags=3", "(nJets==9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
			("10J3M_TTJets_PDF", "Njet=9+, nMtags=3", "(nJets>9 && nMtags>=3 {0})*{1}".format(cut_string,centralweight)),
		]
	elif search_scheme == '9J4M,10J4M':
		cut_baseline += [
			("9J3M_TTJets_PDF", "Njet=9, nMtags=3", "(nJets==9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
			("9J4M_TTJets_PDF", "Njet=9, nMtags=4", "(nJets==9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
			("10J3M_TTJets_PDF", "Njet=9+, nMtags=3", "(nJets>9 && nMtags==3 {0})*{1}".format(cut_string,centralweight)),
			("10J4M_TTJets_PDF", "Njet=9+, nMtags=4", "(nJets>9 && nMtags>=4 {0})*{1}".format(cut_string,centralweight)),
		]
	return cut_baseline

def make_replica(tree,draw_command,cuts_and_weights,gopts):
	print draw_command,cuts_and_weights
	tree.Draw(draw_command,cuts_and_weights,gopts)

def make_replica_unpack(args):
	make_replica(*args)

def make_up_and_down_histograms(config,histogram_draw_options,tree,output_file):

	if not output_file:
		raise RuntimeError("Output file is not ready")

	folder_name = histogram_draw_options[0]
	folder_title = histogram_draw_options[1]
	histogram_name = config.target
	histogram_baseline_cuts  = histogram_draw_options[2]
	histogram_template       = config.custom_binning[config.target][folder_name.split('_')[0]][0]

	output_file.cd()
	dirUp = output_file.mkdir(folder_name+'Up',folder_title)
	dirDown = output_file.mkdir(folder_name+'Down',folder_title)

	print folder_name,histogram_name,output_file
	print histogram_baseline_cuts
	print histogram_template

	temp_hist_name = 'temp_central'
	temp_hist_central = histogram_template.Clone(temp_hist_name)
	temp_hist_central.Reset()
	print config.target+'>>'+temp_hist_name,histogram_baseline_cuts+'*'+str(config.scalefactor)
	tree.Draw(config.target+'>>'+temp_hist_name,histogram_baseline_cuts+'*'+str(config.scalefactor))
	temp_hist_name = 'temp_std'
	temp_hist_stdUp = histogram_template.Clone(temp_hist_name+'_Up')
	temp_hist_stdUp.Reset()
	temp_hist_stdDown = histogram_template.Clone(temp_hist_name+'_Down')
	temp_hist_stdDown.Reset()

	variations_histograms = []
	list_of_arguments = []
	for ivar in range(0,100):
		nnpdfweight = 'pdf_nnpdf[{}]'.format(ivar)
		temp_hist_name = 'temp_'+nnpdfweight
		temp_hist = histogram_template.Clone(temp_hist_name)
		temp_hist.Reset()
		rt.SetOwnership(temp_hist,True)
		logging.debug(nnpdfweight)
		tree.Draw(config.target+'>>'+temp_hist_name,histogram_baseline_cuts+'*'+nnpdfweight+'*'+str(config.scalefactor),'goff')
		list_of_arguments.append((tree,config.target+'>>'+temp_hist_name,histogram_baseline_cuts+'*'+nnpdfweight+'*'+str(config.scalefactor),'goff'))
		variations_histograms.append(temp_hist)

	#threads = 4
	#pool = ThreadPool(threads)
    	#pool.map(make_replica_unpack, list_of_arguments)
    	#pool.close()
    	#pool.join()

	for ibin in range(1,temp_hist_central.GetNbinsX()+1):
		std = 0.
		for h in variations_histograms:
			std += (temp_hist_central.GetBinContent(ibin) - h.GetBinContent(ibin))**2.
		std = rt.TMath.Sqrt(std)
		std /= (len(variations_histograms)-1.)
		temp_hist_stdUp.SetBinContent(ibin,temp_hist_central.GetBinContent(ibin)+std)
		temp_hist_stdDown.SetBinContent(ibin,temp_hist_central.GetBinContent(ibin)-std)
	
	dirUp.cd()
	temp_hist_stdUp.SetName('bdt')
	temp_hist_stdUp.SetDirectory(dirUp)
	temp_hist_stdUp.Write()
	dirDown.cd()
	temp_hist_stdDown.SetName('bdt')
	temp_hist_stdDown.SetDirectory(dirDown)
	temp_hist_stdDown.Write()

def main(arguments,config):

	root_file = rt.TFile.Open(config.inputfile)
	if not root_file:
		raise RuntimeError("Cannot open file: {}".format(config.inputfile))
	root_tree = root_file.Get(config.tree_name)
	if not root_tree:
		raise RuntimeError("Cannot retrieve tree: {} from file {}".format(config.tree_name,config.inputfile))
	
	root_output_file = rt.TFile.Open(config.output_filename,'RECREATE')
	for item in cut_nnpdf('&&'+config.trigger_cuts,config.binning_option):
		make_up_and_down_histograms(config,item,root_tree,root_output_file)
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



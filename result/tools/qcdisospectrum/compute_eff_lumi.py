import ROOT as rt
import imp

configuration_module = imp.load_source('my_config', 'conf_cff_mu.py')
configuration = configuration_module.config

lumi = 35.84

chain_name = 'bookkeeping'
for files in configuration['inputfiles']:
	file_names = configuration['inputfiles'][files][1]
	ch = rt.TChain(chain_name)
	ch.Add(file_names)
	print files, ch.GetEntries()

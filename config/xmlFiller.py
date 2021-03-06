#!/usr/bin/env python

# python script for filling eqlumi into config files

import shutil 
import os
import sys
from ROOT import TChain
import glob
import xml.etree.cElementTree as ET

inputFile = sys.argv[1]
outputFileName = 'output_'+inputFile

summary = []

tree = ET.ElementTree(file=inputFile)
root = tree.getroot()
datasets = root.find('datasets')
for d in datasets:
    if 'data' in d.attrib['name'].lower():
        d.set('EqLumi','1')
        continue
    if d.attrib['add'] == 0:
	continue
    xsec = float(d.attrib['xsection'])
    files = glob.glob(d.attrib['filenames'])
    print files
    root_files = []
    for f in files:
        root_files.append('dcap://maite.iihe.ac.be'+f)
    chain = TChain('eventTree')
    for rf in root_files:
        chain.Add(rf)
    nEntries = chain.GetEntries()
    equivLumi = nEntries/xsec
    d.set('EqLumi',str(equivLumi))
    summary.append( [d.attrib['name'], nEntries, equivLumi] )
print 'filled xml with eqlumis!'
for item in summary:
	print item
tree.write(outputFileName)

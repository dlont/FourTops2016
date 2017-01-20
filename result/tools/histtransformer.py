# Driver class that performs arbitrary transformation of the histograms

import ROOT

class histProcessor:

	def __init__(self, *arguments, **keywords):
		self.processor = None
		self.target = None

		keys = sorted(keywords.keys())
		if keywords['target']:
			targetRootFileHandle =  keywords['target']
			targetRootFileHandle.Print()
			self.target = targetRootFileHandle
		if keywords['proc']:
			print 'Processor supplied'
			self.processor = keywords['proc']

	def setProcessor(self, proc):
		self.processor = proc
	
	def process(self):
		self.processor.setTarget(self.target)
		self.processor.run()
		self.target.Write()
		self.target.Close()

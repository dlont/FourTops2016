
import ROOT

rec_counter = 1
class scaleUncProcessor:
	def __init__(self,nominal):
		self.target = None
		self.nominal = nominal
		return

	def setTarget(self, target):
		self.target = target

	def run(self):
		print 'scaleUncProcessor.run()'
		self.addrenfacscalesysunc(self.target,self.nominal)
		print 'Transformation has been performed'
		

	def addrenfacscalesysunc(self,target,nominal):
		global rec_counter
		#gain time, do not add the objects in the list in memory
		status = ROOT.TH1.AddDirectoryStatus();
		ROOT.TH1.AddDirectory(ROOT.kFALSE);
	
		ROOT.gDirectory.Print()
		full_path = target.GetPath()
		path = str(target.GetPath()).split(':/',1)[1]
	
		nominal.cd(path)
	
		ROOT.gDirectory.Print()
		# loop over all keys in this directory
		for key in ROOT.gDirectory.GetListOfKeys():
			obj = key.ReadObj()
			objname = obj.GetName()
			if (obj.IsA().InheritsFrom( ROOT.TH1.Class() )):
		 		nominal.cd( path )
		 		keynom = ROOT.gDirectory.GetListOfKeys().FindObject(objname)
				hnom = keynom.ReadObj()

				variation_histograms = {
				'hist_muRd_muFd'  : self.nominal.Get('weight1/'+objname), 
				'hist_muRd_muF0'  : self.nominal.Get('weight2/'+objname),
				'hist_muR0_muFd'  : self.nominal.Get('weight3/'+objname),
				'hist_muR0_muFu'  : self.nominal.Get('weight4/'+objname),
				'hist_muRu_muF0'  : self.nominal.Get('weight5/'+objname),
				'hist_muRu_muFu'  : self.nominal.Get('weight7/'+objname)
				}

				if all(variation_histograms):
					# renorm/fact scale variation envelope
					for ibin in range(1,obj.GetNbinsX()+1):
						binvariations = [
							obj.GetBinContent(ibin),
							variation_histograms['hist_muRd_muFd'].GetBinContent(ibin),	
							variation_histograms['hist_muRd_muF0'].GetBinContent(ibin),
							variation_histograms['hist_muR0_muFd'].GetBinContent(ibin),
							variation_histograms['hist_muR0_muFu'].GetBinContent(ibin),
							variation_histograms['hist_muRu_muF0'].GetBinContent(ibin),
							variation_histograms['hist_muRu_muFu'].GetBinContent(ibin)
						]
						binmax = max(binvariations)
						binmin = min(binvariations)
						print obj.GetBinError(ibin), max(binvariations), min(binvariations)
						diff2  = (binmax - binmin)*(binmax - binmin)
						binerror = obj.GetBinError(ibin)*obj.GetBinError(ibin) + diff2
                                		obj.SetBinError(ibin,ROOT.TMath.Sqrt(binerror))
				
	          
			elif ( obj.IsA().InheritsFrom( ROOT.TDirectory.Class() ) ):
				foldername = obj.GetName()
				print "Found subdirectory ", foldername
				if 'allSF' not in foldername: 
					print 'Skipping', foldername
					continue
				nominal.cd(obj.GetName())
				target.cd()
				target.mkdir(obj.GetName())
			        target.cd(obj.GetName())
				newdir = ROOT.gDirectory
				rec_counter+=1
	         		self.addrenfacscalesysunc( newdir, nominal)
	
	      		else:
		        	print "Unknown object type, name: ", obj.GetName(), " title: ", obj.GetTitle()
	
			if ( obj.IsA().InheritsFrom( ROOT.TH1.Class() ) ):
				target.cd(full_path)
				obj.Write( key.GetName() )
	
		#save modifications to target file
		target.SaveSelf(ROOT.kTRUE);
		ROOT.TH1.AddDirectory(status);




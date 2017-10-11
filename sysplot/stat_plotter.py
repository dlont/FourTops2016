import logging

from ROOT import TFile
from ROOT import TCanvas
from ROOT import TPad
from ROOT import TH1
from ROOT import TObject
from ROOT import THStack
from ROOT import TLegend
from ROOT import TAxis
from ROOT import EColor
import ROOT

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
		self.out_format=kwargs.get('format_plot',"png")
		self.source_root = None
		self.reference_root = None

	def set_file(self,root_file_list):
		input_file = [TFile.Open(root_file,'READ') for root_file in root_file_list]
		if not input_file:
			raise NameError('Cannot read ROOT file: %s. Terminating!' % root_file)
		self.source_root = input_file

	def set_reference_file(self,root_file):
		reference_file = TFile.Open(root_file,'READ')
		if not reference_file:
			raise NameError('Cannot read ROOT file: %s. Terminating!' % root_file)
		self.reference_root = reference_file

	def decorate_page(self,master_canvas,config):
		"""
		decorate_page
		"""

		# Set axis label size
		for pad_id, c in enumerate(config['pads']):
			gPad = master_canvas.cd(1).cd(pad_id+1)
			pad_objs = gPad.GetListOfPrimitives()
			pad_num = gPad.GetNumber() - 1
			col = pad_num % config["nx"]
			row = (pad_num - col) / config["nx"]
			st = pad_objs.FindObject("st")
			if st:
				st.GetYaxis().SetLabelSize(0.)
				st.GetXaxis().SetLabelSize(0.)
			if col == 0 and st:
				st.GetYaxis().SetLabelSize(0.1)
			if row == config["ny"]-1 and st: 
				st.GetXaxis().SetLabelSize(0.1)

		# Add legend
		tmp = master_canvas.cd(1).cd(1).GetListOfPrimitives()
		leg1 = TLegend(config["legend"]["coord"][0],config["legend"]["coord"][1],config["legend"]["coord"][2],config["legend"]["coord"][3])
		leg1.SetBorderSize(0)
		leg1.SetTextSize(0.1);
		for entry in tmp:
			if entry.IsA().InheritsFrom("THStack"):	
				for hist in entry.GetHists():
					leg1.AddEntry(hist,"","l")
			else: pass
		
		master_canvas.cd(2)
		leg1.Draw()
		return

	def decorate_pad(self, pad, stack, gPad):
		"""
		decorate_pad
		"""
		stack.GetXaxis().SetNdivisions(5,0,0)
		stack.GetYaxis().SetNdivisions(5,0,0)
		if "title" in pad: stack.SetTitle(pad["title"])
		if "ymax" in pad: stack.SetMaximum(pad["ymax"])
	 	if "ymin" in pad: stack.SetMinimum(pad["ymin"])
		return

	def make_pad(self, pad_tup, root_canvas):
		"""
		make_pad
		"""
		logging.debug(pformat(pad_tup[1]))
	      	gPad = root_canvas.cd(pad_tup[0]+1)
		gPad.SetFillStyle(0)	#transparent pad
		st = None
		st = self.make_stackplot(pad_tup[1],gPad)
	      	self.decorate_pad(pad_tup[1], st, gPad)
	      	return

	def make_pads(self,pads,root_canvas):
		"""
		make_pads
		"""
		for pad in enumerate(pads):
			self.make_pad(pad,root_canvas)
		return

	def make_pages(self,pages_config):
		"""
		make_page
		"""
		canvas = pages_config['canvas']
		i, total = (0, len(canvas))
		for c in canvas:
			##############################
			progress(i, total, 'Progress')
			i += 1
			#############################
			root_canvas = TCanvas('c','CMS',5,45,c['width'],c['height'])
			root_canvas.Divide(2,1); root_canvas.cd(1).SetPad(0.1,0.1,0.7,0.9); root_canvas.cd(2).SetPad(0.7,0.1,0.9,0.9)
			root_canvas.cd(1).Divide(c['nx'],c['ny'],0.,0.)
			self.make_pads(c['pads'],root_canvas.cd(1))
	  		self.decorate_page(root_canvas,c)
			if 'name' in c: root_canvas.Print(c['name']+"."+self.out_format)
			else: root_canvas.Print(str('file_'+str(i)+self.out_format))
	  	return

	def make_stackplot(self, pad, gPad):
		"""
		make_stackplot
		"""

		colors = [ROOT.kGreen+2,ROOT.kYellow+2,ROOT.kMagenta+2,ROOT.kBlue+2,ROOT.kCyan+2,
			  ROOT.kSpring-2, ROOT.kOrange-2, ROOT.kPink-2, ROOT.kViolet-2, ROOT.kAzure-2]

		st = THStack("st","TEST")
		for hist in pad["histograms"]:
			logging.debug("ROOT FILE: %s" % self.source_root)
			logging.debug("NAME HIST: %s" % hist)
			h = None

			if "name" not in hist: continue

			for item,f in  enumerate(self.source_root):
				h = f.Get(str(hist["name"])).Clone(str(hist["name"]))
				if not h:
					raise NameError('Cannot read ROOT histogram: %s. Terminating!' % str(hist["name"]))	
				h.Sumw2(); h.Divide(h)
				for ibin in range (1,h.GetNbinsX()+1): h.SetBinContent(ibin,0.);
				# Set style
				if "style" in hist:  self.set_hist_style(h,hist,colors[item])
				######################
				st.Add(h,'hist pE1')

		gPad.cd()
		st.Draw("nostack")
		return st

	def set_hist_style(self, hist, style,color=None):
		""" Set style """
		if not hist:
			raise NameError('Cannot read ROOT histogram. Terminating!')	
		if "style" in style:
			hist.SetLineWidth(style["style"][0])
			if color is not None:  hist.SetLineColor(color)
			else: hist.SetLineColor(style["style"][1])
			hist.SetLineStyle(style["style"][2])
		if "title" in style:
			hist.SetTitle(style["title"])
		return


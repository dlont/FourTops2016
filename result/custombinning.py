from ROOT import TH1D

from array import array      # to allow making Float_t arrays for ROOT hists

bins_7J2M = array("f", [-1.0, -0.999, -0.96170151233673096, -0.91267025470733643, -0.85475194454193115, -0.79572176933288574, -0.71033287048339844, -0.61591583490371704, -0.53245639801025391, -0.43880739808082581, -0.28634846210479736, 0.54172417783737181, 1.0])
bins_7J3M = array("f", [-1.0, -0.48919474831223486, -0.25977602601051331, -0.18199574947357178, -0.11135745793581009, -0.029694110155105591, 0.051136277616024017, 0.11303293704986572, 0.1767970472574234, 0.2621418833732605, 0.40132340788841248, 0.72396671843528748, 1.0])
bins_7J4M = array("f", [-1.0, -0.035329918205738067, 0.1633145660161972, 0.21130476891994476, 0.26165869832038879, 0.26600342988967896, 0.32578533887863159, 0.40132340788841248, 0.4583432674407959, 0.51377534866333008, 0.59165447950363159, 0.7010195497870445, 1.0])
bins_8J2M = array("f", [-1.0, -0.95991719609498982, -0.7300606369972229, -0.6630483865737915, -0.60926425457000732, -0.5567055344581604, -0.50099712610244751, -0.44009140133857727, -0.36422932147979736, -0.26918497681617737, -0.14393478631973267, 0.57556001234054566, 1.0])
bins_8J3M = array("f", [-1.0, -0.4243357897102833, -0.11802194267511368, -0.035361811518669128, 0.027189165353775024, 0.08193669468164444, 0.13376279175281525, 0.18300051987171173, 0.23792856931686401, 0.30055445432662964, 0.37884560227394104, 0.76904067230224604, 1.0])
bins_8J4M = array("f", [-1.0, -0.054587048415094611, 0.27214184403419495, 0.34744212031364441, 0.39734098315238953, 0.44223576784133911, 0.50382113456726074, 0.5733264684677124, 0.77829304611682892, 1.0])
bins_9J2M = array("f", [-1.0, -0.44602271854877473, -0.26129388809204102, -0.20151934027671814, -0.15229430794715881, -0.1037156730890274, -0.052968818694353104, 0.0023210158105939627, 0.068335063755512238, 0.14716166257858276, 0.25451374053955078, 0.70193092119693756, 1.0])
bins_9J3M = array("f", [-1.0, 0.105458560757339, 0.25572091341018677, 0.30384942889213562, 0.34131729602813721, 0.3714025616645813, 0.40493154525756836, 0.43513250350952148, 0.47289842367172241, 0.51572012901306152, 0.5723755955696106, 0.79686497569084169, 1.0])
bins_9J4M = array("f", [-1.0, 0.36571423360705374, 0.57676023244857788, 0.63315433263778687, 0.68997234106063843, 0.75554049015045166, 0.84892519551515577, 1.0])
bins_10J2M = array("f", [-1.0, -0.048225751295685765, 0.11621873080730438, 0.17444996535778046, 0.21930493414402008, 0.2569197416305542, 0.29406175017356873, 0.33293932676315308, 0.37409999966621399, 0.41503617167472839, 0.47942224144935608, 0.71938856124877926, 1.0])
bins_10J3M = array("f", [-1.0, 0.2541600247621536, 0.4487667977809906, 0.50293558835983276, 0.5480804443359375, 0.58503615856170654, 0.63973820209503174, 0.68949532508850098, 0.89157182872295382, 1.0])
bins_10J4M = array("f", [-1.0, 0.48996552908420565, 0.71670699119567871, 0.7961878776550293, 0.82866770029067993, 0.9224138305187225, 1.0])

custom_binning = {
    # 'allSF':{'BDT9and10jetsplitNoNjw.BDT9and10jetsplitNoNjw', array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0])},
    # '6J2M': {'BDT9and10jetsplitNoNjw.BDT9and10jetsplitNoNjw', array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0])},
    # '6J3M': {'BDT9and10jetsplitNoNjw.BDT9and10jetsplitNoNjw', array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0])},
    # '6J4M': {'BDT9and10jetsplitNoNjw.BDT9and10jetsplitNoNjw', array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0])},
    'BDT9and10jetsplitNoNjw.BDT9and10jetsplitNoNjw' : 
      {'7J2M' : (TH1D("bdt_7J2M"    , ";BDT;entries/bin", len(bins_7J2M)-1,bins_7J2M),TH1D("bdt_Up7J2M"    , ";BDT;entries/bin", len(bins_7J2M)-1,bins_7J2M),TH1D("bdt_Down7J2M"    , ";BDT;entries/bin", len(bins_7J2M)-1,bins_7J2M)),
       '7J3M' : (TH1D("bdt_7J3M"    , ";BDT;entries/bin", len(bins_7J3M)-1,bins_7J3M), TH1D("bdt_Up7J3M"    , ";BDT;entries/bin", len(bins_7J3M)-1,bins_7J3M), TH1D("bdt_Down7J3M"    , ";BDT;entries/bin", len(bins_7J3M)-1,bins_7J3M)),
       '7J4M' : (TH1D("bdt_7J4M"    , ";BDT;entries/bin", len(bins_7J4M)-1,bins_7J4M), TH1D("bdt_Up7J4M"    , ";BDT;entries/bin", len(bins_7J4M)-1,bins_7J4M), TH1D("bdt_Down7J4M"    , ";BDT;entries/bin", len(bins_7J4M)-1,bins_7J4M)),
       '8J2M' : (TH1D("bdt_8J2M"    , ";BDT;entries/bin", len(bins_8J2M)-1,bins_8J2M), TH1D("bdt_Up8J2M"    , ";BDT;entries/bin", len(bins_8J2M)-1,bins_8J2M), TH1D("bdt_Down8J2M"    , ";BDT;entries/bin", len(bins_8J2M)-1,bins_8J2M)),
       '8J3M' : (TH1D("bdt_8J3M"    , ";BDT;entries/bin", len(bins_8J3M)-1,bins_8J3M), TH1D("bdt_Up8J3M"    , ";BDT;entries/bin", len(bins_8J3M)-1,bins_8J3M), TH1D("bdt_Down8J3M"    , ";BDT;entries/bin", len(bins_8J3M)-1,bins_8J3M)),
       '8J4M' : (TH1D("bdt_8J4M"    , ";BDT;entries/bin", len(bins_8J4M)-1,bins_8J4M), TH1D("bdt_Up8J4M"    , ";BDT;entries/bin", len(bins_8J4M)-1,bins_8J4M), TH1D("bdt_Down8J4M"    , ";BDT;entries/bin", len(bins_8J4M)-1,bins_8J4M)),
       '9J2M' : (TH1D("bdt_9J2M"    , ";BDT;entries/bin", len(bins_9J2M)-1,bins_9J2M), TH1D("bdt_Up9J2M"    , ";BDT;entries/bin", len(bins_9J2M)-1,bins_9J2M), TH1D("bdt_Down9J2M"    , ";BDT;entries/bin", len(bins_9J2M)-1,bins_9J2M)),
       '9J3M' : (TH1D("bdt_9J3M"    , ";BDT;entries/bin", len(bins_9J3M)-1,bins_9J3M), TH1D("bdt_Up9J3M"    , ";BDT;entries/bin", len(bins_9J3M)-1,bins_9J3M), TH1D("bdt_Down9J3M"    , ";BDT;entries/bin", len(bins_9J3M)-1,bins_9J3M)),
       '9J4M' : (TH1D("bdt_9J4M"    , ";BDT;entries/bin", len(bins_9J4M)-1,bins_9J4M), TH1D("bdt_Up9J4M"    , ";BDT;entries/bin", len(bins_9J4M)-1,bins_9J4M), TH1D("bdt_Down9J4M"    , ";BDT;entries/bin", len(bins_9J4M)-1,bins_9J4M)),
       '10J2M': (TH1D("bdt_10J2M"    , ";BDT;entries/bin", len(bins_10J2M)-1,bins_10J2M), TH1D("bdt_Up10J2M"    , ";BDT;entries/bin", len(bins_10J2M)-1,bins_10J2M), TH1D("bdt_Down10J2M"    , ";BDT;entries/bin", len(bins_10J2M)-1,bins_10J2M)),
       '10J3M': (TH1D("bdt_10J3M"    , ";BDT;entries/bin", len(bins_10J3M)-1,bins_10J3M), TH1D("bdt_Up10J3M"    , ";BDT;entries/bin", len(bins_10J3M)-1,bins_10J3M), TH1D("bdt_Down10J3M"    , ";BDT;entries/bin", len(bins_10J3M)-1,bins_10J3M)),
       '10J4M': (TH1D("bdt_10J4M"    , ";BDT;entries/bin", len(bins_10J4M)-1,bins_10J4M), TH1D("bdt_Up10J4M"    , ";BDT;entries/bin", len(bins_10J4M)-1,bins_10J4M), TH1D("bdt_Down10J4M"    , ";BDT;entries/bin", len(bins_10J4M)-1,bins_10J4M))}
}


* [ ] Compare fits from combine and theta
* [ ] Make b tagging fake rate and efficiency maps
  - [ ] As function of jet pt/eta
  - [ ] As function of jet pt/eta in different jet multiplicity bins
  - [ ] Compare results with new efficiency maps
* [ ] Make fits as function of e.g. HT, HTb
  - [x] There is a benchmark result as function of HT on github for Freya (https://github.com/dlont/FourTops2016_datacards).
* [ ] Add WZ background
* [ ] Find optimal binning
* [ ] Train tttt against ttZ and ttH in high multipicity events
* [ ] Scan all high BDT Events
* [ ] Switch to v12 data/mc
* [ ] Compare results with and without flavour dependent JEC
  - Long's results show good agreement in significance (see slide 20 of [*])

[*] https://docs.google.com/presentation/d/1Cz8xaVdsIFVl5qpLrsTDBShwBX2j7X5x9Y0dXwpCcHE/edit#slide=id.g2a3b587564_17_123

------------------------

### TODO:
  * task 1 (see 30 Nov)
    - [ ] Repeat the studies with $\mu:$ 8/4 only SR fit
      - [ ] pulls
      - [ ] correlations  
    - [ ] Repeat the studies with $\mu:$ 8/4 only SR fit with $t\bar{t}t\bar{t}H,Z$ and $t\bar{t}t\bar{t}+W,XY$ split in different categories
      - [ ] make pulls
      - [ ] make correlations
  * task 2 (see 4 Dec)
    - [ ] Find fit results in `~/t2016/results/` quoted on slide 5
    - [ ] make pulls
    - [ ] make correlations
  * task 3 (fit with ttz,h,w,xy merged)
    - [ ] Postfit plots with all bins together
    - [ ] Postfit plots with only 4btag bins
    - [ ] Correlation matrix for signal and background
    - [ ] Pulls plot
    - [ ] Normalizations with fixed prefit uncertainties
    - [ ] Prefit mountain range plots (optimized binning)
  * task 4 (make fits of B-F and G-H data)
    - [ ] Postfit plots with all bins together
    - [ ] Postfit plots with only 4btag bins
    - [ ] Correlation matrix for signal and background
    - [ ] Pulls plot
    - [ ] Normalizations with fixed prefit uncertainties
    - [ ] Prefit mountain range plots (optimized binning)


----------------------------------------------

### Existing materials
#### 23 Nov (First unblinding)
**Result:** Fit in all categories ttZ,ttH,ttW,ttXY combined into single source

**Output:** Bad quality post-fit and prefit plots

https://docs.google.com/presentation/d/1CSIHw1sp8k8Al15vF-EspNpOVmZkSLhzGPFshQDzSBE/edit#slide=id.g2898cec9a5_0_0

#### 24 Nov (First unblinding contd.)

**Result:** Same as before. List of high multipicity events. Rebinned prefit plots.
https://docs.google.com/presentation/d/1HXbF5r8oVvfreomeVQ0YN2d-nOCS7QM6X4w1ocChAB0/edit
https://indico.cern.ch/event/683885/contributions/2803053/attachments/1564870/2465441/interesting_events_el.txt
https://indico.cern.ch/event/683885/contributions/2803053/attachments/1564870/2465442/interesting_events_mu.txt
http://mon.iihe.ac.be/~dlontkov/assets/results/TTTT2017/24-11-2017/El/
http://mon.iihe.ac.be/~dlontkov/assets/results/TTTT2017/24-11-2017/Mu/

**Output:** Same as before, with fixed mountain range postfit plots and pulls
**Conclusion:** Normalization discrepancy in *10J3M* is terrible

#### 27 Nov (First unblinding contd.)

**Result:** Same as before.

**Output:** Table with pre and postfit normalizations and event counts

**Conclusion:** In majority of search regions there are more events prefit than observed. The fit over-corrects (sf<1) the number of postfit events such that total number of $t\bar{t}$ event is less than observed. The difference $\text{obs}-t\bar{t}$ is compensated by significant increase of $t\bar{t}t\bar{t}$ contribution

https://indico.cern.ch/event/684047/contributions/2803928/attachments/1565593/2466943/main.pdf

#### 28 Nov (First unblinding contd.)

**Result:** Same as before.

**Output:** Table with pre and postfit normalizations and event counts with fixed observation numbers in $\mu$ 7J category

https://indico.cern.ch/event/684460/contributions/2806057/attachments/1566471/2469000/main.pdf

#### 30 Nov (Fit properties studies)

**Result:** Identified well behaved control regions where the excess is not statistically significant and asymptotic and toys results agree. Event display with highest MVA value in *electron* channel, where there is no MC prediction.

**Output:**

**Conclusion:**

- In the fit in $\mu:$ 7/*, 8/2, 8/3, 9/2 and $e:$ 8/2, 8/3, 9/2 with $t\bar{t}t\bar{t}H,Z,W,XY$ merged in a single $t\bar{t}t\bar{t}+\text{rare}$ category, observed and expected limits agree within $1\sigma$ (see [1] page 2). Discrepancy between Hybrid and Asymptotic significance was later explained by insufficient amount of toys.

- Very small visual difference between **b-only** and **s+b** fit in $\mu:$ 8/4 only SR (see slides 12, 13).
- Although the leptons are shifted from the jets point of origin. This is likely due to incorrect plotting of the of the jets (that seem to originate from the origin of the coordinate system, see  [2]).

[1] https://docs.google.com/presentation/d/1QEf0LLUQEl8zKMVebvEbqWU9nL_u_Kzonw9jutZ9cTk/edit#slide=id.g2a0caa5187_0_33

[2] https://indico.cern.ch/event/680031/contributions/2785440/attachments/1568225/2472486/Screenshot_from_2017-11-30_170317.png

#### 4 Dec (Fit properties studies)

**Result:** Toy example showing how large signal with $1\sigma$ significance can be generated in control regions. Removing high MVA part of the distribution in well behaved CRs makes expected and observed limits very close  ($22^{+9}_{-7} (25)$ exp. (obs), see comparison in [1], slide 3). Comparison of pulls and correlations in 50 bins and optimized binning configuration

**Output:**
  - Asymptotic limits for the fit without high MVA
  - Asymptotic limits for the fit when $r=0$ in CRs
  - pulls/correlations for nominal fit and for optimized binning
  - Normalizations scale factors in different search regions when normalization in every bin is left floating

**Conclusion:**
  - When signal is set to zero in CRs, significant excess doesn't disappear. The origin of the problem is likely to be in bad modelling of background in signal regions (see slide 1 of [1]).
  - __Optimized binning__ has better agreement of nuisance parameters in **b-only** and **s+b** fit, when compared to __50 bins__ configuration, however it features larger correlations (see slides 6-9 of [1])
  - In some cases, as e.g. $t\bar{t}$ ME systematics is sensitive to the slope of the distribution, and the larges effect is visible in the tails (slide 10 of [1])
  - There is $0.5-1 \sigma$ discrepancy in normalization scale factors in 9,10/4 bins between **b-only** and **s+b** fits

[1] https://docs.google.com/presentation/d/1UTTx0vzWRAxB6FgVnDvWJ7AZZr_x7xUUKX3gHkC2JkY/edit#slide=id.p

#### 6 Dec (Nothing from _single lepton_ analysis)

**Result:** Long shows that fixing $t\bar{t}H$ or $t\bar{t}Z$ leads to strange behaviour of the fit. Postfit nuisances are rather different

**Output:**
  - Pre-/Post-fit plots and nuisances for fixed $t\bar{t}H$ or $t\bar{t}Z$ or when both are merged
  - Comparison of significances with and without flavour-dependent JECs

**Conclusions:**

https://docs.google.com/presentation/d/1Cz8xaVdsIFVl5qpLrsTDBShwBX2j7X5x9Y0dXwpCcHE/edit#slide=id.g2a3b587564_17_123

#### 8 Dec (Efficiency/fake rate study)

**Result:** Comparison of Efficiency/fake rate in inclusive and selected $t\bar{t}$ events.

**Output:** Efficiency/fake rate maps as functions of jet pt/eta

**Conclusions:** In selected phase space fake rate and efficiency are lower than in inclusive $t\bar{t}$ events
https://docs.google.com/presentation/d/1ZD-5adJcxcAcNAUI0ehF47Q4G-B6Ti13Yf199qOp2zQ/edit#slide=id.g2a4d4e7b43_0_6

#### 9 Dec (Nothing from _single lepton_ analysis)

#### 13 Dec (Splitting $t\bar{t}+\text{rare}$ into $t\bar{t}H,Z,W,XY$ )

**Result:** Non-sense fits

**Output:** Correlations and pulls of non-sense fits

**Conclusions:** Fit breaks down, when many processes with similar shapes are introduced. One should merge some of the sources.

https://docs.google.com/presentation/d/1Csimftu6JcldeROkwc6ESJ_cnWesJ_JdOz2xJhwbvp8/edit#slide=id.g2c69e9964f_0_51

#### 18 Dec (Splitting $t\bar{t}+\text{rare}$ into $t\bar{t}H,Z,W,XY$)

**Result:**
- Prefit and postfit shape of MVA inputs of $t\bar{t}H,Z$ and $t\bar{t}t\bar{t}$ look very similar. There are differences with $t\bar{t}W$. HT and 5th jet $p_T$ are not very well described.
- Long shows unexpected discrepancy in $dR_{bb}$ between $t\bar{t}H$ and $t\bar{t}Z$.

**Output:** Full collection of pre- and post-fit MVA distributions
**Conclusions:** Keep $t\bar{t}H,Z$ and $t\bar{t}W,XY$ combined in two groups.

https://indico.cern.ch/event/688116/contributions/2824434/attachments/1577281/2491097/template_Scrartcl.pdf

#### 20 Dec (Splitting $t\bar{t}+\text{rare}$ into $t\bar{t}H,Z,W,XY$)

**Result:** Different look on the same results from 18 Dec.

**Output:**
  - Same plots as before but with focus on 4 tag category
  - Postfit and prefit event rates

**Conclusions:** In high b-tag multiplicity categories $t\bar{t}H,Z$ and $t\bar{t}t\bar{t}$ look almost identical. If normalization of these backgrounds is wrong in high b-tag bins, the fit will give wrong results.

https://indico.cern.ch/event/689400/contributions/2830377/attachments/1578306/2493215/main.pdf

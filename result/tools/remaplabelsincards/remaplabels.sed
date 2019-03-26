#!/bin/sed -f

# Find lines starting with 'process' and
# replace every occurence of tttt with NP_overlay_ttttNLO  
/^process/ s/ tttt / NP_overlay_ttttNLO /g
/^shapes/ s/ tttt / NP_overlay_ttttNLO /g

# Find lines starting with 'pu' and
# replace every occurence of 'pu' with 'PU'
# correlate pile-up uncertainties
/^pu/ s|pu|PU|


# Find lines starting with 'jes' and
# replace every occurence of 'jes' with 'JES'
# correlate JES uncertainties
/^jes/ s|jes|JES|


# Find lines starting with 'jer' and
# replace every occurence of 'jer' with 'JER'
# correlate JES uncertainties
/^jer/ s|jer|JER|


# Find lines starting with 'lepeff' and
# replace every occurence of 'lepeff' with 'leptonSF'
# correlate lepton SF uncertainties in SUSY to that in dilepton channel
#/^lepeff/ s|lepeff|leptonSF|


# Find lines starting with 'isrvar' and
# replace every occurence of 'isrvar' with 'TTISR'
# correlate PS ISR uncertainties in SUSY to that in single lepton and dilepton channels
#/^isrvar/ s|isrvar|TTTTISR|


# Find lines starting with 'fsrvar' and
# replace every occurence of 'isrvar' with 'TTFSR'
# correlate PS ISR uncertainties in SUSY to that in single lepton and dilepton channels
#/^fsrvar/ s|fsrvar|TTTTFSR|
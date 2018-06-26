# `chef.histogram.py`
This python script helps you create histograms on several variables from data and MC craneens, including preselection rules, weighting schemes and several systematic uncertainties, and can be scaled according to the specified target luminosity.

## Usage
```
$ python chef_histogram.py -h
usage: chef_histogram.py [-h] [--Datalist plot_list_Data]
                         [--preselection preselection_file]
                         [--weighting weighting_list] [--lumi luminosity]
                         [--systematics SYSTEMATICS]
                         plotprops tree_name dir plot_list_MC

Cooks some histograms from Craneen files for you.

positional arguments:
  plotprops             File containing list of attributes you want in a plot
  tree_name             Tree name you want from Craneen file
  dir                   Directory to store new histogram files
  plot_list_MC          File containing list of MC Craneen files you want

optional arguments:
  -h, --help            show this help message and exit
  --Datalist plot_list_Data
                        File containing list of Data files you want -- Do not
                        use this flag for blind analysis.
  --preselection preselection_file
                        File containing list of preselection cuts you want
  --weighting weighting_list
                        File containing list of weighting schemes you want
  --lumi luminosity     Target luminosity for each histogram -- Overrides
                        luminosity from Datalist option
  --systematics SYSTEMATICS
                        File containing list of central, upper and lower limit
                        of scale factors
```

### File in `plotprops`
Each line in `plotprops` file must contain five sections in the following order:
- Name of variable branch in Craneen tree
- Number of bins
- Start of the range for the histogram
- End of the range for the histogram
- Proper name to be displayed on the x-axis (may contain whitespace)

These five sections must be separated by a whitespace. For example: 
```
LeptonPt 10 0. 800. Lepton p_{T} (GeV)
```
 tells the chef to make histogram from `LeptonPt` leaf, with 10 bins ranging from 0. to 800., with *"Lepton p_{T} (GeV)"* as a proper name.

### File in `plot_list_MC`
`plot_list_MC` supports creating each histogram file from multiple Craneen files representing the same process. To specify all file names in each collection;

1. Start a line with `###` followed by a whitespace and the name of process to be used. No whitespaces are allowed in the name.
2. In each of the following lines, add the path of each Craneen file, followed by a whitespace and the cross-section for the Craneen file *in femtobarns*.
3. Repeat steps 1 and 2 until all samples are included.
4. End the list with `!!!`. **If you do not add this ending line, the last MC set may not be generated.**

### File in `plot_list_Data` (optional)
`plot_list_Data` has a different structure from `plot_list_MC`. Each line must contain the path to the Craneen file, followed by a whitespace and luminosity of each file *in inverse femtobarns*. **If `--lumi` option is used, the total luminosity will be overridden by the value specified in this option instead of the sum of luminosity in the file.**

### File in `preselection_file` (optional)
`preselection_file` supports multiple preselection rules at the same time, as well as preselection rules applied to specific files.

1. Each line must contain the name of preselection criteria *(no whitespace allowed)*, followed by a whitespace and a string with preselection rule in C++ format (whitespaces are allowed here). The chef uses [`TTree::Draw`](https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45) method, so all preselection rules in this file must be compatible with the method.
2. End the list with `###`. 
3. If there are preselection rules to be applied to specific Craneen files, add a line containing the path of a file, followed by a whitespace and another string with preselection rule in C++ format. Again, this preselection rule is used in `TTree::Draw` method, so it must also be compatible.

### File in `weighting` (optional)
`weighting` supports calculating separate weighting schemes in case you want to turn off some scale factors. Each line of the file must contain the name of weighting scheme *(no whitespace allowed)*, a whitespace, and a scale factor *(no whitespace allowed)*. You can multiply multiple factors with `*`, as if you're multiplying them in the code.

### File in `systematics` (optional)
`systematics` supports generating histograms with multiple systematic variations. Each line must be formatted in the following order:
```
[NAME] [CENTRAL_WEIGHT] [UPPER_WEIGHT] [LOWER_WEIGHT]
```

Where `NAME` is the name of systematic variation, `CENTRAL_WEIGHT`, `UPPER_WEIGHT`, and `LOWER_WEIGHT` represent the scale factor at central, upper, and lower values.

# `chef_plot.py`
This python script helps you merge several histogram files into a nicely-formatted plot, along with ratio plots and systematic uncertainties. In order to function properly, `chef_histogram.py` must generate the histograms first before running this script. **This script requires [`tdrstyle` python script from @cbernet](https://github.com/cbernet/tdr-style) in order to work, as it gives CMS style to the plots.**

## Usage
```
$ python chef_plot.py -h
usage: chef_plot.py [-h] [--DataHist data_histogram] [--DataName data_name]
                    [--preselection [PRESELECTION [PRESELECTION ...]]]
                    [--weighting weighting_list] [--lumi luminosity]
                    [--outputName OUTPUTNAME] [--noLog] [--noOverflow]
                    [--systematics SYSTEMATICS]
                    plotprops dir plot_list_MC

Puts together histograms into a nicely formatted plot for you.

positional arguments:
  plotprops             File containing list of attributes you want in a plot
                        (same as chef_histogram.py)
  dir                   Directory to read histogram files
  plot_list_MC          File containing list of MC histograms you want

optional arguments:
  -h, --help            show this help message and exit
  --DataHist data_histogram
                        File containing Data histogram you want -- Do not use
                        this flag for blind analysis.
  --DataName data_name  Custom data Craneen name
  --preselection [PRESELECTION [PRESELECTION ...]]
                        Choose a collection (or multiple collections) to do
                        plots -- Leave blank to get all categories from file
  --weighting weighting_list
                        File containing list of weighting schemes you want
  --lumi luminosity     Target luminosity for each histogram -- Overridden if
                        Datalist option is present
  --outputName OUTPUTNAME
                        Name of output ROOT file containing all plots.
  --noLog               Disables log plots
  --noOverflow          Disables overflow bin
  --systematics SYSTEMATICS
                        File containing list of central, upper and lower limit
                        of scale factors

Run chef_histogram.py first in order to obtain the histograms!
```

File specified in `plotprops`, `preselection`, `weighting`, and `systematics` can use the same format as in `chef_histogram.py`.

### File in `plot_list_MC`
Each line must contain the path to the histogram file, name of the process used to generate the histograms with, the proper name, and the colour code based on [ROOT `TColor` class](https://root.cern.ch/doc/master/classTColor.html). For example, 
```
hist_ttbar.root ttbar t#bar{t}ll 633
```
Specifies the chef to use `hist_ttbar.root` file, look for histograms using the name ttbar, and copy into the plot with the proper name t#bar{t}ll in the legend with slightly dark red colour (633). **If the colour code is 1 (black or `kBlack` by ROOT enum), the histogram will be drawn as a solid line instead. Only one histogram can be allowed to be drawn in the form of a line.**

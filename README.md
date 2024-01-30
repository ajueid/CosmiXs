![alt text](http://github.com/ajueid/DMSpectra/blob/main/img/Logo.png?raw=true)

# CosmiXs: Cosmic messenger spectra for indirect dark matter searches 

The CosmiXs code and repository provides the source spectra at production for the cosmic messengers relevant for dark matter indirect searches, namely $\bar{p}, e^+, \gamma$ or $\nu$. The spectra have been generated with PYTHIA version 8.309 and the VINCIA antenna shower algorithm feeded by amplitudes generated by the MadDM code. The spectra are here provided for dark-matter masses between $5$ GeV and $100$ TeV (with a grid of 64 mass values) and for 29 annihilation channels. For each mass and each annihilation channel, five million events have been generated. 

The annhilation channels are:

* Fermionic channels  

$$
\chi \chi \to e_L^+ e_L^-, e_R^+ e_R^-, e^+ e^-, \mu_L^+ \mu_L^-, \mu_R^+ \mu_R^-, \mu^+ \mu^-, \tau^+_L \tau^-_L, \tau^+_R \tau^-_R, \tau^+ \tau^-, \nu \bar{\nu}, u\bar{u}, d\bar{d}, s\bar{s}, c\bar{c}, b\bar{b}, t\bar{t}.
$$

* Bosonic channels  

$$
\chi\chi \to \gamma\gamma, gg, W^+ W^-, W^+_L W^-_L, W^+_T W^-_T, ZZ, Z_L Z_L, Z_T Z_T, HH, \gamma Z, HZ.
$$

## Novelty of this Analysis

* Inclusion of off-shell effects for $WW, ZZ, HZ$ producing four fermions and covering DM masses from 5 GeV to $M_X, X=W,Z$. 
* Inclusion of helicity information through the LHEF (used as input for PYTHIA). Using the VINCIA shower plugin, which is based on the helicity-depedent Antenna shower, electroweak corrections are taken properly into account.
* Spectra for new channels not previously calculated: $\gamma Z$ and $HZ$.
* Running quark masses are used for the quark annihilation channels.
* Full one-loop form factors are used for the one-loop induced annihilation channels: $\gamma\gamma$, $gg$ and $\gamma Z$.

## Structure of the repository

The repository provides data and code orgenized as follows: 
* `Data/` directory: includes the source spectra for the following cosmic messengers:  
    * AtProduction-AntiP.dat: for the spectra of $\bar{p}$.
    * AtProduction-Gamma.dat: for the spectra of $\gamma$ rays.
    * AtProduction-Nuel.dat: for the spectra of $\nu_e$.
    * AtProduction-Numu.dat: for the spectra of $\nu_\mu$.
    * AtProduction-Nuta.dat: for the spectra of $\nu_\tau$.
    * AtProduction-Positrons.dat: for the spectra of $e^+$.
* `Scripts/` directory: includes the necessary files and commands to generate the spectra:
    * `Models/` directory: includes the model files in the Universal FeynRules Output (UFO) format and includes
        * `DMsimp_s_spin0_MD/` for the simplified model with pseudo-scalar mediator.
        * `DMsimp_s_spin1_MD/` for the simplified model with vector mediator.
        * `ScalarHiggsPortal_NLO_UFO/` for the minimal model with Higgs portal including full NLO QCD corrections.
    * `main101.cc`: a minimal C++ code to calculate the spectra for the cosmic messengers included here with PYTHIA. This code reads the input from `spectrum.cmnd`.
    * `scripts_togenerate.txt`: A plain text file that shows instructions on how to generate events in MadDM.
    * `spectrum.cmnd`: A basic input file to be read by PYTHIA code `main101.cc`, which includes all the necessary parameters to properly activate the VINCIA shower algorithm and generate the spectra.
* `Interpolate.py`: Python code snippet to perform mass interpolations.
* `Example.py`: Python example on how to call the `Interpolate` class and calculate the spectra for dark matter mass values not included in our tables.

## Structure of the Tables

For each cosmic messenger, there is a dedicated file in ASCII format. The tables can be found in the folder `Data/`, where we provide the spectra for 29 annihilation channels and 6 cosmic messengers named as 

AtProduction-FS.dat where FS=AntiP, Gamma, Nuel, Numu, Nuta, Positrons. 

Each file contains 31 columns: The DM mass in GeV, the fraction x -- defined as the kinetic energy divided by the DM mass in 100 bins on the logarithmic scale and the spectrum in units of dN/dlog10(x). The rest of the columns are organised as follows:

```console
dNdlog10(x) [eL]   	dNdlog10(x) [eR] 	 dNdlog10(x) [e]     dNdlog10(x) [muL]   dNdlog10(x) [muR]		dNdlog10(x) [mu]     		dNdlog10(x) [tauL]   	dNdlog10(x) [tauR]  dNdlog10(x) [tau]   dNdlog10(x) [nue]   dNdlog10(x) [numu]   	dNdlog10(x) [nutau]		dNdlog10(x) [u]  		dNdlog10(x) [d]  	 dNdlog10(x) [s]  	  dNdlog10(x) [c]     dNdlog10(x) [b]   		dNdlog10(x) [t]		dNdlog10(x) [a] 		dNdlog10(x) [g]     dNdlog10(x) [W]     dNdlog10(x) [WL]    dNdlog10(x) [WT]        dNdlog10(x) [Z]        dNdlog10(x) [ZL]       dNdlog10(x) [ZT]    dNdlog10(x) [H]     dNdlog10(x) [aZ]	   dNdlog10(x)[ HZ ]    		  
```

## How to generate the spectra with MadDM

Here we show how to generate the spectra for three examples: 

* $\chi \chi \to b\bar{b}$ using the Higgs portal model:
    * `import model ScalarHiggsPortal_NLO_UFO`
    * `define darkmatter n1`
    * `generate indirect_detection b b~`
    * `output folder_name`
    * `launch folder_name`
    * `set indirect = flux_source`
    * `set save_indirect_cont 1e-3`
    * `set save_output spectra`
    * `set precise`
    * `set sigmav_method madevent`
    * `set nevents 100000`
    * `set msdm 1000`

* $\chi\chi \to \nu_e \bar{\nu}_e$ using a simplified model with spin-1 mediator:
    * `import model DMsimp_s_spin1_MD`
    * `define darkmatter ~xd`
    * `generate indirect_detection ve ve~`
    * `output folder_name`
    * `launch folder_name`
    * `set indirect = flux_source`
    * `set gnu11 0.25` 
    * `set gnu22 0.25` 
    * `set gnu33 0.25`
    * `set save_indirect_cont 1e-3`
    * `set save_output spectra`
    * `set precise`
    * `set sigmav_method madevent` 
    * `set nevents 100000`
    * `set msdm 1000`

* $\chi\chi \to HZ$ using a simplified model with pseudo-scalar mediator:
    * `import model DMsimp_s_spin0_MD`
    * `define darkmatter ~xd`
    * `generate ~xd ~xdb > h z`
    * `output folder_name`
    * `launch folder_name` 
    * `set indirect = flux_source`
    * `set save_indirect_cont 1e-3`
    * `set save_output spectra`
    * `set precise`
    * `set sigmav_method madevent` 
    * `set nevents 10000`
    * `set msdm 1000`

## Setup for the VINCIA Antenna shower

* Parameters to select the VINCIA shower with full-fledged electroweak corrections
    * `PartonShowers:model   = 2`
    * `Vincia:ewMode         = 3`
    * `TimeShower:pTminWeak = 1.0000000000e-01`
    * `WeakShower:singleEmission = off`

* Parameters of the Lund string model
    * `StringZ:aLund         =  0.337409`
    * `StringZ:bLund         =  0.784682`
    * `StringPT:sigma        =  0.296569`
    * `StringZ:aExtraDiquark =  1.246986`

* To enable for PYTHIA to decay the muon, $\pi^\pm$, $K_L$, $K^0$ and the neutron 
    * `13:mayDecay=on`
    * `211:mayDecay=on`
    * `321:mayDecay=on`
    * `310:mayDecay=on`
    * `2112:mayDecay=on`

## To Do

* Generate the spectra for DM masses from 100 TeV to 1 PeV.
* Add a code snippet to quickly plot the spectra and perform comparisons.
* Add a code snippet to obtain the spectra for a decaying DM.
* Generate the spectra for the off-shell $W_L W_L, W_T W_T, Z_L Z_L$ and $Z_T Z_T$

## Citations

If you use these Tables please cite:

- [C. Arina, M. Di Mauro, N. Fornengo, J. Heisig, A. Jueid, R. Ruiz de Austri, e-Print:2312.01153](https://arxiv.org/abs/2312.01153)

If you would like to assess QCD uncertainties on the spectra (repo can be found on https://github.com/ajueid/qcd-dm.github.io), please cite:

- [A. Jueid, J.Kip, R. Ruiz de Austri, P.Skands, e-Print:2303.11363](https://arxiv.org/abs/2303.11363)
- [A. Jueid, J.Kip, R. Ruiz de Austri, P.Skands, JCAP 04 (2023) 068](https://arxiv.org/abs/2202.11546)
- [S. Amoroso, S. Caron, A. Jueid, R. Ruiz de Austri, P.Skands, JCAP 05 (2019) 007](https://arxiv.org/abs/1812.07424)


## Contact
If you have any question or bug reports, please contact:
* Mattia Di Mauro (dimauro.mattia@gmail.com)
* Adil Jueid (adil.hep@gmail.com)
* Roberto Ruiz de Austri (rruiz@ific.uv.es)

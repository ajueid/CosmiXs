# Updated spectra of stable particles from dark matter

We provide the spectra of the cosmic messengers such as $\bar{p}, e^+, \gamma$ or $\nu$ at the production for various annihilation channels and dark matter masses. In this case, we use PYTHIA version 8.310 and the VINCIA antenna shower algorithm. The spectra is generated for dark-matter masses between $5$ GeV and $100$ TeV (with a grid of 64 mass values) and 29 annihilation channels. For each mass point and each annihilation channel we have generated five million events using MadDM and passed to PYTHIA 8.310 using VINCIA shower. The annhilation channels considered in this work are:

* Fermionic channels  

$$
\chi \chi \to e_L^+ e_L^-, e_R^+ e_R^-, e^+ e^-, \mu_L^+ \mu_L^-, \mu_R^+ \mu_R^-, \mu^+ \mu^-, \tau^+_L \tau^-_L, \tau^+_R \tau^-_R, \tau^+ \tau^-, \nu \bar{\nu}, u\bar{u}, d\bar{d}, s\bar{s}, c\bar{c}, b\bar{b}, t\bar{t}.
$$

* Bosonic channels  

$$
\chi\chi \to \gamma\gamma, gg, W^+ W^-, W^+_L W^-_L, W^+_T W^-_T, ZZ, Z_L Z_L, Z_T Z_T, HH, \gamma Z, HZ.
$$

## Structure of the repository

The repository includes the following  
* `Data/` directory includes the spectra at the source for the following cosmic messengers:  
    * AtProduction-AntiP.dat: for the spectra of $\bar{p}$.
    * AtProduction-Gamma.dat: for the spectra of $\gamma$ rays.
    * AtProduction-Nuel.dat: for the spectra of $\nu_e$.
    * AtProduction-Numu.dat: for the spectra of $\nu_\mu$.
    * AtProduction-Nuta.dat: for the spectra of $\nu_\tau$.
    * AtProduction-Positrons.dat: for the spectra of $e^+$.
* `Scripts/` directory includes the necessary files and commands to generate the spectra:
    * `Models/` directory includes the model files in the Universal FeynRules Output (UFO) format and includes
        * `DMsimp_s_spin0_MD/` for the simplified model with pseudo-scalar mediator.
        * `DMsimp_s_spin1_MD/` for the simplified model with vector mediator.
        * `ScalarHiggsPortal_NLO_UFO/` for the minimal model with Higgs portal including full NLO QCD corrections.
    * `main101.cc`: a minimal C++ code that calculate the spectra for the cosmic messengers included here with PYTHIA. This code reads the input from `spectrum.cmnd`.
    * `scripts_togenerate.txt`: A plain text file that shows instructions on how to generate events in MadDM.
    * `spectrum.cmnd`: A basic input file to be read by PYTHIA code `main101.cc` and which includes all the necessary parameters to properly activate VINCIA shower algorithm and generate the spectra.
* `Interpolate.py`: Python code snippet to perform mass interpolations.
* `Example.py`: Python example on how to call `Interpolate` class and calculate the spectra for mass values not included in our tables.

## Structure of the Tables

For each stable final state, there is one dedicated file in ascii format. The tables can be found in the following folder `Data/`: 

In this folder, we provide the spectra for 29 annihilation channels and 6 cosmic messengers. Each file contains 31 columns: The DM mass in GeV, the fraction x -- defined as the kinetic energy divided by the DM mass in 100 bins on the logarithmic scale. The rest of the columns are organised as 

```console
dNdx [eL]   	dNdx [eR] 	 dNdx [e]     dNdx [muL]   dNdx [muR]		dNdx [mu]     		dNdx [tauL]   	dNdx [tauR]  dNdx [tau]   dNdx [nue]   dNdx [numu]   	dNdx [nutau]		dNdx [u]  		dNdx [d]  	 dNdx [s]  	  dNdx [c]     dNdx [b]   		dNdx [t]		dNdx [a] 		dNdx [g]     dNdx [W]     dNdx [WL]    dNdx [WT]        dNdx [Z]        dNdx [ZL]       dNdx [ZT]    dNdx [H]     dNdx [aZ]	   dNdx[ HZ ]    		  
```
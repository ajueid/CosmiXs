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

<a name="structure"></a>
## Package structure
&emsp; The package consists of the following:
* `run.sh` shall script that used to excute the package
* `scan_input.py` input file that the user has to fill it. The user can control the run via the switches in this file
* `ML_regressor_genericFunctions.ipynb` google colab notebook that inclide the scan over the generic fucntions. The user can use it to scan ov\
er defined function. The class `scan()` include the following ML models:
  * DNNR: MLP regressor with 4 hidden layers, 100 nueron each and MSE loss function.
  * GBR : GradientBoostingRegressor
  * RFR : RandomForestRegressor
  * SVMRBF: Supported vector regressor with RBF kernel
  * SVMPOLY: Supported vector regressor with polynomial kernel
* `docs/` directory include the following:
  * `Install` documentary on how to install the package
  * `Run the package` documentay on how to run the package
  * `how to adjust the input file` documentray on how the user adjust the input file
  * `work flow` explaination how the package modules and inhertied functions work
* `source/` directory inculde the following source files:
  * `auxiliary.py`  include the auxiliary functions to link spheno with HB/HS and functions for parallel run
  * `MLs_HEP.py`   main file with the scanner loop. The class `scan()` is used to access the type of the needed ML

```console
# DM 	    Log10[x]     dNdx[ eL ]   			dNdx[ eR ]    		dNdx[ e	]      dNdx[ muL ]     		dNdx[ muR ]    		dNdx[ mu ]     		dNdx[ tauL ]     	dNdx[ tauR ]     	dNdx[ tau ]   		dNdx[ u ]  		dNdx[ d ]  		dNdx[ s ]  		dNdx[ c ]    		dNdx[ b ]   		dNdx[ t ]		dNdx[ a ] 		dNdx[ g	]   dNdx[ W ]   	dNdx[ Z ]    		dNdx[ H ]   		dNdx[ aZ ]	dNdx[ HZ ]    		dNdx[ nue ]   		dNdx[ numu ]   	dNdx[ nutau ]
```

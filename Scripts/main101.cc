#include "Pythia8/Pythia.h"
#include "math.h"
#include <iostream>
#include <string>

using namespace std;
using namespace Pythia8; 
int main() {

  // You can always read an plain LHE file,
  // but if you ran "./configure --with-gzip" before "make"
  // then you can also read a gzipped LHE file.
  //#ifdef GZIPSUPPORT
  //bool useGzip = true;
  //#else
  //bool useGzip = false;
  //#endif
  //cout << " useGzip = " << useGzip << endl;

  // Generator. We here stick with default values, but changes
  // could be inserted with readString or readFile.
  Pythia pythia;

  // Initialize Les Houches Event File run. List initialization information.
  //pythia.readString("Beams:frameType = 4");
  //if (useGzip) pythia.readString("Beams:LHEF = ww_events.lhe.gz");
  //else         pythia.readString("Beams:LHEF = ww_events.lhe");
  pythia.readFile("spectrum.cmnd");

  //pythia.settings.mode("Next:numberCount",1000);
  //pythia.settings.mode("Next:numberShowInfo",1);
  //pythia.settings.mode("Next:numberShowProcess",1);
  //pythia.settings.mode("Next:numberShowEvent",1);
  
  //pythia.settings.flag("PartonLevel:ISR",false);
  //pythia.settings.flag("PartonLevel:MPI",false);
  //pythia.settings.flag("PDF:lepton",false);
  //pythia.settings.flag("TimeShower:weakShower",true);
  //pythia.settings.mode("TimeShower:weakShowerMode",0);
  //pythia.settings.mode("TimeShower:pTminWeak",0.1);

  // Initialization
  pythia.init();
 
  // Allow for possibility of a few faulty events.
  int nAbort = 10;
  int iAbort = 0;

  // Setting for the histrogram and choice of variables
  double mDM = pythia.parm("Main:spareParm1"); // divide by the DM mass to get the x variable
  string outdir   = pythia.word("Main:spareWord1"); // Where to write the output files
  cout << "mDM: " << mDM << " outdir: "<<  outdir <<endl;

  double eminh = -9.;
  double emaxh = 0.;
  double nbins = 100;
  double DeltaBin = (emaxh-eminh)/nbins;  

  // Histogram particle spectra
  Hist gamma("gamma spectrum", nbins, eminh, emaxh);
  Hist electron("e+- spectrum", nbins, eminh, emaxh);
  Hist proton("p spectrum", nbins, eminh, emaxh);
  Hist nue("nu_e spectrum", nbins, eminh, emaxh);
  Hist numu("nu_mu spectrum", nbins, eminh, emaxh);
  Hist nutau("nu_tau spectrum", nbins, eminh, emaxh);
  Hist rest("remaining particle spectrum", nbins, eminh, emaxh);

 // Begin event loop.
  int nEvent = 0;
  int maxevent = pythia.settings.mode("Main:NumberOfEvents");

  for (int iEvent = 0; (iEvent < maxevent || maxevent <= 0) ; ++iEvent) {
    // Generate events. Quit if many failures.
    if (!pythia.next()) {
      if (++iAbort < nAbort) continue;
      cout << "Event generation aborted prematurely, owing to error!\n";
      break;
    }

    // Loop over all particles and select wished final state particles for histrograms.
    for (int i = 0; i < pythia.event.size(); ++i) 
      if (pythia.event[i].isFinal()) {
	int idAbs  = pythia.event[i].idAbs();
	int idap  = pythia.event[i].id();
	double eI  = log10((pythia.event[i].e()-pythia.event[i].m())/mDM);
	//select photons
	if (idAbs == 22) gamma.fill(eI); 
	//select electrons (positron equivalent)
	else if (idap == -11)  electron.fill(eI);
	//select proton
	else if (idap == -2212 or idAbs == 2112) proton.fill(eI);
	// select various neutrinos
	else if (idap == 12) nue.fill(eI);
	else if (idap == 14) numu.fill(eI);
	else if (idap == 16) nutau.fill(eI);
	else {
	  rest.fill(eI);
	  //cout << "Error: stable id = " << pythia.event[i].id() << endl;
	}
      }
  // End of event loop
    nEvent = iEvent;
  }
  

  //Statistic and histrograms
  pythia.stat();
  
  gamma.operator*=(1./nEvent/DeltaBin);
  electron.operator*=(1./nEvent/DeltaBin);
  proton.operator*=(1./nEvent/DeltaBin);
  nue.operator*=(1./nEvent/DeltaBin);
  numu.operator*=(1./nEvent/DeltaBin);
  nutau.operator*=(1./nEvent/DeltaBin);

  gamma.table("gammas_spectrum_pythia8.dat");
  electron.table("positrons_spectrum_pythia8.dat");
  proton.table("antiprotons_spectrum_pythia8.dat");
  nue.table("neutrinos_e_spectrum_pythia8.dat");
  numu.table("neutrinos_mu_spectrum_pythia8.dat");
  nutau.table("neutrinos_tau_spectrum_pythia8.dat");
  rest.table("restx_spectrum_pythia8.dat");

  cout << gamma << electron << proton << nue << numu << nutau << rest;
  
  //Done
  return 0;
}

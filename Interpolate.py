import pandas as pd
from pathlib import Path

# Interpolates the computed spectra and their uncertainties for given parameters
# Heavily based on the interpolate.py code shipped in the following github repo
# https://github.com/ajueid/qcd-dm.github.io.git

class Interpolate:
    def __init__(self, mass, channel, final_state, path = None):
        self.mass = mass
        self.channel = channel 
        self.final_state = final_state
        self.path = path

        self._check_input_parameters()

    #Checks if the input parameters are in a proper format
    def _check_input_parameters(self):
        self._check_mass_format()
        self._check_channel_name()
        self._check_final_state_name()

    # Checks if the entry for mass is a number and if it is between the computed bounds.
    def _check_mass_format(self):
        try:
            self.mass = float(self.mass)
            if self.mass < 5.0:
                raise Exception('The dark-matter mass needs to be higher than 5 GeV')
            elif self.mass > 100000:
                raise Exception('The dark-matter mass needs to be lower than 100 TeV')
        except ValueError:
            raise ValueError('The mass entry needs to be a number')

    # Checks if the given final-state name is in the tables.
    def _check_final_state_name(self):
        valid_final_states = ['AntiP', 'Gamma', 'Nuel', 'Numu', 'Nuta', 'Positrons']
        if self.final_state not in valid_final_states:
            raise NameError('{} is not valid. Valid final states are AntiP, Gamma, Nuel, Numu, Nuta or Positrons'.format(self.final_state))

    # Checks if the given channel name is in the tables.
    def _check_channel_name(self):
        valid_channels = ['eL', 'eR', 'e', 'muL', 'muR', 'mu', 'tauL', 'tauR', 'tau', 'nue', 'numu', 'nutau', 'u', 'd', 's', 'c', 'b', 't', 'a', 'g', 'W', 'WL', 'WT', 'Z', 'ZL', 'ZT', 'H', 'aZ', 'HZ']
        if self.channel not in valid_channels:
            raise NameError('{} is not a valid channel. Valid channels are eL, eR, e, muL, muR, mu, tauL, tauR,	tau, nue, numu or nutau, u, d, s, c, b, t, a, g, W, WL, WT, Z, ZL, ZT, H, aZ or HZ'.format(self.channel))

    # Fetches the requested data from the appropriate table.
    def _get_data_from_table(self):
        if self.path == None:
            df = pd.read_table('{0}/{1}'.format(Path(__file__).parent.absolute(), 'Data/AtProduction-{}.dat'.format(self.final_state)), sep = '\s\s+', engine='python')
        else:
            df = pd.read_table('{0}/AtProduction-{1}.dat'.format(self.path, self.final_state), sep = '\s\s+', engine='python')
        dm = df['# DM']
        
        if not '+DHad [{}]'.format(self.channel) in list(df.columns):
            if self.mass in dm.unique():
                x       = list(df[df['# DM'] == self.mass]['Log10[x]'])
                dNdLog10x    = list(df[df['# DM'] == self.mass]['dNdLog10x [{}]'.format(self.channel)])
                return x, dNdLog10x
            else:
                mass_lower, mass_upper = self._check_mass_enclosure(dm)
                x_upper       = list(df[df['# DM'] == mass_upper]['Log10[x]'])
                dNdx_upper    = list(df[df['# DM'] == mass_upper]['dNdLog10x [{}]'.format(self.channel)])
                x_lower       = list(df[df['# DM'] == mass_lower]['Log10[x]'])
                dNdx_lower    = list(df[df['# DM'] == mass_lower]['dNdLog10x [{}]'.format(self.channel)])
                return mass_upper, x_upper, dNdx_upper, mass_lower, x_lower, dNdx_lower
    
    # Checks between wich two computed masses the user-specified mass is.
    def _check_mass_enclosure(self, dm):
        masses = dm.unique()
        for m in masses:
            if self.mass < m:
                mass_upper = m
                break
            mass_lower = m
        return mass_lower, mass_upper
    
    # Computes the linear fit between two points and subsequently returns the corresponding value for a given mass.
    def _linear_function(self, mass_lower, mass_upper, flux_lower, flux_upper):
        a = (flux_lower - flux_upper)/(mass_lower-mass_upper)
        b = (flux_upper*mass_lower - flux_lower*mass_upper)/(mass_lower - mass_upper)
        return a * self.mass + b
    
    # Call _linear_function for all variations and values of x and returns the computed arrays.
    def _linear_interpolation(self):
        data = self._get_data_from_table()
        if len(data) == 2:
            return data
        elif len(data) == 6:
            dNdLog10x = []
            for i in range(len(data[1])):
                dNdLog10x.append(self._linear_function(data[3], data[0], data[2][i], data[5][i]))
            return data[1], dNdLog10x

    # A dataframe is being made that will be the final output.
    def _generate_dataframe_output(self, f):
        return pd.DataFrame(data = {'Log10[x]': f[0], 'dNdLog10x': f[1]})

    # The function that will provide the output of the spectrum for a given mass, channel, and final state in a pandas dataframe format.
    def make_spectrum(self):
        f = self._linear_interpolation()
        return self._generate_dataframe_output(f)

def annihilation_spectrum(mass, channel, final_state, path=None):
    """
    Returns the linearly interpolated data for the given arguments in a pandas dataframe format

    Parameters:     
        mass : float
            The mass of the annihilating particle in GeV.

        channel : str 
            The annihilation channels. The accepted channels are eL, eR, e, muL, muR, mu, tauL, tauR, tau, nue, numu or nutau, u, d, s, c, b, t, a, g, W, WL, WT, Z, ZL, ZT, H, aZ or HZ
        
        final_state : str
            The spectra of final-state particles. Accepted arguments are AntiP, Gamma, Nuel, Numu, Nuta, Positrons. These stand for antiprotons, gamma rays, electron neutrinos, muon neutrinos, tau neutrinos, or positrons respectively.

        path : str, optional
            The path to the annihilation spectra tables. 
                        
    Returns:        
        pandas.DataFrame   

    """
    spectrum = Interpolate(mass, channel, final_state, path)
    return spectrum.make_spectrum()



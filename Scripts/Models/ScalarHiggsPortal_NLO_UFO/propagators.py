
# This file was automatically created by The UFO_usermod   

from object_library import all_propagators, Propagator
S = Propagator(name = 'S',
               numerator = 'complex(0,1)',
               denominator = 'P(\'mu\', id) * P(\'mu\', id) - Mass(id) * Mass(id) + complex(0,1) * Mass(id) * Width(id)')


F = Propagator(name = 'F',
               numerator = 'complex(0,1) * (Gamma(\'mu\', 1, 2) * P(\'mu\', id) + Mass(id) * Identity(1, 2))',
               denominator = 'P(\'mu\', id) * P(\'mu\', id) - Mass(id) * Mass(id) + complex(0,1) * Mass(id) * Width(id)')


V1 = Propagator(name = 'V1',
                numerator = 'complex(0,1) * (-1 * Metric(1, 2) + Metric(1,\'mu\')* P(\'mu\', id) * P(2, id) / Mass(id)**2 ',
                denominator = 'P(\'mu\', id) * P(\'mu\', id) - Mass(id) * Mass(id) + complex(0,1) * Mass(id) * Width(id)')


V2 = Propagator(name = 'V2',
                numerator = 'complex(0,-1) * Metric(1, 2)',
                denominator = 'P(\'mu\', id) * P(\'mu\', id)')


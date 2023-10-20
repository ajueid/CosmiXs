
# This file was automatically created by The UFO_usermod        

import cmath
from object_library import all_functions, Function

complexconjugate = Function(arguments = ('z',),
                            expression = 'z.conjugate()',
                            name = 'complexconjugate')


re = Function(arguments = ('z',),
              expression = 'z.real',
              name = 're')


im = Function(arguments = ('z',),
              expression = 'z.imag',
              name = 'im')


sec = Function(arguments = ('z',),
               expression = '1./cmath.cos(z.real)',
               name = 'sec')


asec = Function(arguments = ('z',),
                expression = 'cmath.acos(1./(z.real))',
                name = 'asec')


csc = Function(arguments = ('z',),
               expression = '1./cmath.sin(z.real)',
               name = 'csc')


acsc = Function(arguments = ('z',),
                expression = 'cmath.asin(1./(z.real))',
                name = 'acsc')


cot = Function(arguments = ('z',),
               expression = '1./cmath.tan(z.real)',
               name = 'cot')


theta_function = Function(arguments = ('x','y','z'),
                          expression = 'y if x else z',
                          name = 'theta_function')


cond = Function(arguments = ('condition','ExprTrue','ExprFalse'),
                expression = '(ExprTrue if condition==0.0 else ExprFalse)',
                name = 'cond')


reglog = Function(arguments = 'z',
                  expression = '(0.0 if z==0.0 else cmath.log(z.real))',
                  name = 'reglog')


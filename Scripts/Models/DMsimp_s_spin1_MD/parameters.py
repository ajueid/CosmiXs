# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 11.0.1 for Mac OS X x86 (64-bit) (September 21, 2016)
# Date: Wed 26 Oct 2016 18:23:35



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

gVXc = Parameter(name = 'gVXc',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{VXc}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 1 ])

gVXd = Parameter(name = 'gVXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{VXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 2 ])

gAXd = Parameter(name = 'gAXd',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{AXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 3 ])

gVd11 = Parameter(name = 'gVd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 4 ])

gVu11 = Parameter(name = 'gVu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 5 ])

gVd22 = Parameter(name = 'gVd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 6 ])

gVu22 = Parameter(name = 'gVu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 7 ])

gVd33 = Parameter(name = 'gVd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 8 ])

gVu33 = Parameter(name = 'gVu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 9 ])

gVl11 = Parameter(name = 'gVl11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ve}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 10 ])

gVl22 = Parameter(name = 'gVl22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Vmu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 11 ])

gVl33 = Parameter(name = 'gVl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Vta}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 12 ])

gAd11 = Parameter(name = 'gAd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 13 ])

gAu11 = Parameter(name = 'gAu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 14 ])

gAd22 = Parameter(name = 'gAd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 15 ])

gAu22 = Parameter(name = 'gAu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 16 ])

gAd33 = Parameter(name = 'gAd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 17 ])

gAu33 = Parameter(name = 'gAu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 18 ])

gAl11 = Parameter(name = 'gAl11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ae}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 19 ])

gAl22 = Parameter(name = 'gAl22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Amu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 20 ])

gAl33 = Parameter(name = 'gAl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ata}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 21 ])

gnu11 = Parameter(name = 'gnu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{nue}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 22 ])

gnu22 = Parameter(name = 'gnu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{num}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 23 ])

gnu33 = Parameter(name = 'gnu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{nut}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 24 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MXr = Parameter(name = 'MXr',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXr}',
                lhablock = 'MASS',
                lhacode = [ 5000511 ])

MXc = Parameter(name = 'MXc',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXc}',
                lhablock = 'MASS',
                lhacode = [ 5000512 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 5000521 ])

MY1 = Parameter(name = 'MY1',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MY1}',
                lhablock = 'MASS',
                lhacode = [ 5000001 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WY1 = Parameter(name = 'WY1',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WY1}',
                lhablock = 'DECAY',
                lhacode = [ 5000001 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  texname = '\\text{I1a12}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a22}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x1)',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I2a12}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a22}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yup',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yup',
                  texname = '\\text{I3a12}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yc',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yc',
                  texname = '\\text{I3a22}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys',
                  texname = '\\text{I4a12}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ydo',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ys',
                  texname = '\\text{I4a22}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I4a33}')


# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Fri 28 Feb 2020 16:27:26



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
KprimeRe = Parameter(name = 'KprimeRe',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{KprimeRe}',
                     lhablock = 'NP',
                     lhacode = [ 1 ])

KprimeIm = Parameter(name = 'KprimeIm',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KprimeIm}',
                     lhablock = 'NP',
                     lhacode = [ 2 ])

Epsilon = Parameter(name = 'Epsilon',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{Epsilon}',
                    lhablock = 'NP',
                    lhacode = [ 3 ])

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

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

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

MFm1 = Parameter(name = 'MFm1',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MFm1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

MFm2 = Parameter(name = 'MFm2',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MFm2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000006 ])

MFm3 = Parameter(name = 'MFm3',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MFm3}',
                 lhablock = 'MASS',
                 lhacode = [ 9000007 ])

MFz1 = Parameter(name = 'MFz1',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MFz1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000008 ])

MFz2 = Parameter(name = 'MFz2',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MFz2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000009 ])

MFz3 = Parameter(name = 'MFz3',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MFz3}',
                 lhablock = 'MASS',
                 lhacode = [ 9000010 ])

MS11 = Parameter(name = 'MS11',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS11}',
                 lhablock = 'MASS',
                 lhacode = [ 9000011 ])

MS12 = Parameter(name = 'MS12',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS12}',
                 lhablock = 'MASS',
                 lhacode = [ 9000012 ])

MS13 = Parameter(name = 'MS13',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS13}',
                 lhablock = 'MASS',
                 lhacode = [ 9000013 ])

MS21 = Parameter(name = 'MS21',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS21}',
                 lhablock = 'MASS',
                 lhacode = [ 9000014 ])

MS22 = Parameter(name = 'MS22',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS22}',
                 lhablock = 'MASS',
                 lhacode = [ 9000015 ])

MS23 = Parameter(name = 'MS23',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS23}',
                 lhablock = 'MASS',
                 lhacode = [ 9000016 ])

MS31 = Parameter(name = 'MS31',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS31}',
                 lhablock = 'MASS',
                 lhacode = [ 9000017 ])

MS32 = Parameter(name = 'MS32',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS32}',
                 lhablock = 'MASS',
                 lhacode = [ 9000018 ])

MS33 = Parameter(name = 'MS33',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS33}',
                 lhablock = 'MASS',
                 lhacode = [ 9000019 ])

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

WFm1 = Parameter(name = 'WFm1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{WFm1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

WFm2 = Parameter(name = 'WFm2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WFm2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

WFm3 = Parameter(name = 'WFm3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WFm3}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000007 ])

WFz1 = Parameter(name = 'WFz1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{WFz1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000008 ])

WFz2 = Parameter(name = 'WFz2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WFz2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000009 ])

WFz3 = Parameter(name = 'WFz3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WFz3}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000010 ])

WS11 = Parameter(name = 'WS11',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS11}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000011 ])

WS12 = Parameter(name = 'WS12',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS12}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000012 ])

WS13 = Parameter(name = 'WS13',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS13}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000013 ])

WS21 = Parameter(name = 'WS21',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS21}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000014 ])

WS22 = Parameter(name = 'WS22',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS22}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000015 ])

WS23 = Parameter(name = 'WS23',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS23}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000016 ])

WS31 = Parameter(name = 'WS31',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS31}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000017 ])

WS32 = Parameter(name = 'WS32',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS32}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000018 ])

WS33 = Parameter(name = 'WS33',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WS33}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000019 ])

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

K = Parameter(name = 'K',
              nature = 'internal',
              type = 'complex',
              value = 'Epsilon*KprimeRe',
              texname = 'K')

Kprime = Parameter(name = 'Kprime',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*KprimeIm + KprimeRe',
                   texname = '\\text{Kprime}')

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

Hvev = Parameter(name = 'Hvev',
                 nature = 'internal',
                 type = 'real',
                 value = 'vev',
                 texname = '\\text{Hvev}')

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

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')


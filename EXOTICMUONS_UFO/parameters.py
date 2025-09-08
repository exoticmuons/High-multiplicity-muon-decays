# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.2.0 for Mac OS X ARM (64-bit) (December 26, 2024)
# Date: Mon 8 Sep 2025 08:32:52



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

alpha = Parameter(name = 'alpha',
                  nature = 'external',
                  type = 'real',
                  value = 0.0072973525205055605,
                  texname = '\\alpha',
                  lhablock = 'FRBlock',
                  lhacode = [ 1 ])

Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 1000000,
                   texname = '\\text{Lambda}',
                   lhablock = 'FRBlock',
                   lhacode = [ 2 ])

c1mue = Parameter(name = 'c1mue',
                  nature = 'external',
                  type = 'real',
                  value = 0.10566,
                  texname = '\\text{c1mue}',
                  lhablock = 'FRBlock',
                  lhacode = [ 3 ])

c1emu = Parameter(name = 'c1emu',
                  nature = 'external',
                  type = 'real',
                  value = 0.10566,
                  texname = '\\text{c1emu}',
                  lhablock = 'FRBlock',
                  lhacode = [ 4 ])

c2mue = Parameter(name = 'c2mue',
                  nature = 'external',
                  type = 'real',
                  value = 0.10566,
                  texname = '\\text{c2mue}',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

c2emu = Parameter(name = 'c2emu',
                  nature = 'external',
                  type = 'real',
                  value = 0.10566,
                  texname = '\\text{c2emu}',
                  lhablock = 'FRBlock',
                  lhacode = [ 6 ])

c3mue = Parameter(name = 'c3mue',
                  nature = 'external',
                  type = 'real',
                  value = 0.10566,
                  texname = '\\text{c3mue}',
                  lhablock = 'FRBlock',
                  lhacode = [ 7 ])

c3emu = Parameter(name = 'c3emu',
                  nature = 'external',
                  type = 'real',
                  value = 0.10566,
                  texname = '\\text{c3emu}',
                  lhablock = 'FRBlock',
                  lhacode = [ 8 ])

cSee = Parameter(name = 'cSee',
                 nature = 'external',
                 type = 'real',
                 value = 0.0001,
                 texname = '\\text{cSee}',
                 lhablock = 'FRBlock',
                 lhacode = [ 9 ])

Mmu = Parameter(name = 'Mmu',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{Mmu}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.02,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 9000001 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.0005110000000000001,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

Wmu = Parameter(name = 'Wmu',
                nature = 'external',
                type = 'real',
                value = 0.0001,
                texname = '\\text{Wmu}',
                lhablock = 'DECAY',
                lhacode = [ 13 ])

WS = Parameter(name = 'WS',
               nature = 'external',
               type = 'real',
               value = 0.0001,
               texname = '\\text{WS}',
               lhablock = 'DECAY',
               lhacode = [ 9000001 ])


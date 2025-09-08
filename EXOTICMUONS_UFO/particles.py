# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.2.0 for Mac OS X ARM (64-bit) (December 26, 2024)
# Date: Mon 8 Sep 2025 08:32:52


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.Mmu,
                       width = Param.Wmu,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = 0)

mu__plus__ = mu__minus__.anti()

S = Particle(pdg_code = 9000001,
             name = 'S',
             antiname = 'S',
             spin = 1,
             color = 1,
             mass = Param.MS,
             width = Param.WS,
             texname = 'S',
             antitexname = 'S',
             charge = 0)

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = 0)

e__plus__ = e__minus__.anti()


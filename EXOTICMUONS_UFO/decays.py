# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.2.0 for Mac OS X ARM (64-bit) (December 26, 2024)
# Date: Mon 8 Sep 2025 08:32:52


from object_library import all_decays, Decay
import particles as P


Decay_S = Decay(name = 'Decay_S',
                particle = P.S,
                partial_widths = {(P.e__minus__,P.e__plus__):'((-8*cSee**2*Me**2 + 2*cSee**2*MS**2)*cmath.sqrt(-4*Me**2*MS**2 + MS**4))/(16.*cmath.pi*abs(MS)**3)',
                                  (P.e__minus__,P.mu__plus__):'((-((c1emu**2*Me**2)/Lambda**2) - (c1mue**2*Me**2)/Lambda**2 - (4*c1emu*c1mue*Me*Mmu)/Lambda**2 - (c1emu**2*Mmu**2)/Lambda**2 - (c1mue**2*Mmu**2)/Lambda**2 + (c1emu**2*MS**2)/Lambda**2 + (c1mue**2*MS**2)/Lambda**2)*cmath.sqrt(Me**4 - 2*Me**2*Mmu**2 + Mmu**4 - 2*Me**2*MS**2 - 2*Mmu**2*MS**2 + MS**4))/(16.*cmath.pi*abs(MS)**3)',
                                  (P.mu__minus__,P.e__plus__):'((-((c1emu**2*Me**2)/Lambda**2) - (c1mue**2*Me**2)/Lambda**2 - (4*c1emu*c1mue*Me*Mmu)/Lambda**2 - (c1emu**2*Mmu**2)/Lambda**2 - (c1mue**2*Mmu**2)/Lambda**2 + (c1emu**2*MS**2)/Lambda**2 + (c1mue**2*MS**2)/Lambda**2)*cmath.sqrt(Me**4 - 2*Me**2*Mmu**2 + Mmu**4 - 2*Me**2*MS**2 - 2*Mmu**2*MS**2 + MS**4))/(16.*cmath.pi*abs(MS)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.S,P.e__minus__):'(((c1emu**2*Me**2)/Lambda**2 + (c1mue**2*Me**2)/Lambda**2 + (4*c1emu*c1mue*Me*Mmu)/Lambda**2 + (c1emu**2*Mmu**2)/Lambda**2 + (c1mue**2*Mmu**2)/Lambda**2 - (c1emu**2*MS**2)/Lambda**2 - (c1mue**2*MS**2)/Lambda**2)*cmath.sqrt(Me**4 - 2*Me**2*Mmu**2 + Mmu**4 - 2*Me**2*MS**2 - 2*Mmu**2*MS**2 + MS**4))/(32.*cmath.pi*abs(Mmu)**3)'})

Decay_e__minus__ = Decay(name = 'Decay_e__minus__',
                         particle = P.e__minus__,
                         partial_widths = {(P.S,P.mu__minus__):'(((c1emu**2*Me**2)/Lambda**2 + (c1mue**2*Me**2)/Lambda**2 + (4*c1emu*c1mue*Me*Mmu)/Lambda**2 + (c1emu**2*Mmu**2)/Lambda**2 + (c1mue**2*Mmu**2)/Lambda**2 - (c1emu**2*MS**2)/Lambda**2 - (c1mue**2*MS**2)/Lambda**2)*cmath.sqrt(Me**4 - 2*Me**2*Mmu**2 + Mmu**4 - 2*Me**2*MS**2 - 2*Mmu**2*MS**2 + MS**4))/(32.*cmath.pi*abs(Me)**3)'})


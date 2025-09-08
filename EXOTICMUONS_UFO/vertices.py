# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.2.0 for Mac OS X ARM (64-bit) (December 26, 2024)
# Date: Mon 8 Sep 2025 08:32:52


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.e__plus__, P.e__minus__, P.S ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1})

V_2 = Vertex(name = 'V_2',
             particles = [ P.mu__plus__, P.e__minus__, P.S ],
             color = [ '1' ],
             lorentz = [ L.FFS2, L.FFS3 ],
             couplings = {(0,0):C.GC_7,(0,1):C.GC_6})

V_3 = Vertex(name = 'V_3',
             particles = [ P.mu__plus__, P.e__minus__, P.S, P.S ],
             color = [ '1' ],
             lorentz = [ L.FFSS1, L.FFSS2 ],
             couplings = {(0,0):C.GC_5,(0,1):C.GC_4})

V_4 = Vertex(name = 'V_4',
             particles = [ P.mu__plus__, P.e__minus__, P.S, P.S, P.S ],
             color = [ '1' ],
             lorentz = [ L.FFSSS1, L.FFSSS2 ],
             couplings = {(0,0):C.GC_3,(0,1):C.GC_2})

V_5 = Vertex(name = 'V_5',
             particles = [ P.e__plus__, P.mu__minus__, P.S ],
             color = [ '1' ],
             lorentz = [ L.FFS2, L.FFS3 ],
             couplings = {(0,0):C.GC_6,(0,1):C.GC_7})

V_6 = Vertex(name = 'V_6',
             particles = [ P.e__plus__, P.mu__minus__, P.S, P.S ],
             color = [ '1' ],
             lorentz = [ L.FFSS1, L.FFSS2 ],
             couplings = {(0,0):C.GC_4,(0,1):C.GC_5})

V_7 = Vertex(name = 'V_7',
             particles = [ P.e__plus__, P.mu__minus__, P.S, P.S, P.S ],
             color = [ '1' ],
             lorentz = [ L.FFSSS1, L.FFSSS2 ],
             couplings = {(0,0):C.GC_2,(0,1):C.GC_3})


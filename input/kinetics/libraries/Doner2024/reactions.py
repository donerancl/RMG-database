#!/usr/bin/env python
# encoding: utf-8

name = "Doner2024"
shortDesc = u"Doner2024"
longDesc =u"""
Calculated with ARC
"""

entry( # acutal product is ONNH2O
    index = 1,
    label = "ONHNHO(S) <=> H2NO + NO1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(121566,'s^-1'), n=2.68711, Ea=(182.343,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
by 1,2 H shift
TS method summary for TS4 in ONHNHO(S) <=> H2NO + NO1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.24178100   -0.15257200   -0.46373600
N       1.13417800   -0.76618500   -0.73871500
O      -1.33164700   -0.66777900   -0.54203900
H      -0.12408700    0.89090300   -0.47859900
O       1.91751400    0.09117700   -1.03638900
H       0.66999100   -0.66877200    0.47298400

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [3, 1, 2, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)
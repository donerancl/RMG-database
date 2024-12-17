#!/usr/bin/env python
# encoding: utf-8

name = "Wang2024"
shortDesc = u"Wang2024"
longDesc =u"""
"""

entry(
    index = 0,
    label = "NH2 + N2O <=> N2H2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.890E-13, 'cm^3/(mol*s)'), n=6.115, Ea=(871, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Wang2024]""",
    longDesc =
u"""
from New insights into the NH3/N2O/Ar system: key steps in N2O evolution 
""",
)

entry(
    index = 1,
    label = "NH2 + N2O <=> H2NN(S) + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.126E4, 'cm^3/(mol*s)'), n=2.313, Ea=(2.197E4, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Wang2024]""",
    longDesc =
u"""
from New insights into the NH3/N2O/Ar system: key steps in N2O evolution 
""",
)
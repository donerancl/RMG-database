#!/usr/bin/env python
# encoding: utf-8

name = "2025_Klippenstein"
shortDesc = u"2025_Klippenstein"
longDesc =u"""
Peter Glarborg, Eva Fabricius-Bjerre, Tor K. Joensen, Hamid Hashemi, Stephen J. Klippenstein,
An experimental, theoretical and kinetic modeling study of the N2O-H2 system: Implications for N2O + H,
Combustion and Flame,
Volume 271,
2025,
113810,
ISSN 0010-2180,
https://doi.org/10.1016/j.combustflame.2024.113810.
(https://www.sciencedirect.com/science/article/pii/S0010218024005194)
divided each A by 2 because cis/trans isomers - a crude estimation
"""

entry(
    index = 1,
    label = "HNNO + H <=> NH2 + NO",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(
        A=(9E12, 'cm^3/(mol*s)'), 
        n=0.183, 
        Ea=(-45, 'cal/mol'), 
        T0=(1, 'K'), 
        Tmin=(300, 'K'), 
        Tmax=(2500, 'K')
        ),
    shortDesc = u"""""",
    longDesc =
u"""
trans HNNO
"""
)
entry(
    index = 2,
    label = "HNNO + H <=> NH2 + NO",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(
        A=(2.9E10, 'cm^3/(mol*s)'), 
        n=0.313, 
        Ea=(-182, 'cal/mol'), 
        T0=(1, 'K'), 
        Tmin=(300, 'K'), 
        Tmax=(2500, 'K')
        ),
    shortDesc = u"""""",
    longDesc =
u"""
cis HNNO
"""
)

entry(
    index = 3,
    label = "HNNO + H <=> N2 + H + OH",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(
        A=(6.0E13, 'cm^3/(mol*s)'), 
        n=-0.077, 
        Ea=(126, 'cal/mol'), 
        T0=(1, 'K'), 
        Tmin=(300, 'K'), 
        Tmax=(2500, 'K')
        ),
    shortDesc = u"""""",
    longDesc =
u"""
trans HNNO
"""
)

entry(
    index = 4,
    label = "HNNO + H <=> N2 + H + OH",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(
        A=(5.0E13, 'cm^3/(mol*s)'), 
        n=-0.157, 
        Ea=(180, 'cal/mol'), 
        T0=(1, 'K'), 
        Tmin=(300, 'K'), 
        Tmax=(2500, 'K')
        ),
    shortDesc = u"""""",
    longDesc =
u"""
cis HNNO
"""
)

entry(
    index = 5,
    label = "HNNO + H <=> N2 + H2O",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(
        A=(3.95E13, 'cm^3/(mol*s)'), 
        n=-0.139, 
        Ea=(270, 'cal/mol'), 
        T0=(1, 'K'), 
        Tmin=(300, 'K'), 
        Tmax=(2500, 'K')
        ),
    shortDesc = u"""""",
    longDesc =
u"""
trans HNNO
"""
)

entry(
    index = 6,
    label = "HNNO + H <=> N2 + H2O",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(
        A=(4.55E13, 'cm^3/(mol*s)'), 
        n=-0.088, 
        Ea=(75, 'cal/mol'), 
        T0=(1, 'K'), 
        Tmin=(300, 'K'), 
        Tmax=(2500, 'K')
        ),
    shortDesc = u"""""",
    longDesc =
u"""
cis HNNO
"""
)

entry(
    index = 7,
    label = "HNNO + H <=> N2O + H2",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(
        A=(3.35E6, 'cm^3/(mol*s)'), 
        n=1.878, 
        Ea=(143, 'cal/mol'), 
        T0=(1, 'K'), 
        Tmin=(300, 'K'), 
        Tmax=(2500, 'K')
        ),
    shortDesc = u"""""",
    longDesc =
u"""
trans HNNO
"""
)

entry(
    index = 8,
    label = "HNNO + H <=> N2O + H2",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(
        A=(1.5E13, 'cm^3/(mol*s)'), 
        n=0.095, 
        Ea=(60, 'cal/mol'), 
        T0=(1, 'K'), 
        Tmin=(300, 'K'), 
        Tmax=(2500, 'K')
        ),
    shortDesc = u"""""",
    longDesc =
u"""
cis HNNO
"""
)
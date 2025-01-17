#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C8H7"
shortDesc = u"Phenyl radical first acetylene addition"
longDesc = u"""
Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene
Alexander M. Mebel, Yuri Georgievskii, Ahren W. Jasper, Stephen J. Klippenstein
Proceedings of the Combustion Institute 36 (2017) 919–926

New species W4, W5, P2 were added by Te-Chun Chu at the same G3(MP2,CC)//B3LYP/6-311G** level of theory. TST rates are all calculated in Arkane by using molecular information from the literature.
"""
autoGenerated=False
entry(
    index = 0,
    label = "R1 + C2H2 <=> W1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.043e+06, 'cm^3/(mol*s)'),
        n = 2.093,
        Ea = (3.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 9 data points; dA = *|/ 1.05598, dn = +|- 0.00685289, dEa = +|- 0.0443482 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 9 data points; dA = *|/ 1.05598, dn = +|- 0.00685289, dEa = +|- 0.0443482 kJ/mol
""",
)

entry(
    index = 1,
    label = "W1 <=> P1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.103e+11, 's^-1'),
        n = 1.148,
        Ea = (37.938, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 9 data points; dA = *|/ 1.67838, dn = +|- 0.0651477, dEa = +|- 0.4216 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 9 data points; dA = *|/ 1.67838, dn = +|- 0.0651477, dEa = +|- 0.4216 kJ/mol
""",
)

entry(
    index = 2,
    label = "W1 <=> W3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.2494, 's^-1'),
        n = 3.708,
        Ea = (17.398, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 9 data points; dA = *|/ 72.1843, dn = +|- 0.538364, dEa = +|- 3.484 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 9 data points; dA = *|/ 72.1843, dn = +|- 0.538364, dEa = +|- 3.484 kJ/mol
""",
)

entry(
    index = 3,
    label = "W1 <=> W4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.397e+11, 's^-1'),
        n = 0.356,
        Ea = (34.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 9 data points; dA = *|/ 1.03615, dn = +|- 0.00446785, dEa = +|- 0.0289135 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 9 data points; dA = *|/ 1.03615, dn = +|- 0.00446785, dEa = +|- 0.0289135 kJ/mol
""",
)

entry(
    index = 4,
    label = "W3 <=> W5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.551e+10, 's^-1'),
        n = 0.442,
        Ea = (32.272, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 9 data points; dA = *|/ 1.08701, dn = +|- 0.0104962, dEa = +|- 0.0679255 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 9 data points; dA = *|/ 1.08701, dn = +|- 0.0104962, dEa = +|- 0.0679255 kJ/mol
""",
)

entry(
    index = 5,
    label = "W4 <=> W5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.443e-30, 's^-1'),
        n = 11.694,
        Ea = (9.872, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 9 data points; dA = *|/ 5.253e+06, dn = +|- 1.9468, dEa = +|- 12.5987 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 9 data points; dA = *|/ 5.253e+06, dn = +|- 1.9468, dEa = +|- 12.5987 kJ/mol
""",
)

entry(
    index = 6,
    label = "W4 <=> P2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.045e+11, 's^-1'),
        n = 0.932,
        Ea = (40.574, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 9 data points; dA = *|/ 1.80557, dn = +|- 0.0743374, dEa = +|- 0.481072 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 9 data points; dA = *|/ 1.80557, dn = +|- 0.0743374, dEa = +|- 0.481072 kJ/mol
""",
)

entry(
    index = 7,
    label = "W5 <=> P2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.9e+10, 's^-1'),
        n = 1.092,
        Ea = (60.837, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Fitted to 9 data points; dA = *|/ 2.02124, dn = +|- 0.0885332, dEa = +|- 0.572939 kJ/mol',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Fitted to 9 data points; dA = *|/ 2.02124, dn = +|- 0.0885332, dEa = +|- 0.572939 kJ/mol
""",
)


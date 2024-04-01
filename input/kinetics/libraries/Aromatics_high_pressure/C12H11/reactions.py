#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C12H11"
shortDesc = u"Phenyl radical addition to benzene"
longDesc = u"""
Reaction between benzene and phenyl radical
Calulated by Max Liu at the CBS-QB3 level of theory
"""
autoGenerated=False
entry(
    index = 0,
    label = "benzene + phenyl <=> s5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (347.5, 'cm^3/(mol*s)'),
        n = 3.132,
        Ea = (1.752, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "s5 <=> H + biphenyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.646e+08, 's^-1'), n=1.264, Ea=(27.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

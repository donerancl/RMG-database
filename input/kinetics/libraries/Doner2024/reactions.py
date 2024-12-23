#!/usr/bin/env python
# encoding: utf-8

name = "Doner2024"
shortDesc = u"Doner2024"
longDesc =u"""
Calculated with ARC
"""
entry(
    index = 0,
    label = "NH3O <=> HNO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.25028e+06,'s^-1'), n=2.48106, Ea=(197.566,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in NH3O <=> HNO + H2:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -3.23906800    3.19147700    0.50491000
H      -3.91944200    3.48327400   -0.22247600
H      -3.04423900    2.11453300    0.38614900
H      -2.85026400    2.13778500   -0.75844200
O      -2.38244300    3.99306500    0.83773900


No rotors considered for this TS.
""",
)

entry(
    index = 1,
    label = "NH2OH <=> NH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4346.85,'s^-1'), n=2.69202, Ea=(179.358,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS4 in NH2OH <=> NH3O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
N      -1.31186000    3.49159400   -0.10221300
O      -1.66484200    4.87836200   -0.52925700
H      -0.94928900    2.96047100   -0.88003600
H      -2.09340600    3.05113900    0.36011200
H      -0.80566400    4.38952200    0.29912900

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [3, 1, 2, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)




entry(
    index = 2,
    label = "O + HNO <=> HNO2(T)",
    degeneracy = 1.0,
    elementary_high_p = True,
    kinetics = Arrhenius(A=(4.41348e+14,'cm^3/(mol*s)'), n=-0.165555, Ea=(-1.59594,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3500,'K')),
)


entry(
    index=3,
    label = 'HNO2(T) <=> HONOT',
    elementary_high_p = True,
    kinetics = Arrhenius(
        A = (0.000316369, 's^-1'),
        n = 4.96095,
        Ea = (76.9289, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 28.7534, dn = +|- 0.441274, dEa = +|- 2.40139 kJ/mol',
    ),
)


entry(
    index=4,
    label = 'HNO2(T) <=> NO1 + OH',
    elementary_high_p = True,
    kinetics = Arrhenius(
        A = (9.29929e+07, 's^-1'),
        n = 1.7915,
        Ea = (118.348, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 2.62912, dn = +|- 0.126999, dEa = +|- 0.691122 kJ/mol',
    ),
)

entry(
    index=5,
    label = 'HNO2(T) <=> H + NO2',
    elementary_high_p=True,
    kinetics = Arrhenius(
        A = (7.19602e+08, 's^-1'),
        n = 1.66988,
        Ea = (154.009, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.42328, dn = +|- 0.0463728, dEa = +|- 0.252359 kJ/mol',
    ),
)

entry(
    index=6,
    label = 'HONOT <=> NO1 + OH',
    elementary_high_p=True,
    kinetics = Arrhenius(
        A = (1.28331e+12, 's^-1'),
        n = 0.459905,
        Ea = (5.69065, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.14074, dn = +|- 0.0172999, dEa = +|- 0.0941455 kJ/mol',
    ),
)

entry(
    index=7,
    label = 'HONOT <=> H + NO2',
    elementary_high_p=True,
    kinetics = Arrhenius(
        A = (70059.1, 's^-1'),
        n = 2.4851,
        Ea = (129.365, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 2.59476, dn = +|- 0.12527, dEa = +|- 0.681714 kJ/mol',
    ),
)


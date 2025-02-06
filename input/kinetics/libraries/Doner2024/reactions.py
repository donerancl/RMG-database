#!/usr/bin/env python
# encoding: utf-8

name = "Doner2024"
shortDesc = u"Doner2024"
longDesc =u"""
Calculated with ARC
"""



entry(
    index=0,
    label = 'NH + O <=> H + NO1',
    kinetics = Arrhenius(
        A = (1.410E14,'cm^3/(mol*s)'),
        n = -0.21603,
        Ea = (46.37343, "cal/mol"),
        T0 = (1,'K'),
        Tmin = (100,'K'),
        Tmax = (500,'K'),
        comment = "Fit from calculations of Li et al. JCP 2011"
    )

)



entry(
    index = 1,
    label = "H2NO + H <=> HNO(T) + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(806982,'cm^3/(mol*s)'), n=2.27427, Ea=(8.64302,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in H2NO + H <=> HNO(T) + H2:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
N      -0.58921600    0.13978500   -0.01259800
O       0.61040800   -0.17636600    0.01538600
H      -0.90527800    1.20834300    0.00679900
H      -1.32127800   -0.56307800   -0.05400800
H      -1.30293600    2.27821000    0.02374400


No rotors considered for this TS.
""",
)

# entry(
#     index=2,
#     label = 'H + H2NO <=> H2 + HNO',
#     kinetics = Arrhenius(
#         A = (1.59173e+07, 'cm^3/(mol*s)'),
#         n = 1.61242,
#         Ea = (1.7829, 'kJ/mol'),
#         T0 = (1, 'K'),
#         Tmin = (298, 'K'),
#         Tmax = (2500, 'K'),
#         comment = 'direct H abstraction, CCSD(T)/cc-pVQZ//wb97xd/def2-qzvp',
#     ),
# )

entry(
    index=2,
    label = 'H + H2NO <=> H2 + HNO',
    kinetics =Arrhenius(A=(9.6E8,'cm^3/(mol*s)'), n=1.5, Ea=(6.96547,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="RMG estimate"),
)


entry(
    index=3,
    label='O + HNO <=> OH + NO1',
    kinetics = MultiArrhenius(
        arrhenius=[
            Arrhenius(A=(9.63E16, 'cm^3/(mol*s)'), n=-1.49, Ea=(0.19, 'kJ/mol'),T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.5E10, 'cm^3/(mol*s)'), n=1.04, Ea=(0.0, 'kJ/mol'),T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K'))
            ],
    )
)


entry(
    index=4,
    label = 'HNONO <=> NO1 + HNO(T)',
    elementary_high_p=True,
    kinetics = Arrhenius(A=(0.000000614,'m^3/(mol*s)'), n=2.756, Ea=(32.5005,'kJ/mol'), T0=(1,'K'), comment="""estimated 3 orders of magnitude slower than the reaction with NO1 + HNO(S) products
which was Estimated using template [R_R;N3J] for rate rule [Od_N3d;N3dJ_O]
Euclidian distance = 3.605551275463989
family: R_Addition_MultipleBond
Ea raised from 27.8 to 32.5 kJ/mol to match endothermicity of reaction.""")
)
entry(
    index=5,
    label = 'HNOH <=> H + HNO(T)',
    elementary_high_p=True,
    kinetics = Arrhenius(A=(1.23922e+23,'s^-1'), n=-3.67073, Ea=(323.848,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2000,'K'), comment="""Fitted to 29 data points; dA = *|/ 1.52491, dn = +|- 0.055859, dEa = +|- 0.292019 kJ/mol""")
)

entry(
    index=6,
    label = 'H2NO <=> H + HNO(T)',
    elementary_high_p=True,
    kinetics =Arrhenius(A=(5.82313e+24,'s^-1'), n=-4.18073, Ea=(328.689,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2000,'K'), comment="""Fitted to 29 data points; dA = *|/ 1.52491, dn = +|- 0.055859, dEa = +|- 0.292019 kJ/mol""")
)



# entry(
#     index = 0,
#     label = "NH3O <=> HNO + H2",
#     degeneracy = 1.0,
#     elementary_high_p = True,
#     kinetics = Arrhenius(A=(1.25028e+06,'s^-1'), n=2.48106, Ea=(197.566,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# TS method summary for TS0 in NH3O <=> HNO + H2:

# The method that generated the best TS guess and its output used for the optimization: user guess 0


# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# N      -3.23906800    3.19147700    0.50491000
# H      -3.91944200    3.48327400   -0.22247600
# H      -3.04423900    2.11453300    0.38614900
# H      -2.85026400    2.13778500   -0.75844200
# O      -2.38244300    3.99306500    0.83773900


# No rotors considered for this TS.
# """,
# )

# entry(
#     index = 1,
#     label = "NH2OH <=> NH3O",
#     degeneracy = 1.0,
#     elementary_high_p = True,
#     kinetics = Arrhenius(A=(4346.85,'s^-1'), n=2.69202, Ea=(179.358,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# TS method summary for TS4 in NH2OH <=> NH3O:

# The method that generated the best TS guess and its output used for the optimization: user guess 0


# TS external symmetry: 1, TS optical isomers: 1

# Optimized TS geometry:
# N      -1.31186000    3.49159400   -0.10221300
# O      -1.66484200    4.87836200   -0.52925700
# H      -0.94928900    2.96047100   -0.88003600
# H      -2.09340600    3.05113900    0.36011200
# H      -0.80566400    4.38952200    0.29912900

# 1D rotors:
# * Invalidated! pivots: [1, 2], dihedral: [3, 1, 2, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
# """,
# )




# entry(
#     index = 2,
#     label = "O + HNO <=> HNO2(T)",
#     degeneracy = 1.0,
#     elementary_high_p = True,
#     kinetics = Arrhenius(A=(4.41348e+14,'cm^3/(mol*s)'), n=-0.165555, Ea=(-1.59594,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3500,'K')),
# )


# entry(
#     index=3,
#     label = 'HNO2(T) <=> HONOT',
#     elementary_high_p = True,
#     kinetics = Arrhenius(
#         A = (0.000316369, 's^-1'),
#         n = 4.96095,
#         Ea = (76.9289, 'kJ/mol'),
#         T0 = (1, 'K'),
#         Tmin = (298, 'K'),
#         Tmax = (2500, 'K'),
#         comment = 'Fitted to 50 data points; dA = *|/ 28.7534, dn = +|- 0.441274, dEa = +|- 2.40139 kJ/mol',
#     ),
# )


# entry(
#     index=4,
#     label = 'HNO2(T) <=> NO1 + OH',
#     elementary_high_p = True,
#     kinetics = Arrhenius(
#         A = (9.29929e+07, 's^-1'),
#         n = 1.7915,
#         Ea = (118.348, 'kJ/mol'),
#         T0 = (1, 'K'),
#         Tmin = (298, 'K'),
#         Tmax = (2500, 'K'),
#         comment = 'Fitted to 50 data points; dA = *|/ 2.62912, dn = +|- 0.126999, dEa = +|- 0.691122 kJ/mol',
#     ),
# )

# entry(
#     index=5,
#     label = 'HNO2(T) <=> H + NO2',
#     elementary_high_p=True,
#     kinetics = Arrhenius(
#         A = (7.19602e+08, 's^-1'),
#         n = 1.66988,
#         Ea = (154.009, 'kJ/mol'),
#         T0 = (1, 'K'),
#         Tmin = (298, 'K'),
#         Tmax = (2500, 'K'),
#         comment = 'Fitted to 50 data points; dA = *|/ 1.42328, dn = +|- 0.0463728, dEa = +|- 0.252359 kJ/mol',
#     ),
# )

# entry(
#     index=6,
#     label = 'HONOT <=> NO1 + OH',
#     elementary_high_p=True,
#     kinetics = Arrhenius(
#         A = (1.28331e+12, 's^-1'),
#         n = 0.459905,
#         Ea = (5.69065, 'kJ/mol'),
#         T0 = (1, 'K'),
#         Tmin = (298, 'K'),
#         Tmax = (2500, 'K'),
#         comment = 'Fitted to 50 data points; dA = *|/ 1.14074, dn = +|- 0.0172999, dEa = +|- 0.0941455 kJ/mol',
#     ),
# )

# entry(
#     index=7,
#     label = 'HONOT <=> H + NO2',
#     elementary_high_p=True,
#     kinetics = Arrhenius(
#         A = (70059.1, 's^-1'),
#         n = 2.4851,
#         Ea = (129.365, 'kJ/mol'),
#         T0 = (1, 'K'),
#         Tmin = (298, 'K'),
#         Tmax = (2500, 'K'),
#         comment = 'Fitted to 50 data points; dA = *|/ 2.59476, dn = +|- 0.12527, dEa = +|- 0.681714 kJ/mol',
#     ),
# )
# entry(
#     index=2,
#     label = 'HONOT <=> HNO2(T)',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (1.88166e+11, 's^-1'),
#                 n = -2.87794,
#                 Ea = (154.104, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 141.243, dn = +|- 0.638362, dEa = +|- 3.81244 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (9.87084e+11, 's^-1'),
#                 n = -2.56498,
#                 Ea = (157.062, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 148.231, dn = +|- 0.644589, dEa = +|- 3.84963 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.97839e+10, 's^-1'),
#                 n = -1.57522,
#                 Ea = (155.614, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 117.229, dn = +|- 0.614332, dEa = +|- 3.66892 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (8.94613e+06, 's^-1'),
#                 n = -0.0755833,
#                 Ea = (152.002, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 129.89, dn = +|- 0.627557, dEa = +|- 3.74791 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (48043.8, 's^-1'),
#                 n = 1.14188,
#                 Ea = (150.816, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 304.324, dn = +|- 0.737345, dEa = +|- 4.40359 kJ/mol',
#             ),
#         ],
#     ),
# )

#   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   3.299e+08   3.286e+09   3.231e+10   3.049e+11   2.578e+12
#          1650   1.964e+09   1.937e+10   1.818e+11   1.559e+12   1.074e+13
#       1137.93   2.698e+09   2.663e+10   2.477e+11   2.065e+12   1.364e+13
#       868.421   3.820e+09   3.778e+10   3.507e+11   2.832e+12   1.784e+13
#       702.128   5.267e+09   5.202e+10   4.782e+11   3.757e+12   2.263e+13
#       589.286   7.850e+09   7.742e+10   7.034e+11   5.328e+12   3.019e+13
#       507.692   1.035e+10   1.007e+11   8.861e+11   6.592e+12   3.595e+13
#       445.946   1.352e+10   1.312e+11   1.151e+12   8.276e+12   4.333e+13
#        397.59   1.835e+10   1.798e+11   1.568e+12   1.086e+13   5.393e+13
#       358.696   2.903e+10   2.763e+11   2.293e+12   1.512e+13   6.970e+13
#       326.733   3.820e+10   3.608e+11   2.933e+12   1.867e+13   8.227e+13
#           300   3.947e+10   3.796e+11   3.072e+12   1.951e+13   8.602e+13
#   =========== =========== =========== =========== =========== =========== 
# entry(
#     index=3,
#     label = 'O + HNO <=> HNO2(T)',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (1.23362e+14, 'cm^3/(mol*s)'),
#                 n = -1.57875,
#                 Ea = (
#                     -2.41045,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 11.058, dn = +|- 0.309885, dEa = +|- 1.8507 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.35619e+15, 'cm^3/(mol*s)'),
#                 n = -1.59065,
#                 Ea = (
#                     -2.22091,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 10.4633, dn = +|- 0.302757, dEa = +|- 1.80813 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.46441e+16, 'cm^3/(mol*s)'),
#                 n = -1.60141,
#                 Ea = (
#                     -1.65683,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 9.21371, dn = +|- 0.286357, dEa = +|- 1.71019 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (9.30484e+16, 'cm^3/(mol*s)'),
#                 n = -1.55034,
#                 Ea = (
#                     -0.910316,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 7.93549, dn = +|- 0.267099, dEa = +|- 1.59517 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (2.31217e+17, 'cm^3/(mol*s)'),
#                 n = -1.39772,
#                 Ea = (
#                     -0.142988,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 5.9119, dn = +|- 0.229139, dEa = +|- 1.36847 kJ/mol',
#             ),
#         ],
#     ),
# )

#   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   1.362e+00   8.332e+01   5.263e+03   4.266e+05   3.582e+07
#          1650   1.370e+00   5.069e+01   1.578e+03   7.098e+04   4.055e+06
#       1137.93   2.199e-01   7.488e+00   1.704e+02   4.197e+03   1.522e+05
#       868.421   2.427e-02   7.388e-01   1.455e+01   2.647e+02   6.493e+03
#       702.128   2.162e-03   5.709e-02   1.010e+00   1.535e+01   2.831e+02
#       589.286   1.828e-04   4.048e-03   6.333e-02   8.522e-01   1.290e+01
#       507.692   1.417e-05   2.643e-04   3.752e-03   4.584e-02   5.941e-01
#       445.946   1.124e-06   1.760e-05   2.243e-04   2.547e-03   2.946e-02
#        397.59   8.876e-08   1.175e-06   1.355e-05   1.451e-04   1.551e-03
#       358.696   7.402e-09   8.533e-08   9.108e-07   9.373e-06   9.554e-05
#       326.733   7.323e-10   7.758e-09   7.941e-08   8.006e-07   7.980e-06
#           300   1.449e-10   1.476e-09   1.486e-08   1.487e-07   1.464e-06
#   =========== =========== =========== =========== =========== =========== 
#   entry(
#       reactants = ['HNO2(T)'],
#       products = ['HONOT'],
#       kinetics = PDepArrhenius(
#           pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#           arrhenius = [
#               Arrhenius(
#                   A = (2.60878e+12, 's^-1'),
#                   n = -3.03272,
#                   Ea = (86.8747, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 187.438, dn = +|- 0.67485, dEa = +|- 4.03035 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (1.36852e+13, 's^-1'),
#                   n = -2.71976,
#                   Ea = (89.8319, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 193.954, dn = +|- 0.679257, dEa = +|- 4.05667 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (2.74288e+11, 's^-1'),
#                   n = -1.73,
#                   Ea = (88.3839, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 150.621, dn = +|- 0.646652, dEa = +|- 3.86195 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (1.24031e+08, 's^-1'),
#                   n = -0.230363,
#                   Ea = (84.772, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 167.935, dn = +|- 0.660682, dEa = +|- 3.94574 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (666091, 's^-1'),
#                   n = 0.987096,
#                   Ea = (83.5859, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 400.691, dn = +|- 0.772819, dEa = +|- 4.61544 kJ/mol',
#               ),
#           ],
#       ),
#   )
#   
#   #   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   3.487e+06   3.487e+07   3.486e+08   3.478e+09   3.408e+10
#          1650   2.840e+06   2.839e+07   2.835e+08   2.808e+09   2.634e+10
#       1137.93   2.317e+06   2.316e+07   2.308e+08   2.272e+09   2.093e+10
#       868.421   2.098e+06   2.096e+07   2.083e+08   2.028e+09   1.810e+10
#       702.128   2.057e+06   2.053e+07   2.030e+08   1.946e+09   1.673e+10
#       589.286   2.133e+06   2.127e+07   2.088e+08   1.957e+09   1.597e+10
#       507.692   2.336e+06   2.322e+07   2.256e+08   2.072e+09   1.619e+10
#       445.946   2.574e+06   2.555e+07   2.463e+08   2.202e+09   1.640e+10
#        397.59   2.622e+06   2.603e+07   2.479e+08   2.151e+09   1.513e+10
#       358.696   2.520e+06   2.477e+07   2.310e+08   1.926e+09   1.262e+10
#       326.733   2.369e+06   2.317e+07   2.125e+08   1.714e+09   1.066e+10
#           300   3.441e+06   3.378e+07   3.060e+08   2.433e+09   1.480e+10
#   =========== =========== =========== =========== =========== =========== 
# entry(
#     index=4,
#     label = "O + HNO <=> HONOT",
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (8906.83, 'cm^3/(mol*s)'),
#                 n = 0.727516,
#                 Ea = (
#                     -4.21492,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.64995, dn = +|- 0.125667, dEa = +|- 0.750509 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (97526.1, 'cm^3/(mol*s)'),
#                 n = 0.716626,
#                 Ea = (
#                     -4.09195,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.70446, dn = +|- 0.128292, dEa = +|- 0.766189 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.41045e+06, 'cm^3/(mol*s)'),
#                 n = 0.672486,
#                 Ea = (
#                     -3.56223,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.7576, dn = +|- 0.130801, dEa = +|- 0.781175 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (2.67043e+07, 'cm^3/(mol*s)'),
#                 n = 0.597061,
#                 Ea = (
#                     -2.46031,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.89558, dn = +|- 0.137097, dEa = +|- 0.818774 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (5.09724e+08, 'cm^3/(mol*s)'),
#                 n = 0.521555,
#                 Ea = (
#                     -0.645296,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 3.13463, dn = +|- 0.147326, dEa = +|- 0.879864 kJ/mol',
#             ),
#         ],
#     ),
# )

#   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   1.481e+07   1.475e+08   1.451e+09   1.369e+10   1.157e+11
#          1650   3.954e+06   3.900e+07   3.660e+08   3.138e+09   2.162e+10
#       1137.93   1.777e+05   1.754e+06   1.631e+07   1.360e+08   8.982e+08
#       868.421   7.200e+03   7.121e+04   6.609e+05   5.338e+06   3.362e+07
#       702.128   2.644e+02   2.611e+03   2.400e+04   1.886e+05   1.136e+06
#       589.286   1.006e+01   9.924e+01   9.016e+02   6.829e+03   3.870e+04
#       507.692   3.304e-01   3.216e+00   2.829e+01   2.105e+02   1.148e+03
#       445.946   1.059e-02   1.028e-01   9.021e-01   6.485e+00   3.395e+01
#        397.59   3.502e-04   3.431e-03   2.992e-02   2.073e-01   1.029e+00
#       358.696   1.344e-05   1.279e-04   1.061e-03   6.998e-03   3.226e-02
#       326.733   4.286e-07   4.048e-06   3.290e-05   2.095e-04   9.231e-04
#           300   1.074e-08   1.033e-07   8.359e-07   5.309e-06   2.341e-05
#   =========== =========== =========== =========== =========== =========== 
#   entry(
#       reactants = ['HNO2(T)'],
#       products = ['O', 'HNO'],
#       kinetics = PDepArrhenius(
#           pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#           arrhenius = [
#               Arrhenius(
#                   A = (5.97957e+18, 's^-1'),
#                   n = -2.72189,
#                   Ea = (114.976, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 13.7709, dn = +|- 0.338178, dEa = +|- 2.01967 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (6.57367e+19, 's^-1'),
#                   n = -2.73378,
#                   Ea = (115.165, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 13.0705, dn = +|- 0.331446, dEa = +|- 1.97947 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (7.09825e+20, 's^-1'),
#                   n = -2.74455,
#                   Ea = (115.729, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 11.4842, dn = +|- 0.314762, dEa = +|- 1.87983 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (4.51021e+21, 's^-1'),
#                   n = -2.69347,
#                   Ea = (116.476, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 9.90102, dn = +|- 0.295634, dEa = +|- 1.76559 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (1.12074e+22, 's^-1'),
#                   n = -2.54085,
#                   Ea = (117.243, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 7.41361, dn = +|- 0.258327, dEa = +|- 1.54278 kJ/mol',
#               ),
#           ],
#       ),
#   )
#   
#   #   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   2.724e+03   2.724e+04   2.723e+05   2.717e+06   2.662e+07
#          1650   9.342e+00   9.340e+01   9.326e+02   9.236e+03   8.666e+04
#       1137.93   2.593e-02   2.592e-01   2.583e+00   2.543e+01   2.342e+02
#       868.421   7.228e-05   7.221e-04   7.175e-03   6.985e-02   6.236e-01
#       702.128   2.051e-07   2.048e-06   2.025e-05   1.941e-04   1.668e-03
#       589.286   5.911e-10   5.896e-09   5.788e-08   5.425e-07   4.426e-06
#       507.692   1.751e-12   1.741e-11   1.691e-10   1.553e-09   1.213e-08
#       445.946   5.123e-15   5.084e-14   4.901e-13   4.382e-12   3.263e-11
#        397.59   1.367e-17   1.358e-16   1.293e-15   1.122e-14   7.891e-14
#       358.696   3.417e-20   3.359e-19   3.132e-18   2.612e-17   1.712e-16
#       326.733   8.303e-23   8.120e-22   7.449e-21   6.009e-20   3.738e-19
#           300   3.108e-25   3.051e-24   2.763e-23   2.197e-22   1.336e-21
#   =========== =========== =========== =========== =========== =========== 
#   entry(
#       reactants = ['HONOT'],
#       products = ['O', 'HNO'],
#       kinetics = PDepArrhenius(
#           pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#           arrhenius = [
#               Arrhenius(
#                   A = (3.11397e+07, 's^-1'),
#                   n = -0.26084,
#                   Ea = (180.401, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 2.63982, dn = +|- 0.125173, dEa = +|- 0.747558 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (3.40967e+08, 's^-1'),
#                   n = -0.27173,
#                   Ea = (180.524, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 2.6945, dn = +|- 0.127816, dEa = +|- 0.763347 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (4.93114e+09, 's^-1'),
#                   n = -0.31587,
#                   Ea = (181.054, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 2.74393, dn = +|- 0.13016, dEa = +|- 0.777346 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (9.33627e+10, 's^-1'),
#                   n = -0.391294,
#                   Ea = (182.155, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 2.88412, dn = +|- 0.136586, dEa = +|- 0.81572 kJ/mol',
#               ),
#               Arrhenius(
#                   A = (1.78208e+12, 's^-1'),
#                   n = -0.466801,
#                   Ea = (183.97, 'kJ/mol'),
#                   T0 = (1, 'K'),
#                   Tmin = (300, 'K'),
#                   Tmax = (3000, 'K'),
#                   comment = 'Fitted to 12 data points; dA = *|/ 3.13495, dn = +|- 0.147339, dEa = +|- 0.879944 kJ/mol',
#               ),
#           ],
#       ),
#   )
#   
#   #   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   3.966e+05   3.963e+06   3.960e+07   3.956e+08   3.922e+09
#          1650   3.372e+03   3.073e+04   2.901e+05   2.838e+06   2.755e+07
#       1137.93   6.707e+01   3.578e+02   1.664e+03   1.115e+04   9.341e+04
#       868.421   4.513e+00   1.995e+01   5.454e+01   1.716e+02   8.723e+02
#       702.128   2.834e-01   1.136e+00   2.634e+00   5.614e+00   1.771e+01
#       589.286   1.753e-02   6.163e-02   1.254e-01   2.201e-01   5.119e-01
#       507.692   9.317e-04   2.920e-03   5.479e-03   8.357e-03   1.540e-02
#       445.946   5.000e-05   1.371e-04   2.331e-04   3.229e-04   5.012e-04
#        397.59   2.774e-06   6.520e-06   9.992e-06   1.276e-05   1.747e-05
#       358.696   1.580e-07   3.135e-07   4.321e-07   5.163e-07   6.425e-07
#       326.733   8.643e-09   1.490e-08   1.897e-08   2.147e-08   2.470e-08
#           300   4.643e-10   7.210e-10   8.723e-10   9.467e-10   1.020e-09
#   =========== =========== =========== =========== =========== =========== 
# entry(
#     index=5,
#     label = 'HNO2(T) <=> NO2 + H',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (0.00211602, 's^-1'),
#                 n = 2.71117,
#                 Ea = (76.0086, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 46.9511, dn = +|- 0.49634, dEa = +|- 2.96425 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (0.000888677, 's^-1'),
#                 n = 3.12668,
#                 Ea = (78.632, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 61.7363, dn = +|- 0.531642, dEa = +|- 3.17508 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.20377e-06, 's^-1'),
#                 n = 4.2609,
#                 Ea = (77.8977, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 54.0004, dn = +|- 0.514378, dEa = +|- 3.07198 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.91857e-09, 's^-1'),
#                 n = 5.39181,
#                 Ea = (78.0518, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 35.0449, dn = +|- 0.458626, dEa = +|- 2.73901 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (3.99242e-10, 's^-1'),
#                 n = 5.92491,
#                 Ea = (82.0395, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 45.5269, dn = +|- 0.492368, dEa = +|- 2.94053 kJ/mol',
#             ),
#         ],
#     ),
# )

#   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   4.044e+04   4.044e+05   4.044e+06   4.042e+07   4.029e+08
#          1650   3.429e+02   3.429e+03   3.429e+04   3.427e+05   3.408e+06
#       1137.93   2.933e+00   2.933e+01   2.933e+02   2.931e+03   2.910e+04
#       868.421   2.643e-02   2.643e-01   2.642e+00   2.640e+01   2.617e+02
#       702.128   2.494e-04   2.494e-03   2.494e-02   2.491e-01   2.465e+00
#       589.286   2.470e-06   2.470e-05   2.470e-04   2.467e-03   2.437e-02
#       507.692   2.604e-08   2.604e-07   2.604e-06   2.600e-05   2.564e-04
#       445.946   2.864e-10   2.864e-09   2.864e-08   2.859e-07   2.815e-06
#        397.59   3.083e-12   3.082e-11   3.082e-10   3.077e-09   3.029e-08
#       358.696   3.332e-14   3.332e-13   3.332e-12   3.327e-11   3.280e-10
#       326.733   3.923e-16   3.923e-15   3.923e-14   3.918e-13   3.867e-12
#           300   8.068e-18   8.068e-17   8.066e-16   8.052e-15   7.912e-14
#   =========== =========== =========== =========== =========== =========== 
# entry(
#     index=6,
#     label = 'HONOT <=> NO2 + H',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (1013.79, 's^-1'),
#                 n = 1.14325,
#                 Ea = (132.721, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 7.68127, dn = +|- 0.2629, dEa = +|- 1.5701 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (10137.4, 's^-1'),
#                 n = 1.14325,
#                 Ea = (132.721, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 7.68125, dn = +|- 0.2629, dEa = +|- 1.5701 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (101328, 's^-1'),
#                 n = 1.14331,
#                 Ea = (132.721, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 7.68106, dn = +|- 0.262897, dEa = +|- 1.57008 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.00869e+06, 's^-1'),
#                 n = 1.14384,
#                 Ea = (132.722, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 7.67909, dn = +|- 0.262864, dEa = +|- 1.56988 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (9.64147e+06, 's^-1'),
#                 n = 1.14917,
#                 Ea = (132.725, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 7.66039, dn = +|- 0.262549, dEa = +|- 1.568 kJ/mol',
#             ),
#         ],
#     ),
# )

#   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   1.069e+13   1.069e+13   1.069e+13   1.069e+13   1.063e+13
#          1650   1.065e+12   1.065e+12   1.065e+12   1.064e+12   1.052e+12
#       1137.93   1.363e+11   1.363e+11   1.363e+11   1.361e+11   1.348e+11
#       868.421   2.424e+10   2.424e+10   2.423e+10   2.416e+10   2.374e+10
#       702.128   6.713e+09   6.711e+09   6.700e+09   6.644e+09   6.369e+09
#       589.286   3.070e+09   3.068e+09   3.052e+09   2.988e+09   2.735e+09
#       507.692   2.027e+09   2.023e+09   2.001e+09   1.928e+09   1.686e+09
#       445.946   1.619e+09   1.614e+09   1.587e+09   1.499e+09   1.251e+09
#        397.59   1.428e+09   1.423e+09   1.387e+09   1.278e+09   1.012e+09
#       358.696   1.337e+09   1.324e+09   1.272e+09   1.135e+09   8.428e+08
#       326.733   1.299e+09   1.282e+09   1.215e+09   1.054e+09   7.425e+08
#           300   1.307e+09   1.291e+09   1.209e+09   1.031e+09   7.060e+08
#   =========== =========== =========== =========== =========== =========== 
# entry(
#     index=7,
#     label = 'O + HNO <=> NO2 + H',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (7.46344e-11, 'cm^3/(mol*s)'),
#                 n = 6.64843,
#                 Ea = (
#                     -15.3859,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 77.5634, dn = +|- 0.561071, dEa = +|- 3.35084 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (8.01547e-11, 'cm^3/(mol*s)'),
#                 n = 6.63979,
#                 Ea = (
#                     -15.2994,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 76.725, dn = +|- 0.55967, dEa = +|- 3.34247 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.10914e-10, 'cm^3/(mol*s)'),
#                 n = 6.60051,
#                 Ea = (
#                     -14.8987,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 73.2815, dn = +|- 0.553749, dEa = +|- 3.30711 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (2.28305e-10, 'cm^3/(mol*s)'),
#                 n = 6.51378,
#                 Ea = (
#                     -13.9395,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 67.1908, dn = +|- 0.54256, dEa = +|- 3.24028 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (8.69257e-10, 'cm^3/(mol*s)'),
#                 n = 6.3548,
#                 Ea = (
#                     -11.8926,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 60.6046, dn = +|- 0.529256, dEa = +|- 3.16084 kJ/mol',
#             ),
#         ],
#     ),
# )

#   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   4.129e+06   2.930e+07   2.228e+08   1.995e+09   1.802e+10
#          1650   2.143e+06   8.209e+06   2.818e+07   1.465e+08   9.592e+08
#       1137.93   2.643e+05   9.090e+05   2.111e+06   5.521e+06   2.224e+07
#       868.421   2.408e+04   7.392e+04   1.469e+05   2.729e+05   7.079e+05
#       702.128   1.835e+03   4.891e+03   8.707e+03   1.337e+04   2.536e+04
#       589.286   1.356e+02   3.032e+02   4.772e+02   6.463e+02   9.945e+02
#       507.692   9.209e+00   1.736e+01   2.479e+01   3.043e+01   3.983e+01
#       445.946   6.576e-01   1.040e+00   1.333e+00   1.520e+00   1.769e+00
#        397.59   5.159e-02   6.892e-02   7.988e-02   8.580e-02   9.213e-02
#       358.696   4.660e-03   5.411e-03   5.795e-03   5.975e-03   6.105e-03
#       326.733   5.107e-04   5.433e-04   5.572e-04   5.623e-04   5.610e-04
#           300   7.299e-05   7.452e-05   7.507e-05   7.513e-05   7.397e-05
#   =========== =========== =========== =========== =========== =========== 
# entry(
#     index=8,
#     label = "HNO2(T) <=> NO1 + OH",
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (8.5193e+14, 's^-1'),
#                 n = -1.90711,
#                 Ea = (84.2467, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 151.258, dn = +|- 0.647196, dEa = +|- 3.8652 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.68222e+14, 's^-1'),
#                 n = -1.45933,
#                 Ea = (86.6392, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 135.199, dn = +|- 0.632723, dEa = +|- 3.77876 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (9.02738e+10, 's^-1'),
#                 n = -0.28642,
#                 Ea = (84.4719, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 93.7677, dn = +|- 0.585536, dEa = +|- 3.49695 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (2.2176e+06, 's^-1'),
#                 n = 1.30468,
#                 Ea = (80.6487, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 110.989, dn = +|- 0.607279, dEa = +|- 3.6268 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1064.06, 's^-1'),
#                 n = 2.55073,
#                 Ea = (79.6269, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 337.118, dn = +|- 0.750542, dEa = +|- 4.4824 kJ/mol',
#             ),
#         ],
#     ),
# )

#   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   1.856e+07   1.856e+08   1.856e+09   1.855e+10   1.846e+11
#          1650   2.743e+07   2.743e+08   2.742e+09   2.738e+10   2.702e+11
#       1137.93   3.516e+07   3.514e+08   3.504e+09   3.480e+10   3.380e+11
#       868.421   4.227e+07   4.226e+08   4.214e+09   4.148e+10   3.914e+11
#       702.128   4.925e+07   4.918e+08   4.869e+09   4.727e+10   4.296e+11
#       589.286   5.561e+07   5.555e+08   5.497e+09   5.245e+10   4.544e+11
#       507.692   6.069e+07   6.064e+08   6.021e+09   5.722e+10   4.707e+11
#       445.946   6.714e+07   6.702e+08   6.597e+09   6.060e+10   4.700e+11
#        397.59   6.632e+07   6.615e+08   6.466e+09   5.793e+10   4.286e+11
#       358.696   5.886e+07   5.871e+08   5.737e+09   5.079e+10   3.635e+11
#       326.733   4.960e+07   4.950e+08   4.858e+09   4.315e+10   3.018e+11
#           300   7.321e+07   7.222e+08   6.645e+09   5.414e+10   3.428e+11
#   =========== =========== =========== =========== =========== =========== 
# entry(
#     index=9,
#     label = 'HONOT <=> NO1 + OH',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (2.9952e+10, 's^-1'),
#                 n = -0.916608,
#                 Ea = (2.30741, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 3.44469, dn = +|- 0.159489, dEa = +|- 0.952503 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (3.13012e+11, 's^-1'),
#                 n = -0.921994,
#                 Ea = (2.35891, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 3.38487, dn = +|- 0.15723, dEa = +|- 0.939012 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (4.02798e+12, 's^-1'),
#                 n = -0.952635,
#                 Ea = (2.67583, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 3.10001, dn = +|- 0.145894, dEa = +|- 0.871313 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (6.96841e+13, 's^-1'),
#                 n = -1.01755,
#                 Ea = (3.55147, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.81302, dn = +|- 0.133367, dEa = +|- 0.796497 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.64705e+15, 's^-1'),
#                 n = -1.11651,
#                 Ea = (5.38923, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.47182, dn = +|- 0.116694, dEa = +|- 0.69692 kJ/mol',
#             ),
#         ],
#     ),
# )

#   =========== =========== =========== =========== =========== =========== 
#         T / P   1.000e-02   1.000e-01   1.000e+00   1.000e+01   1.000e+02
#   =========== =========== =========== =========== =========== =========== 
#          3000   2.251e+13   2.251e+13   2.251e+13   2.247e+13   2.216e+13
#          1650   9.208e+12   9.207e+12   9.199e+12   9.141e+12   8.733e+12
#       1137.93   4.695e+12   4.694e+12   4.684e+12   4.635e+12   4.367e+12
#       868.421   2.980e+12   2.978e+12   2.964e+12   2.905e+12   2.661e+12
#       702.128   2.231e+12   2.228e+12   2.208e+12   2.132e+12   1.880e+12
#       589.286   1.879e+12   1.874e+12   1.844e+12   1.743e+12   1.457e+12
#       507.692   1.726e+12   1.717e+12   1.673e+12   1.547e+12   1.234e+12
#       445.946   1.673e+12   1.662e+12   1.605e+12   1.445e+12   1.094e+12
#        397.59   1.680e+12   1.668e+12   1.592e+12   1.389e+12   9.912e+11
#       358.696   1.754e+12   1.725e+12   1.612e+12   1.351e+12   8.966e+11
#       326.733   1.852e+12   1.812e+12   1.665e+12   1.350e+12   8.483e+11
#           300   1.983e+12   1.948e+12   1.767e+12   1.410e+12   8.650e+11
#   =========== =========== =========== =========== =========== =========== 
# entry(
#     index=10,
#     duplicate=True,
#     label = 'O + HNO <=> NO1 + OH',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (138676, 'cm^3/(mol*s)'),
#                 n = 2.33541,
#                 Ea = (
#                     -7.76556,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.27326, dn = +|- 0.105895, dEa = +|- 0.632429 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (152223, 'cm^3/(mol*s)'),
#                 n = 2.32421,
#                 Ea = (
#                     -7.64186,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.2456, dn = +|- 0.104317, dEa = +|- 0.623002 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (224507, 'cm^3/(mol*s)'),
#                 n = 2.27764,
#                 Ea = (
#                     -7.10211,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.14904, dn = +|- 0.0986489, dEa = +|- 0.589153 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (458680, 'cm^3/(mol*s)'),
#                 n = 2.19298,
#                 Ea = (
#                     -5.95133,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.02054, dn = +|- 0.0906986, dEa = +|- 0.541672 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.11733e+06, 'cm^3/(mol*s)'),
#                 n = 2.08878,
#                 Ea = (
#                     -3.95196,
#                     'kJ/mol',
#                 ),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 1.89891, dn = +|- 0.0826925, dEa = +|- 0.493858 kJ/mol',
#             ),
#         ],
#     ),
# )

# entry(
#     index=11,
#     duplicate=True,
#     label = 'O + HNO <=> NO1 + OH',
#     kinetics = Arrhenius(
#         A = (4.27E8, 'cm^3/(mol*s)'),
#         n = 1.63,
#         T0 = (1,'K'),
#         Ea = (-851,'J/mol'),
#         Tmin = (1,'K'),
#         Tmax = (2500,'K'),
#         comment = """
#         direct abstraction rate calculated by Timo Pekkanen with geometries calculated at CASPT2/aug-cc-pVTZ and 
#         energies calculated at CASPT2/CBS extrapolated from aug-cc-pVTZ and aug-cc-pVQZ
#         """
#     )
# )


# entry(
#     index = 13,
#     label = "O + HNO <=> HNOO",
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (4.58567e+10, 'cm^3/(mol*s)'),
#                 n = -1.27118,
#                 Ea = (75.3568, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 6.0858, dn = +|- 0.232877, dEa = +|- 1.39079 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (4.58446e+11, 'cm^3/(mol*s)'),
#                 n = -1.27113,
#                 Ea = (75.3583, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 6.08193, dn = +|- 0.232795, dEa = +|- 1.39031 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (4.57183e+12, 'cm^3/(mol*s)'),
#                 n = -1.27068,
#                 Ea = (75.3724, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 6.0437, dn = +|- 0.231982, dEa = +|- 1.38545 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (4.41485e+13, 'cm^3/(mol*s)'),
#                 n = -1.26533,
#                 Ea = (75.4983, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 5.69732, dn = +|- 0.224372, dEa = +|- 1.34 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (2.82147e+14, 'cm^3/(mol*s)'),
#                 n = -1.20296,
#                 Ea = (76.2458, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 3.90258, dn = +|- 0.175583, dEa = +|- 1.04862 kJ/mol',
#             ),
#         ],
#     ),
# )

# entry(
#     index = 14,
#     label = 'HNOO <=> NO1 + OH',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (7.26039e+17, 's^-1'),
#                 n = -3.3895,
#                 Ea = (9.99508, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 7.45672, dn = +|- 0.259074, dEa = +|- 1.54725 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (7.26031e+18, 's^-1'),
#                 n = -3.38942,
#                 Ea = (10.0073, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 7.39775, dn = +|- 0.258051, dEa = +|- 1.54113 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (7.25254e+19, 's^-1'),
#                 n = -3.38856,
#                 Ea = (10.1197, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 6.90914, dn = +|- 0.249239, dEa = +|- 1.48851 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (6.49735e+20, 's^-1'),
#                 n = -3.37065,
#                 Ea = (10.7695, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 5.10695, dn = +|- 0.210265, dEa = +|- 1.25575 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.05848e+21, 's^-1'),
#                 n = -3.13444,
#                 Ea = (11.9528, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.82963, dn = +|- 0.134126, dEa = +|- 0.801031 kJ/mol',
#             ),
#         ],
#     ),
# )

# entry(
#     index =15,
#     label = "O + HNO <=> NO1 + OH",
#     duplicate = True,
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (1.16874e+09, 'cm^3/(mol*s)'),
#                 n = 0.69767,
#                 Ea = (70.0815, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.1969, dn = +|- 0.10149, dEa = +|- 0.606118 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.16858e+09, 'cm^3/(mol*s)'),
#                 n = 0.697697,
#                 Ea = (70.0827, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.19625, dn = +|- 0.101451, dEa = +|- 0.605889 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.167e+09, 'cm^3/(mol*s)'),
#                 n = 0.697963,
#                 Ea = (70.0952, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.18981, dn = +|- 0.101072, dEa = +|- 0.603626 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.14909e+09, 'cm^3/(mol*s)'),
#                 n = 0.700816,
#                 Ea = (70.2128, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 2.13226, dn = +|- 0.0976385, dEa = +|- 0.583118 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (9.29931e+08, 'cm^3/(mol*s)'),
#                 n = 0.733778,
#                 Ea = (71.0229, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 1.91413, dn = +|- 0.0837223, dEa = +|- 0.500008 kJ/mol',
#             ),
#         ],
#     ),
# )


# entry(
#     index=16,
#     label = 'HNOO <=> NH + O2',
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (5.68466e+14, 's^-1'),
#                 n = -2.06185,
#                 Ea = (22.6573, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 4.56334, dn = +|- 0.195752, dEa = +|- 1.16908 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (5.68422e+15, 's^-1'),
#                 n = -2.06184,
#                 Ea = (22.6579, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 4.56204, dn = +|- 0.195716, dEa = +|- 1.16886 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (5.67977e+16, 's^-1'),
#                 n = -2.0617,
#                 Ea = (22.6639, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 4.5491, dn = +|- 0.195349, dEa = +|- 1.16667 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (5.63347e+17, 's^-1'),
#                 n = -2.06023,
#                 Ea = (22.7229, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 4.42583, dn = +|- 0.191807, dEa = +|- 1.14551 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (5.06574e+18, 's^-1'),
#                 n = -2.04344,
#                 Ea = (23.1924, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 3.58456, dn = +|- 0.164622, dEa = +|- 0.983156 kJ/mol',
#             ),
#         ],
#     ),
# )
# entry(
    
#     index =17,
#     label = "O + HNO <=> NH + O2",
#     kinetics = PDepArrhenius(
#         pressures = ([0.01, 0.1, 1, 10, 100], 'bar'),
#         arrhenius = [
#             Arrhenius(
#                 A = (1.59006e+08, 'cm^3/(mol*s)'),
#                 n = 1.37641,
#                 Ea = (77.0322, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 1.0897, dn = +|- 0.0110776, dEa = +|- 0.0661581 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.59023e+08, 'cm^3/(mol*s)'),
#                 n = 1.3764,
#                 Ea = (77.0328, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 1.08954, dn = +|- 0.0110582, dEa = +|- 0.0660421 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.59186e+08, 'cm^3/(mol*s)'),
#                 n = 1.37631,
#                 Ea = (77.0383, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 1.08791, dn = +|- 0.0108656, dEa = +|- 0.064892 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.60747e+08, 'cm^3/(mol*s)'),
#                 n = 1.37542,
#                 Ea = (77.0919, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 1.07332, dn = +|- 0.00912366, dEa = +|- 0.0544885 kJ/mol',
#             ),
#             Arrhenius(
#                 A = (1.70255e+08, 'cm^3/(mol*s)'),
#                 n = 1.37102,
#                 Ea = (77.5404, 'kJ/mol'),
#                 T0 = (1, 'K'),
#                 Tmin = (300, 'K'),
#                 Tmax = (3000, 'K'),
#                 comment = 'Fitted to 12 data points; dA = *|/ 1.12437, dn = +|- 0.0151158, dEa = +|- 0.0902751 kJ/mol',
#             ),
#         ],
#     ),
# )



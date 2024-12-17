#!/usr/bin/env python
# encoding: utf-8

name = "Knyazev_Korobeinichev2010"
shortDesc = u"Knyazev_Korobeinichev2010"
longDesc =u"""
[KK2010] Vadim D. Knyazev, and Oleg P. Korobeinichev "Thermal Decomposition of HN3" J. Phys. Chem. A 2010, 114, 839–846
Chebyshev Polynomial Rate Coefficients for N2 bath gas
"""

entry(
    index=0,
    label="HN3 <=> NH + N2",
    duplicate=False,
    kinetics=Chebyshev(
        coeffs=[
            [2.516, 1.328, -2.866E-1, -2.719E-2, 1.046E-2],
            [-3.277, -4.355E-1, 9.448E-3, 2.399E-2, -7.554E-3],
            [-2.917E-1, 1.205E-2, 9.056E-3, -1.080E-3, 2.298E-4],
            [6.103E-2, 8.875E-3, -4.070E-4, -1.368E-4,1.915E-4],
            [-6.781E-3, -4.095E-3, -2.709E-4, 9.722E-5, -5.443E-5]],
        kunits='s^-1', Tmin=(800, 'K'), Tmax=(3000, 'K'), Pmin=(0.001, 'atm'), Pmax=(100, 'atm'),
    ),
    shortDesc=u"""[KK2010]""",
    longDesc=
    u"""
    """,
)

entry(
    index=1,
    label="HN3 <=> NH(S) + N2",
    duplicate=False,
    kinetics=Chebyshev(
        coeffs=[
            [8.686E-1, 4.137, -5.246E-1, -1.804E-1, 3.052E-2],
            [-3.650, -2.374E-1, -1.415E-1, 2.495E-2, -1.687E-2],
            [-3.262E-1, -6.310E-3, 1.286E-2, -5.535E-4, 3.252E-4],
            [6.495E-2, 8.846E-3, -1.900E-3, -1.990E-4, 1.782E-4],
            [-7.880E-3, -4.176E-3, 1.422E-4, 1.760E-4, -6.227E-5]],
        kunits='s^-1', Tmin=(800, 'K'), Tmax=(3000, 'K'), Pmin=(0.001, 'atm'), Pmax=(100, 'atm'),
    ),
    shortDesc=u"""[KK2010]""",
    longDesc=
    u"""
    """,
)
entry(
    index = 2,
    label = "H + HN3 <=> HNNNH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
        Arrhenius(A=(3.13E9, 'cm^3/(mol*s)'), n=1.34, Ea=(5941, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(200, 'K'), Tmax=(500, 'K')),
        Arrhenius(A=(1.06554E-5, 'cm^3/(mol*s)'), n=3.15, Ea=(1814, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(500, 'K'), Tmax=(3500, 'K'))
    ],
    ),
    elementary_high_p = True,
    shortDesc = u"""[K]""",
    longDesc =
u"""

""",
)

# entry(
#     index = 3,
#     label = "HNNNH <=> H + HN3",
#     degeneracy = 1,
#     kinetics = [
#         Arrhenius(A=(3.799E36, 'cm^3/(mol*s)'), n=0.641, Ea=(16669, 'cal/mol'), T0=(1, 'K'),
#                          Tmin=(200, 'K'), Tmax=(500, 'K')),
#         Arrhenius(A=(3.09E16, 'cm^3/(mol*s)'), n=7.11, Ea=(26971, 'cal/mol'), T0=(1, 'K'),
#                          Tmin=(500, 'K'), Tmax=(3500, 'K'))
#     ],
#     elementary_high_p = True,
#     shortDesc = u"""[K]""",
#     longDesc =
# u"""

# """,
# )


entry(
    index = 4,
    label = "H + HN3 <=> NH2 + N2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
        Arrhenius(A=(9.3912E-8, 'cm^3/(mol*s)'), n=6.64, Ea=(665, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(200, 'K'), Tmax=(500, 'K')),
        Arrhenius(A=(1.499E8, 'cm^3/(mol*s)'), n=1.68, Ea=(4930, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(500, 'K'), Tmax=(3500, 'K'))
    ],
    ),
    elementary_high_p = False,
    shortDesc = u"""[K]""",
    longDesc =
u"""

""",
)


entry(
    index = 5,
    label = "H + HN3 <=> H2 + N3",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
        Arrhenius(A=(1.3545E-11, 'cm^3/(mol*s)'), n=7.59, Ea=(-1987, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(200, 'K'), Tmax=(500, 'K')),
        Arrhenius(A=(1.680E5, 'cm^3/(mol*s)'), n=2.48, Ea=(3336, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(500, 'K'), Tmax=(3500, 'K'))
    ],
    ),
    elementary_high_p = False,
    shortDesc = u"""[K]""",
    longDesc =
u"""

""",
)

# entry(
#     index = 6,
#     label = "NH2 + N2 <=> H + HN3",
#     degeneracy = 1,
#     kinetics = [
#         Arrhenius(A=(1.535E-10, 'cm^3/(mol*s)'), n=7.04, Ea=(78492, 'cal/mol'), T0=(1, 'K'),
#                          Tmin=(200, 'K'), Tmax=(500, 'K')),
#         Arrhenius(A=(122.808, 'cm^3/(mol*s)'), n=3.15, Ea=(81821, 'cal/mol'), T0=(1, 'K'),
#                          Tmin=(500, 'K'), Tmax=(3500, 'K'))
#     ],
#     elementary_high_p = False,
#     shortDesc = u"""[K]""",
#     longDesc =
# u"""

# """,
# )

# entry(
#     index = 7,
#     label = "H2 + N3 <=> H + HN3",
#     degeneracy = 1,
#     kinetics = [
#         Arrhenius(A=(2.55E-10, 'cm^3/(mol*s)'), n=7.11, Ea=(13380, 'cal/mol'), T0=(1, 'K'),
#                          Tmin=(200, 'K'), Tmax=(500, 'K')),
#         Arrhenius(A=(6742.4, 'cm^3/(mol*s)'), n=2.84, Ea=(17760, 'cal/mol'), T0=(1, 'K'),
#                          Tmin=(500, 'K'), Tmax=(3500, 'K'))
#     ],
#     elementary_high_p = False,
#     shortDesc = u"""[K]""",
#     longDesc =
# u"""

# """,
# )
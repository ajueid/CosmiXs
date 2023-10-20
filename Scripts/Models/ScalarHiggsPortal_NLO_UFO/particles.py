
# This file was automatically created by The UFO_usermod        

from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             counterterm = None,
             charge = 0.0,
             line = 'wavy',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = True)


Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             counterterm = None,
             charge = 0.0,
             line = 'wavy',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = True)


W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     counterterm = None,
                     charge = 1.0,
                     line = 'wavy',
                     propagating = True,
                     goldstoneboson = False,
                     propagator = None,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0,
                     selfconjugate = False)


W__minus__ = Particle(pdg_code = -24,
                      name = 'W-',
                      antiname = 'W+',
                      spin = 3,
                      color = 1,
                      mass = Param.MW,
                      width = Param.WW,
                      texname = 'W-',
                      antitexname = 'W+',
                      counterterm = None,
                      charge = -1.0,
                      line = 'wavy',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0,
                      selfconjugate = False)


g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             counterterm = None,
             charge = 0.0,
             line = 'curly',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = True)


ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               counterterm = None,
               charge = 0.0,
               line = 'dotted',
               propagating = True,
               goldstoneboson = False,
               propagator = None,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0,
               selfconjugate = False)


ghA__tilde__ = Particle(pdg_code = -9000001,
                        name = 'ghA~',
                        antiname = 'ghA',
                        spin = -1,
                        color = 1,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'ghA~',
                        antitexname = 'ghA',
                        counterterm = None,
                        charge = -0.0,
                        line = 'dotted',
                        propagating = True,
                        goldstoneboson = False,
                        propagator = None,
                        GhostNumber = -1,
                        LeptonNumber = 0,
                        Y = 0,
                        selfconjugate = False)


ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               counterterm = None,
               charge = 0.0,
               line = 'dotted',
               propagating = True,
               goldstoneboson = False,
               propagator = None,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0,
               selfconjugate = False)


ghZ__tilde__ = Particle(pdg_code = -9000002,
                        name = 'ghZ~',
                        antiname = 'ghZ',
                        spin = -1,
                        color = 1,
                        mass = Param.MZ,
                        width = Param.WZ,
                        texname = 'ghZ~',
                        antitexname = 'ghZ',
                        counterterm = None,
                        charge = -0.0,
                        line = 'dotted',
                        propagating = True,
                        goldstoneboson = False,
                        propagator = None,
                        GhostNumber = -1,
                        LeptonNumber = 0,
                        Y = 0,
                        selfconjugate = False)


ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                counterterm = None,
                charge = 1.0,
                line = 'dotted',
                propagating = True,
                goldstoneboson = False,
                propagator = None,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0,
                selfconjugate = False)


ghWp__tilde__ = Particle(pdg_code = -9000003,
                         name = 'ghWp~',
                         antiname = 'ghWp',
                         spin = -1,
                         color = 1,
                         mass = Param.MW,
                         width = Param.WW,
                         texname = 'ghWp~',
                         antitexname = 'ghWp',
                         counterterm = None,
                         charge = -1.0,
                         line = 'dotted',
                         propagating = True,
                         goldstoneboson = False,
                         propagator = None,
                         GhostNumber = -1,
                         LeptonNumber = 0,
                         Y = 0,
                         selfconjugate = False)


ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                counterterm = None,
                charge = -1.0,
                line = 'dotted',
                propagating = True,
                goldstoneboson = False,
                propagator = None,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0,
                selfconjugate = False)


ghWm__tilde__ = Particle(pdg_code = -9000004,
                         name = 'ghWm~',
                         antiname = 'ghWm',
                         spin = -1,
                         color = 1,
                         mass = Param.MW,
                         width = Param.WW,
                         texname = 'ghWm~',
                         antitexname = 'ghWm',
                         counterterm = None,
                         charge = 1.0,
                         line = 'dotted',
                         propagating = True,
                         goldstoneboson = False,
                         propagator = None,
                         GhostNumber = -1,
                         LeptonNumber = 0,
                         Y = 0,
                         selfconjugate = False)


ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               counterterm = None,
               charge = 0.0,
               line = 'dotted',
               propagating = True,
               goldstoneboson = False,
               propagator = None,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0,
               selfconjugate = False)


ghG__tilde__ = Particle(pdg_code = -82,
                        name = 'ghG~',
                        antiname = 'ghG',
                        spin = -1,
                        color = 8,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'ghG~',
                        antitexname = 'ghG',
                        counterterm = None,
                        charge = -0.0,
                        line = 'dotted',
                        propagating = True,
                        goldstoneboson = False,
                        propagator = None,
                        GhostNumber = -1,
                        LeptonNumber = 0,
                        Y = 0,
                        selfconjugate = False)


ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              counterterm = None,
              charge = 0.0,
              line = 'straight',
              propagating = True,
              goldstoneboson = False,
              propagator = None,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0,
              selfconjugate = False)


ve__tilde__ = Particle(pdg_code = -12,
                       name = 've~',
                       antiname = 've',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 've~',
                       antitexname = 've',
                       counterterm = None,
                       charge = -0.0,
                       line = 'straight',
                       propagating = True,
                       goldstoneboson = False,
                       propagator = None,
                       GhostNumber = 0,
                       LeptonNumber = -1,
                       Y = 0,
                       selfconjugate = False)


vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              counterterm = None,
              charge = 0.0,
              line = 'straight',
              propagating = True,
              goldstoneboson = False,
              propagator = None,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0,
              selfconjugate = False)


vm__tilde__ = Particle(pdg_code = -14,
                       name = 'vm~',
                       antiname = 'vm',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'vm~',
                       antitexname = 'vm',
                       counterterm = None,
                       charge = -0.0,
                       line = 'straight',
                       propagating = True,
                       goldstoneboson = False,
                       propagator = None,
                       GhostNumber = 0,
                       LeptonNumber = -1,
                       Y = 0,
                       selfconjugate = False)


vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              counterterm = None,
              charge = 0.0,
              line = 'straight',
              propagating = True,
              goldstoneboson = False,
              propagator = None,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0,
              selfconjugate = False)


vt__tilde__ = Particle(pdg_code = -16,
                       name = 'vt~',
                       antiname = 'vt',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'vt~',
                       antitexname = 'vt',
                       counterterm = None,
                       charge = -0.0,
                       line = 'straight',
                       propagating = True,
                       goldstoneboson = False,
                       propagator = None,
                       GhostNumber = 0,
                       LeptonNumber = -1,
                       Y = 0,
                       selfconjugate = False)


e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      counterterm = None,
                      charge = -1.0,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0,
                      selfconjugate = False)


e__plus__ = Particle(pdg_code = -11,
                     name = 'e+',
                     antiname = 'e-',
                     spin = 2,
                     color = 1,
                     mass = Param.Me,
                     width = Param.ZERO,
                     texname = 'e+',
                     antitexname = 'e-',
                     counterterm = None,
                     charge = 1.0,
                     line = 'straight',
                     propagating = True,
                     goldstoneboson = False,
                     propagator = None,
                     GhostNumber = 0,
                     LeptonNumber = -1,
                     Y = 0,
                     selfconjugate = False)


mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       counterterm = None,
                       charge = -1.0,
                       line = 'straight',
                       propagating = True,
                       goldstoneboson = False,
                       propagator = None,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0,
                       selfconjugate = False)


mu__plus__ = Particle(pdg_code = -13,
                      name = 'mu+',
                      antiname = 'mu-',
                      spin = 2,
                      color = 1,
                      mass = Param.MMU,
                      width = Param.ZERO,
                      texname = 'mu+',
                      antitexname = 'mu-',
                      counterterm = None,
                      charge = 1.0,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = -1,
                      Y = 0,
                      selfconjugate = False)


ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       counterterm = None,
                       charge = -1.0,
                       line = 'straight',
                       propagating = True,
                       goldstoneboson = False,
                       propagator = None,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0,
                       selfconjugate = False)


ta__plus__ = Particle(pdg_code = -15,
                      name = 'ta+',
                      antiname = 'ta-',
                      spin = 2,
                      color = 1,
                      mass = Param.MTA,
                      width = Param.ZERO,
                      texname = 'ta+',
                      antitexname = 'ta-',
                      counterterm = None,
                      charge = 1.0,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = -1,
                      Y = 0,
                      selfconjugate = False)


u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             counterterm = None,
             charge = 0.666666666667,
             line = 'straight',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = False)


u__tilde__ = Particle(pdg_code = -2,
                      name = 'u~',
                      antiname = 'u',
                      spin = 2,
                      color = -3,
                      mass = Param.MU,
                      width = Param.ZERO,
                      texname = 'u~',
                      antitexname = 'u',
                      counterterm = None,
                      charge = -0.666666666667,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0,
                      selfconjugate = False)


c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             counterterm = None,
             charge = 0.666666666667,
             line = 'straight',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = False)


c__tilde__ = Particle(pdg_code = -4,
                      name = 'c~',
                      antiname = 'c',
                      spin = 2,
                      color = -3,
                      mass = Param.MC,
                      width = Param.ZERO,
                      texname = 'c~',
                      antitexname = 'c',
                      counterterm = None,
                      charge = -0.666666666667,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0,
                      selfconjugate = False)


t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             counterterm = None,
             charge = 0.666666666667,
             line = 'straight',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = False)


t__tilde__ = Particle(pdg_code = -6,
                      name = 't~',
                      antiname = 't',
                      spin = 2,
                      color = -3,
                      mass = Param.MT,
                      width = Param.WT,
                      texname = 't~',
                      antitexname = 't',
                      counterterm = None,
                      charge = -0.666666666667,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0,
                      selfconjugate = False)


d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             counterterm = None,
             charge = -0.333333333333,
             line = 'straight',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = False)


d__tilde__ = Particle(pdg_code = -1,
                      name = 'd~',
                      antiname = 'd',
                      spin = 2,
                      color = -3,
                      mass = Param.MD,
                      width = Param.ZERO,
                      texname = 'd~',
                      antitexname = 'd',
                      counterterm = None,
                      charge = 0.333333333333,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0,
                      selfconjugate = False)


s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             counterterm = None,
             charge = -0.333333333333,
             line = 'straight',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = False)


s__tilde__ = Particle(pdg_code = -3,
                      name = 's~',
                      antiname = 's',
                      spin = 2,
                      color = -3,
                      mass = Param.MS,
                      width = Param.ZERO,
                      texname = 's~',
                      antitexname = 's',
                      counterterm = None,
                      charge = 0.333333333333,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0,
                      selfconjugate = False)


b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             counterterm = None,
             charge = -0.333333333333,
             line = 'straight',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = False)


b__tilde__ = Particle(pdg_code = -5,
                      name = 'b~',
                      antiname = 'b',
                      spin = 2,
                      color = -3,
                      mass = Param.MB,
                      width = Param.ZERO,
                      texname = 'b~',
                      antitexname = 'b',
                      counterterm = None,
                      charge = 0.333333333333,
                      line = 'straight',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0,
                      selfconjugate = False)


H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             counterterm = None,
             charge = 0.0,
             line = 'dashed',
             propagating = True,
             goldstoneboson = False,
             propagator = None,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             selfconjugate = True)


G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              counterterm = None,
              charge = 0.0,
              line = 'dashed',
              propagating = True,
              goldstoneboson = False,
              propagator = None,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0,
              goldstone = True,
              selfconjugate = True)


G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     counterterm = None,
                     charge = 1.0,
                     line = 'dashed',
                     propagating = True,
                     goldstoneboson = False,
                     propagator = None,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0,
                     goldstone = True,
                     selfconjugate = False)


G__minus__ = Particle(pdg_code = -251,
                      name = 'G-',
                      antiname = 'G+',
                      spin = 1,
                      color = 1,
                      mass = Param.MW,
                      width = Param.WW,
                      texname = 'G-',
                      antitexname = 'G+',
                      counterterm = None,
                      charge = -1.0,
                      line = 'dashed',
                      propagating = True,
                      goldstoneboson = False,
                      propagator = None,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0,
                      goldstone = -1,
                      selfconjugate = False)


P__tilde__SDM = Particle(pdg_code = 1000022,
                         name = '~SDM',
                         antiname = '~SDM',
                         spin = 1,
                         color = 1,
                         mass = Param.mSDM,
                         width = Param.Wsdm,
                         texname = '~SDM',
                         antitexname = '~SDM',
                         counterterm = None,
                         charge = 0.0,
                         line = 'dashed',
                         propagating = True,
                         goldstoneboson = False,
                         propagator = None,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0,
                         selfconjugate = True)


Fsdm = Particle(pdg_code = 999000007,
                name = 'Fsdm',
                antiname = 'Fsdm',
                spin = 1,
                color = 1,
                mass = Param.MFsdm,
                width = Param.WFsdm,
                texname = 'Fsdm',
                antitexname = 'Fsdm',
                counterterm = None,
                charge = 0.0,
                line = 'dashed',
                propagating = True,
                goldstoneboson = False,
                propagator = None,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0,
                selfconjugate = True)


P__tilde__fdm = Particle(pdg_code = 999000008,
                         name = '~fdm',
                         antiname = '~fdm',
                         spin = 2,
                         color = 1,
                         mass = Param.fdmm,
                         width = Param.Wfdm,
                         texname = '~fdm',
                         antitexname = '~fdm',
                         counterterm = None,
                         charge = 0.0,
                         line = 'swavy',
                         propagating = True,
                         goldstoneboson = False,
                         propagator = None,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0,
                         selfconjugate = True)


P__tilde__vdm = Particle(pdg_code = 999000009,
                         name = '~vdm',
                         antiname = '~vdm',
                         spin = 3,
                         color = 1,
                         mass = Param.vdmm,
                         width = Param.Wvdm,
                         texname = '~vdm',
                         antitexname = '~vdm',
                         counterterm = None,
                         charge = 0.0,
                         line = 'wavy',
                         propagating = True,
                         goldstoneboson = False,
                         propagator = None,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0,
                         selfconjugate = True)


Fvdm = Particle(pdg_code = 999000010,
                name = 'Fvdm',
                antiname = 'Fvdm',
                spin = 3,
                color = 1,
                mass = Param.MFvdm,
                width = Param.WFvdm,
                texname = 'Fvdm',
                antitexname = 'Fvdm',
                counterterm = None,
                charge = 0.0,
                line = 'wavy',
                propagating = True,
                goldstoneboson = False,
                propagator = None,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0,
                selfconjugate = True)


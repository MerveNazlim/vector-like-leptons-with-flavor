# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Wed 22 Jan 2020 09:39:38


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

psie = Particle(pdg_code = 9000005,
                name = 'psie',
                antiname = 'psie~',
                spin = 2,
                color = 1,
                mass = Param.MF1,
                width = Param.WF1,
                texname = ' \\psi_1',
                antitexname = '\\bar \\psi_1',
                charge = -1,
                GhostNumber = 0,
                LeptonNumber = 1,
                Y = 0)

psie__tilde__ = psie.anti()

psimu = Particle(pdg_code = 9000006,
                 name = 'psimu',
                 antiname = 'psimu~',
                 spin = 2,
                 color = 1,
                 mass = Param.MF2,
                 width = Param.WF2,
                 texname = '\\psi_2',
                 antitexname = '\\bar\\psi_2',
                 charge = -1,
                 GhostNumber = 0,
                 LeptonNumber = 1,
                 Y = 0)

psimu__tilde__ = psimu.anti()

psita = Particle(pdg_code = 9000007,
                 name = 'psita',
                 antiname = 'psita~',
                 spin = 2,
                 color = 1,
                 mass = Param.MF3,
                 width = Param.WF3,
                 texname = '\\psi_3',
                 antitexname = '\\bar\\psi_3',
                 charge = -1,
                 GhostNumber = 0,
                 LeptonNumber = 1,
                 Y = 0)

psita__tilde__ = psita.anti()

S11 = Particle(pdg_code = 9000008,
               name = 'S11',
               antiname = 'S11~',
               spin = 1,
               color = 1,
               mass = Param.MS11,
               width = Param.WS11,
               texname = 'S11',
               antitexname = 'S11~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S11__tilde__ = S11.anti()

S12 = Particle(pdg_code = 9000009,
               name = 'S12',
               antiname = 'S12~',
               spin = 1,
               color = 1,
               mass = Param.MS12,
               width = Param.WS12,
               texname = 'S12',
               antitexname = 'S12~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S12__tilde__ = S12.anti()

S13 = Particle(pdg_code = 9000010,
               name = 'S13',
               antiname = 'S13~',
               spin = 1,
               color = 1,
               mass = Param.MS13,
               width = Param.WS13,
               texname = 'S13',
               antitexname = 'S13~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S13__tilde__ = S13.anti()

S21 = Particle(pdg_code = 9000011,
               name = 'S21',
               antiname = 'S21~',
               spin = 1,
               color = 1,
               mass = Param.MS21,
               width = Param.WS21,
               texname = 'S21',
               antitexname = 'S21~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S21__tilde__ = S21.anti()

S22 = Particle(pdg_code = 9000012,
               name = 'S22',
               antiname = 'S22~',
               spin = 1,
               color = 1,
               mass = Param.MS22,
               width = Param.WS22,
               texname = 'S22',
               antitexname = 'S22~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S22__tilde__ = S22.anti()

S23 = Particle(pdg_code = 9000013,
               name = 'S23',
               antiname = 'S23~',
               spin = 1,
               color = 1,
               mass = Param.MS23,
               width = Param.WS23,
               texname = 'S23',
               antitexname = 'S23~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S23__tilde__ = S23.anti()

S31 = Particle(pdg_code = 9000014,
               name = 'S31',
               antiname = 'S31~',
               spin = 1,
               color = 1,
               mass = Param.MS31,
               width = Param.WS31,
               texname = 'S31',
               antitexname = 'S31~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S31__tilde__ = S31.anti()

S32 = Particle(pdg_code = 9000015,
               name = 'S32',
               antiname = 'S32~',
               spin = 1,
               color = 1,
               mass = Param.MS32,
               width = Param.WS32,
               texname = 'S32',
               antitexname = 'S32~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S32__tilde__ = S32.anti()

S33 = Particle(pdg_code = 9000016,
               name = 'S33',
               antiname = 'S33~',
               spin = 1,
               color = 1,
               mass = Param.MS33,
               width = Param.WS33,
               texname = 'S33',
               antitexname = 'S33~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S33__tilde__ = S33.anti()


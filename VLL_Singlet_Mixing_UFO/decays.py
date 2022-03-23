# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Wed 22 Jan 2020 09:39:38


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.e__minus__,P.psie__tilde__):'((-MF1**2 + MH**2)*(-(K*MF1**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.psimu__tilde__):'((-MF2**2 + MH**2)*(-(K*MF2**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.psie,P.e__plus__):'((-MF1**2 + MH**2)*(-(K*MF1**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.psimu,P.mu__plus__):'((-MF2**2 + MH**2)*(-(K*MF2**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.psita,P.ta__plus__):'((-(K*MF3**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2. - (K*MTA**2*complexconjugate(K))/2.)*cmath.sqrt(MF3**4 - 2*MF3**2*MH**2 + MH**4 - 2*MF3**2*MTA**2 - 2*MH**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.psita__tilde__):'((-(K*MF3**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2. - (K*MTA**2*complexconjugate(K))/2.)*cmath.sqrt(MF3**4 - 2*MF3**2*MH**2 + MH**4 - 2*MF3**2*MTA**2 - 2*MH**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_psie = Decay(name = 'Decay_psie',
                   particle = P.psie,
                   partial_widths = {(P.H,P.e__minus__):'((MF1**2 - MH**2)*((K*MF1**2*complexconjugate(K))/2. - (K*MH**2*complexconjugate(K))/2.))/(32.*cmath.pi*abs(MF1)**3)',
                                     (P.S11,P.e__minus__):'((MF1**2 - MS11**2)*(Kprime*MF1**2*complexconjugate(Kprime) - Kprime*MS11**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MF1)**3)',
                                     (P.S21,P.mu__minus__):'((MF1**2 - MS21**2)*(Kprime*MF1**2*complexconjugate(Kprime) - Kprime*MS21**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MF1)**3)',
                                     (P.S31,P.ta__minus__):'((Kprime*MF1**2*complexconjugate(Kprime) - Kprime*MS31**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF1**4 - 2*MF1**2*MS31**2 + MS31**4 - 2*MF1**2*MTA**2 - 2*MS31**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MF1)**3)',
                                     (P.W__minus__,P.ve):'((MF1**2 - MW**2)*((ee**2*K*vev**2*complexconjugate(K))/(4.*sw**2) + (ee**2*K*MF1**2*vev**2*complexconjugate(K))/(4.*MW**2*sw**2) - (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MF1**2*sw**2)))/(32.*cmath.pi*abs(MF1)**3)',
                                     (P.Z,P.e__minus__):'((MF1**2 - MZ**2)*((ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) + (ee**2*K*MF1**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) - (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF1**2*sw**2)))/(32.*cmath.pi*abs(MF1)**3)'})

Decay_psimu = Decay(name = 'Decay_psimu',
                    particle = P.psimu,
                    partial_widths = {(P.H,P.mu__minus__):'((MF2**2 - MH**2)*((K*MF2**2*complexconjugate(K))/2. - (K*MH**2*complexconjugate(K))/2.))/(32.*cmath.pi*abs(MF2)**3)',
                                      (P.S12,P.e__minus__):'((MF2**2 - MS12**2)*(Kprime*MF2**2*complexconjugate(Kprime) - Kprime*MS12**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MF2)**3)',
                                      (P.S22,P.mu__minus__):'((MF2**2 - MS22**2)*(Kprime*MF2**2*complexconjugate(Kprime) - Kprime*MS22**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MF2)**3)',
                                      (P.S32,P.ta__minus__):'((Kprime*MF2**2*complexconjugate(Kprime) - Kprime*MS32**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF2**4 - 2*MF2**2*MS32**2 + MS32**4 - 2*MF2**2*MTA**2 - 2*MS32**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MF2)**3)',
                                      (P.W__minus__,P.vm):'((MF2**2 - MW**2)*((ee**2*K*vev**2*complexconjugate(K))/(4.*sw**2) + (ee**2*K*MF2**2*vev**2*complexconjugate(K))/(4.*MW**2*sw**2) - (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MF2**2*sw**2)))/(32.*cmath.pi*abs(MF2)**3)',
                                      (P.Z,P.mu__minus__):'((MF2**2 - MZ**2)*((ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) + (ee**2*K*MF2**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) - (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF2**2*sw**2)))/(32.*cmath.pi*abs(MF2)**3)'})

Decay_psita = Decay(name = 'Decay_psita',
                    particle = P.psita,
                    partial_widths = {(P.H,P.ta__minus__):'(((K*MF3**2*complexconjugate(K))/2. - (K*MH**2*complexconjugate(K))/2. + (K*MTA**2*complexconjugate(K))/2.)*cmath.sqrt(MF3**4 - 2*MF3**2*MH**2 + MH**4 - 2*MF3**2*MTA**2 - 2*MH**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MF3)**3)',
                                      (P.S13,P.e__minus__):'((MF3**2 - MS13**2)*(Kprime*MF3**2*complexconjugate(Kprime) - Kprime*MS13**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MF3)**3)',
                                      (P.S23,P.mu__minus__):'((MF3**2 - MS23**2)*(Kprime*MF3**2*complexconjugate(Kprime) - Kprime*MS23**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MF3)**3)',
                                      (P.S33,P.ta__minus__):'((Kprime*MF3**2*complexconjugate(Kprime) - Kprime*MS33**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF3**4 - 2*MF3**2*MS33**2 + MS33**4 - 2*MF3**2*MTA**2 - 2*MS33**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MF3)**3)',
                                      (P.W__minus__,P.vt):'((MF3**2 - MW**2)*((ee**2*K*vev**2*complexconjugate(K))/(4.*sw**2) + (ee**2*K*MF3**2*vev**2*complexconjugate(K))/(4.*MW**2*sw**2) - (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MF3**2*sw**2)))/(32.*cmath.pi*abs(MF3)**3)',
                                      (P.Z,P.ta__minus__):'(((ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(8.*cw**2*MF3**2*sw**2) + (ee**2*K*MF3**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*cw**2*MZ**2*sw**2) + (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(8.*cw**2*MF3**2*MZ**2*sw**2) - (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF3**2*sw**2))*cmath.sqrt(MF3**4 - 2*MF3**2*MTA**2 + MTA**4 - 2*MF3**2*MZ**2 - 2*MTA**2*MZ**2 + MZ**4))/(32.*cmath.pi*abs(MF3)**3)'})

Decay_S11 = Decay(name = 'Decay_S11',
                  particle = P.S11,
                  partial_widths = {(P.e__minus__,P.e__plus__):'(Hvev**2*K*Kprime*MS11**4*complexconjugate(K)*complexconjugate(Kprime))/(32.*cmath.pi*MF1**2*abs(MS11)**3)',
                                    (P.psie,P.e__plus__):'((-MF1**2 + MS11**2)*(-(Kprime*MF1**2*complexconjugate(Kprime)) + Kprime*MS11**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS11)**3)'})

Decay_S12 = Decay(name = 'Decay_S12',
                  particle = P.S12,
                  partial_widths = {(P.mu__minus__,P.e__plus__):'(Hvev**2*K*Kprime*MS12**4*complexconjugate(K)*complexconjugate(Kprime))/(32.*cmath.pi*MF1**2*abs(MS12)**3)',
                                    (P.psimu,P.e__plus__):'((-MF2**2 + MS12**2)*(-(Kprime*MF2**2*complexconjugate(Kprime)) + Kprime*MS12**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS12)**3)'})

Decay_S13 = Decay(name = 'Decay_S13',
                  particle = P.S13,
                  partial_widths = {(P.psita,P.e__plus__):'((-MF3**2 + MS13**2)*(-(Kprime*MF3**2*complexconjugate(Kprime)) + Kprime*MS13**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS13)**3)',
                                    (P.ta__minus__,P.e__plus__):'((MS13**2 - MTA**2)*((Hvev**2*K*Kprime*MS13**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF1**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF1**2)))/(16.*cmath.pi*abs(MS13)**3)'})

Decay_S21 = Decay(name = 'Decay_S21',
                  particle = P.S21,
                  partial_widths = {(P.e__minus__,P.mu__plus__):'(Hvev**2*K*Kprime*MS21**4*complexconjugate(K)*complexconjugate(Kprime))/(32.*cmath.pi*MF2**2*abs(MS21)**3)',
                                    (P.psie,P.mu__plus__):'((-MF1**2 + MS21**2)*(-(Kprime*MF1**2*complexconjugate(Kprime)) + Kprime*MS21**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS21)**3)'})

Decay_S22 = Decay(name = 'Decay_S22',
                  particle = P.S22,
                  partial_widths = {(P.mu__minus__,P.mu__plus__):'(Hvev**2*K*Kprime*MS22**4*complexconjugate(K)*complexconjugate(Kprime))/(32.*cmath.pi*MF2**2*abs(MS22)**3)',
                                    (P.psimu,P.mu__plus__):'((-MF2**2 + MS22**2)*(-(Kprime*MF2**2*complexconjugate(Kprime)) + Kprime*MS22**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS22)**3)'})

Decay_S23 = Decay(name = 'Decay_S23',
                  particle = P.S23,
                  partial_widths = {(P.psita,P.mu__plus__):'((-MF3**2 + MS23**2)*(-(Kprime*MF3**2*complexconjugate(Kprime)) + Kprime*MS23**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS23)**3)',
                                    (P.ta__minus__,P.mu__plus__):'((MS23**2 - MTA**2)*((Hvev**2*K*Kprime*MS23**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF2**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF2**2)))/(16.*cmath.pi*abs(MS23)**3)'})

Decay_S31 = Decay(name = 'Decay_S31',
                  particle = P.S31,
                  partial_widths = {(P.e__minus__,P.ta__plus__):'((MS31**2 - MTA**2)*((Hvev**2*K*Kprime*MS31**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2)))/(16.*cmath.pi*abs(MS31)**3)',
                                    (P.psie,P.ta__plus__):'((-(Kprime*MF1**2*complexconjugate(Kprime)) + Kprime*MS31**2*complexconjugate(Kprime) - Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF1**4 - 2*MF1**2*MS31**2 + MS31**4 - 2*MF1**2*MTA**2 - 2*MS31**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MS31)**3)'})

Decay_S32 = Decay(name = 'Decay_S32',
                  particle = P.S32,
                  partial_widths = {(P.mu__minus__,P.ta__plus__):'((MS32**2 - MTA**2)*((Hvev**2*K*Kprime*MS32**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2)))/(16.*cmath.pi*abs(MS32)**3)',
                                    (P.psimu,P.ta__plus__):'((-(Kprime*MF2**2*complexconjugate(Kprime)) + Kprime*MS32**2*complexconjugate(Kprime) - Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF2**4 - 2*MF2**2*MS32**2 + MS32**4 - 2*MF2**2*MTA**2 - 2*MS32**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MS32)**3)'})

Decay_S33 = Decay(name = 'Decay_S33',
                  particle = P.S33,
                  partial_widths = {(P.psita,P.ta__plus__):'((-(Kprime*MF3**2*complexconjugate(Kprime)) + Kprime*MS33**2*complexconjugate(Kprime) - Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF3**4 - 2*MF3**2*MS33**2 + MS33**4 - 2*MF3**2*MTA**2 - 2*MS33**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MS33)**3)',
                                    (P.ta__minus__,P.ta__plus__):'(((Hvev**2*K*Kprime*MS33**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/MF3**2)*cmath.sqrt(MS33**4 - 4*MS33**2*MTA**2))/(16.*cmath.pi*abs(MS33)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.H,P.psita):'(((K*MF3**2*complexconjugate(K))/2. - (K*MH**2*complexconjugate(K))/2. + (K*MTA**2*complexconjugate(K))/2.)*cmath.sqrt(MF3**4 - 2*MF3**2*MH**2 + MH**4 - 2*MF3**2*MTA**2 - 2*MH**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S13,P.e__minus__):'((-MS13**2 + MTA**2)*(-(Hvev**2*K*Kprime*MS13**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF1**2) + (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF1**2)))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S23,P.mu__minus__):'((-MS23**2 + MTA**2)*(-(Hvev**2*K*Kprime*MS23**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF2**2) + (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF2**2)))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S31__tilde__,P.e__minus__):'((-MS31**2 + MTA**2)*(-(Hvev**2*K*Kprime*MS31**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2) + (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2)))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S31__tilde__,P.psie):'((Kprime*MF1**2*complexconjugate(Kprime) - Kprime*MS31**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF1**4 - 2*MF1**2*MS31**2 + MS31**4 - 2*MF1**2*MTA**2 - 2*MS31**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S32__tilde__,P.mu__minus__):'((-MS32**2 + MTA**2)*(-(Hvev**2*K*Kprime*MS32**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2) + (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MF3**2)))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S32__tilde__,P.psimu):'((Kprime*MF2**2*complexconjugate(Kprime) - Kprime*MS32**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF2**4 - 2*MF2**2*MS32**2 + MS32**4 - 2*MF2**2*MTA**2 - 2*MS32**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S33__tilde__,P.psita):'((Kprime*MF3**2*complexconjugate(Kprime) - Kprime*MS33**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MF3**4 - 2*MF3**2*MS33**2 + MS33**4 - 2*MF3**2*MTA**2 - 2*MS33**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.Z,P.psita):'(((ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(8.*cw**2*MF3**2*sw**2) + (ee**2*K*MF3**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*cw**2*MZ**2*sw**2) + (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(8.*cw**2*MF3**2*MZ**2*sw**2) - (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF3**2*sw**2))*cmath.sqrt(MF3**4 - 2*MF3**2*MTA**2 + MTA**4 - 2*MF3**2*MZ**2 - 2*MTA**2*MZ**2 + MZ**4))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.psie__tilde__):'((-MF1**2 + MW**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(4.*sw**2) - (ee**2*K*MF1**2*vev**2*complexconjugate(K))/(4.*MW**2*sw**2) + (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MF1**2*sw**2)))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.psimu__tilde__):'((-MF2**2 + MW**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(4.*sw**2) - (ee**2*K*MF2**2*vev**2*complexconjugate(K))/(4.*MW**2*sw**2) + (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MF2**2*sw**2)))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.psita__tilde__):'((-MF3**2 + MW**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(4.*sw**2) - (ee**2*K*MF3**2*vev**2*complexconjugate(K))/(4.*MW**2*sw**2) + (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MF3**2*sw**2)))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.psie__tilde__):'((-MF1**2 + MZ**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MF1**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF1**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.psimu__tilde__):'((-MF2**2 + MZ**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MF2**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF2**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psie,P.e__plus__):'((-MF1**2 + MZ**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MF1**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF1**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psie,P.psie__tilde__):'(((8*ee**2*MF1**2*sw**2)/cw**2 + (4*ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MF1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psimu,P.mu__plus__):'((-MF2**2 + MZ**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MF2**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF2**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psimu,P.psimu__tilde__):'(((8*ee**2*MF2**2*sw**2)/cw**2 + (4*ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MF2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psita,P.psita__tilde__):'(((8*ee**2*MF3**2*sw**2)/cw**2 + (4*ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MF3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psita,P.ta__plus__):'((-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(8.*cw**2*MF3**2*sw**2) - (ee**2*K*MF3**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*cw**2*MZ**2*sw**2) - (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(8.*cw**2*MF3**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF3**2*sw**2))*cmath.sqrt(MF3**4 - 2*MF3**2*MTA**2 + MTA**4 - 2*MF3**2*MZ**2 - 2*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.psita__tilde__):'((-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(8.*cw**2*MF3**2*sw**2) - (ee**2*K*MF3**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*cw**2*MZ**2*sw**2) - (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(8.*cw**2*MF3**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MF3**2*sw**2))*cmath.sqrt(MF3**4 - 2*MF3**2*MTA**2 + MTA**4 - 2*MF3**2*MZ**2 - 2*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})


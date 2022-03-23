# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Fri 28 Feb 2020 16:27:26


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.e__minus__,P.psiem__tilde__):'((-MFm1**2 + MH**2)*(-(K*MFm1**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.psimum__tilde__):'((-MFm2**2 + MH**2)*(-(K*MFm2**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.psiem,P.e__plus__):'((-MFm1**2 + MH**2)*(-(K*MFm1**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.psimum,P.mu__plus__):'((-MFm2**2 + MH**2)*(-(K*MFm2**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.psitam,P.ta__plus__):'((-(K*MFm3**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2. - (K*MTA**2*complexconjugate(K))/2.)*cmath.sqrt(MFm3**4 - 2*MFm3**2*MH**2 + MH**4 - 2*MFm3**2*MTA**2 - 2*MH**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.psitam__tilde__):'((-(K*MFm3**2*complexconjugate(K))/2. + (K*MH**2*complexconjugate(K))/2. - (K*MTA**2*complexconjugate(K))/2.)*cmath.sqrt(MFm3**4 - 2*MFm3**2*MH**2 + MH**4 - 2*MFm3**2*MTA**2 - 2*MH**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_psiem = Decay(name = 'Decay_psiem',
                    particle = P.psiem,
                    partial_widths = {(P.H,P.e__minus__):'((MFm1**2 - MH**2)*((K*MFm1**2*complexconjugate(K))/2. - (K*MH**2*complexconjugate(K))/2.))/(32.*cmath.pi*abs(MFm1)**3)',
                                      (P.S11__tilde__,P.e__minus__):'((MFm1**2 - MS11**2)*(Kprime*MFm1**2*complexconjugate(Kprime) - Kprime*MS11**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFm1)**3)',
                                      (P.S21__tilde__,P.mu__minus__):'((MFm1**2 - MS21**2)*(Kprime*MFm1**2*complexconjugate(Kprime) - Kprime*MS21**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFm1)**3)',
                                      (P.S31__tilde__,P.ta__minus__):'((Kprime*MFm1**2*complexconjugate(Kprime) - Kprime*MS31**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm1**4 - 2*MFm1**2*MS31**2 + MS31**4 - 2*MFm1**2*MTA**2 - 2*MS31**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MFm1)**3)',
                                      (P.W__minus__,P.psiez):'(((ee**2*MFm1**2)/sw**2 - (6*ee**2*MFm1*MFz1)/sw**2 + (ee**2*MFz1**2)/sw**2 + (ee**2*MFm1**4)/(MW**2*sw**2) - (2*ee**2*MFm1**2*MFz1**2)/(MW**2*sw**2) + (ee**2*MFz1**4)/(MW**2*sw**2) - (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm1**4 - 2*MFm1**2*MFz1**2 + MFz1**4 - 2*MFm1**2*MW**2 - 2*MFz1**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MFm1)**3)',
                                      (P.Z,P.e__minus__):'((MFm1**2 - MZ**2)*((ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) + (ee**2*K*MFm1**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) - (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm1**2*sw**2)))/(32.*cmath.pi*abs(MFm1)**3)'})

Decay_psimum = Decay(name = 'Decay_psimum',
                     particle = P.psimum,
                     partial_widths = {(P.H,P.mu__minus__):'((MFm2**2 - MH**2)*((K*MFm2**2*complexconjugate(K))/2. - (K*MH**2*complexconjugate(K))/2.))/(32.*cmath.pi*abs(MFm2)**3)',
                                       (P.S12__tilde__,P.e__minus__):'((MFm2**2 - MS12**2)*(Kprime*MFm2**2*complexconjugate(Kprime) - Kprime*MS12**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFm2)**3)',
                                       (P.S22__tilde__,P.mu__minus__):'((MFm2**2 - MS22**2)*(Kprime*MFm2**2*complexconjugate(Kprime) - Kprime*MS22**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFm2)**3)',
                                       (P.S32__tilde__,P.ta__minus__):'((Kprime*MFm2**2*complexconjugate(Kprime) - Kprime*MS32**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm2**4 - 2*MFm2**2*MS32**2 + MS32**4 - 2*MFm2**2*MTA**2 - 2*MS32**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MFm2)**3)',
                                       (P.W__minus__,P.psimuz):'(((ee**2*MFm2**2)/sw**2 - (6*ee**2*MFm2*MFz2)/sw**2 + (ee**2*MFz2**2)/sw**2 + (ee**2*MFm2**4)/(MW**2*sw**2) - (2*ee**2*MFm2**2*MFz2**2)/(MW**2*sw**2) + (ee**2*MFz2**4)/(MW**2*sw**2) - (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm2**4 - 2*MFm2**2*MFz2**2 + MFz2**4 - 2*MFm2**2*MW**2 - 2*MFz2**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MFm2)**3)',
                                       (P.Z,P.mu__minus__):'((MFm2**2 - MZ**2)*((ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) + (ee**2*K*MFm2**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) - (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm2**2*sw**2)))/(32.*cmath.pi*abs(MFm2)**3)'})

Decay_psitam = Decay(name = 'Decay_psitam',
                     particle = P.psitam,
                     partial_widths = {(P.H,P.ta__minus__):'(((K*MFm3**2*complexconjugate(K))/2. - (K*MH**2*complexconjugate(K))/2. + (K*MTA**2*complexconjugate(K))/2.)*cmath.sqrt(MFm3**4 - 2*MFm3**2*MH**2 + MH**4 - 2*MFm3**2*MTA**2 - 2*MH**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MFm3)**3)',
                                       (P.S13__tilde__,P.e__minus__):'((MFm3**2 - MS13**2)*(Kprime*MFm3**2*complexconjugate(Kprime) - Kprime*MS13**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFm3)**3)',
                                       (P.S23__tilde__,P.mu__minus__):'((MFm3**2 - MS23**2)*(Kprime*MFm3**2*complexconjugate(Kprime) - Kprime*MS23**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFm3)**3)',
                                       (P.S33__tilde__,P.ta__minus__):'((Kprime*MFm3**2*complexconjugate(Kprime) - Kprime*MS33**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm3**4 - 2*MFm3**2*MS33**2 + MS33**4 - 2*MFm3**2*MTA**2 - 2*MS33**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MFm3)**3)',
                                       (P.W__minus__,P.psitaz):'(((ee**2*MFm3**2)/sw**2 - (6*ee**2*MFm3*MFz3)/sw**2 + (ee**2*MFz3**2)/sw**2 + (ee**2*MFm3**4)/(MW**2*sw**2) - (2*ee**2*MFm3**2*MFz3**2)/(MW**2*sw**2) + (ee**2*MFz3**4)/(MW**2*sw**2) - (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm3**4 - 2*MFm3**2*MFz3**2 + MFz3**4 - 2*MFm3**2*MW**2 - 2*MFz3**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MFm3)**3)',
                                       (P.Z,P.ta__minus__):'(((ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(8.*cw**2*MFm3**2*sw**2) + (ee**2*K*MFm3**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*cw**2*MZ**2*sw**2) + (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(8.*cw**2*MFm3**2*MZ**2*sw**2) - (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm3**2*sw**2))*cmath.sqrt(MFm3**4 - 2*MFm3**2*MTA**2 + MTA**4 - 2*MFm3**2*MZ**2 - 2*MTA**2*MZ**2 + MZ**4))/(32.*cmath.pi*abs(MFm3)**3)'})

Decay_psiez = Decay(name = 'Decay_psiez',
                    particle = P.psiez,
                    partial_widths = {(P.S11__tilde__,P.ve):'((MFz1**2 - MS11**2)*(Kprime*MFz1**2*complexconjugate(Kprime) - Kprime*MS11**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz1)**3)',
                                      (P.S21__tilde__,P.vm):'((MFz1**2 - MS21**2)*(Kprime*MFz1**2*complexconjugate(Kprime) - Kprime*MS21**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz1)**3)',
                                      (P.S31__tilde__,P.vt):'((MFz1**2 - MS31**2)*(Kprime*MFz1**2*complexconjugate(Kprime) - Kprime*MS31**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz1)**3)',
                                      (P.W__plus__,P.e__minus__):'((MFz1**2 - MW**2)*((ee**2*K*MFz1**2*vev**2*complexconjugate(K))/(4.*MFm1**2*sw**2) + (ee**2*K*MFz1**4*vev**2*complexconjugate(K))/(4.*MFm1**2*MW**2*sw**2) - (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MFm1**2*sw**2)))/(32.*cmath.pi*abs(MFz1)**3)',
                                      (P.W__plus__,P.psiem):'(((ee**2*MFm1**2)/sw**2 - (6*ee**2*MFm1*MFz1)/sw**2 + (ee**2*MFz1**2)/sw**2 + (ee**2*MFm1**4)/(MW**2*sw**2) - (2*ee**2*MFm1**2*MFz1**2)/(MW**2*sw**2) + (ee**2*MFz1**4)/(MW**2*sw**2) - (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm1**4 - 2*MFm1**2*MFz1**2 + MFz1**4 - 2*MFm1**2*MW**2 - 2*MFz1**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MFz1)**3)'})

Decay_psimuz = Decay(name = 'Decay_psimuz',
                     particle = P.psimuz,
                     partial_widths = {(P.S12__tilde__,P.ve):'((MFz2**2 - MS12**2)*(Kprime*MFz2**2*complexconjugate(Kprime) - Kprime*MS12**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz2)**3)',
                                       (P.S22__tilde__,P.vm):'((MFz2**2 - MS22**2)*(Kprime*MFz2**2*complexconjugate(Kprime) - Kprime*MS22**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz2)**3)',
                                       (P.S32__tilde__,P.vt):'((MFz2**2 - MS32**2)*(Kprime*MFz2**2*complexconjugate(Kprime) - Kprime*MS32**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz2)**3)',
                                       (P.W__plus__,P.mu__minus__):'((MFz2**2 - MW**2)*((ee**2*K*MFz2**2*vev**2*complexconjugate(K))/(4.*MFm2**2*sw**2) + (ee**2*K*MFz2**4*vev**2*complexconjugate(K))/(4.*MFm2**2*MW**2*sw**2) - (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MFm2**2*sw**2)))/(32.*cmath.pi*abs(MFz2)**3)',
                                       (P.W__plus__,P.psimum):'(((ee**2*MFm2**2)/sw**2 - (6*ee**2*MFm2*MFz2)/sw**2 + (ee**2*MFz2**2)/sw**2 + (ee**2*MFm2**4)/(MW**2*sw**2) - (2*ee**2*MFm2**2*MFz2**2)/(MW**2*sw**2) + (ee**2*MFz2**4)/(MW**2*sw**2) - (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm2**4 - 2*MFm2**2*MFz2**2 + MFz2**4 - 2*MFm2**2*MW**2 - 2*MFz2**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MFz2)**3)'})

Decay_psitaz = Decay(name = 'Decay_psitaz',
                     particle = P.psitaz,
                     partial_widths = {(P.S13__tilde__,P.ve):'((MFz3**2 - MS13**2)*(Kprime*MFz3**2*complexconjugate(Kprime) - Kprime*MS13**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz3)**3)',
                                       (P.S23__tilde__,P.vm):'((MFz3**2 - MS23**2)*(Kprime*MFz3**2*complexconjugate(Kprime) - Kprime*MS23**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz3)**3)',
                                       (P.S33__tilde__,P.vt):'((MFz3**2 - MS33**2)*(Kprime*MFz3**2*complexconjugate(Kprime) - Kprime*MS33**2*complexconjugate(Kprime)))/(32.*cmath.pi*abs(MFz3)**3)',
                                       (P.W__plus__,P.psitam):'(((ee**2*MFm3**2)/sw**2 - (6*ee**2*MFm3*MFz3)/sw**2 + (ee**2*MFz3**2)/sw**2 + (ee**2*MFm3**4)/(MW**2*sw**2) - (2*ee**2*MFm3**2*MFz3**2)/(MW**2*sw**2) + (ee**2*MFz3**4)/(MW**2*sw**2) - (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm3**4 - 2*MFm3**2*MFz3**2 + MFz3**4 - 2*MFm3**2*MW**2 - 2*MFz3**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MFz3)**3)',
                                       (P.W__plus__,P.ta__minus__):'(((ee**2*K*MFz3**2*vev**2*complexconjugate(K))/(4.*MFm3**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*MFm3**2*sw**2) + (ee**2*K*MFz3**4*vev**2*complexconjugate(K))/(4.*MFm3**2*MW**2*sw**2) - (ee**2*K*MFz3**2*MTA**2*vev**2*complexconjugate(K))/(2.*MFm3**2*MW**2*sw**2) + (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(4.*MFm3**2*MW**2*sw**2) - (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MFm3**2*sw**2))*cmath.sqrt(MFz3**4 - 2*MFz3**2*MTA**2 + MTA**4 - 2*MFz3**2*MW**2 - 2*MTA**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MFz3)**3)'})

Decay_S11 = Decay(name = 'Decay_S11',
                  particle = P.S11,
                  partial_widths = {(P.e__minus__,P.e__plus__):'(Hvev**2*K*Kprime*MS11**4*complexconjugate(K)*complexconjugate(Kprime))/(32.*cmath.pi*MFm1**2*abs(MS11)**3)',
                                    (P.e__minus__,P.psiem__tilde__):'((-MFm1**2 + MS11**2)*(-(Kprime*MFm1**2*complexconjugate(Kprime)) + Kprime*MS11**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS11)**3)',
                                    (P.ve,P.psiez__tilde__):'((-MFz1**2 + MS11**2)*(-(Kprime*MFz1**2*complexconjugate(Kprime)) + Kprime*MS11**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS11)**3)'})

Decay_S12 = Decay(name = 'Decay_S12',
                  particle = P.S12,
                  partial_widths = {(P.e__minus__,P.mu__plus__):'(Hvev**2*K*Kprime*MS12**4*complexconjugate(K)*complexconjugate(Kprime))/(32.*cmath.pi*MFm1**2*abs(MS12)**3)',
                                    (P.e__minus__,P.psimum__tilde__):'((-MFm2**2 + MS12**2)*(-(Kprime*MFm2**2*complexconjugate(Kprime)) + Kprime*MS12**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS12)**3)',
                                    (P.ve,P.psimuz__tilde__):'((-MFz2**2 + MS12**2)*(-(Kprime*MFz2**2*complexconjugate(Kprime)) + Kprime*MS12**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS12)**3)'})

Decay_S13 = Decay(name = 'Decay_S13',
                  particle = P.S13,
                  partial_widths = {(P.e__minus__,P.psitam__tilde__):'((-MFm3**2 + MS13**2)*(-(Kprime*MFm3**2*complexconjugate(Kprime)) + Kprime*MS13**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS13)**3)',
                                    (P.e__minus__,P.ta__plus__):'((MS13**2 - MTA**2)*((Hvev**2*K*Kprime*MS13**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm1**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm1**2)))/(16.*cmath.pi*abs(MS13)**3)',
                                    (P.ve,P.psitaz__tilde__):'((-MFz3**2 + MS13**2)*(-(Kprime*MFz3**2*complexconjugate(Kprime)) + Kprime*MS13**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS13)**3)'})

Decay_S21 = Decay(name = 'Decay_S21',
                  particle = P.S21,
                  partial_widths = {(P.mu__minus__,P.e__plus__):'(Hvev**2*K*Kprime*MS21**4*complexconjugate(K)*complexconjugate(Kprime))/(32.*cmath.pi*MFm2**2*abs(MS21)**3)',
                                    (P.mu__minus__,P.psiem__tilde__):'((-MFm1**2 + MS21**2)*(-(Kprime*MFm1**2*complexconjugate(Kprime)) + Kprime*MS21**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS21)**3)',
                                    (P.vm,P.psiez__tilde__):'((-MFz1**2 + MS21**2)*(-(Kprime*MFz1**2*complexconjugate(Kprime)) + Kprime*MS21**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS21)**3)'})

Decay_S22 = Decay(name = 'Decay_S22',
                  particle = P.S22,
                  partial_widths = {(P.mu__minus__,P.mu__plus__):'(Hvev**2*K*Kprime*MS22**4*complexconjugate(K)*complexconjugate(Kprime))/(32.*cmath.pi*MFm2**2*abs(MS22)**3)',
                                    (P.mu__minus__,P.psimum__tilde__):'((-MFm2**2 + MS22**2)*(-(Kprime*MFm2**2*complexconjugate(Kprime)) + Kprime*MS22**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS22)**3)',
                                    (P.vm,P.psimuz__tilde__):'((-MFz2**2 + MS22**2)*(-(Kprime*MFz2**2*complexconjugate(Kprime)) + Kprime*MS22**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS22)**3)'})

Decay_S23 = Decay(name = 'Decay_S23',
                  particle = P.S23,
                  partial_widths = {(P.mu__minus__,P.psitam__tilde__):'((-MFm3**2 + MS23**2)*(-(Kprime*MFm3**2*complexconjugate(Kprime)) + Kprime*MS23**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS23)**3)',
                                    (P.mu__minus__,P.ta__plus__):'((MS23**2 - MTA**2)*((Hvev**2*K*Kprime*MS23**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm2**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm2**2)))/(16.*cmath.pi*abs(MS23)**3)',
                                    (P.vm,P.psitaz__tilde__):'((-MFz3**2 + MS23**2)*(-(Kprime*MFz3**2*complexconjugate(Kprime)) + Kprime*MS23**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS23)**3)'})

Decay_S31 = Decay(name = 'Decay_S31',
                  particle = P.S31,
                  partial_widths = {(P.ta__minus__,P.e__plus__):'((MS31**2 - MTA**2)*((Hvev**2*K*Kprime*MS31**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2)))/(16.*cmath.pi*abs(MS31)**3)',
                                    (P.ta__minus__,P.psiem__tilde__):'((-(Kprime*MFm1**2*complexconjugate(Kprime)) + Kprime*MS31**2*complexconjugate(Kprime) - Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm1**4 - 2*MFm1**2*MS31**2 + MS31**4 - 2*MFm1**2*MTA**2 - 2*MS31**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MS31)**3)',
                                    (P.vt,P.psiez__tilde__):'((-MFz1**2 + MS31**2)*(-(Kprime*MFz1**2*complexconjugate(Kprime)) + Kprime*MS31**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS31)**3)'})

Decay_S32 = Decay(name = 'Decay_S32',
                  particle = P.S32,
                  partial_widths = {(P.ta__minus__,P.mu__plus__):'((MS32**2 - MTA**2)*((Hvev**2*K*Kprime*MS32**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2)))/(16.*cmath.pi*abs(MS32)**3)',
                                    (P.ta__minus__,P.psimum__tilde__):'((-(Kprime*MFm2**2*complexconjugate(Kprime)) + Kprime*MS32**2*complexconjugate(Kprime) - Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm2**4 - 2*MFm2**2*MS32**2 + MS32**4 - 2*MFm2**2*MTA**2 - 2*MS32**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MS32)**3)',
                                    (P.vt,P.psimuz__tilde__):'((-MFz2**2 + MS32**2)*(-(Kprime*MFz2**2*complexconjugate(Kprime)) + Kprime*MS32**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS32)**3)'})

Decay_S33 = Decay(name = 'Decay_S33',
                  particle = P.S33,
                  partial_widths = {(P.ta__minus__,P.psitam__tilde__):'((-(Kprime*MFm3**2*complexconjugate(Kprime)) + Kprime*MS33**2*complexconjugate(Kprime) - Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm3**4 - 2*MFm3**2*MS33**2 + MS33**4 - 2*MFm3**2*MTA**2 - 2*MS33**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(MS33)**3)',
                                    (P.ta__minus__,P.ta__plus__):'(((Hvev**2*K*Kprime*MS33**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2) - (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/MFm3**2)*cmath.sqrt(MS33**4 - 4*MS33**2*MTA**2))/(16.*cmath.pi*abs(MS33)**3)',
                                    (P.vt,P.psitaz__tilde__):'((-MFz3**2 + MS33**2)*(-(Kprime*MFz3**2*complexconjugate(Kprime)) + Kprime*MS33**2*complexconjugate(Kprime)))/(16.*cmath.pi*abs(MS33)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.H,P.psitam):'(((K*MFm3**2*complexconjugate(K))/2. - (K*MH**2*complexconjugate(K))/2. + (K*MTA**2*complexconjugate(K))/2.)*cmath.sqrt(MFm3**4 - 2*MFm3**2*MH**2 + MH**4 - 2*MFm3**2*MTA**2 - 2*MH**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S13__tilde__,P.e__minus__):'((-MS13**2 + MTA**2)*(-(Hvev**2*K*Kprime*MS13**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm1**2) + (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm1**2)))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S23__tilde__,P.mu__minus__):'((-MS23**2 + MTA**2)*(-(Hvev**2*K*Kprime*MS23**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm2**2) + (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm2**2)))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S31,P.e__minus__):'((-MS31**2 + MTA**2)*(-(Hvev**2*K*Kprime*MS31**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2) + (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2)))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S31,P.psiem):'((Kprime*MFm1**2*complexconjugate(Kprime) - Kprime*MS31**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm1**4 - 2*MFm1**2*MS31**2 + MS31**4 - 2*MFm1**2*MTA**2 - 2*MS31**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S32,P.mu__minus__):'((-MS32**2 + MTA**2)*(-(Hvev**2*K*Kprime*MS32**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2) + (Hvev**2*K*Kprime*MTA**2*complexconjugate(K)*complexconjugate(Kprime))/(2.*MFm3**2)))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S32,P.psimum):'((Kprime*MFm2**2*complexconjugate(Kprime) - Kprime*MS32**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm2**4 - 2*MFm2**2*MS32**2 + MS32**4 - 2*MFm2**2*MTA**2 - 2*MS32**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S33,P.psitam):'((Kprime*MFm3**2*complexconjugate(Kprime) - Kprime*MS33**2*complexconjugate(Kprime) + Kprime*MTA**2*complexconjugate(Kprime))*cmath.sqrt(MFm3**4 - 2*MFm3**2*MS33**2 + MS33**4 - 2*MFm3**2*MTA**2 - 2*MS33**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.psitaz):'(((ee**2*K*MFz3**2*vev**2*complexconjugate(K))/(4.*MFm3**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*MFm3**2*sw**2) + (ee**2*K*MFz3**4*vev**2*complexconjugate(K))/(4.*MFm3**2*MW**2*sw**2) - (ee**2*K*MFz3**2*MTA**2*vev**2*complexconjugate(K))/(2.*MFm3**2*MW**2*sw**2) + (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(4.*MFm3**2*MW**2*sw**2) - (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MFm3**2*sw**2))*cmath.sqrt(MFz3**4 - 2*MFz3**2*MTA**2 + MTA**4 - 2*MFz3**2*MW**2 - 2*MTA**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.Z,P.psitam):'(((ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(8.*cw**2*MFm3**2*sw**2) + (ee**2*K*MFm3**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*cw**2*MZ**2*sw**2) + (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(8.*cw**2*MFm3**2*MZ**2*sw**2) - (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm3**2*sw**2))*cmath.sqrt(MFm3**4 - 2*MFm3**2*MTA**2 + MTA**4 - 2*MFm3**2*MZ**2 - 2*MTA**2*MZ**2 + MZ**4))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.psiez,P.e__plus__):'((-MFz1**2 + MW**2)*(-(ee**2*K*MFz1**2*vev**2*complexconjugate(K))/(4.*MFm1**2*sw**2) - (ee**2*K*MFz1**4*vev**2*complexconjugate(K))/(4.*MFm1**2*MW**2*sw**2) + (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MFm1**2*sw**2)))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.psiez,P.psiem__tilde__):'((-((ee**2*MFm1**2)/sw**2) + (6*ee**2*MFm1*MFz1)/sw**2 - (ee**2*MFz1**2)/sw**2 - (ee**2*MFm1**4)/(MW**2*sw**2) + (2*ee**2*MFm1**2*MFz1**2)/(MW**2*sw**2) - (ee**2*MFz1**4)/(MW**2*sw**2) + (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm1**4 - 2*MFm1**2*MFz1**2 + MFz1**4 - 2*MFm1**2*MW**2 - 2*MFz1**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.psimuz,P.mu__plus__):'((-MFz2**2 + MW**2)*(-(ee**2*K*MFz2**2*vev**2*complexconjugate(K))/(4.*MFm2**2*sw**2) - (ee**2*K*MFz2**4*vev**2*complexconjugate(K))/(4.*MFm2**2*MW**2*sw**2) + (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MFm2**2*sw**2)))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.psimuz,P.psimum__tilde__):'((-((ee**2*MFm2**2)/sw**2) + (6*ee**2*MFm2*MFz2)/sw**2 - (ee**2*MFz2**2)/sw**2 - (ee**2*MFm2**4)/(MW**2*sw**2) + (2*ee**2*MFm2**2*MFz2**2)/(MW**2*sw**2) - (ee**2*MFz2**4)/(MW**2*sw**2) + (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm2**4 - 2*MFm2**2*MFz2**2 + MFz2**4 - 2*MFm2**2*MW**2 - 2*MFz2**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.psitaz,P.psitam__tilde__):'((-((ee**2*MFm3**2)/sw**2) + (6*ee**2*MFm3*MFz3)/sw**2 - (ee**2*MFz3**2)/sw**2 - (ee**2*MFm3**4)/(MW**2*sw**2) + (2*ee**2*MFm3**2*MFz3**2)/(MW**2*sw**2) - (ee**2*MFz3**4)/(MW**2*sw**2) + (2*ee**2*MW**2)/sw**2)*cmath.sqrt(MFm3**4 - 2*MFm3**2*MFz3**2 + MFz3**4 - 2*MFm3**2*MW**2 - 2*MFz3**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.psitaz,P.ta__plus__):'((-(ee**2*K*MFz3**2*vev**2*complexconjugate(K))/(4.*MFm3**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*MFm3**2*sw**2) - (ee**2*K*MFz3**4*vev**2*complexconjugate(K))/(4.*MFm3**2*MW**2*sw**2) + (ee**2*K*MFz3**2*MTA**2*vev**2*complexconjugate(K))/(2.*MFm3**2*MW**2*sw**2) - (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(4.*MFm3**2*MW**2*sw**2) + (ee**2*K*MW**2*vev**2*complexconjugate(K))/(2.*MFm3**2*sw**2))*cmath.sqrt(MFz3**4 - 2*MFz3**2*MTA**2 + MTA**4 - 2*MFz3**2*MW**2 - 2*MTA**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.psiem__tilde__):'((-MFm1**2 + MZ**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MFm1**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm1**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.psimum__tilde__):'((-MFm2**2 + MZ**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MFm2**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm2**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psiem,P.e__plus__):'((-MFm1**2 + MZ**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MFm1**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm1**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psiem,P.psiem__tilde__):'((-4*ee**2*MFm1**2 - 2*ee**2*MZ**2 + (2*cw**2*ee**2*MFm1**2)/sw**2 + (cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MFm1**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MFm1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psimum,P.mu__plus__):'((-MFm2**2 + MZ**2)*(-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MFm2**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm2**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psimum,P.psimum__tilde__):'((-4*ee**2*MFm2**2 - 2*ee**2*MZ**2 + (2*cw**2*ee**2*MFm2**2)/sw**2 + (cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MFm2**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MFm2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psitam,P.psitam__tilde__):'((-4*ee**2*MFm3**2 - 2*ee**2*MZ**2 + (2*cw**2*ee**2*MFm3**2)/sw**2 + (cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MFm3**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MFm3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psitam,P.ta__plus__):'((-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(8.*cw**2*MFm3**2*sw**2) - (ee**2*K*MFm3**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*cw**2*MZ**2*sw**2) - (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(8.*cw**2*MFm3**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm3**2*sw**2))*cmath.sqrt(MFm3**4 - 2*MFm3**2*MTA**2 + MTA**4 - 2*MFm3**2*MZ**2 - 2*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psiez,P.psiez__tilde__):'((4*ee**2*MFz1**2 + 2*ee**2*MZ**2 + (2*cw**2*ee**2*MFz1**2)/sw**2 + (cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MFz1**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MFz1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psimuz,P.psimuz__tilde__):'((4*ee**2*MFz2**2 + 2*ee**2*MZ**2 + (2*cw**2*ee**2*MFz2**2)/sw**2 + (cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MFz2**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MFz2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.psitaz,P.psitaz__tilde__):'((4*ee**2*MFz3**2 + 2*ee**2*MZ**2 + (2*cw**2*ee**2*MFz3**2)/sw**2 + (cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MFz3**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MFz3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.psitam__tilde__):'((-(ee**2*K*vev**2*complexconjugate(K))/(8.*cw**2*sw**2) - (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(8.*cw**2*MFm3**2*sw**2) - (ee**2*K*MFm3**2*vev**2*complexconjugate(K))/(8.*cw**2*MZ**2*sw**2) + (ee**2*K*MTA**2*vev**2*complexconjugate(K))/(4.*cw**2*MZ**2*sw**2) - (ee**2*K*MTA**4*vev**2*complexconjugate(K))/(8.*cw**2*MFm3**2*MZ**2*sw**2) + (ee**2*K*MZ**2*vev**2*complexconjugate(K))/(4.*cw**2*MFm3**2*sw**2))*cmath.sqrt(MFm3**4 - 2*MFm3**2*MTA**2 + MTA**4 - 2*MFm3**2*MZ**2 - 2*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})


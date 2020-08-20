#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl
from scipy.interpolate import spline


mpl.style.use('classic')

# Data for plotting
R42191=np.loadtxt('./r42191.dat')
R42193=np.loadtxt('./r42193.dat')
R42194=np.loadtxt('./r42194.dat')
R42199=np.loadtxt('./r42199.dat')
R42189=np.loadtxt('./r42189.dat')
R42188=np.loadtxt('./r42188.dat')
R42198=np.loadtxt('./r42198.dat')
R42197=np.loadtxt('./r42197.dat')
R42196=np.loadtxt('./r42196.dat')
R42195=np.loadtxt('./r42195.dat')
R42200=np.loadtxt('./r42200.dat')
R42201=np.loadtxt('./r42201.dat')
R42207=np.loadtxt('./r42207.dat')

R62191=np.loadtxt('./r62191.dat')
R62193=np.loadtxt('./r62193.dat')
R62194=np.loadtxt('./r62194.dat')
R62199=np.loadtxt('./r62199.dat')
R62198=np.loadtxt('./r62198.dat')
R62197=np.loadtxt('./r62197.dat')
R62196=np.loadtxt('./r62196.dat')
R62195=np.loadtxt('./r62195.dat')
R62207=np.loadtxt('./r62207.dat')
R62200=np.loadtxt('./r62200.dat')
R62201=np.loadtxt('./r62201.dat')
R62189=np.loadtxt('./r62189.dat')
mubfrg=np.loadtxt('./mub.dat')
cmu=1./1.110
cmu1=1./(1.110+0.066)
cmu2=1./(1.110-0.066)
ct=1./1.247
ct1=1./1.235
ct2=1./1.259
WBup=np.loadtxt('./r42r62mubtlat/WB/r42lat150up.dat')
WBdown=np.loadtxt('./r42r62mubtlat/WB/r42lat150down.dat')
WBmub=np.loadtxt('./r42r62mubtlat/WB/latmubt.dat')

WBc2=np.loadtxt('./r42r62mubtlat/data1/WB_chi2.dat')
WBc4=np.loadtxt('./r42r62mubtlat/data1/WB_chi4.dat')
WBc6=np.loadtxt('./r42r62mubtlat/data1/WB_chi6.dat')
WBc8=np.loadtxt('./r42r62mubtlat/data1/WB_chi8.dat')
WBerrc2=np.zeros((18))
WBerrc4=np.loadtxt('./r42r62mubtlat/data1/WB_chi4erro.dat')
WBerrc6=np.loadtxt('./r42r62mubtlat/data1/WB_chi6erro.dat')
WBerrc8=np.loadtxt('./r42r62mubtlat/data1/WB_chi8erro.dat')
WBT=[135.,140.,145.,150.,155.,160.,165.,170.,175.,180.,185.,190.,195.,200.,205.,210.,215.,220.]
WBR42=np.zeros((101,18))
WBerrR42=np.zeros((101,18))
WBerrR422=np.zeros((101,18))
WBR62=np.zeros((101,18))
WBerrR62=np.zeros((101,18))
WBerrR622=np.zeros((101,18))
chi=np.loadtxt('./chiBre.dat')
T=chi[:,0]
c2=chi[:,1]
c4=chi[:,3]
c6=chi[:,5]
c8=chi[:,7]
errc2=chi[:,2]
errc4=chi[:,4]
errc6=chi[:,6]
errc8=chi[:,8]
chi1=np.zeros((101,101))
chi2=np.zeros((101,101))
chi3=np.zeros((101,101))
chi4=np.zeros((101,101))
chi5=np.zeros((101,101))
chi6=np.zeros((101,101))
chi7=np.zeros((101,101))
chi8=np.zeros((101,101))
R12=np.zeros((101,101))
R42=np.zeros((101,101))
R62=np.zeros((101,101))
R82=np.zeros((101,101))
mub=np.zeros(101)
A1b1=np.zeros((101,101))
A1b3=np.zeros((101,101))
A1b5=np.zeros((101,101))
A1b7=np.zeros((101,101))
A2=np.zeros((101,101))
A3=np.zeros((101,101))
A4=np.zeros((101,101))
A5=np.zeros((101,101))
A6=np.zeros((101,101))
A7=np.zeros((101,101))
A8=np.zeros((101,101))
errR12=np.zeros((101,101))
errR42=np.zeros((101,101))
errR422=np.zeros((101,101))
errR423=np.zeros((101,101))
errR62=np.zeros((101,101))
errR622=np.zeros((101,101))
errR623=np.zeros((101,101))
errR82=np.zeros((101,101))
for num1 in range(0,101):
    for num2 in range(0,101):
    	mub[num1]=4.*num1
    	b0=1.
    	b1=(4.*num1/T[num2])
    	b2=1./2. *(4.*num1/T[num2])**2.
    	b3=1./(3.*2.*1.) *(4.*num1/T[num2])**3.
    	b4=1./(4.*3.*2.*1.) *(4.*num1/T[num2])**4.
    	b5=1./(5.*4.*3.*2.*1.) *(4.*num1/T[num2])**5.
    	b6=1./(6.*5.*4.*3.*2.*1.) *(4.*num1/T[num2])**6.
    	b7=1./(7.*6.*5.*4.*3.*2.*1.) *(4.*num1/T[num2])**7.
    	b8=1./(8.*7.*6.*5.*4.*3.*2.*1.) *(4.*num1/T[num2])**8.
        chi1[num1,num2]=c2[num2]*4.*num1/T[num2]+1./(3.*2.*1.) *c4[num2]* (4.*num1/T[num2])**3. +1./(5.*4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**5.+1./(7.*6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**7.
        chi2[num1,num2]=c2[num2]+1./(2.*1.) *c4[num2]* (4.*num1/T[num2])**2. +1./(4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**6.
        chi3[num1,num2]=c4[num2]* (4.*num1/T[num2]) +1./(3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**3.+1./(5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**5.
        chi4[num1,num2]=c4[num2] +1./(2.*1.) *c6[num2]* (4.*num1/T[num2])**2.+1./(4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**4.
        chi5[num1,num2]=c6[num2]* (4.*num1/T[num2])+1./(3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**3.
        chi6[num1,num2]=c6[num2]+1./(2.*1.) *c8[num2]* (4.*num1/T[num2])**2.
        chi7[num1,num2]=c8[num2]* (4.*num1/T[num2])
        chi8[num1,num2]=c8[num2]
        R12[num1,num2]=chi1[num1,num2]/chi2[num1,num2]
        R42[num1,num2]=chi4[num1,num2]/chi2[num1,num2]
        R62[num1,num2]=chi6[num1,num2]/chi2[num1,num2]
        R82[num1,num2]=chi8[num1,num2]/chi2[num1,num2]
        #A1[num1,num2]=1./(c2[num2]*4.*num1/T[num2]+1./(3.*2.*1.) *c4[num2]* (4.*num1/T[num2])**3. +1./(5.*4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**5.+1./(7.*6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**7.)
        A2[num1,num2]=1./(c2[num2]+1./(2.*1.) *c4[num2]* (4.*num1/T[num2])**2. +1./(4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**6.)
        #A3[num1,num2]=1./(c4[num2]* (4.*num1/T[num2]) +1./(3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**3.+1./(5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**5.)
        A4[num1,num2]=1./(c4[num2] +1./(2.*1.) *c6[num2]* (4.*num1/T[num2])**2.+1./(4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**4.)
        #A5[num1,num2]=1./(c6[num2]* (4.*num1/T[num2])+1./(3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**3.)
        A6[num1,num2]=1./(c6[num2]+1./(2.*1.) *c8[num2]* (4.*num1/T[num2])**2.)
        #A7[num1,num2]=1./(c8[num2]* (4.*num1/T[num2]))
        A8[num1,num2]=1./(c8[num2])
        A1b1[num1,num2]=1./(c2[num2]+1./(3.*2.*1.)*(4.*num1/T[num2])**2*c4[num2]+1./(5.*4.*3.*2.*1.)*(4*num1/T[num2])**4*c6[num2]+1./(7.*6.*5.*4.*3.*2.*1.)*(4*num1/T[num2])**6*c8[num2])
        A1b3[num1,num2]=(1./(3.*2.*1.)*(4.*num1/T[num2])**2)/(c2[num2]+1./(3.*2.*1.) *c4[num2]* (4.*num1/T[num2])**2. +1./(5.*4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**4.+1./(7.*6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**6.)
        A1b5[num1,num2]=(1./(5.*4.*3.*2.*1.)*(4.*num1/T[num2])**4)/(c2[num2]+1./(3.*2.*1.) *c4[num2]* (4.*num1/T[num2])**2. +1./(5.*4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**4.+1./(7.*6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**6.)
        A1b7[num1,num2]=(1./(7.*6.*5.*4.*3.*2.*1.)*(4.*num1/T[num2])**6)/(c2[num2]+1./(3.*2.*1.) *c4[num2]* (4.*num1/T[num2])**2. +1./(5.*4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**4.+1./(7.*6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**6.)
        #errR42[num1,num2]=(abs(A2[num1,num2])*errc2[num2]+abs(A4[num1,num2]-A2[num1,num2]*b2)*errc4[num2]+abs(A4[num1,num2]*b2-A2[num1,num2]*b4)*errc6[num2]+abs(A4[num1,num2]*b4-A2[num1,num2]*b6)*errc8[num2])*R42[num1,num2]
        #errR422[num1,num2]=abs(chi4[num1,num2]/(chi2[num1,num2]**2))*errc2[num2]+abs(1./chi2[num1,num2]-chi4[num1,num2]/(chi2[num1,num2])**2*1./(2.*1.)*(4.*num1/T[num2])**2)*errc4[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/T[num2])**2-chi4[num1,num2]/(chi2[num1,num2])**2*1./(4.*3.*2.*1.)*(4.*num1/T[num2])**4)*errc6[num2]+abs(1./chi2[num1,num2]*1./(4.*3.*2.*1.)*(4.*num1/T[num2])**4-chi4[num1,num2]/(chi2[num1,num2])**2*1./(6.*5.*4.*3.*2.*1.)*(4.*num1/T[num2])**6)*errc8[num2]
        errR42[num1,num2]=abs(chi4[num1,num2]/(chi2[num1,num2]**2))*errc2[num2]+abs(1./chi2[num1,num2]-chi4[num1,num2]/(chi2[num1,num2])**2*1./(2.*1.)*(4.*num1/T[num2])**2)*errc4[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/T[num2])**2)*errc6[num2]
        errR422[num1,num2]=((((chi4[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi6[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2])**2)*errc2[num2])**2 \
                           +  ((1./(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2])-(chi4[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi6[num1,num2])*1./(1.*2.)*(4.*num1/T[num2])**2/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2])**2)*errc4[num2])**2 \
                           +  (((1./(1.*2.)*(4.*num1/T[num2])**2)/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2]))*errc6[num2])**2)**0.5
        errR62[num1,num2]=abs(chi6[num1,num2]/(chi2[num1,num2]**2))*errc2[num2]+abs(chi6[num1,num2]/(chi2[num1,num2]**2)*1./(2.*1.)*(4.*num1/T[num2])**2)*errc4[num2]+abs(1./chi2[num1,num2])*errc6[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/T[num2])**2)*errc8[num2]
        errR622[num1,num2]=((((chi6[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi8[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2])**2)*errc2[num2])**2 \
                           + (((chi6[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi8[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2])**2)*(1./(1.*2.)*(4.*num1/T[num2])**2)*errc4[num2])**2 \
                           + ((1./(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2]))*errc6[num2])**2 \
                           + (((1./(1.*2.)*(4.*num1/T[num2])**2)/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2]))*errc8[num2])**2)**0.5
        errR423[num1,num2]= ((-(chi4[num1,num2]/chi2[num1,num2]**2))**2*errc2[num2]**2 +   \
                            (1/chi2[num1,num2] - chi4[num1,num2]/chi2[num1,num2]**2*0.5*   \
                            ((4*num1)/T[num2])**2)**2*errc4[num2]**2 +                     \
                            ((0.5*((4*num1)/T[num2])**2)/chi2[num1,num2] -                 \
                            chi4[num1,num2]/chi2[num1,num2]**2*1/(4.*3.*2.)*               \
                            ((4*num1)/T[num2])**4)**2*errc6[num2]**2 +                     \
                            ((1/(4.*3.*2.)*((4*num1)/T[num2])**4)/chi2[num1,num2] -        \
                            chi4[num1,num2]/chi2[num1,num2]**2*1/(6.*5.*4.*3.*2.)*         \
                            ((4*num1)/T[num2])**6)**2*errc8[num2]**2)**0.5
        errR623[num1,num2]=((-(chi6[num1,num2]/chi2[num1,num2]**2))**2*errc2[num2]**2 +          \
                           (-(chi6[num1,num2]/chi2[num1,num2]**2)*0.5*((4*num1)/T[num2])**2)**2* \
                           errc4[num2]**2 + (1/chi2[num1,num2] -                                 \
                           chi6[num1,num2]/chi2[num1,num2]**2*1/(4.*3.*2.)*                      \
                           ((4*num1)/T[num2])**4)**2*errc6[num2]**2 +                            \
                           ((0.5*((4*num1)/T[num2])**2)/chi2[num1,num2] -                        \
                           chi6[num1,num2]/chi2[num1,num2]**2*1/(6.*5.*4.*3.*2.)*                \
                           ((4*num1)/T[num2])**6)**2*errc8[num2]**2)**0.5



for num1 in range(0,101):
    for num2 in range(0,18):
        chi2[num1,num2]=WBc2[num2]+1./(2.*1.) *WBc4[num2]* (4.*num1/WBT[num2])**2. +1./(4.*3.*2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**6.
        chi4[num1,num2]=WBc4[num2] +1./(2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**2.+1./(4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**4.   
        WBR42[num1,num2]=chi4[num1,num2]/chi2[num1,num2]
        WBerrR42[num1,num2]=abs(chi4[num1,num2]/(chi2[num1,num2]**2))*WBerrc2[num2]+abs(1./chi2[num1,num2]-chi4[num1,num2]/(chi2[num1,num2])**2*1./(2.*1.)*(4.*num1/WBT[num2])**2)*WBerrc4[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/WBT[num2])**2)*WBerrc6[num2]
#        WBerrR422[num1,num2]=((((chi4[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi6[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])**2)*WBerrc2[num2])**2 \
#                           +  ((1./(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])-(chi4[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi6[num1,num2])*1./(1.*2.)*(4.*num1/WBT[num2])**2/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])**2)*WBerrc4[num2])**2 \
#                           +  (((1./(1.*2.)*(4.*num1/WBT[num2])**2)/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2]))*WBerrc6[num2])**2)**0.5
        WBerrR422[num1,num2]= ((-(chi4[num1,num2]/chi2[num1,num2]**2))**2*WBerrc2[num2]**2 +   \
                            (1/chi2[num1,num2] - chi4[num1,num2]/chi2[num1,num2]**2*0.5*   \
                            ((4*num1)/WBT[num2])**2)**2*WBerrc4[num2]**2 +                     \
                            ((0.5*((4*num1)/WBT[num2])**2)/chi2[num1,num2] -                 \
                            chi4[num1,num2]/chi2[num1,num2]**2*1/(4.*3.*2.)*               \
                            ((4*num1)/WBT[num2])**4)**2*WBerrc6[num2]**2 +                     \
                            ((1/(4.*3.*2.)*((4*num1)/WBT[num2])**4)/chi2[num1,num2] -        \
                            chi4[num1,num2]/chi2[num1,num2]**2*1/(6.*5.*4.*3.*2.)*         \
                            ((4*num1)/WBT[num2])**6)**2*WBerrc8[num2]**2)**0.5



for num1 in range(0,101):
    for num2 in range(0,18):
        chi1[num1,num2]=WBc2[num2]*4.*num1/WBT[num2]+1./(3.*2.*1.) *WBc4[num2]* (4.*num1/WBT[num2])**3. +1./(5.*4.*3.*2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**5.+1./(7.*6.*5.*4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**7.
        chi2[num1,num2]=WBc2[num2]+1./(2.*1.) *WBc4[num2]* (4.*num1/WBT[num2])**2. +1./(4.*3.*2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**6.
        chi3[num1,num2]=WBc4[num2]* (4.*num1/WBT[num2]) +1./(3.*2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**3.+1./(5.*4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**5.
        chi4[num1,num2]=WBc4[num2] +1./(2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**2.+1./(4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**4.
        chi5[num1,num2]=WBc6[num2]* (4.*num1/WBT[num2])+1./(3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**3.
        chi6[num1,num2]=WBc6[num2]+1./(2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**2.
        chi7[num1,num2]=WBc8[num2]* (4.*num1/WBT[num2])
        chi8[num1,num2]=WBc8[num2]
        WBR62[num1,num2]=chi6[num1,num2]/chi2[num1,num2]
        WBerrR62[num1,num2]=abs(chi6[num1,num2]/(chi2[num1,num2]**2))*WBerrc2[num2]+abs(chi6[num1,num2]/(chi2[num1,num2]**2)*1./(2.*1.)*(4.*num1/WBT[num2])**2)*WBerrc4[num2]+abs(1./chi2[num1,num2])*WBerrc6[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/WBT[num2])**2)*WBerrc8[num2]
#        WBerrR622[num1,num2]=((((chi6[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi8[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])**2)*WBerrc2[num2])**2 \
#                           + (((chi6[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi8[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])**2)*(1./(1.*2.)*(4.*num1/WBT[num2])**2)*WBerrc4[num2])**2 \
#                           + ((1./(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2]))*WBerrc6[num2])**2 \
#                           + (((1./(1.*2.)*(4.*num1/WBT[num2])**2)/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2]))*WBerrc8[num2])**2)**0.5
        WBerrR622[num1,num2]=((-(chi6[num1,num2]/chi2[num1,num2]**2))**2*WBerrc2[num2]**2 +          \
                           (-(chi6[num1,num2]/chi2[num1,num2]**2)*0.5*((4*num1)/WBT[num2])**2)**2* \
                           WBerrc4[num2]**2 + (1/chi2[num1,num2] -                                 \
                           chi6[num1,num2]/chi2[num1,num2]**2*1/(4.*3.*2.)*                      \
                           ((4*num1)/WBT[num2])**4)**2*WBerrc6[num2]**2 +                            \
                           ((0.5*((4*num1)/WBT[num2])**2)/chi2[num1,num2] -                        \
                           chi6[num1,num2]/chi2[num1,num2]**2*1/(6.*5.*4.*3.*2.)*                \
                           ((4*num1)/WBT[num2])**6)**2*WBerrc8[num2]**2)**0.5




# Create figure
fig=plt.figure(figsize=(9., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(121)
x1=mubfrg*cmu2/(198.0*ct1)
x2=mubfrg*cmu1/(201.0*ct2)


line_FRG_T160,=ax1.plot(mubfrg*cmu/(200.0*ct),R42200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)

xsame=np.linspace(0.,1.2,100)
#power1=spline(x1,R42198,xsame)
#power2=spline(x2,R42201,xsame)
power1=spline(x1,R42198,xsame)
power2=spline(x2,R42201,xsame)

band_FRG_T160=ax1.fill_between(xsame,power1,power2,alpha=0.3,facecolor='m',edgecolor='',zorder=12,label=r'This work T=160 MeV')


#x3=mubfrg*cmu2/(193.0*ct1)
#x4=mubfrg*cmu1/(196.0*ct2)
x3=mubfrg*cmu2/(191.0*ct1)
x4=mubfrg*cmu1/(195.0*ct2)
#line_FRG_T155,=ax1.plot(mubfrg*cmu/(195.0*ct),R42195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)
#line_FRG_T155,=ax1.plot(mubfrg*cmu/(194.0*ct),R42194,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)
line_FRG_T155,=ax1.plot(mubfrg*cmu/(193.0*ct),R42193,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)

xsame2=np.linspace(0.,1.2,100)
#power3=spline(x3,R42193,xsame2)
#power4=spline(x4,R42196,xsame2)
power3=spline(x3,R42191,xsame2)
power4=spline(x4,R42195,xsame2)
band_FRG_T155=ax1.fill_between(xsame2,power3,power4,alpha=0.3,facecolor='r',edgecolor='',zorder=11,label=r'This work T=155 MeV')



r42150up=R42[:,40]+errR422[:,40]
r42150down=R42[:,40]-errR422[:,40]
r42160up=R42[:,60]+errR422[:,60]
r42160down=R42[:,60]-errR422[:,60]

band_WB_T160=ax1.fill_between(mub/160.,WBR42[:,5]-WBerrR422[:,5],WBR42[:,5]+WBerrR422[:,5],alpha=0.3,facecolor=(0.8,0.5,0),edgecolor='',label=r'WB T=160 MeV')
band_WB_T155=ax1.fill_between(mub/155.,WBR42[:,4]-WBerrR422[:,4],WBR42[:,4]+WBerrR422[:,4],alpha=0.3,facecolor='b',edgecolor='',label=r'WB T=155 MeV')

plt.axes([0.13, 0.212, 0.15, 0.27]) #不用figure的形式则无须用set
line_FRG_T160,=plt.plot(mubfrg*cmu/(200.0*ct),R42200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)
band_FRG_T160=plt.fill_between(xsame,power1,power2,alpha=0.3,facecolor='m',edgecolor='',zorder=12,label=r'This work T=160 MeV')
#line_FRG_T155,=plt.plot(mubfrg*cmu/(195.0*ct),R42195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)
line_FRG_T155,=plt.plot(mubfrg*cmu/(193.0*ct),R42193,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)
band_FRG_T155=plt.fill_between(xsame2,power3,power4,alpha=0.3,facecolor='r',edgecolor='',zorder=11,label=r'This work T=155 MeV')
band_HotQCD_T160=plt.fill_between(mub/160.,r42160up,r42160down,alpha=0.3,facecolor='c',edgecolor='',label=r'HotQCD T=160 MeV')
band_HotQCD_T155=plt.fill_between(mub/155.,R42[:,50]-errR422[:,50],R42[:,50]+errR422[:,50],alpha=0.3,facecolor='green',edgecolor='',label=r'HotQCD T=155 MeV')


plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.axis([0.,0.8,0.2,0.9])

ax1.axis([0,0.8,0.3,0.9])

ax1.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax1.set_ylabel('$R^B_{42}$', fontsize=14, color='black')


#ax1.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160),band_HotQCD_T155,band_HotQCD_T160,band_WB_T155,band_WB_T160),(r'This work $T=155$ MeV',r'This work $T=160$ MeV',r'HotQCD $T=155$ MeV',r'HotQCD $T=160$ MeV',r'WB $T=155$ MeV',r'WB $T=160$ MeV'),loc=0,fontsize='7',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

#############################################################################################################################################################
ax2=fig.add_subplot(122)
x1=mubfrg*cmu2/(198.0*ct1)
x2=mubfrg*cmu1/(201.0*ct2)
line_FRG_T160,=ax2.plot(mubfrg*cmu/(200.0*ct),R62200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)
xsame=np.linspace(0.,1.2,100)
power1=spline(x1,R62198,xsame)
power2=spline(x2,R62201,xsame)
band_FRG_T160=ax2.fill_between(xsame,power1,power2,alpha=0.3,facecolor='m',edgecolor='',zorder=12,label=r'This work T=160 MeV')
#x3=mubfrg*cmu2/(193.0*ct1)
#x4=mubfrg*cmu1/(196.0*ct2)
x3=mubfrg*cmu2/(191.0*ct1)
x4=mubfrg*cmu1/(195.0*ct2)
#line_FRG_T155,=ax2.plot(mubfrg*cmu/(195.0*ct),R62195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)#,label=r'This work T=155 MeV')
line_FRG_T155,=ax2.plot(mubfrg*cmu/(193.0*ct),R62193,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=20)#,label=r'This work T=155 MeV')
xsame2=np.linspace(0.,1.2,100)
#power3=spline(x3,R62193,xsame2)
#power4=spline(x4,R62196,xsame2)
power3=spline(x3,R62191,xsame2)
power4=spline(x4,R62195,xsame2)
band_FRG_T155=ax2.fill_between(xsame2,power3,power4,alpha=0.3,facecolor='r',edgecolor='',zorder=11,label=r'This work T=155 MeV')

band_WB_T160=ax2.fill_between(mub/160.,WBR62[:,5]-WBerrR622[:,5],WBR62[:,5]+WBerrR622[:,5],alpha=0.3,facecolor=(0.8,0.5,0),edgecolor='',label=r'WB T=160 MeV')

band_WB_T155=ax2.fill_between(mub/155.,WBR62[:,4]-WBerrR622[:,4],WBR62[:,4]+WBerrR622[:,4],alpha=0.3,facecolor='b',edgecolor='',label=r'WB T=155 MeV')


plt.axes([0.613, 0.212, 0.15, 0.27]) #不用figure的形式则无须用set
line_FRG_T160,=plt.plot(mubfrg*cmu/(200.0*ct),R62200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5)
band_FRG_T160=plt.fill_between(xsame,power1,power2,alpha=0.4,facecolor='m',edgecolor='',zorder=12,label=r'This work T=160 MeV')
line_FRG_T155,=plt.plot(mubfrg*cmu/(195.0*ct),R62195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5)#,label=r'This work T=155 MeV')
band_FRG_T155=plt.fill_between(xsame2,power3,power4,alpha=0.4,facecolor='r',edgecolor='',zorder=11,label=r'This work T=155 MeV')
band_HotQCD_T160=plt.fill_between(mub/160.,R62[:,60]-errR622[:,60],R62[:,60]+errR622[:,60],alpha=0.3,facecolor='c',edgecolor='',label=r'HotQCD T=160 MeV')
band_HotQCD_T155=plt.fill_between(mub/155.,R62[:,50]-errR622[:,50],R62[:,50]+errR622[:,50],alpha=0.3,facecolor='green',edgecolor='',label=r'HotQCD T=155 MeV')

#x=range(0,1,0.2)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.axis([0,0.8,-3,1])

ax2.axis([0,0.8,-3,1.])

ax2.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax2.set_ylabel('$R^B_{62}$', fontsize=14, color='black')

ax2.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160),band_HotQCD_T155,band_HotQCD_T160,band_WB_T155,band_WB_T160),(r'fRG-LEFT $T=155$ MeV',r'fRG-LEFT $T=160$ MeV',r'HotQCD $T=155$ MeV',r'HotQCD $T=160$ MeV',r'WB $T=155$ MeV',r'WB $T=160$ MeV'),loc=[0.54,0.085],fontsize='7',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.15, left=0.09, right=0.95, hspace=0.35,
                    wspace=0.25)


fig.savefig("R42R62-muBoTwithouthotQCD.pdf")

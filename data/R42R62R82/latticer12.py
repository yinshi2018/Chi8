#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl

mpl.style.use('classic')

# Data for plotting
R12194=np.loadtxt('./r12194.dat')
R12199=np.loadtxt('./r12199.dat')
R12189=np.loadtxt('./r12189.dat')
WBc2=np.loadtxt('./r42r62mubtlat/data1/WB_chi2.dat')
WBc4=np.loadtxt('./r42r62mubtlat/data1/WB_chi4.dat')
WBc6=np.loadtxt('./r42r62mubtlat/data1/WB_chi6.dat')
WBc8=np.loadtxt('./r42r62mubtlat/data1/WB_chi8.dat')
WBT=[135.,140.,145.,150.,155.,160.,165.,170.,175.,180.,185.,190.,195.,200.,205.,210.,215.,220.]
WBR12=np.zeros((101,18))
mubfrg=np.loadtxt('./mub.dat')
#ct=1./1.247
#cmu=1./1.110
ct=1.
cmu=1.
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
errR62=np.zeros((101,101))
errR82=np.zeros((101,101))
for num1 in range(0,100):
    for num2 in range(0,100):
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
        errR12[num1,num2]=(abs(A1b1[num1,num2]-A2[num1,num2]*b0)*errc2[num2]+abs(A1b3[num1,num2]-A2[num1,num2]*b2)*errc4[num2]+abs(A1b5[num1,num2]-A2[num1,num2]*b4)*errc6[num2]+abs(A1b7[num1,num2]-A2[num1,num2]*b6)*errc8[num2])*R12[num1,num2]
    


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
        WBR12[num1,num2]=chi1[num1,num2]/chi2[num1,num2]

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(mubfrg*cmu/(194.0*ct),R12194,'-',color='k',linewidth=1,label=r'$T=194\,\mathrm{MeV}$')
ax1.plot(mubfrg*cmu/(199.0*ct),R12199,'-',color='r',linewidth=1,label=r'$T=199\,\mathrm{MeV}$')
ax1.plot(mubfrg*cmu/(189.0*ct),R12189,'-',color='g',linewidth=1,label=r'$T=189\,\mathrm{MeV}$')
ax1.errorbar(mub/155.,WBR12[:,4],yerr=errR12[:,53],color='blue',marker='o',linestyle='',linewidth=2,markersize=2,fillstyle='none',alpha=1,label=r'HotQCD')
#ax1.plot(mub/155,R12[:,50],'k-',linewidth=2,markersize=5,label=r'$T$')
#ax1.errorbar(mub/156.,R12[:,53],yerr=errR12[:,53],color='blue',marker='o',linestyle='',linewidth=2,markersize=2,fillstyle='none',alpha=1,label=r'HotQCD')

ax1.axis([0,1.3,0,1.2])

ax1.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax1.set_ylabel('$R^B_{12}$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.17, left=0.15, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("r12.pdf")

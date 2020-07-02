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
Tfrg=np.loadtxt('./TMeV.dat')

chi2frg=np.loadtxt('../mub0/final/buffer/chi2.dat')
chi4frg=np.loadtxt('../mub0/final/buffer/chi4.dat')
chi6frg=np.loadtxt('../mub0/final/buffer/chi6.dat')
chi8frg=np.loadtxt('../mub0/final/buffer/chi8.dat')
chi10frg=np.loadtxt('../mub0/final/buffer/chi10.dat')
chi2f=np.zeros((300,101))
chi4f=np.zeros((300,101))
chi6f=np.zeros((300,101))
chi8f=np.zeros((300,101))


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
WBerrc2=np.zeros((18))
WBerrc4=np.loadtxt('./r42r62mubtlat/data1/WB_chi4erro.dat')
WBerrc6=np.loadtxt('./r42r62mubtlat/data1/WB_chi6erro.dat')
WBT=[135.,140.,145.,150.,155.,160.,165.,170.,175.,180.,185.,190.,195.,200.,205.,210.,215.,220.]
WBR42=np.zeros((101,18))
WBerrR42=np.zeros((101,18))
WBerrR422=np.zeros((101,18))

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
errR62=np.zeros((101,101))
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
        chi2[num1,num2]=c2[num2]+1./(2.*1.) *c4[num2]* (4.*num1/T[num2])**2. #+1./(4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**6.
        chi3[num1,num2]=c4[num2]* (4.*num1/T[num2]) +1./(3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**3.+1./(5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**5.
        chi4[num1,num2]=c4[num2] +1./(2.*1.) *c6[num2]* (4.*num1/T[num2])**2.#+1./(4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**4.
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

for num1 in range(0,101):
    for num2 in range(0,18):
        chi2[num1,num2]=WBc2[num2]+1./(2.*1.) *WBc4[num2]* (4.*num1/WBT[num2])**2. #+1./(4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**6.
        chi4[num1,num2]=WBc4[num2] +1./(2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**2.#+1./(4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**4.        chi7[num1,num2]=c8[num2]* (4.*num1/T[num2])
        WBR42[num1,num2]=chi4[num1,num2]/chi2[num1,num2]
        WBerrR42[num1,num2]=abs(chi4[num1,num2]/(chi2[num1,num2]**2))*WBerrc2[num2]+abs(1./chi2[num1,num2]-chi4[num1,num2]/(chi2[num1,num2])**2*1./(2.*1.)*(4.*num1/WBT[num2])**2)*WBerrc4[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/WBT[num2])**2)*WBerrc6[num2]
        WBerrR422[num1,num2]=((((chi4[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi6[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])**2)*WBerrc2[num2])**2 \
                           +  ((1./(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])-(chi4[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi6[num1,num2])*1./(1.*2.)*(4.*num1/WBT[num2])**2/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])**2)*WBerrc4[num2])**2 \
                           +  (((1./(1.*2.)*(4.*num1/WBT[num2])**2)/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2]))*WBerrc6[num2])**2)**0.5

#print(chi2frg[1])
for num1 in range(0,101):
    for num2 in range(0,300):
        chi2f[num2,num1]=chi2frg[num2]+1./(2.*1.) *chi4frg[num2]* (4.*num1/Tfrg[num2])**2. +1./(4.*3.*2.*1.) *chi6frg[num2]* (4.*num1/Tfrg[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *chi8frg[num2]* (4.*num1/Tfrg[num2])**6.#+1./(8.*7.*6.*5.*4.*3.*2.*1.) *chi10frg[num2]* (4.*num1/Tfrg[num2])**8.
        chi4f[num2,num1]=chi4frg[num2] +1./(2.*1.) *chi6frg[num2]* (4.*num1/Tfrg[num2])**2.+1./(4.*3.*2.*1.) *chi8frg[num2]* (4.*num1/Tfrg[num2])**4.#+1./(6.*5.*4.*3.*2.*1.) *chi10frg[num2]* (4.*num1/Tfrg[num2])**6.       



# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
x1=mubfrg*cmu2/(198.0*ct1)
x2=mubfrg*cmu1/(201.0*ct2)
line_FRG_T160,=ax1.plot(mubfrg*cmu/(200.0*ct),R42200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5)
xsame=np.linspace(0.,1.2,100)
power1=spline(x1,R42198,xsame)
power2=spline(x2,R42201,xsame)
#band_FRG_T160=ax1.fill_between(xsame,power1,power2,alpha=0.4,facecolor='m',edgecolor='',zorder=12,label=r'This work T=160 MeV')
x3=mubfrg*cmu2/(193.0*ct1)
x4=mubfrg*cmu1/(196.0*ct2)
line_FRG_T155,=ax1.plot(mubfrg*cmu/(195.0*ct),R42195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5)
xsame2=np.linspace(0.,1.2,100)
power3=spline(x3,R42193,xsame2)
power4=spline(x4,R42196,xsame2)
#band_FRG_T155=ax1.fill_between(xsame2,power3,power4,alpha=0.4,facecolor='r',edgecolor='',zorder=11,label=r'This work T=155 MeV')
xup160=mub*cmu2/(198.*ct1)
xdown160=mub*cmu1/(201.*ct2)
xsame=np.linspace(0.,1.2,100)
powerup160=spline(xup160,chi4f[197,:]/chi2f[197,:],xsame)
powerdown160=spline(xdown160,chi4f[200,:]/chi2f[200,:],xsame)
#bandexp_FRG_T160=ax1.fill_between(xsame,powerup160,powerdown160,alpha=0.4,facecolor='b',edgecolor='',zorder=12,label=r'Expansion T=160 MeV')
xup155=mub*cmu2/(193.*ct1)
xdown155=mub*cmu1/(196.*ct2)
xsame=np.linspace(0.,1.2,100)
powerup155=spline(xup155,chi4f[193,:]/chi2f[193,:],xsame)
powerdown155=spline(xdown155,chi4f[196,:]/chi2f[196,:],xsame)
#bandexp_FRG_T155=ax1.fill_between(xsame,powerup155,powerdown155,alpha=0.4,facecolor='b',edgecolor='',zorder=12,label=r'Expansion T=155 MeV')
exp_FRG_T155,=ax1.plot(mub*cmu/(195*ct),chi4f[194,:]/chi2f[194,:],'--',dashes=(5,2),color='b',linewidth=1.5,alpha=0.5)
exp_FRG_T160,=ax1.plot(mub*cmu/(200*ct),chi4f[199,:]/chi2f[199,:],'--',dashes=(1,2),color='b',linewidth=1.5,alpha=0.5)


ax1.axis([0,1.5,0.1,0.9])

ax1.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax1.set_ylabel('$R^B_{42}$', fontsize=14, color='black')


#ax1.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160)),(r'This work $T=155$ MeV',r'This work $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax1.legend(((line_FRG_T155),(line_FRG_T160),(exp_FRG_T155),(exp_FRG_T160)),(r'Calculation result $T=155$ MeV',r'Calculation result $T=160$ MeV',r'Expansion result $T=155$ MeV',r'Expansion result $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.15, left=0.15, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("R42expansion-muBoT.pdf")
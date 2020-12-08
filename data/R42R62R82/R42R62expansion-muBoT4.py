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
Tfrg=np.loadtxt('./TMeV.dat')

chi2frg=np.loadtxt('../mub0old/final/buffer/chi2.dat')
chi4frg=np.loadtxt('../mub0old/final/buffer/chi4.dat')
chi6frg=np.loadtxt('../mub0old/final/buffer/chi6.dat')
chi8frg=np.loadtxt('../mub0old/final/buffer/chi8.dat')
chi10frg=np.loadtxt('../mub0old/final/buffer/chi10.dat')

chi2f=np.zeros((300,201))
chi4f=np.zeros((300,201))
chi6f=np.zeros((300,201))
chi8f=np.zeros((300,201))
chi10f=np.zeros((300,201))

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
chi1=np.zeros((201,101))
chi2=np.zeros((201,101))
chi3=np.zeros((201,101))
chi4=np.zeros((201,101))
chi5=np.zeros((201,101))
chi6=np.zeros((201,101))
chi7=np.zeros((201,101))
chi8=np.zeros((201,101))
R12=np.zeros((201,101))
R42=np.zeros((201,101))
R62=np.zeros((201,101))
R82=np.zeros((201,101))
mub=np.zeros(201)
A1b1=np.zeros((201,101))
A1b3=np.zeros((201,101))
A1b5=np.zeros((201,101))
A1b7=np.zeros((201,101))
A2=np.zeros((201,101))
A3=np.zeros((201,101))
A4=np.zeros((201,101))
A5=np.zeros((201,101))
A6=np.zeros((201,101))
A7=np.zeros((201,101))
A8=np.zeros((201,101))
errR12=np.zeros((101,101))
errR42=np.zeros((101,101))
errR422=np.zeros((101,101))
errR62=np.zeros((101,101))
errR82=np.zeros((101,101))
for num1 in range(0,201):
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


#print(chi2frg[1])
for num1 in range(0,201):
    for num2 in range(0,300):
        chi2f[num2,num1]=chi2frg[num2]+1./(2.*1.) *chi4frg[num2]* (4.*num1/Tfrg[num2])**2. +1./(4.*3.*2.*1.) *chi6frg[num2]* (4.*num1/Tfrg[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *chi8frg[num2]* (4.*num1/Tfrg[num2])**6.#+1./(8.*7.*6.*5.*4.*3.*2.*1.) *chi10frg[num2]* (4.*num1/Tfrg[num2])**8.
        chi4f[num2,num1]=chi4frg[num2] +1./(2.*1.) *chi6frg[num2]* (4.*num1/Tfrg[num2])**2.+1./(4.*3.*2.*1.) *chi8frg[num2]* (4.*num1/Tfrg[num2])**4.      
        chi6f[num2,num1]=chi6frg[num2] +1./(2.*1.) *chi8frg[num2]* (4.*num1/Tfrg[num2])**2.





xsame=np.linspace(0.,3.,100)
# Create figure
fig=plt.figure(figsize=(9., 7.))
#fig=plt.figure()
ax1=fig.add_subplot(221)
powerh=np.zeros(100)
powerl=np.zeros(100)
x1=mubfrg*cmu2/(198.0*ct1)
x2=mubfrg*cmu1/(201.0*ct2)
x3=mubfrg*cmu2/(199.0*ct1)
x4=mubfrg*cmu1/(200.0*ct2)
x5=mubfrg*cmu1/(198.0*ct2)
x6=mubfrg*cmu2/(201.0*ct1)
x7=mubfrg*cmu1/(199.0*ct2)
x8=mubfrg*cmu2/(200.0*ct1)
x9=mubfrg*cmu2/(198.0*ct2)
x10=mubfrg*cmu2/(201.0*ct2)
x11=mubfrg*cmu2/(199.0*ct2)
x12=mubfrg*cmu2/(200.0*ct2)
x13=mubfrg*cmu1/(198.0*ct1)
x14=mubfrg*cmu1/(201.0*ct1)
x15=mubfrg*cmu1/(199.0*ct1)
x16=mubfrg*cmu1/(200.0*ct1)
power1=spline(x1,R42198,xsame)
power2=spline(x2,R42201,xsame)
power3=spline(x3,R42199,xsame)
power4=spline(x4,R42200,xsame)
power5=spline(x5,R42198,xsame)
power6=spline(x6,R42201,xsame)
power7=spline(x7,R42199,xsame)
power8=spline(x8,R42200,xsame)
power9=spline(x9,R42198,xsame)
power10=spline(x10,R42201,xsame)
power11=spline(x11,R42199,xsame)
power12=spline(x12,R42200,xsame)
power13=spline(x13,R42198,xsame)
power14=spline(x14,R42201,xsame)
power15=spline(x15,R42199,xsame)
power16=spline(x16,R42200,xsame)
for i in range(0,100):
    A=np.array([power1[i],power2[i],power3[i],power4[i],power5[i],power6[i],power7[i],power8[i],power9[i],power10[i],power11[i],power12[i],power13[i],power14[i],power15[i],power16[i]])
    powerh[i]=max(A)
    powerl[i]=min(A)
powerl[66]=powerl[65]
powerl[67]=powerl[65]
powerl[68]=powerl[65]
powerl[69]=powerl[65]
line_FRG_T160,=ax1.plot(mubfrg*cmu/(200.0*ct),R42200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5,zorder=2)
xsame2=np.linspace(0.,3.,100)
band_FRG_T160=ax1.fill_between(xsame,powerh,powerl,alpha=0.3,facecolor='m',edgecolor='',zorder=1,label=r'This work T=160 MeV')
powerh=np.zeros(100)
powerl=np.zeros(100)
x1=mubfrg*cmu2/(193.0*ct1)
x2=mubfrg*cmu1/(196.0*ct2)
x3=mubfrg*cmu2/(194.0*ct1)
x4=mubfrg*cmu1/(195.0*ct2)
x5=mubfrg*cmu1/(193.0*ct2)
x6=mubfrg*cmu2/(196.0*ct1)
x7=mubfrg*cmu1/(194.0*ct2)
x8=mubfrg*cmu2/(195.0*ct1)
x9=mubfrg*cmu2/(193.0*ct2)
x10=mubfrg*cmu2/(196.0*ct2)
x11=mubfrg*cmu2/(194.0*ct2)
x12=mubfrg*cmu2/(195.0*ct2)
x13=mubfrg*cmu1/(193.0*ct1)
x14=mubfrg*cmu1/(196.0*ct1)
x15=mubfrg*cmu1/(194.0*ct1)
x16=mubfrg*cmu1/(195.0*ct1)
power1=spline(x1,R42193,xsame)
power2=spline(x2,R42196,xsame)
power3=spline(x3,R42194,xsame)
power4=spline(x4,R42195,xsame)
power5=spline(x5,R42193,xsame)
power6=spline(x6,R42196,xsame)
power7=spline(x7,R42194,xsame)
power8=spline(x8,R42195,xsame)
power9=spline(x9,R42193,xsame)
power10=spline(x10,R42196,xsame)
power11=spline(x11,R42194,xsame)
power12=spline(x12,R42195,xsame)
power13=spline(x13,R42193,xsame)
power14=spline(x14,R42196,xsame)
power15=spline(x15,R42194,xsame)
power16=spline(x16,R42195,xsame)
for i in range(0,100):
    A=np.array([power1[i],power2[i],power3[i],power4[i],power5[i],power6[i],power7[i],power8[i],power9[i],power10[i],power11[i],power12[i],power13[i],power14[i],power15[i],power16[i]])
    powerh[i]=max(A)
    powerl[i]=min(A)
powerl[73]=powerl[72]
powerl[74]=powerl[72]
powerl[75]=powerl[72]
powerl[76]=powerl[72]
powerl[77]=powerl[72]
powerl[78]=powerl[72]
powerl[79]=powerl[72]
line_FRG_T155,=ax1.plot(mubfrg*cmu/(195.0*ct),R42195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=2)
band_FRG_T155=ax1.fill_between(xsame2,powerh,powerl,alpha=0.3,facecolor='r',edgecolor='',zorder=1,label=r'This work T=155 MeV')

xup160=mub*cmu2/(198.*ct1)
xdown160=mub*cmu1/(201.*ct2)
xsame=np.linspace(0.,3.,100)
powerup160=spline(xup160,chi4f[197,:]/chi2f[197,:],xsame)
powerdown160=spline(xdown160,chi4f[200,:]/chi2f[200,:],xsame)
bandexp_FRG_T160=ax1.fill_between(xsame,powerup160,powerdown160,alpha=0.3,facecolor='c',edgecolor='',zorder=1,label=r'Expansion T=160 MeV')
xup155=mub*cmu2/(193.*ct1)
xdown155=mub*cmu1/(196.*ct2)
xsame=np.linspace(0.,3.,100)
powerup155=spline(xup155,chi4f[192,:]/chi2f[192,:],xsame)
powerdown155=spline(xdown155,chi4f[195,:]/chi2f[195,:],xsame)
bandexp_FRG_T155=ax1.fill_between(xsame,powerup155,powerdown155,alpha=0.3,facecolor='b',edgecolor='',zorder=1,label=r'Expansion T=155 MeV')
exp_FRG_T155,=ax1.plot(mub*cmu/(195*ct),chi4f[194,:]/chi2f[194,:],'--',dashes=(5,2),color='b',linewidth=1.,zorder=2,alpha=0.5)
exp_FRG_T160,=ax1.plot(mub*cmu/(200*ct),chi4f[199,:]/chi2f[199,:],'--',dashes=(1,2),color='b',linewidth=1.,zorder=2,alpha=0.5)

ax1.text(2.0, 0.5, r'up to $\chi^B_{8}$',fontsize=12., color='k')
ax1.axis([0,3,-1,1])

ax1.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax1.set_ylabel('$R^B_{42}$', fontsize=14, color='black')


ax1.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160),(bandexp_FRG_T155,exp_FRG_T155),(bandexp_FRG_T160,exp_FRG_T160)),(r'fRG-LEFT full $T=155$ MeV',r'fRG-LEFT full $T=160$ MeV',r'fRG-LEFT expansion $T=155$ MeV',r'fRG-LEFT expansion $T=160$ MeV'),loc=0,fontsize=7.3,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax1.legend(((line_FRG_T155),(line_FRG_T160),(exp_FRG_T155),(exp_FRG_T160)),(r'Calculation result $T=155$ MeV',r'Calculation result $T=160$ MeV',r'Expansion result $T=155$ MeV',r'Expansion result $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)
########################################################################################################################################################
ax2=fig.add_subplot(223)
powerh=np.zeros(100)
powerl=np.zeros(100)
x1=mubfrg*cmu2/(198.0*ct1)
x2=mubfrg*cmu1/(201.0*ct2)
x3=mubfrg*cmu2/(199.0*ct1)
x4=mubfrg*cmu1/(200.0*ct2)
x5=mubfrg*cmu1/(198.0*ct2)
x6=mubfrg*cmu2/(201.0*ct1)
x7=mubfrg*cmu1/(199.0*ct2)
x8=mubfrg*cmu2/(200.0*ct1)
x9=mubfrg*cmu2/(198.0*ct2)
x10=mubfrg*cmu2/(201.0*ct2)
x11=mubfrg*cmu2/(199.0*ct2)
x12=mubfrg*cmu2/(200.0*ct2)
x13=mubfrg*cmu1/(198.0*ct1)
x14=mubfrg*cmu1/(201.0*ct1)
x15=mubfrg*cmu1/(199.0*ct1)
x16=mubfrg*cmu1/(200.0*ct1)
power1=spline(x1,R62198,xsame)
power2=spline(x2,R62201,xsame)
power3=spline(x3,R62199,xsame)
power4=spline(x4,R62200,xsame)
power5=spline(x5,R62198,xsame)
power6=spline(x6,R62201,xsame)
power7=spline(x7,R62199,xsame)
power8=spline(x8,R62200,xsame)
power9=spline(x9,R62198,xsame)
power10=spline(x10,R62201,xsame)
power11=spline(x11,R62199,xsame)
power12=spline(x12,R62200,xsame)
power13=spline(x13,R62198,xsame)
power14=spline(x14,R62201,xsame)
power15=spline(x15,R62199,xsame)
power16=spline(x16,R62200,xsame)
for i in range(0,100):
    A=np.array([power1[i],power2[i],power3[i],power4[i],power5[i],power6[i],power7[i],power8[i],power9[i],power10[i],power11[i],power12[i],power13[i],power14[i],power15[i],power16[i]])
    powerh[i]=max(A)
    powerl[i]=min(A)
powerl[41]=powerl[40]
powerl[42]=powerl[40]
powerl[43]=powerl[40]
powerl[44]=powerl[40]
powerl[45]=powerl[40]
powerh[66]=powerh[65]
powerh[67]=powerh[65]
powerh[68]=powerh[65]
powerh[69]=powerh[65]
powerh[70]=powerh[65]
powerl[81]=powerl[82]
powerl[82]=powerl[82]
powerl[83]=powerl[82]
powerl[84]=powerl[82]
powerl[85]=powerl[82]
powerl[86]=powerl[82]
powerl[87]=powerl[82]
powerl[88]=powerl[82]
powerl[89]=powerl[82]
powerl[90]=powerl[82]
line_FRG_T160,=ax2.plot(mubfrg*cmu/(200.0*ct),R62200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5,zorder=2)
band_FRG_T160=ax2.fill_between(xsame,powerh,powerl,alpha=0.3,facecolor='m',edgecolor='',zorder=1,label=r'This work T=160 MeV')
powerh=np.zeros(100)
powerl=np.zeros(100)
x1=mubfrg*cmu2/(193.0*ct1)
x2=mubfrg*cmu1/(196.0*ct2)
x3=mubfrg*cmu2/(194.0*ct1)
x4=mubfrg*cmu1/(195.0*ct2)
x5=mubfrg*cmu1/(193.0*ct2)
x6=mubfrg*cmu2/(196.0*ct1)
x7=mubfrg*cmu1/(194.0*ct2)
x8=mubfrg*cmu2/(195.0*ct1)
x9=mubfrg*cmu2/(193.0*ct2)
x10=mubfrg*cmu2/(196.0*ct2)
x11=mubfrg*cmu2/(194.0*ct2)
x12=mubfrg*cmu2/(195.0*ct2)
x13=mubfrg*cmu1/(193.0*ct1)
x14=mubfrg*cmu1/(196.0*ct1)
x15=mubfrg*cmu1/(194.0*ct1)
x16=mubfrg*cmu1/(195.0*ct1)
power1=spline(x1,R62193,xsame)
power2=spline(x2,R62196,xsame)
power3=spline(x3,R62194,xsame)
power4=spline(x4,R62195,xsame)
power5=spline(x5,R62193,xsame)
power6=spline(x6,R62196,xsame)
power7=spline(x7,R62194,xsame)
power8=spline(x8,R62195,xsame)
power9=spline(x9,R62193,xsame)
power10=spline(x10,R62196,xsame)
power11=spline(x11,R62194,xsame)
power12=spline(x12,R62195,xsame)
power13=spline(x13,R62193,xsame)
power14=spline(x14,R62196,xsame)
power15=spline(x15,R62194,xsame)
power16=spline(x16,R62195,xsame)
for i in range(0,100):
    A=np.array([power1[i],power2[i],power3[i],power4[i],power5[i],power6[i],power7[i],power8[i],power9[i],power10[i],power11[i],power12[i],power13[i],power14[i],power15[i],power16[i]])
    powerh[i]=max(A)
    powerl[i]=min(A)
print(powerl)
print(powerl[90])
powerl[54]=powerl[53]
powerl[55]=powerl[53]
powerl[56]=powerl[53]
powerl[57]=powerl[53]

powerl[91]=powerl[90]
powerl[92]=powerl[90]
powerl[93]=powerl[90]
powerl[94]=powerl[90]
powerl[95]=powerl[90]
powerl[96]=powerl[90]
powerl[97]=powerl[90]
powerl[98]=powerl[90]

powerh[73]=powerh[72]
powerh[74]=powerh[72]
powerh[75]=powerh[72]
powerh[76]=powerh[72]
powerh[77]=powerh[72]
powerh[78]=powerh[72]
powerh[79]=powerh[72]
powerh[80]=powerh[72]
powerh[81]=powerh[72]
powerh[82]=powerh[72]
print(powerh)
print(powerh[72])
line_FRG_T155,=ax2.plot(mubfrg*cmu/(195.0*ct),R62195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=2)
band_FRG_T155=ax2.fill_between(xsame2,powerh,powerl,alpha=0.3,facecolor='r',edgecolor='',zorder=1,label=r'This work T=155 MeV')
xup160=mub*cmu2/(198.*ct1)
xdown160=mub*cmu1/(201.*ct2)
xsame=np.linspace(0.,3.,100)
powerup160=spline(xup160,chi6f[197,:]/chi2f[197,:],xsame)
powerdown160=spline(xdown160,chi6f[200,:]/chi2f[200,:],xsame)
bandexp_FRG_T160=ax2.fill_between(xsame,powerup160,powerdown160,alpha=0.3,facecolor='c',edgecolor='',zorder=1,label=r'Expansion T=160 MeV')
xup155=mub*cmu2/(193.*ct1)
xdown155=mub*cmu1/(196.*ct2)
xsame=np.linspace(0.,3.,100)
powerup155=spline(xup155,chi6f[192,:]/chi2f[192,:],xsame)
powerdown155=spline(xdown155,chi6f[195,:]/chi2f[195,:],xsame)
bandexp_FRG_T155=ax2.fill_between(xsame,powerup155,powerdown155,alpha=0.3,facecolor='b',edgecolor='',zorder=1,label=r'Expansion T=155 MeV')
exp_FRG_T155,=ax2.plot(mub*cmu/(195*ct),chi6f[194,:]/chi2f[194,:],'--',dashes=(5,2),color='b',linewidth=1.,alpha=0.5,zorder=2)
exp_FRG_T160,=ax2.plot(mub*cmu/(200*ct),chi6f[199,:]/chi2f[199,:],'--',dashes=(1,2),color='b',linewidth=1.,alpha=0.5,zorder=2)

ax2.text(0.5, 3., r'up to $\chi^B_{8}$',fontsize=12., color='k')
ax2.axis([0,3,-5,8.5])

ax2.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax2.set_ylabel('$R^B_{62}$', fontsize=14, color='black')

ax2.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160),(bandexp_FRG_T155,exp_FRG_T155),(bandexp_FRG_T160,exp_FRG_T160)),(r'fRG-LEFT full $T=155$ MeV',r'fRG-LEFT full $T=160$ MeV',r'fRG-LEFT expansion $T=155$ MeV',r'fRG-LEFT expansion $T=160$ MeV'),loc=0,fontsize=7.3,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160)),(r'This work $T=155$ MeV',r'This work $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.legend(((line_FRG_T155),(line_FRG_T160),(exp_FRG_T155),(exp_FRG_T160)),(r'Calculation result $T=155$ MeV',r'Calculation result $T=160$ MeV',r'Expansion result $T=155$ MeV',r'Expansion result $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


for num1 in range(0,201):
    for num2 in range(0,300):
        chi2f[num2,num1]=chi2frg[num2]+1./(2.*1.) *chi4frg[num2]* (4.*num1/Tfrg[num2])**2. +1./(4.*3.*2.*1.) *chi6frg[num2]* (4.*num1/Tfrg[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *chi8frg[num2]* (4.*num1/Tfrg[num2])**6.+1./(8.*7.*6.*5.*4.*3.*2.*1.) *chi10frg[num2]* (4.*num1/Tfrg[num2])**8.
        chi4f[num2,num1]=chi4frg[num2] +1./(2.*1.) *chi6frg[num2]* (4.*num1/Tfrg[num2])**2.+1./(4.*3.*2.*1.) *chi8frg[num2]* (4.*num1/Tfrg[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *chi10frg[num2]* (4.*num1/Tfrg[num2])**6.   
        chi6f[num2,num1]=chi6frg[num2] +1./(2.*1.) *chi8frg[num2]* (4.*num1/Tfrg[num2])**2.+1./(4.*3.*2.*1.) *chi10frg[num2]* (4.*num1/Tfrg[num2])**4.

ax3=fig.add_subplot(222)
powerh=np.zeros(100)
powerl=np.zeros(100)
x1=mubfrg*cmu2/(198.0*ct1)
x2=mubfrg*cmu1/(201.0*ct2)
x3=mubfrg*cmu2/(199.0*ct1)
x4=mubfrg*cmu1/(200.0*ct2)
x5=mubfrg*cmu1/(198.0*ct2)
x6=mubfrg*cmu2/(201.0*ct1)
x7=mubfrg*cmu1/(199.0*ct2)
x8=mubfrg*cmu2/(200.0*ct1)
x9=mubfrg*cmu2/(198.0*ct2)
x10=mubfrg*cmu2/(201.0*ct2)
x11=mubfrg*cmu2/(199.0*ct2)
x12=mubfrg*cmu2/(200.0*ct2)
x13=mubfrg*cmu1/(198.0*ct1)
x14=mubfrg*cmu1/(201.0*ct1)
x15=mubfrg*cmu1/(199.0*ct1)
x16=mubfrg*cmu1/(200.0*ct1)
power1=spline(x1,R42198,xsame)
power2=spline(x2,R42201,xsame)
power3=spline(x3,R42199,xsame)
power4=spline(x4,R42200,xsame)
power5=spline(x5,R42198,xsame)
power6=spline(x6,R42201,xsame)
power7=spline(x7,R42199,xsame)
power8=spline(x8,R42200,xsame)
power9=spline(x9,R42198,xsame)
power10=spline(x10,R42201,xsame)
power11=spline(x11,R42199,xsame)
power12=spline(x12,R42200,xsame)
power13=spline(x13,R42198,xsame)
power14=spline(x14,R42201,xsame)
power15=spline(x15,R42199,xsame)
power16=spline(x16,R42200,xsame)
for i in range(0,100):
    A=np.array([power1[i],power2[i],power3[i],power4[i],power5[i],power6[i],power7[i],power8[i],power9[i],power10[i],power11[i],power12[i],power13[i],power14[i],power15[i],power16[i]])
    powerh[i]=max(A)
    powerl[i]=min(A)
powerl[66]=powerl[65]
powerl[67]=powerl[65]
powerl[68]=powerl[65]
powerl[69]=powerl[65]
line_FRG_T160,=ax3.plot(mubfrg*cmu/(200.0*ct),R42200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5,zorder=2)
xsame2=np.linspace(0.,3.,100)
band_FRG_T160=ax3.fill_between(xsame,powerh,powerl,alpha=0.3,facecolor='m',edgecolor='',zorder=1,label=r'This work T=160 MeV')
powerh=np.zeros(100)
powerl=np.zeros(100)
x1=mubfrg*cmu2/(193.0*ct1)
x2=mubfrg*cmu1/(196.0*ct2)
x3=mubfrg*cmu2/(194.0*ct1)
x4=mubfrg*cmu1/(195.0*ct2)
x5=mubfrg*cmu1/(193.0*ct2)
x6=mubfrg*cmu2/(196.0*ct1)
x7=mubfrg*cmu1/(194.0*ct2)
x8=mubfrg*cmu2/(195.0*ct1)
x9=mubfrg*cmu2/(193.0*ct2)
x10=mubfrg*cmu2/(196.0*ct2)
x11=mubfrg*cmu2/(194.0*ct2)
x12=mubfrg*cmu2/(195.0*ct2)
x13=mubfrg*cmu1/(193.0*ct1)
x14=mubfrg*cmu1/(196.0*ct1)
x15=mubfrg*cmu1/(194.0*ct1)
x16=mubfrg*cmu1/(195.0*ct1)
power1=spline(x1,R42193,xsame)
power2=spline(x2,R42196,xsame)
power3=spline(x3,R42194,xsame)
power4=spline(x4,R42195,xsame)
power5=spline(x5,R42193,xsame)
power6=spline(x6,R42196,xsame)
power7=spline(x7,R42194,xsame)
power8=spline(x8,R42195,xsame)
power9=spline(x9,R42193,xsame)
power10=spline(x10,R42196,xsame)
power11=spline(x11,R42194,xsame)
power12=spline(x12,R42195,xsame)
power13=spline(x13,R42193,xsame)
power14=spline(x14,R42196,xsame)
power15=spline(x15,R42194,xsame)
power16=spline(x16,R42195,xsame)
for i in range(0,100):
    A=np.array([power1[i],power2[i],power3[i],power4[i],power5[i],power6[i],power7[i],power8[i],power9[i],power10[i],power11[i],power12[i],power13[i],power14[i],power15[i],power16[i]])
    powerh[i]=max(A)
    powerl[i]=min(A)
powerl[73]=powerl[72]
powerl[74]=powerl[72]
powerl[75]=powerl[72]
powerl[76]=powerl[72]
powerl[77]=powerl[72]
powerl[78]=powerl[72]
powerl[79]=powerl[72]
line_FRG_T155,=ax3.plot(mubfrg*cmu/(195.0*ct),R42195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=2)
band_FRG_T155=ax3.fill_between(xsame2,powerh,powerl,alpha=0.3,facecolor='r',edgecolor='',zorder=1,label=r'This work T=155 MeV')

x1601=mub*cmu2/(198.*ct1)
x1602=mub*cmu1/(199.*ct2)
x1603=mub*cmu2/(200.*ct2)
x1604=mub*cmu1/(201.*ct2)
powerup160=np.zeros(100)
powerdown160=np.zeros(100)
xsame=np.linspace(0.,3.,100)
power1601=spline(x1601,chi4f[197,:]/chi2f[197,:],xsame)
power1602=spline(x1602,chi4f[198,:]/chi2f[198,:],xsame)
power1603=spline(x1603,chi4f[199,:]/chi2f[199,:],xsame)
power1604=spline(x1604,chi4f[200,:]/chi2f[200,:],xsame)
for i in range(0,100):
    power160=np.array([power1601[i],power1602[i],power1603[i],power1604[i]])
    powerup160[i]=max(power160)
    powerdown160[i]=min(power160)
bandexp_FRG_T160=ax3.fill_between(xsame,powerup160,powerdown160,alpha=0.3,facecolor='c',edgecolor='',zorder=1,label=r'Expansion T=160 MeV')
xup155=mub*cmu2/(193.*ct1)
xdown155=mub*cmu1/(196.*ct2)
xsame=np.linspace(0.,3.,100)
powerup155=spline(xup155,chi4f[192,:]/chi2f[192,:],xsame)
powerdown155=spline(xdown155,chi4f[195,:]/chi2f[195,:],xsame)
bandexp_FRG_T155=ax3.fill_between(xsame,powerup155,powerdown155,alpha=0.3,facecolor='b',edgecolor='',zorder=1,label=r'Expansion T=155 MeV')
exp_FRG_T155,=ax3.plot(mub*cmu/(195*ct),chi4f[194,:]/chi2f[194,:],'--',dashes=(5,2),color='b',linewidth=1.,zorder=2,alpha=0.5)
exp_FRG_T160,=ax3.plot(mub*cmu/(200*ct),chi4f[199,:]/chi2f[199,:],'--',dashes=(1,2),color='b',linewidth=1.,zorder=2,alpha=0.5)

ax3.text(2.0, 0.5, r'up to $\chi^B_{10}$',fontsize=12., color='k')
ax3.axis([0,3,-1,1])

ax3.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
#ax3.set_ylabel('$R^B_{42}$', fontsize=14, color='black')


#ax3.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160),(bandexp_FRG_T155,exp_FRG_T155),(bandexp_FRG_T160,exp_FRG_T160)),(r'fRG-LEFT full $T=155$ MeV',r'fRG-LEFT full $T=160$ MeV',r'fRG-LEFT expansion $T=155$ MeV',r'fRG-LEFT expansion $T=160$ MeV'),loc=0,fontsize=7.,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax3.legend(((line_FRG_T155),(line_FRG_T160),(exp_FRG_T155),(exp_FRG_T160)),(r'Calculation result $T=155$ MeV',r'Calculation result $T=160$ MeV',r'Expansion result $T=155$ MeV',r'Expansion result $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax3.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(10)
########################################################################################################################################################
ax4=fig.add_subplot(224)
powerh=np.zeros(100)
powerl=np.zeros(100)
x1=mubfrg*cmu2/(198.0*ct1)
x2=mubfrg*cmu1/(201.0*ct2)
x3=mubfrg*cmu2/(199.0*ct1)
x4=mubfrg*cmu1/(200.0*ct2)
x5=mubfrg*cmu1/(198.0*ct2)
x6=mubfrg*cmu2/(201.0*ct1)
x7=mubfrg*cmu1/(199.0*ct2)
x8=mubfrg*cmu2/(200.0*ct1)
x9=mubfrg*cmu2/(198.0*ct2)
x10=mubfrg*cmu2/(201.0*ct2)
x11=mubfrg*cmu2/(199.0*ct2)
x12=mubfrg*cmu2/(200.0*ct2)
x13=mubfrg*cmu1/(198.0*ct1)
x14=mubfrg*cmu1/(201.0*ct1)
x15=mubfrg*cmu1/(199.0*ct1)
x16=mubfrg*cmu1/(200.0*ct1)
power1=spline(x1,R62198,xsame)
power2=spline(x2,R62201,xsame)
power3=spline(x3,R62199,xsame)
power4=spline(x4,R62200,xsame)
power5=spline(x5,R62198,xsame)
power6=spline(x6,R62201,xsame)
power7=spline(x7,R62199,xsame)
power8=spline(x8,R62200,xsame)
power9=spline(x9,R62198,xsame)
power10=spline(x10,R62201,xsame)
power11=spline(x11,R62199,xsame)
power12=spline(x12,R62200,xsame)
power13=spline(x13,R62198,xsame)
power14=spline(x14,R62201,xsame)
power15=spline(x15,R62199,xsame)
power16=spline(x16,R62200,xsame)
for i in range(0,100):
    A=np.array([power1[i],power2[i],power3[i],power4[i],power5[i],power6[i],power7[i],power8[i],power9[i],power10[i],power11[i],power12[i],power13[i],power14[i],power15[i],power16[i]])
    powerh[i]=max(A)
    powerl[i]=min(A)
powerl[41]=powerl[40]
powerl[42]=powerl[40]
powerl[43]=powerl[40]
powerl[44]=powerl[40]
powerl[45]=powerl[40]
powerh[66]=powerh[65]
powerh[67]=powerh[65]
powerh[68]=powerh[65]
powerh[69]=powerh[65]
powerh[70]=powerh[65]
powerl[81]=powerl[82]
powerl[82]=powerl[82]
powerl[83]=powerl[82]
powerl[84]=powerl[82]
powerl[85]=powerl[82]
powerl[86]=powerl[82]
powerl[87]=powerl[82]
powerl[88]=powerl[82]
powerl[89]=powerl[82]
powerl[90]=powerl[82]
line_FRG_T160,=ax4.plot(mubfrg*cmu/(200.0*ct),R62200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5,zorder=2)
band_FRG_T160=ax4.fill_between(xsame,powerh,powerl,alpha=0.3,facecolor='m',edgecolor='',zorder=1,label=r'This work T=160 MeV')
powerh=np.zeros(100)
powerl=np.zeros(100)
x1=mubfrg*cmu2/(193.0*ct1)
x2=mubfrg*cmu1/(196.0*ct2)
x3=mubfrg*cmu2/(194.0*ct1)
x4=mubfrg*cmu1/(195.0*ct2)
x5=mubfrg*cmu1/(193.0*ct2)
x6=mubfrg*cmu2/(196.0*ct1)
x7=mubfrg*cmu1/(194.0*ct2)
x8=mubfrg*cmu2/(195.0*ct1)
x9=mubfrg*cmu2/(193.0*ct2)
x10=mubfrg*cmu2/(196.0*ct2)
x11=mubfrg*cmu2/(194.0*ct2)
x12=mubfrg*cmu2/(195.0*ct2)
x13=mubfrg*cmu1/(193.0*ct1)
x14=mubfrg*cmu1/(196.0*ct1)
x15=mubfrg*cmu1/(194.0*ct1)
x16=mubfrg*cmu1/(195.0*ct1)
power1=spline(x1,R62193,xsame)
power2=spline(x2,R62196,xsame)
power3=spline(x3,R62194,xsame)
power4=spline(x4,R62195,xsame)
power5=spline(x5,R62193,xsame)
power6=spline(x6,R62196,xsame)
power7=spline(x7,R62194,xsame)
power8=spline(x8,R62195,xsame)
power9=spline(x9,R62193,xsame)
power10=spline(x10,R62196,xsame)
power11=spline(x11,R62194,xsame)
power12=spline(x12,R62195,xsame)
power13=spline(x13,R62193,xsame)
power14=spline(x14,R62196,xsame)
power15=spline(x15,R62194,xsame)
power16=spline(x16,R62195,xsame)
for i in range(0,100):
    A=np.array([power1[i],power2[i],power3[i],power4[i],power5[i],power6[i],power7[i],power8[i],power9[i],power10[i],power11[i],power12[i],power13[i],power14[i],power15[i],power16[i]])
    powerh[i]=max(A)
    powerl[i]=min(A)
print(powerl)
print(powerl[90])
powerl[54]=powerl[53]
powerl[55]=powerl[53]
powerl[56]=powerl[53]
powerl[57]=powerl[53]

powerl[91]=powerl[90]
powerl[92]=powerl[90]
powerl[93]=powerl[90]
powerl[94]=powerl[90]
powerl[95]=powerl[90]
powerl[96]=powerl[90]
powerl[97]=powerl[90]
powerl[98]=powerl[90]

powerh[73]=powerh[72]
powerh[74]=powerh[72]
powerh[75]=powerh[72]
powerh[76]=powerh[72]
powerh[77]=powerh[72]
powerh[78]=powerh[72]
powerh[79]=powerh[72]
powerh[80]=powerh[72]
powerh[81]=powerh[72]
powerh[82]=powerh[72]
print(powerh)
print(powerh[72])
line_FRG_T155,=ax4.plot(mubfrg*cmu/(195.0*ct),R62195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5,zorder=2)
band_FRG_T155=ax4.fill_between(xsame2,powerh,powerl,alpha=0.3,facecolor='r',edgecolor='',zorder=1,label=r'This work T=155 MeV')


x1601=mub*cmu2/(198.*ct1)
x1602=mub*cmu1/(199.*ct1)
x1603=mub*cmu2/(200.*ct1)
x1604=mub*cmu1/(201.*ct2)
powerup160=np.zeros(100)
powerdown160=np.zeros(100)
xsame=np.linspace(0.,3.,100)
power1601=spline(x1601,chi6f[197,:]/chi2f[197,:],xsame)
power1602=spline(x1602,chi6f[198,:]/chi2f[198,:],xsame)
power1603=spline(x1603,chi6f[199,:]/chi2f[199,:],xsame)
power1604=spline(x1604,chi6f[200,:]/chi2f[200,:],xsame)
for i in range(0,100):
    power160=np.array([power1601[i],power1602[i],power1603[i],power1604[i]])
    powerup160[i]=max(power160)
    powerdown160[i]=min(power160)
#xup160=mub*cmu2/(198.*ct1)
#xdown160=mub*cmu1/(201.*ct2)
#xsame=np.linspace(0.,3.,100)
#powerup160=spline(xup160,chi6f[197,:]/chi2f[197,:],xsame)
#powerdown160=spline(xdown160,chi6f[200,:]/chi2f[200,:],xsame)
bandexp_FRG_T160=ax4.fill_between(xsame,powerup160,powerdown160,alpha=0.3,facecolor='c',edgecolor='',zorder=1,label=r'Expansion T=160 MeV')
xup155=mub*cmu2/(193.*ct1)
xdown155=mub*cmu1/(196.*ct2)
xsame=np.linspace(0.,3.,100)
powerup155=spline(xup155,chi6f[192,:]/chi2f[192,:],xsame)
powerdown155=spline(xdown155,chi6f[195,:]/chi2f[195,:],xsame)
bandexp_FRG_T155=ax4.fill_between(xsame,powerup155,powerdown155,alpha=0.3,facecolor='b',edgecolor='',zorder=1,label=r'Expansion T=155 MeV')
exp_FRG_T155,=ax4.plot(mub*cmu/(195*ct),chi6f[194,:]/chi2f[194,:],'--',dashes=(5,2),color='b',linewidth=1.,alpha=0.5,zorder=2)
exp_FRG_T160,=ax4.plot(mub*cmu/(200*ct),chi6f[199,:]/chi2f[199,:],'--',dashes=(1,2),color='b',linewidth=1.,alpha=0.5,zorder=2)


ax4.text(0.5, 3., r'up to $\chi^B_{10}$',fontsize=12., color='k')
ax4.axis([0,3,-5,8.5])

ax4.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
#ax4.set_ylabel('$R^B_{62}$', fontsize=14, color='black')


#ax4.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160)),(r'This work $T=155$ MeV',r'This work $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax4.legend(((line_FRG_T155),(line_FRG_T160),(exp_FRG_T155),(exp_FRG_T160)),(r'Calculation result $T=155$ MeV',r'Calculation result $T=160$ MeV',r'Expansion result $T=155$ MeV',r'Expansion result $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax4.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax4.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.95, bottom=0.1, left=0.09, right=0.95, hspace=0.25,
                    wspace=0.23)


fig.savefig("R42R62expansion-muBoT4.pdf")

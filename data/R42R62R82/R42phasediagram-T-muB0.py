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
HRGR42=np.loadtxt('../HRG/R42ofTmu0.dat')
HRGR62=np.loadtxt('../HRG/R62ofTmu0.dat')
HRGR82=np.loadtxt('../HRG/R82ofTmu0.dat')

R62194=np.loadtxt('./r62194.dat')
R62199=np.loadtxt('./r62199.dat')
R62189=np.loadtxt('./r62189.dat')
chi8=np.loadtxt('../mub0/final/buffer/chi8.dat')
chi6=np.loadtxt('../mub0/final/buffer/chi6.dat')
chi4=np.loadtxt('../mub0/final/buffer/chi4.dat')
chi2=np.loadtxt('../mub0/final/buffer/chi2.dat')
r42=chi4/chi2
r62=chi6/chi2
r82=chi8/chi2

hotQCDR42=np.loadtxt('./r42r62mubtlat/data1/hotQCD_R42.dat')
WBR42=np.loadtxt('./r42r62mubtlat/data1/WB_R42.dat')
WBchi2=np.loadtxt('./r42r62mubtlat/data1/WB_chi2.dat')
WBchi6=np.loadtxt('./r42r62mubtlat/data1/WB_chi6.dat')
WBchi6erro=np.loadtxt('./r42r62mubtlat/data1/WB_chi6erro.dat')
WBchi8=np.loadtxt('./r42r62mubtlat/data1/WB_chi8.dat')
WBchi8erro=np.loadtxt('./r42r62mubtlat/data1/WB_chi8erro.dat')
WBchix=np.loadtxt('./r42r62mubtlat/data1/WB_chix.dat')
hotQCDR62=np.loadtxt('./r42r62mubtlat/data1/hotQCD_R62.dat')
hotQCDb=np.loadtxt('./r42r62mubtlat/data1/hotQCDR62_b.dat')
hotQCDg=np.loadtxt('./r42r62mubtlat/data1/hotQCDR62_g.dat')
T=np.loadtxt('./TMeV.dat')
R62erro=WBchi6erro/WBchi2
R82erro=WBchi8erro/WBchi2

chi8mub0=np.loadtxt('../mub0/final/buffer/chi8.dat')
chi6mub0=np.loadtxt('../mub0/final/buffer/chi6.dat')
chi4mub0=np.loadtxt('../mub0/final/buffer/chi4.dat')
chi2mub0=np.loadtxt('../mub0/final/buffer/chi2.dat')
Tfrg=np.loadtxt('./TMeV.dat')
frgchi2=np.zeros((101,300))
frgchi6=np.zeros((101,300))
frgr62=np.zeros((101,300))
ct=1.247
ct1=1.235
ct2=1.259
r82m=np.zeros((300,10))
xsame=np.linspace(0.,300.,300)
ct3=np.linspace(ct1,ct2,10)
for t in range(0,10):
    r82m[:,t]=spline(Tfrg/ct3[t],r82,xsame)

for num in range(1,10):
    if num==1:
       max82=np.maximum(r82m[:,num-1],r82m[:,num])
       min82=np.minimum(r82m[:,num-1],r82m[:,num])
    else:
       max82=np.maximum(max82,r82m[:,num])
       min82=np.minimum(min82,r82m[:,num])
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
errR622=np.zeros((101,101))
errR822=np.zeros((101,101))
errR62=np.zeros((101,101))
errR82=np.zeros((101,101))
for num1 in range(0,101):
    for num2 in range(0,101):
    	mub[num1]=4.*num1
    	b0=1.
    	b1=(num1/T[num2])
    	b2=1./2. *(num1/T[num2])**2.
    	b3=1./(3.*2.*1.) *(num1/T[num2])**3.
    	b4=1./(4.*3.*2.*1.) *(num1/T[num2])**4.
    	b5=1./(5.*4.*3.*2.*1.) *(num1/T[num2])**5.
    	b6=1./(6.*5.*4.*3.*2.*1.) *(num1/T[num2])**6.
    	b7=1./(7.*6.*5.*4.*3.*2.*1.) *(num1/T[num2])**7.
    	b8=1./(8.*7.*6.*5.*4.*3.*2.*1.) *(num1/T[num2])**8.
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
        errR42[num1,num2]=abs(chi4[num1,num2]/(chi2[num1,num2]**2))*errc2[num2]+abs(1./chi2[num1,num2]-chi4[num1,num2]/(chi2[num1,num2])**2*1./(2.*1.)*(4.*num1/T[num2])**2)*errc4[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/T[num2])**2-chi4[num1,num2]/(chi2[num1,num2])**2*1./(4.*3.*2.*1.)*(4.*num1/T[num2])**4)*errc6[num2]+abs(1./chi2[num1,num2]*1./(4.*3.*2.*1.)*(4.*num1/T[num2])**4-chi4[num1,num2]/(chi2[num1,num2])**2*1./(6.*5.*4.*3.*2.*1.)*(4.*num1/T[num2])**6)*errc8[num2]
        errR62[num1,num2]=abs(chi6[num1,num2]/(chi2[num1,num2]**2))*errc2[num2]+abs(chi6[num1,num2]/(chi2[num1,num2]**2)*1./(2.*1.)*(4.*num1/T[num2])**2)*errc4[num2]+abs(1./chi2[num1,num2]-chi6[num1,num2]/(chi2[num1,num2])**2*1./(4.*3.*2.*1.)*(4.*num1/T[num2])**4)*errc6[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/T[num2])**2-chi6[num1,num2]/(chi2[num1,num2])**2*1./(6.*5.*4.*3.*2.*1.)*(4.*num1/T[num2])**6)*errc8[num2]
        errR82[num1,num2]=abs(chi8[num1,num2]/(chi2[num1,num2]**2))*errc2[num2]+abs(chi8[num1,num2]/(chi2[num1,num2]**2)*1./(2.*1.)*(4.*num1/T[num2])**2)*errc4[num2]+abs(chi8[num1,num2]/(chi2[num1,num2])**2*1./(4.*3.*2.*1.)*(4.*num1/T[num2])**4)*errc6[num2]+abs(1./chi2[num1,num2]-chi8[num1,num2]/(chi2[num1,num2])**2*1./(6.*5.*4.*3.*2.*1.)*(4.*num1/T[num2])**6)*errc8[num2]
        errR422[num1,num2]=((errc4[num2]/c2[num2])**2+((c4[num2]*errc2[num2])**2/(c2[num2])**4))**0.5
        errR622[num1,num2]=((errc6[num2]/c2[num2])**2+((c4[num2]*errc2[num2])**2/(c2[num2])**4))**0.5
        errR822[num1,num2]=((errc8[num2]/c2[num2])**2+((c4[num2]*errc2[num2])**2/(c2[num2])**4))**0.5




#print(chi2mub0[200])
# Create figure
fig=plt.figure(figsize=(9., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(121)
band_FRG=ax1.fill_betweenx(r42,Tfrg/ct1,Tfrg/ct2,alpha=0.25,facecolor='r',edgecolor='r',label=r'This work')
#ax1.axvspan(Tfrg/ct1,Tfrg/ct2 , r42, alpha=0.5, color='red')
line_FRG,=ax1.plot(Tfrg/ct,r42,'-',color='r',linewidth=1,alpha=0.5)#,label=r'ct between 1.24 and 1.26')
#ax1.plot(Tfrg/ct1,r42,'-',color='b',linewidth=1)#,label=r'This work')
#ax1.plot(Tfrg/ct2,r42,'-',color='r',linewidth=1)#,label=r'This work')

#ax1.plot(mubfrg/199.0,R42199,'-',color='r',linewidth=1,label=r'$T=199\,\mathrm{MeV}$')
#ax1.plot(mubfrg/189.0,R42189,'-',color='g',linewidth=1,label=r'$T=189\,\mathrm{MeV}$')
#band_HotQCD17=ax1.fill_between(hotQCDR42[:,0],hotQCDR42[:,1]+hotQCDR42[:,2],hotQCDR42[:,1]-hotQCDR42[:,2],alpha=0.25,facecolor='b',edgecolor='',label=r'HotQCD 1708.04897')

#line_HotQCD,=ax1.plot(T,c4/c2,'g-',linewidth=1,markersize=5,alpha=0.5)#,label=r'$mid$')
#band_HotQCD=ax1.fill_between(T,R42[0,:]+errR422[0,:],R42[0,:]-errR422[0,:],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD 2001.08530')
#ax1.errorbar(mub/158.,R42[:,56],yerr=errR422[:,56],color='blue',marker='o',linestyle='',linewidth=2,markersize=2,fillstyle='none',alpha=1,label=r'HotQCD')
#ax2.fill_between(hotQCDR62[:,0]/156,hotQCDR62[:,1],hotQCDR62[:,2],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD cont. est')
points_WB=ax1.errorbar(WBR42[:,0],WBR42[:,1],yerr=WBR42[:,2],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'WB 1805.04445')
#HRG,=ax1.plot(HRGR42[:,0],HRGR42[:,1],dashes=[4,2],color='m',linewidth=1,alpha=1)
ax1.axis([80,230,0,1.2])

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$R^B_{42}$', fontsize=14, color='black')

#ax1.legend(((band_FRG,line_FRG),(band_HotQCD,line_HotQCD),band_HotQCD17,points_WB,HRG),(r'fRG-LEFT',r'HotQCD (2020)',r'HotQCD (2017)',r'WB',r'HRG'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax1.legend(((band_FRG,line_FRG),points_WB),(r'fRG-LEFT',r'WB'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)


for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

muB=np.loadtxt('../phase-diagram/Nf2p1/CEP/muB.dat')

pb_Nf2p1=np.loadtxt('../phase-diagram/Nf2p1/CEP/pb-Nf2p1.dat')
Tc_Nf2p1=np.loadtxt('../phase-diagram/Nf2p1/CEP/Tc.dat')

muB_CEP_Nf2p1=np.loadtxt('../phase-diagram/Nf2p1/CEP/CEPmuB.dat')
T_CEP_Nf2p1=np.loadtxt('../phase-diagram/Nf2p1/CEP/CEPT.dat')

pb_Nf2=np.loadtxt('../phase-diagram/Nf2/CEP/pb-Nf2.dat')
Tc_Nf2=np.loadtxt('../phase-diagram/Nf2/CEP/Tc.dat')

muB_CEP_Nf2=np.loadtxt('../phase-diagram/Nf2/CEP/CEPmuB.dat')
T_CEP_Nf2=np.loadtxt('../phase-diagram/Nf2/CEP/CEPT.dat')

ct=1.0915
cmu=0.995
# Create figure

#fig=plt.figure()
ax2=fig.add_subplot(122)
#ax1=plt.subplot(111)

line_Nf2,=ax2.plot(pb_Nf2[:,0]/cmu,Tc_Nf2/ct,'r--',linewidth=1.5,markersize=5,zorder=6,label=r'$N_f=2$')
CEP_Nf2,=ax2.plot(muB_CEP_Nf2/cmu,T_CEP_Nf2/ct,'r*',markersize=8,zorder=6,label=r'CEP: $N_f=2$')
band_Nf2=ax2.fill_between(pb_Nf2[:,0]/cmu,pb_Nf2[:,1]/ct,pb_Nf2[:,2]/ct,color='gray',alpha=.4,zorder=6,label=r'$N_f=2$')


line_Nf2p1,=ax2.plot(pb_Nf2p1[:,0],Tc_Nf2p1,'k--',dashes=(5,2),linewidth=1.5,markersize=5,zorder=5,label=r'$N_f=2+1$')
CEP_Nf2p1,=ax2.plot(muB_CEP_Nf2p1,T_CEP_Nf2p1,'ko',markersize=8,label=r'CEP: $N_f=2+1$')
band_Nf2p1=ax2.fill_between(pb_Nf2p1[:,0],pb_Nf2p1[:,1],pb_Nf2p1[:,2],color='blue',alpha=0.4,label=r'$N_f=2+1$')



ax2.plot(muB,muB/2.,'k:',linewidth=1.,markersize=5)
ax2.plot(muB,muB/3.,'k:',linewidth=1.,markersize=5)
ax2.text(90, 100, r'$\frac{\mu_B}{T}=2$',fontsize=10, color='k')
ax2.text(340, 100, r'$\frac{\mu_B}{T}=3$',fontsize=10, color='k')
ax2.axis([0,1000,0,200])
#ax1.set_xscale('log')

ax2.set_xlabel(r'$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$T\,[\mathrm{MeV}]$', fontsize=14, color='black')

ax2.legend(((band_Nf2,line_Nf2),(band_Nf2p1,line_Nf2p1),CEP_Nf2,CEP_Nf2p1),(r'rescaled fRG-QCD $N_f=2$',r' fRG-QCD $N_f=2+1$',r'CEP: $N_f=2$',r'CEP: $N_f=2+1$'),loc=4,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.15, left=0.07, right=0.96, hspace=0.35, wspace=0.25)

fig.savefig("R42phasediagram-T-muB0.pdf")

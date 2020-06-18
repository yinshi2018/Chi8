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
cmu=1./1.110
cmu1=1./(1.110+0.066)
cmu2=1./(1.110-0.066)
ct=1./1.247
ct1=1./1.235
ct2=1./1.259
#print(R62194[0])

WBc2=np.loadtxt('./r42r62mubtlat/data1/WB_chi2.dat')
WBc4=np.loadtxt('./r42r62mubtlat/data1/WB_chi4.dat')
WBc6=np.loadtxt('./r42r62mubtlat/data1/WB_chi6.dat')
WBc8=np.loadtxt('./r42r62mubtlat/data1/WB_chi8.dat')
WBerrc2=np.zeros((18))
WBerrc4=np.loadtxt('./r42r62mubtlat/data1/WB_chi4erro.dat')
WBerrc6=np.loadtxt('./r42r62mubtlat/data1/WB_chi6erro.dat')
WBerrc8=np.loadtxt('./r42r62mubtlat/data1/WB_chi8erro.dat')
WBT=[135.,140.,145.,150.,155.,160.,165.,170.,175.,180.,185.,190.,195.,200.,205.,210.,215.,220.]
WBR62=np.zeros((101,18))
WBerrR62=np.zeros((101,18))
WBerrR622=np.zeros((101,18))

mubfrg=np.loadtxt('./mub.dat')

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
        chi2[num1,num2]=c2[num2]+1./(2.*1.) *c4[num2]* (4.*num1/T[num2])**2.# +1./(4.*3.*2.*1.) *c6[num2]* (4.*num1/T[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *c8[num2]* (4.*num1/T[num2])**6.
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
        #errR62[num1,num2]=abs(chi6[num1,num2]/(chi2[num1,num2]**2))*errc2[num2]+abs(chi6[num1,num2]/(chi2[num1,num2]**2)*1./(2.*1.)*(4.*num1/T[num2])**2)*errc4[num2]+abs(1./chi2[num1,num2]-chi6[num1,num2]/(chi2[num1,num2])**2*1./(4.*3.*2.*1.)*(4.*num1/T[num2])**4)*errc6[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/T[num2])**2-chi6[num1,num2]/(chi2[num1,num2])**2*1./(6.*5.*4.*3.*2.*1.)*(4.*num1/T[num2])**6)*errc8[num2]
        errR62[num1,num2]=abs(chi6[num1,num2]/(chi2[num1,num2]**2))*errc2[num2]+abs(chi6[num1,num2]/(chi2[num1,num2]**2)*1./(2.*1.)*(4.*num1/T[num2])**2)*errc4[num2]+abs(1./chi2[num1,num2])*errc6[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/T[num2])**2)*errc8[num2]
        errR622[num1,num2]=((((chi6[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi8[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2])**2)*errc2[num2])**2 \
                           + (((chi6[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi8[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2])**2)*(1./(1.*2.)*(4.*num1/T[num2])**2)*errc4[num2])**2 \
                           + ((1./(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2]))*errc6[num2])**2 \
                           + (((1./(1.*2.)*(4.*num1/T[num2])**2)/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/T[num2])**2*chi4[num1,num2]))*errc8[num2])**2)**0.5
for num1 in range(0,101):
    for num2 in range(0,18):
        chi1[num1,num2]=WBc2[num2]*4.*num1/WBT[num2]+1./(3.*2.*1.) *WBc4[num2]* (4.*num1/WBT[num2])**3. +1./(5.*4.*3.*2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**5.+1./(7.*6.*5.*4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**7.
        chi2[num1,num2]=WBc2[num2]+1./(2.*1.) *WBc4[num2]* (4.*num1/WBT[num2])**2.# +1./(4.*3.*2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**4.+1./(6.*5.*4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**6.
        chi3[num1,num2]=WBc4[num2]* (4.*num1/WBT[num2]) +1./(3.*2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**3.+1./(5.*4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**5.
        chi4[num1,num2]=WBc4[num2] +1./(2.*1.) *WBc6[num2]* (4.*num1/WBT[num2])**2.+1./(4.*3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**4.
        chi5[num1,num2]=WBc6[num2]* (4.*num1/WBT[num2])+1./(3.*2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**3.
        chi6[num1,num2]=WBc6[num2]+1./(2.*1.) *WBc8[num2]* (4.*num1/WBT[num2])**2.
        chi7[num1,num2]=WBc8[num2]* (4.*num1/WBT[num2])
        chi8[num1,num2]=WBc8[num2]
        WBR62[num1,num2]=chi6[num1,num2]/chi2[num1,num2]
        WBerrR62[num1,num2]=abs(chi6[num1,num2]/(chi2[num1,num2]**2))*WBerrc2[num2]+abs(chi6[num1,num2]/(chi2[num1,num2]**2)*1./(2.*1.)*(4.*num1/WBT[num2])**2)*WBerrc4[num2]+abs(1./chi2[num1,num2])*WBerrc6[num2]+abs(1./chi2[num1,num2]*1./(2.*1.)*(4.*num1/WBT[num2])**2)*WBerrc8[num2]
        WBerrR622[num1,num2]=((((chi6[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi8[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])**2)*WBerrc2[num2])**2 \
                           + (((chi6[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi8[num1,num2])/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2])**2)*(1./(1.*2.)*(4.*num1/WBT[num2])**2)*WBerrc4[num2])**2 \
                           + ((1./(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2]))*WBerrc6[num2])**2 \
                           + (((1./(1.*2.)*(4.*num1/WBT[num2])**2)/(chi2[num1,num2]+1./(1.*2.)*(4.*num1/WBT[num2])**2*chi4[num1,num2]))*WBerrc8[num2])**2)**0.5

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
x1=mubfrg*cmu2/(198.0*ct1)
x2=mubfrg*cmu1/(201.0*ct2)
line_FRG_T160,=ax1.plot(mubfrg*cmu/(200.0*ct),R62200,'--',dashes=(1,2),color='k',linewidth=1.5,alpha=0.5)
xsame=np.linspace(0.,1.2,100)
power1=spline(x1,R62198,xsame)
power2=spline(x2,R62201,xsame)
band_FRG_T160=ax1.fill_between(xsame,power1,power2,alpha=0.4,facecolor='m',edgecolor='',zorder=12,label=r'This work T=160 MeV')
x3=mubfrg*cmu2/(193.0*ct1)
x4=mubfrg*cmu1/(196.0*ct2)
line_FRG_T155,=ax1.plot(mubfrg*cmu/(195.0*ct),R62195,'--',dashes=(5,2),color='k',linewidth=1.5,alpha=0.5)#,label=r'This work T=155 MeV')
xsame2=np.linspace(0.,1.2,100)
power3=spline(x3,R62193,xsame2)
power4=spline(x4,R62196,xsame2)
band_FRG_T155=ax1.fill_between(xsame2,power3,power4,alpha=0.4,facecolor='r',edgecolor='',zorder=11,label=r'This work T=155 MeV')


#ax1.plot(mubfrg*cmu/(200.0*ct),R62200,'-',color='b',linewidth=1,alpha=0.5)#,label=r'This work T=160 MeV')
#ax1.plot(mubfrg*cmu/(194.0*ct),R62194,'-',color='k',linewidth=1,alpha=0.5)#,label=r'This work T=155 MeV')
#ax1.fill_betweenx(R62200,mubfrg*cmu1/(200.0*ct1),mubfrg*cmu2/(200.0*ct2),alpha=0.5,facecolor='b',edgecolor='',label=r'This work T=160 MeV')
#ax1.fill_betweenx(R62194,mubfrg*cmu1/(194.0*ct1),mubfrg*cmu2/(194.0*ct2),alpha=0.5,facecolor='k',edgecolor='',label=r'This work T=155 MeV')





#ax1.plot(mub/155,R12[:,50],'k-',linewidth=2,markersize=5,label=r'$T$')
#ax1.errorbar(mub/155.,R62[:,50],yerr=errR62[:,50],color='blue',marker='o',linestyle='',linewidth=2,markersize=2,fillstyle='none',alpha=1,label=r'HotQCD  T=155')
#ax1.errorbar(mub/158.,R62[:,56],yerr=errR62[:,56],color='red',marker='o',linestyle='',linewidth=2,markersize=2,fillstyle='none',alpha=1,label=r'HotQCD  T=158')
band_HotQCD_T160=ax1.fill_between(mub/160.,R62[:,60]-errR622[:,60],R62[:,60]+errR622[:,60],alpha=0.4,facecolor='c',edgecolor='',label=r'HotQCD T=160 MeV')
band_HotQCD_T155=ax1.fill_between(mub/155.,R62[:,50]-errR622[:,50],R62[:,50]+errR622[:,50],alpha=0.4,facecolor='green',edgecolor='',label=r'HotQCD T=155 MeV')
band_WB_T160=ax1.fill_between(mub/160.,WBR62[:,5]-WBerrR622[:,5],WBR62[:,5]+WBerrR622[:,5],alpha=0.4,facecolor=(0.8,0.5,0),edgecolor='',label=r'WB T=160 MeV')

band_WB_T155=ax1.fill_between(mub/155.,WBR62[:,4]-WBerrR622[:,4],WBR62[:,4]+WBerrR622[:,4],alpha=0.4,facecolor='b',edgecolor='',label=r'WB T=155 MeV')

ax1.axis([0,0.8,-3,1.])

ax1.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax1.set_ylabel('$R^B_{62}$', fontsize=14, color='black')

ax1.legend(((band_FRG_T155,line_FRG_T155),(band_FRG_T160,line_FRG_T160),band_HotQCD_T155,band_HotQCD_T160,band_WB_T155,band_WB_T160),(r'This work $T=155$ MeV',r'This work $T=160$ MeV',r'HotQCD $T=155$ MeV',r'HotQCD $T=160$ MeV',r'WB $T=155$ MeV',r'WB $T=160$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("R62-muBoT.pdf")

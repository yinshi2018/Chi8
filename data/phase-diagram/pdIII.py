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
#muB=np.loadtxt('CEP/muB.dat')
#T_low=np.loadtxt('CEP/Tlow.dat')
#T_high=np.loadtxt('CEP/Thigh.dat')
#muB_CEP=np.loadtxt('CEP/CEPmuB.dat')
#T_CEP=np.loadtxt('CEP/CEPT.dat')
muB=np.loadtxt('Nf2p1/CEP/muB.dat')


muB_Nf2p1=np.loadtxt('Nf2p1/CEP/muB.dat')
pb_Nf2p1=np.loadtxt('Nf2p1/CEP/pb-Nf2p1.dat')
Tc_Nf2p1=np.loadtxt('Nf2p1/CEP/Tc.dat')
Unit_Nf2p1=1.

muB_CEP_Nf2p1=np.loadtxt('Nf2p1/CEP/CEPmuB.dat')
T_CEP_Nf2p1=np.loadtxt('Nf2p1/CEP/CEPT.dat')

pb_Zphip0_minus=np.loadtxt('Nf2p1/CEP/Zphip0-minus.dat')
pb_inhom=np.loadtxt('Nf2p1/CEP/inhomo-80.dat')
pb_Zphip0_minus_min=np.loadtxt('Nf2p1/CEP/Zphip0-minus-min.dat')


# Wuppertal-Budapest
pd_WB=np.loadtxt('WB/pd_data.dat')

# HotQCD
Tc0_Hot=156.5
kappa2_Hot=0.012
kappa4_Hot=0.
dTc0_Hot=1.5
dkappa2_Hot=0.004
dkappa4_Hot=0.004

Ns_Hot=101
muB_Hot=np.linspace(0.,300.,Ns_Hot)
TcFun_Hot=np.zeros(Ns_Hot,dtype=float)
dTcFun_Hot=np.zeros(Ns_Hot,dtype=float)

for i in range(Ns_Hot):
    TcFun_Hot[i]=Tc0_Hot*(1.-kappa4_Hot*muB_Hot[i]**4/Tc0_Hot**4
                          -kappa2_Hot*muB_Hot[i]**2/Tc0_Hot**2)
    dTcFun_Hot[i]=(dkappa4_Hot**2*muB_Hot[i]**8*Tc0_Hot**2+dkappa2_Hot**2*muB_Hot[i]**4*Tc0_Hot**6
                   +dTc0_Hot**2*(3.*kappa4_Hot*muB_Hot[i]**4+kappa2_Hot*muB_Hot[i]**2*Tc0_Hot**2
                                 +Tc0_Hot**4)**2)**0.5/Tc0_Hot**4

# Fischer
pd_Fischer=np.loadtxt('Fischer/cross.dat')
CEP_Fischer=np.loadtxt('Fischer/CEP.dat')

# Gao
pd_Gao1=np.loadtxt('Gao/cross1.dat')
CEP_Gao1=np.loadtxt('Gao/CEP1.dat')
pd_Gao2=np.loadtxt('Gao/cross2.dat')
CEP_Gao2=np.loadtxt('Gao/CEP2.dat')

#freeze out data (star)
freeze_star=np.loadtxt('freeze-out/star.dat')

#freeze out data (alba)
freeze_alba=np.loadtxt('freeze-out/alba.dat')

#freeze out data (becattini)
freeze_becattini=np.loadtxt('freeze-out/becattini.dat')
freeze_becattini2=np.loadtxt('freeze-out/becattini2.dat')

#freeze out data (vovchenko)
freeze_vovchenko=np.loadtxt('freeze-out/vovchenko/vovchenko.dat')

#freeze out data (andronic)
freeze_andronic=np.loadtxt('freeze-out/andronic/andronic.dat')

#freeze out data (Sagun)
freeze_Sagun=np.loadtxt('freeze-out/Sagun/Sagun.dat')


# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
#ax1=plt.subplot(111)

#band_FRG2p1=ax1.fill_between(pb_Nf2p1[:,0]*Unit_Nf2p1,pb_Nf2p1[:,1]*Unit_Nf2p1,pb_Nf2p1[:,2]*Unit_Nf2p1,color='blue',alpha=0.4,label=r'FRG $N_f=2+1$')
line_FRG2p1,=ax1.plot(pb_Nf2p1[:,0],Tc_Nf2p1,'k--',dashes=(5,2),linewidth=1.5,markersize=5,zorder=5,label=r'FRG: $N_f=2+1$')
CEP_FRG2p1,=ax1.plot(muB_CEP_Nf2p1,T_CEP_Nf2p1,'ko',zorder=5,markersize=8)

band_Zphip0_minus=ax1.fill_between(pb_Zphip0_minus[:,0],pb_Zphip0_minus[:,1],pb_Zphip0_minus[:,2],color='blue',alpha=0.3,label=r'FRG: $Z_\phi<0$')

band_inhom=ax1.fill_between(pb_inhom[:,0],pb_inhom[:,1],pb_inhom[:,2],color='',alpha=0.8,hatch='///////',edgecolor='red',zorder=4,label=r'FRG: inhom')

line_Zphip0_minus_min,=ax1.plot(pb_Zphip0_minus_min[:,0],pb_Zphip0_minus_min[:,2],'b-.',linewidth=1.5,markersize=5,label=r'FRG: $Z_\phi<0$')


ax1.plot(muB,muB/2.,'k:',linewidth=1.,markersize=5)
ax1.plot(muB,muB/3.,'k:',linewidth=1.,markersize=5)
ax1.text(70, 110, r'$\mu_B/T=2$',fontsize=10, color='k')
ax1.text(350, 110, r'$\mu_B/T=3$',fontsize=10, color='k')

#print(muB_CEP_Nf2p1*Unit_Nf2p1)
#print(T_CEP_Nf2p1*Unit_Nf2p1)

#ax1.plot(pd_WB[...,0],pd_WB[...,1],'r-',linewidth=1,markersize=5,label='WB')
#band_WB=ax1.fill_between(pd_WB[...,0],pd_WB[...,1]-pd_WB[...,2],pd_WB[...,1]+pd_WB[...,3],alpha=0.5,hatch='///////',facecolor='green',edgecolor='black',label=r'Lattice: WB')

#band_HotQCD=ax1.fill_between(muB_Hot,TcFun_Hot-dTcFun_Hot,TcFun_Hot+dTcFun_Hot,color=(0.8,0.5,0),alpha=0.5,label=r'Lattice: HotQCD')


#line_Fischer,=ax1.plot(pd_Fischer[...,0],pd_Fischer[...,1],'r-.',linewidth=1.5,markersize=5,label=r'DSE: Fischer et al.')
#ax1.plot(CEP_Fischer[...,0],CEP_Fischer[...,1],'rD',markersize=5)

#line_Gao,=ax1.plot(pd_Gao1[...,0],pd_Gao1[...,1],'m:',linewidth=1.5,markersize=5,label=r'DSE: Gao et al.')
#ax1.plot(CEP_Gao1[...,0],CEP_Gao1[...,1],'mv',markersize=5)

#ax1.plot(pd_Gao2[...,0],pd_Gao2[...,1],'m:',linewidth=1,markersize=5,label=r'DSE: Gao and Liu')
#ax1.plot(CEP_Gao2[...,0],CEP_Gao2[...,1],'m^',markersize=5)

#freeze out data
points_star=ax1.errorbar(freeze_star[...,1],freeze_star[...,3],yerr=freeze_star[...,4],xerr=freeze_star[...,2],fmt='cs',ecolor='c',markersize=5,alpha=0.8,label=r'freezeout: STAR')

points_alba=ax1.errorbar(freeze_alba[...,1],freeze_alba[...,3],yerr=freeze_alba[...,4],xerr=freeze_alba[...,2],fmt='y<',ecolor='y',markersize=5,alpha=0.8,label=r'freezeout: Alba et al.')

points_becattini=ax1.errorbar(freeze_becattini[...,1],freeze_becattini[...,3],yerr=freeze_becattini[...,4],xerr=freeze_becattini[...,2],color=(0.5,0.5,0),marker='>',linestyle='',ecolor=(0.5,0.5,0),markersize=5,alpha=0.8,label=r'freezeout: Becattini et al.')

points_becattini2=ax1.errorbar(freeze_becattini2[...,1],freeze_becattini2[...,3],yerr=freeze_becattini2[...,4],xerr=freeze_becattini2[...,2],color='#1089CF',marker='>',linestyle='',ecolor='#1089CF',markersize=5,alpha=0.6,label=r'freezeout: Becattini et al.')

points_vovchenko=ax1.errorbar(freeze_vovchenko[...,3],freeze_vovchenko[...,0],yerr=[freeze_vovchenko[...,2],freeze_vovchenko[...,1]],xerr=[freeze_vovchenko[...,5],freeze_vovchenko[...,4]],color=(0.5,0.8,0),marker='p',linestyle='',ecolor=(0.5,0.8,0),markersize=5,alpha=0.5,label=r'freezeout: Vovchenko et al.')

points_andronic=ax1.errorbar(freeze_andronic[...,2],freeze_andronic[...,1],yerr=[freeze_andronic[...,4],freeze_andronic[...,5]],xerr=[freeze_andronic[...,6],freeze_andronic[...,7]],color=(0.8,0.4,0.4),marker='h',linestyle='',ecolor=(0.8,0.4,0.4),markersize=5,alpha=0.5,label=r'freezeout: Andronic et al.')

points_Sagun=ax1.errorbar(freeze_Sagun[:,4],freeze_Sagun[:,1],yerr=[freeze_Sagun[:,3],freeze_Sagun[:,2]],xerr=[freeze_Sagun[:,6],freeze_Sagun[:,5]],color='blue',marker='H',linestyle='',ecolor='blue',markersize=5,alpha=0.5,label=r'freezeout: Andronic et al.')


ax1.axis([0,1000,0,180])
#ax1.set_xscale('log')

ax1.set_xlabel(r'$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$T\,[\mathrm{MeV}]$', fontsize=14, color='black')

#ax1.legend(handles=[line_FRG2p1,band_WB,band_HotQCD,line_Fischer,line_Gao,points_star,points_alba,points_andronic,points_becattini,points_vovchenko],loc=3,fontsize='xx-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax1.legend((line_FRG2p1,band_inhom,(band_Zphip0_minus,line_Zphip0_minus_min),points_star,points_alba,points_andronic,points_becattini,points_vovchenko,points_Sagun),(r'FRG: $N_f=2+1$',r'FRG: inhom',r'FRG: $Z_\phi<0$',r'freezeout: STAR',r'freezeout: Alba et al.',r'freezeout: Andronic et al.',r'freezeout: Becattini et al.',r'freezeout: Vovchenko et al.',r'freezeout: Sagun et al.'),loc=3,fontsize='xx-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)


#for ax in fig.axes:
#    ax.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
#plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.15, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("phasediagramIII.pdf")

#plt.show()

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

muB=np.loadtxt('Nf2p1/CEP/muB.dat')

pb_Nf2p1=np.loadtxt('Nf2p1/CEP/pb-Nf2p1.dat')
Tc_Nf2p1=np.loadtxt('Nf2p1/CEP/Tc.dat')

muB_CEP_Nf2p1=np.loadtxt('Nf2p1/CEP/CEPmuB.dat')
T_CEP_Nf2p1=np.loadtxt('Nf2p1/CEP/CEPT.dat')

pb_Nf2=np.loadtxt('Nf2/CEP/pb-Nf2.dat')
Tc_Nf2=np.loadtxt('Nf2/CEP/Tc.dat')

muB_CEP_Nf2=np.loadtxt('Nf2/CEP/CEPmuB.dat')
T_CEP_Nf2=np.loadtxt('Nf2/CEP/CEPT.dat')


# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
#ax1=plt.subplot(111)

line_Nf2,=ax1.plot(pb_Nf2[:,0],Tc_Nf2,'r--',linewidth=1.5,markersize=5,zorder=1,label=r'$N_f=2$')
CEP_Nf2,=ax1.plot(muB_CEP_Nf2,T_CEP_Nf2,'r*',markersize=8,label=r'CEP: $N_f=2$')
band_Nf2=ax1.fill_between(pb_Nf2[:,0],pb_Nf2[:,1],pb_Nf2[:,2],color='gray',alpha=.4,label=r'$N_f=2$')


line_Nf2p1,=ax1.plot(pb_Nf2p1[:,0],Tc_Nf2p1,'k--',dashes=(5,2),linewidth=1.5,markersize=5,zorder=5,label=r'$N_f=2+1$')
CEP_Nf2p1,=ax1.plot(muB_CEP_Nf2p1,T_CEP_Nf2p1,'ko',markersize=8,label=r'CEP: $N_f=2+1$')
band_Nf2p1=ax1.fill_between(pb_Nf2p1[:,0],pb_Nf2p1[:,1],pb_Nf2p1[:,2],color='blue',alpha=0.4,label=r'$N_f=2+1$')



ax1.plot(muB,muB/2.,'k:',linewidth=1.,markersize=5)
ax1.plot(muB,muB/3.,'k:',linewidth=1.,markersize=5)
ax1.text(90, 100, r'$\frac{\mu_B}{T}=2$',fontsize=10, color='k')
ax1.text(340, 100, r'$\frac{\mu_B}{T}=3$',fontsize=10, color='k')
ax1.axis([0,1000,0,200])
#ax1.set_xscale('log')

ax1.set_xlabel(r'$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$T\,[\mathrm{MeV}]$', fontsize=14, color='black')

ax1.legend(((band_Nf2,line_Nf2),(band_Nf2p1,line_Nf2p1),CEP_Nf2,CEP_Nf2p1),(r'$N_f=2$',r'$N_f=2+1$',r'CEP: $N_f=2$',r'CEP: $N_f=2+1$'),loc=4,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

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


fig.savefig("phasediagram.pdf")

#plt.show()

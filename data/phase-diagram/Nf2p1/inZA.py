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
r=1.e3

k_T1_muB0=np.loadtxt('T-muB/T1-muB0/kMeV.dat')
ZA_T1_muB0=np.loadtxt('T-muB/T1-muB0/ZA.dat')
inZA_T1_muB0=1/ZA_T1_muB0
GA_T1_muB0=1/(ZA_T1_muB0*k_T1_muB0**2)*r**2

k_T150_muB0=np.loadtxt('T-muB/T158-muB0/kMeV.dat')
ZA_T150_muB0=np.loadtxt('T-muB/T158-muB0/ZA.dat')
inZA_T150_muB0=1/ZA_T150_muB0
GA_T150_muB0=1/(ZA_T150_muB0*k_T150_muB0**2)*r**2

k_T200_muB0=np.loadtxt('T-muB/T210-muB0/kMeV.dat')
ZA_T200_muB0=np.loadtxt('T-muB/T210-muB0/ZA.dat')
inZA_T200_muB0=1/ZA_T200_muB0
GA_T200_muB0=1/(ZA_T200_muB0*k_T200_muB0**2)*r**2

k_T280_muB0=np.loadtxt('T-muB/T294-muB0/kMeV.dat')
ZA_T280_muB0=np.loadtxt('T-muB/T294-muB0/ZA.dat')
inZA_T280_muB0=1/ZA_T280_muB0
GA_T280_muB0=1/(ZA_T280_muB0*k_T280_muB0**2)*r**2

Unit_Nf2p1=0.951599

# Create figure
fig=plt.figure(figsize=(9., 3.5))
ax1=fig.add_subplot(121)

ax1.plot(k_T1_muB0*Unit_Nf2p1,inZA_T1_muB0,'k-',linewidth=2,markersize=5,label=r'$T=0$')
ax1.plot(k_T150_muB0*Unit_Nf2p1,inZA_T150_muB0,'r--',linewidth=2,markersize=5,label=r'$T=150\,\mathrm{MeV}$')
ax1.plot(k_T200_muB0*Unit_Nf2p1,inZA_T200_muB0,'b-.',linewidth=2,markersize=5,label=r'$T=200$')
ax1.plot(k_T280_muB0*Unit_Nf2p1,inZA_T280_muB0,'g:',linewidth=2,markersize=5,label=r'$T=280$')
ax1.axis([10,20000,0,3])
ax1.set_xscale('log')

ax1.set_xlabel('$k\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$1/Z_A$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)


# Plot two
ax2=fig.add_subplot(122)

ax2.plot(k_T1_muB0*Unit_Nf2p1,GA_T1_muB0/Unit_Nf2p1**2,'k-',linewidth=2,markersize=5,label=r'$T=0$')
ax2.plot(k_T150_muB0*Unit_Nf2p1,GA_T150_muB0/Unit_Nf2p1**2,'r--',linewidth=2,markersize=5,label=r'$T=150\,\mathrm{MeV}$')
ax2.plot(k_T200_muB0*Unit_Nf2p1,GA_T200_muB0/Unit_Nf2p1**2,'b-.',linewidth=2,markersize=5,label=r'$T=200$')
ax2.plot(k_T280_muB0*Unit_Nf2p1,GA_T280_muB0/Unit_Nf2p1**2,'g:',linewidth=2,markersize=5,label=r'$T=300$')
ax2.axis([0.01,20000,0,8])
ax2.set_xscale('log')

ax2.set_xlabel('$k\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$G_A\,[{\mathrm{GeV}}^{-2}]$', fontsize=14, color='black')

#ax2.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)

#for ax in fig.axes:
#    ax.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
#plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.10, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("inZA.pdf")

#plt.show()

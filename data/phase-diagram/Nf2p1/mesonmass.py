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
T=np.loadtxt('muB-Tto300/muB0/TMeV.dat')

mPion0=np.loadtxt('muB-Tto300/muB0/mPion.dat')
mSigma0=np.loadtxt('muB-Tto300/muB0/mSigma.dat')
mPion400=np.loadtxt('muB-Tto300/muB420/mPion.dat')
mSigma400=np.loadtxt('muB-Tto300/muB420/mSigma.dat')
mPion560=np.loadtxt('muB-Tto300/muB589/mPion.dat')
mSigma560=np.loadtxt('muB-Tto300/muB589/mSigma.dat')

Unit_Nf2p1=0.951599

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.plot(T*Unit_Nf2p1,mPion0*Unit_Nf2p1,'b-.',linewidth=2,markersize=5,label=r'$\mu_B=0$')
ax1.plot(T*Unit_Nf2p1,mSigma0*Unit_Nf2p1,'b-.',linewidth=1,markersize=5)
ax1.plot(T*Unit_Nf2p1,mPion400*Unit_Nf2p1,'r--',linewidth=2,markersize=5,label=r'$\mu_B=400\,\mathrm{MeV}$')
ax1.plot(T*Unit_Nf2p1,mSigma400*Unit_Nf2p1,'r--',linewidth=1,markersize=5)
ax1.plot(T*Unit_Nf2p1,mPion560*Unit_Nf2p1,'k-',linewidth=2,markersize=5,label=r'$\mu_B=560$')
ax1.plot(T*Unit_Nf2p1,mSigma560*Unit_Nf2p1,'k-',linewidth=1,markersize=5)
ax1.text(20, 160, r'$m_{\pi}$',fontsize=10, color='m')
ax1.text(20, 580, r'$m_{\sigma}$',fontsize=10, color='m')
ax1.axis([0,300,100,10000])
ax1.set_yscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$m\,[\mathrm{MeV}]$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

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


fig.savefig("mesonmass.pdf")

#plt.show()

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

Zpsi_muB0=np.loadtxt('muB-Tto300/muB0/Zpsi.dat')
Zphi_muB0=np.loadtxt('muB-Tto300/muB0/Zphi.dat')

Zpsi_muB400=np.loadtxt('muB-Tto300/muB420/Zpsi.dat')
Zphi_muB400=np.loadtxt('muB-Tto300/muB420/Zphi.dat')

Zpsi_muB560=np.loadtxt('muB-Tto300/muB589/Zpsi.dat')
Zphi_muB560=np.loadtxt('muB-Tto300/muB589/Zphi.dat')

Unit_Nf2p1=0.951599

# Create figure
fig=plt.figure(figsize=(9., 3.5))
ax1=fig.add_subplot(121)

ax1.plot(T*Unit_Nf2p1,Zpsi_muB0,'k-',linewidth=2,markersize=5,label=r'$\mu_B=0$')
ax1.plot(T*Unit_Nf2p1,Zpsi_muB400,'r--',linewidth=2,markersize=5,label=r'$\mu_B=400\,\mathrm{MeV}$')
ax1.plot(T*Unit_Nf2p1,Zpsi_muB560,'b-.',linewidth=2,markersize=5,label=r'$\mu_B=560$')
#ax1.axis([0,300,1.1,1.5])
#ax1.set_xscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$Z_{q,k=0}/Z_{q,k=\Lambda}$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)


# Plot two
ax2=fig.add_subplot(122)

ax2.plot(T*Unit_Nf2p1,Zphi_muB0,'k-',linewidth=2,markersize=5,label=r'$\mu_B=0$')
ax2.plot(T*Unit_Nf2p1,Zphi_muB400,'r--',linewidth=2,markersize=5,label=r'$\mu_B=400\,\mathrm{MeV}$')
ax2.plot(T*Unit_Nf2p1,Zphi_muB560,'b-.',linewidth=2,markersize=5,label=r'$\mu_B=560$')
ax2.axis([0,300,5*10**4,10**7])
ax2.set_yscale('log')

ax2.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$Z_{\phi,k=0}/Z_{\phi,k=\Lambda}$', fontsize=14, color='black')

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


fig.savefig("Zpsi.pdf")

#plt.show()

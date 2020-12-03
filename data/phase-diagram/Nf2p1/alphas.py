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
k_T1_muB0=np.loadtxt('T-muB/T1-muB0/kMeV.dat')
alphaS_T1_muB0=np.loadtxt('T-muB/T1-muB0/alphaS.dat')
alphaS3A_T1_muB0=np.loadtxt('T-muB/T1-muB0/alphaS3A.dat')
alphaSqbAqs_T1_muB0=np.loadtxt('T-muB/T1-muB0/alphaSqbAq_s.dat')

k_T150_muB0=np.loadtxt('T-muB/T158-muB0/kMeV.dat')
alphaS_T150_muB0=np.loadtxt('T-muB/T158-muB0/alphaS.dat')
alphaS3A_T150_muB0=np.loadtxt('T-muB/T158-muB0/alphaS3A.dat')
alphaSqbAqs_T150_muB0=np.loadtxt('T-muB/T158-muB0/alphaSqbAq_s.dat')


k_T280_muB0=np.loadtxt('T-muB/T294-muB0/kMeV.dat')
alphaS_T280_muB0=np.loadtxt('T-muB/T294-muB0/alphaS.dat')
alphaS3A_T280_muB0=np.loadtxt('T-muB/T294-muB0/alphaS3A.dat')
alphaSqbAqs_T280_muB0=np.loadtxt('T-muB/T294-muB0/alphaSqbAq_s.dat')

Unit_Nf2p1=0.951599

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.plot(k_T1_muB0*Unit_Nf2p1,alphaS_T1_muB0,'k-',linewidth=2,markersize=5,label=r'$T=0,\,\alpha_{\bar q A q}$')
ax1.plot(k_T150_muB0*Unit_Nf2p1,alphaS_T150_muB0,'k--',linewidth=2,markersize=5,label=r'$T=150,\,\alpha_{\bar q A q}$')
ax1.plot(k_T280_muB0*Unit_Nf2p1,alphaS_T280_muB0,'k:',linewidth=2,markersize=5,label=r'$T=280,\,\alpha_{\bar q A q}$')
ax1.plot(k_T1_muB0*Unit_Nf2p1,alphaSqbAqs_T1_muB0,'r-',linewidth=1,markersize=5,label=r'$T=0,\,\alpha_{\bar s A s}$')
ax1.plot(k_T150_muB0*Unit_Nf2p1,alphaSqbAqs_T150_muB0,'r--',linewidth=1,markersize=5,label=r'$T=150,\,\alpha_{\bar s A s}$')
ax1.plot(k_T280_muB0*Unit_Nf2p1,alphaSqbAqs_T280_muB0,'r:',linewidth=1,markersize=5,label=r'$T=280,\,\alpha_{\bar s A s}$')
ax1.plot(k_T1_muB0*Unit_Nf2p1,alphaS3A_T1_muB0,'b-',linewidth=1.5,markersize=5,label=r'$T=0,\,\alpha_{A^3}$')
ax1.plot(k_T150_muB0*Unit_Nf2p1,alphaS3A_T150_muB0,'b--',linewidth=1.5,markersize=5,label=r'$T=150,\,\alpha_{A^3}$')
ax1.plot(k_T280_muB0*Unit_Nf2p1,alphaS3A_T280_muB0,'b:',linewidth=1.5,markersize=5,label=r'$T=280,\,\alpha_{A^3}$')
#ax1.text(20, 1, r'$\mu_B=0$',fontsize=10, color='m')
ax1.axis([10,20000,0,2.5])
ax1.set_xscale('log')

ax1.set_xlabel('$k\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\alpha_s$', fontsize=14, color='black')

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


fig.savefig("alphas.pdf")

#plt.show()

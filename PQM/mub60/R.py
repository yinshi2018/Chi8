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
chi2=np.loadtxt(r'chi2.dat')
chi4=np.loadtxt(r'chi4.dat')
chi6=np.loadtxt(r'chi6.dat')
chi8=np.loadtxt(r'chi8.dat')
r42=chi4/chi2
r62=chi6/chi2
r82=chi8/chi2
# Create figure
fig=plt.figure(figsize=(13., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
ax1.plot(r42,'k-',linewidth=1,markersize=5,label=r'$\chi_4/\chi_2$')
ax1.axis([80,300,0,1.2])
#ax1.set_xscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(132)
ax2.plot(r62,color='k',linestyle='-',linewidth=1,markersize=5,label=r'$\chi_6/\chi_2$')
ax2.axis([80,300,-0.5,1.2])
#ax2.set_xscale('log')

ax2.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(133)
ax3.plot(r82,color='k',linestyle='-',linewidth=1,markersize=5,label=r'$\chi_8/\chi_2$')
ax3.axis([80,300,-2.5,2])
#ax2.set_xscale('log')

ax3.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

ax3.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax3.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(10)

#for ax in fig.axes:
#    ax.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
#plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.05, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("r.pdf")

#plt.show()

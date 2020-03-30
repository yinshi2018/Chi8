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
kur=np.loadtxt(r'./kur.dat')
s=np.loadtxt(r'./sqrts.dat')
expkur=np.loadtxt(r'./expkur.dat')
err=np.loadtxt(r'./expkurerr.dat')


# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(s,expkur,marker='o',color='red',markersize=1,linewidth=1)#,label=r'$\mathrm{PQM}$')
ax1.errorbar(s,expkur,yerr=err,color='red',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'STAR  0-5%')
ax1.plot(s,kur,marker='^',linewidth=1,label=r'$\mathrm{PQM}$')

ax1.axis([7,210,-3,3])
ax1.set_xscale('log')

ax1.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

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
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.14, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("finmub.pdf")

#plt.show()

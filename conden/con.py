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
T=np.loadtxt('./TMeV.dat')
dRl=np.loadtxt('./deltaRlat.dat')
dRf=np.loadtxt('./deltaR.dat')
n=335100625
dRf1=dRf/n


T1=T/225

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.plot(T1,dRf1,'k-',linewidth=2,markersize=5,label=r'$FRG,Tc=270,\alpha=0.7$')
ax1.errorbar(dRl[:,0]/156,dRl[:,1],yerr=dRl[:,2],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax1.axis([0.5,1.7,0.,0.5])

ax1.set_xlabel('$T [\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$\Delta_{l,R}$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.17, left=0.15, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("d2.pdf")

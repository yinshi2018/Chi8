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
T=np.loadtxt('./source/buffer/TMeV.dat')
dRl=np.loadtxt('./deltaRlat.dat')
dRfeqcd=np.loadtxt('./source/buffer/delta_lR.dat')
dRfeqcd400=np.loadtxt('./eQCDmub400/buffer/delta_lR.dat')
dRfpqm=np.loadtxt('./PQM/mub0/buffer/delta_lR.dat')
dRfpqm400=np.loadtxt('./PQM/mub400/buffer/delta_lR.dat')
neqcd=12.3
dRfeqcd1=dRfeqcd/neqcd
dRfeqcd2=dRfeqcd400/neqcd
npqm=20
dRfpqm1=dRfpqm/npqm
dRfpqm2=dRfpqm400/npqm

T1=T/156
T2=T/213
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.plot(T1,dRfeqcd1,'k-',linewidth=2,markersize=5,label=r'$EASY\,\,QCD\quad \mu_B=0\,MeV$')
ax1.plot(T2,dRfpqm1,'r-',linewidth=1.5,markersize=5,label=r'$PQM\quad \mu_B=0\,MeV$')
ax1.plot(T1,dRfeqcd2,'k--',linewidth=2,markersize=5,label=r'$EASY\,\,QCD\quad \mu_B=400\,MeV$')
ax1.plot(T2,dRfpqm2,'r--',linewidth=1.5,markersize=5,label=r'$PQM\quad \mu_B=400\,MeV$')

ax1.errorbar(dRl[:,0]/156,dRl[:,1],yerr=dRl[:,2],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax1.axis([0,1.7,0.,0.5])

ax1.set_xlabel('$T/T_c [\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$\Delta_{l,R}$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.17, left=0.15, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("d2.pdf")

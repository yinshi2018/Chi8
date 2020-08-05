#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl
from scipy.interpolate import spline

mpl.style.use('classic')
#t = np.linspace(50, 160, 100)
muB = np.linspace(1, 800, 100)
# print(x, y)
T=np.zeros(100)
#muB= np.meshgrid(mub)
T = 158.4/(1.+np.exp(2.6-np.log(1307.5/(muB*0.288)-1./0.288)/0.45))
# Data for plotting
expdata=np.loadtxt('./andronic-origin.dat')
paradata=np.loadtxt('./paradata.dat')
intdata=np.loadtxt('./intdata.dat')
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
exppoint=ax1.errorbar(expdata[:,2],expdata[:,1],xerr=[expdata[:,6],expdata[:,7]],yerr=[expdata[:,4],expdata[:,5]],color='r',marker='s',linestyle='',linewidth=1,markersize=5,fillstyle='full',label=r'Experiment',zorder=1)
expline,=ax1.plot(expdata[:,2],expdata[:,1],color='r',zorder=1)
#paraline,=ax1.plot(muB, T,label=r'Parameterization')
parapoint=ax1.scatter(paradata[:,0],paradata[:,1],color='b',label=r'Freeze-out',zorder=2)
intpoint=ax1.scatter(intdata[:,0],intdata[:,1],color='g',zorder=3)
ax1.axis([0,600,100,200])

ax1.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')

#ax1.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

ax1.legend((parapoint,(exppoint,expline),intpoint),(r'Parameterization',r'Experiment',r'Interpolation'),loc=2,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("Phase.pdf")

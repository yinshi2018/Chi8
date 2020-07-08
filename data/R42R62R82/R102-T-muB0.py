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

# Data for plotting
chi10=np.loadtxt('../mub0/final/buffer/chi10.dat')
chi8=np.loadtxt('../mub0/final/buffer/chi8.dat')
chi6=np.loadtxt('../mub0/final/buffer/chi6.dat')
chi4=np.loadtxt('../mub0/final/buffer/chi4.dat')
chi2=np.loadtxt('../mub0/final/buffer/chi2.dat')
r42=chi4/chi2
r62=chi6/chi2
r82=chi8/chi2
r102=chi10/chi2
ctcen=1.247
ctdown=1.235
ctup=1.259
r102m=np.zeros((300,10))
xsame=np.linspace(0.,300.,300)
ct=np.linspace(ctdown,ctup,10)
Tfrg=np.loadtxt('./TMeV.dat')
for t in range(0,10):
    r102m[:,t]=spline(Tfrg/ct[t],r102,xsame)

for num in range(1,10):
    if num==1:
       max102=np.maximum(r102m[:,num-1],r102m[:,num])
       min102=np.minimum(r102m[:,num-1],r102m[:,num])
    else:
       max102=np.maximum(max102,r102m[:,num])
       min102=np.minimum(min102,r102m[:,num])
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
band_FRG=ax1.fill_between(xsame,max102,min102,alpha=0.25,facecolor='r',edgecolor='r',label=r'This work')
line_FRG,=ax1.plot(Tfrg/ctcen,r102,'-',color='r',linewidth=1,alpha=0.5)

ax1.axis([80,220,-23,20])

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$R^B_{10,2}$', fontsize=14, color='black')

#ax1.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

ax1.legend(((band_FRG,line_FRG),),(r'This work',),loc=2,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("R102-muBoT.pdf")

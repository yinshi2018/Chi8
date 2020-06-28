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
T1=np.zeros((300,10))
chi2mub0=np.loadtxt(r'./mub0/final/buffer/chi2.dat')
chi4mub0=np.loadtxt(r'./mub0/final/buffer/chi4.dat')
chi6mub0=np.loadtxt(r'./mub0/final/buffer/chi6.dat')
chi8mub0=np.loadtxt(r'./mub0/final/buffer/chi8.dat')
r42mub0=chi4mub0/chi2mub0
r62mub0=chi6mub0/chi2mub0
r82mub0=chi8mub0/chi2mub0
#############################################################################
chi2mub20cen=np.loadtxt(r'./mub20/cmucen/final/buffer/chi2.dat')
chi4mub20cen=np.loadtxt(r'./mub20/cmucen/final/buffer/chi4.dat')
chi6mub20cen=np.loadtxt(r'./mub20/cmucen/final/buffer/chi6.dat')
chi8mub20cen=np.loadtxt(r'./mub20/cmucen/final/buffer/chi8.dat')
r42mub20cen=chi4mub20cen/chi2mub20cen
r62mub20cen=chi6mub20cen/chi2mub20cen
r82mub20cen=chi8mub20cen/chi2mub20cen
chi2mub20up=np.loadtxt(r'./mub20/cmuup/final/buffer/chi2.dat')
chi4mub20up=np.loadtxt(r'./mub20/cmuup/final/buffer/chi4.dat')
chi6mub20up=np.loadtxt(r'./mub20/cmuup/final/buffer/chi6.dat')
chi8mub20up=np.loadtxt(r'./mub20/cmuup/final/buffer/chi8.dat')
r42mub20up=chi4mub20up/chi2mub20up
r62mub20up=chi6mub20up/chi2mub20up
r82mub20up=chi8mub20up/chi2mub20up
chi2mub20down=np.loadtxt(r'./mub20/cmudown/final/buffer/chi2.dat')
chi4mub20down=np.loadtxt(r'./mub20/cmudown/final/buffer/chi4.dat')
chi6mub20down=np.loadtxt(r'./mub20/cmudown/final/buffer/chi6.dat')
chi8mub20down=np.loadtxt(r'./mub20/cmudown/final/buffer/chi8.dat')
r42mub20down=chi4mub20down/chi2mub20down
r62mub20down=chi6mub20down/chi2mub20down
r82mub20down=chi8mub20down/chi2mub20down
############################################################################
chi2mub100cen=np.loadtxt(r'./mub100/cmucen/final/buffer/chi2.dat')
chi4mub100cen=np.loadtxt(r'./mub100/cmucen/final/buffer/chi4.dat')
chi6mub100cen=np.loadtxt(r'./mub100/cmucen/final/buffer/chi6.dat')
chi8mub100cen=np.loadtxt(r'./mub100/cmucen/final/buffer/chi8.dat')
r42mub100cen=chi4mub100cen/chi2mub100cen
r62mub100cen=chi6mub100cen/chi2mub100cen
r82mub100cen=chi8mub100cen/chi2mub100cen
chi2mub100up=np.loadtxt(r'./mub100/cmuup/final/buffer/chi2.dat')
chi4mub100up=np.loadtxt(r'./mub100/cmuup/final/buffer/chi4.dat')
chi6mub100up=np.loadtxt(r'./mub100/cmuup/final/buffer/chi6.dat')
chi8mub100up=np.loadtxt(r'./mub100/cmuup/final/buffer/chi8.dat')
r42mub100up=chi4mub100up/chi2mub100up
r62mub100up=chi6mub100up/chi2mub100up
r82mub100up=chi8mub100up/chi2mub100up
chi2mub100down=np.loadtxt(r'./mub100/cmudown/final/buffer/chi2.dat')
chi4mub100down=np.loadtxt(r'./mub100/cmudown/final/buffer/chi4.dat')
chi6mub100down=np.loadtxt(r'./mub100/cmudown/final/buffer/chi6.dat')
chi8mub100down=np.loadtxt(r'./mub100/cmudown/final/buffer/chi8.dat')
r42mub100down=chi4mub100down/chi2mub100down
r62mub100down=chi6mub100down/chi2mub100down
r82mub100down=chi8mub100down/chi2mub100down
r42100=np.zeros((300,20))
r62100=np.zeros((300,20))
r82100=np.zeros((300,20))
#################################################################################
chi2mub160cen=np.loadtxt(r'./mub160/cmucen/final/buffer/chi2.dat')
chi4mub160cen=np.loadtxt(r'./mub160/cmucen/final/buffer/chi4.dat')
chi6mub160cen=np.loadtxt(r'./mub160/cmucen/final/buffer/chi6.dat')
chi8mub160cen=np.loadtxt(r'./mub160/cmucen/final/buffer/chi8.dat')
r42mub160cen=chi4mub160cen/chi2mub160cen
r62mub160cen=chi6mub160cen/chi2mub160cen
r82mub160cen=chi8mub160cen/chi2mub160cen
chi2mub160up=np.loadtxt(r'./mub160/cmuup/final/buffer/chi2.dat')
chi4mub160up=np.loadtxt(r'./mub160/cmuup/final/buffer/chi4.dat')
chi6mub160up=np.loadtxt(r'./mub160/cmuup/final/buffer/chi6.dat')
chi8mub160up=np.loadtxt(r'./mub160/cmuup/final/buffer/chi8.dat')
r42mub160up=chi4mub160up/chi2mub160up
r62mub160up=chi6mub160up/chi2mub160up
r82mub160up=chi8mub160up/chi2mub160up
chi2mub160down=np.loadtxt(r'./mub160/cmudown/final/buffer/chi2.dat')
chi4mub160down=np.loadtxt(r'./mub160/cmudown/final/buffer/chi4.dat')
chi6mub160down=np.loadtxt(r'./mub160/cmudown/final/buffer/chi6.dat')
chi8mub160down=np.loadtxt(r'./mub160/cmudown/final/buffer/chi8.dat')
r42mub160down=chi4mub160down/chi2mub160down
r62mub160down=chi6mub160down/chi2mub160down
r82mub160down=chi8mub160down/chi2mub160down
r42160=np.zeros((300,20))
r62160=np.zeros((300,20))
r82160=np.zeros((300,20))
#####################################################################################
T=np.loadtxt(r'./TMeV.dat')
Tcen=T/1.247
Tup=T/1.259
Tdown=T/1.235
ctup=1.259
ctdown=1.235
ct=np.linspace(ctdown,ctup,10)
xsame=np.linspace(0.,300.,300)
# Create figure
fig=plt.figure(figsize=(13.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
band_mub0=ax1.fill_betweenx(r42mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=ax1.plot(Tcen,r42mub0,'r',linewidth=1,alpha=0.5)

#########################################################################################
for t in range(0,20):
    if t<10:
       r42100[:,t]=spline(T/ct[t],r42mub100up,xsame)
    else:
       r42100[:,t]=spline(T/ct[t-10],r42mub100down,xsame)


for num in range(1,20):
    if num==1:
       max100=np.maximum(r42100[:,num-1],r42100[:,num])
       min100=np.minimum(r42100[:,num-1],r42100[:,num])
    else:
       max100=np.maximum(max100,r42100[:,num])
       min100=np.minimum(min100,r42100[:,num])

band_mub100=ax1.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=ax1.plot(Tcen,r42mub100cen,'b',linewidth=1,alpha=0.5)


#########################################################################################
for t in range(0,20):
    if t<10:
       r42160[:,t]=spline(T/ct[t],r42mub160up,xsame)
    else:
       r42160[:,t]=spline(T/ct[t-10],r42mub160down,xsame)


for num in range(1,20):
    if num==1:
       max160=np.maximum(r42160[:,num-1],r42160[:,num])
       min160=np.minimum(r42160[:,num-1],r42160[:,num])
    else:
       max160=np.maximum(max160,r42160[:,num])
       min160=np.minimum(min160,r42160[:,num])

band_mub160=ax1.fill_between(xsame,max160,min160,alpha=0.25,facecolor='k',edgecolor='')
line_mub160,=ax1.plot(Tcen,r42mub160cen,'k',linewidth=1,alpha=0.5)



ax1.axis([80,230,0,1.2])
#ax1.set_xscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$R^B_{42}$', fontsize=14, color='black')

ax1.legend([(band_mub0,line_mub0),(band_mub100,line_mub100),(band_mub160,line_mub160)],[r'$\mu_B=0$',r'$\mu_B=100$ MeV',r'$\mu_B=160$ MeV'],loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)
#######################################################################################################################
ax2=fig.add_subplot(132)

band_mub0=ax2.fill_betweenx(r62mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=ax2.plot(Tcen,r62mub0,'r',linewidth=1,alpha=0.5)

###############################################################################################################
for t in range(0,20):
    if t<10:
       r62100[:,t]=spline(T/ct[t],r62mub100up,xsame)
    else:
       r62100[:,t]=spline(T/ct[t-10],r62mub100down,xsame)


for num in range(1,20):
    if num==1:
       max100=np.maximum(r62100[:,num-1],r62100[:,num])
       min100=np.minimum(r62100[:,num-1],r62100[:,num])
    else:
       max100=np.maximum(max100,r62100[:,num])
       min100=np.minimum(min100,r62100[:,num])

band_mub100=ax2.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=ax2.plot(Tcen,r62mub100cen,'b',linewidth=1,alpha=0.5)

#####################################################################################################################
for t in range(0,20):
    if t<10:
       r62160[:,t]=spline(T/ct[t],r62mub160up,xsame)
    else:
       r62160[:,t]=spline(T/ct[t-10],r62mub160down,xsame)


for num in range(1,20):
    if num==1:
       max160=np.maximum(r62160[:,num-1],r62160[:,num])
       min160=np.minimum(r62160[:,num-1],r62160[:,num])
    else:
       max160=np.maximum(max160,r62160[:,num])
       min160=np.minimum(min160,r62160[:,num])

band_mub160=ax2.fill_between(xsame,max160,min160,alpha=0.25,facecolor='k',edgecolor='')
line_mub160,=ax2.plot(Tcen,r62mub160cen,'k',linewidth=1,alpha=0.5)

ax2.axis([80,230,-1.3,1.5])
#ax2.set_xscale('log')
ax2.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$R^B_{62}$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)

############################################################################################################################
ax3=fig.add_subplot(133)
band_mub0=ax3.fill_betweenx(r82mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=ax3.plot(Tcen,r82mub0,'r',linewidth=1,alpha=0.5)
####################################################################################################################
for t in range(0,20):
    if t<10:
       r82100[:,t]=spline(T/ct[t],r82mub100up,xsame)
    else:
       r82100[:,t]=spline(T/ct[t-10],r82mub100down,xsame)


for num in range(1,20):
    if num==1:
       max100=np.maximum(r82100[:,num-1],r82100[:,num])
       min100=np.minimum(r82100[:,num-1],r82100[:,num])
    else:
       max100=np.maximum(max100,r82100[:,num])
       min100=np.minimum(min100,r82100[:,num])

band_mub100=ax3.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=ax3.plot(Tcen,r82mub100cen,'b',linewidth=1,alpha=0.5)

#######################################################################################################################33
for t in range(0,20):
    if t<10:
       r82160[:,t]=spline(T/ct[t],r82mub160up,xsame)
    else:
       r82160[:,t]=spline(T/ct[t-10],r82mub160down,xsame)


for num in range(1,20):
    if num==1:
       max160=np.maximum(r82160[:,num-1],r82160[:,num])
       min160=np.minimum(r82160[:,num-1],r82160[:,num])
    else:
       max160=np.maximum(max160,r82160[:,num])
       min160=np.minimum(min160,r82160[:,num])

band_mub160=ax3.fill_between(xsame,max160,min160,alpha=0.25,facecolor='k',edgecolor='')
line_mub160,=ax3.plot(Tcen,r82mub160cen,'k',linewidth=1,alpha=0.5)


ax3.axis([80,220,-15,10])
#ax3.set_xscale('log')

ax3.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.set_ylabel(r'$R^B_{82}$', fontsize=14, color='black')

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
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.06, right=0.96, hspace=0.35, wspace=0.25)


fig.savefig("R42R62R82-T-muB0to160.pdf")

#plt.show()

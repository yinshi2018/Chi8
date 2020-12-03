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


mf0=np.loadtxt('muB-Tto300/muB0/mf.dat')
mf400=np.loadtxt('muB-Tto300/muB420/mf.dat')
mf500=np.loadtxt('muB-Tto300/muB525/mf.dat')
mf560=np.loadtxt('muB-Tto300/muB589/mf.dat')

Unit_Nf2p1=0.951599

#####
y_data=mf0
n_data=len(y_data)

dydx_data=np.empty(n_data,dtype = float)
for i in range(n_data):
    if i==0:
        dydx_data[i]=(y_data[i+1]-y_data[i])
    elif i==n_data-1:
        dydx_data[i]=(y_data[i]-y_data[i-1])
    else:
        dydx_data[i]=(y_data[i+1]-y_data[i-1])/2.

dydx_data=dydx_data*(-1.)

dmf0dT=dydx_data

#####

y_data=mf400
n_data=len(y_data)

dydx_data=np.empty(n_data,dtype = float)
for i in range(n_data):
    if i==0:
        dydx_data[i]=(y_data[i+1]-y_data[i])
    elif i==n_data-1:
        dydx_data[i]=(y_data[i]-y_data[i-1])
    else:
        dydx_data[i]=(y_data[i+1]-y_data[i-1])/2.
dydx_data=dydx_data*(-1.)

dmf400dT=dydx_data

#####

y_data=mf500
n_data=len(y_data)

dydx_data=np.empty(n_data,dtype = float)
for i in range(n_data):
    if i==0:
        dydx_data[i]=(y_data[i+1]-y_data[i])
    elif i==n_data-1:
        dydx_data[i]=(y_data[i]-y_data[i-1])
    else:
        dydx_data[i]=(y_data[i+1]-y_data[i-1])/2.
dydx_data=dydx_data*(-1.)

dmf500dT=dydx_data

#####

y_data=mf560
n_data=len(y_data)

dydx_data=np.empty(n_data,dtype = float)
for i in range(n_data):
    if i==0:
        dydx_data[i]=(y_data[i+1]-y_data[i])
    elif i==n_data-1:
        dydx_data[i]=(y_data[i]-y_data[i-1])
    else:
        dydx_data[i]=(y_data[i+1]-y_data[i-1])/2.
dydx_data=dydx_data*(-1.)

dmf560dT=dydx_data

#####




# Create figure
fig=plt.figure(figsize=(9., 3.5))
ax1=fig.add_subplot(121)

ax1.plot(T*Unit_Nf2p1,mf0*Unit_Nf2p1,'k-',linewidth=2,markersize=5,label=r'$\mu_B=0$')
ax1.plot(T*Unit_Nf2p1,mf400*Unit_Nf2p1,'r--',linewidth=2,markersize=5,label=r'$\mu_B=400\,\mathrm{MeV}$')
ax1.plot(T*Unit_Nf2p1,mf500*Unit_Nf2p1,'g-.',linewidth=2,markersize=5,label=r'$\mu_B=500$')
ax1.plot(T*Unit_Nf2p1,mf560*Unit_Nf2p1,'b:',linewidth=2,markersize=5,label=r'$\mu_B=560$')
#ax1.axis([0,300,0,80])

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$m_q\,[\mathrm{MeV}]$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)


# Plot two
ax2=fig.add_subplot(122)

ax2.plot(T*Unit_Nf2p1,dmf0dT,'k-',linewidth=2,markersize=5,label=r'$\mu_B=0$')
ax2.plot(T*Unit_Nf2p1,dmf400dT,'r--',linewidth=2,markersize=5,label=r'$\mu_B=400$')
ax2.plot(T*Unit_Nf2p1,dmf500dT,'g-.',linewidth=2,markersize=5,label=r'$\mu_B=500$')
ax2.plot(T*Unit_Nf2p1,dmf560dT,'b:',linewidth=2,markersize=5,label=r'$\mu_B=560$')

ax2.axis([0,300,0,20])
#ax2.set_xscale('log')

ax2.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$|\partial\,m_q/\partial\,T\,|$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

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


fig.savefig("mf.pdf")

#plt.show()

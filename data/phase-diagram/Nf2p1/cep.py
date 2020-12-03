#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker


# Data for plotting

#dmfdT_qti=np.loadtxt('muB/muB0/dmfdT.dat')
#TMeV=np.loadtxt('muB/muB0/TMeV.dat')
list1 =  np.zeros((60,3))

for ii in range(60):
    fns = str(ii)
    filename_mf = 'muB/muB'+fns+'0/mf.dat'
    filename_TMeV = 'muB/muB'+fns+'0/TMeV.dat'

    mf= np.loadtxt(filename_mf)
#mf=np.loadtxt('muB/muB0/mf.dat')

    T=np.loadtxt(filename_TMeV)

#muB=np.loadtxt('CEP/muB.dat')
#T_low=np.loadtxt('CEP/Tlow.dat')
#T_high=np.loadtxt('CEP/Thigh.dat')

#Tc=np.loadtxt('CEP/Tc.dat')
#Tc1=np.loadtxt('CEP/Tc1.dat')


    y_data=mf
    n_data=len(y_data)

    dydx_data=range(n_data)
    for i in range(n_data):
        if i==0:
            dydx_data[i]=(y_data[i+1]-y_data[i])
        elif i==n_data-1:
            dydx_data[i]=(y_data[i]-y_data[i-1])
        else:
            dydx_data[i]=(y_data[i+1]-y_data[i-1])/2.
    dydx_data=dydx_data/np.amin(dydx_data)

    y_cut=0.8

    for i in range(n_data-1):
        if dydx_data[i]<=y_cut and dydx_data[i+1]>y_cut :
            T_cut_low=(y_cut-dydx_data[i])/(dydx_data[i+1]-dydx_data[i])+T[i]
        elif dydx_data[i]>y_cut and dydx_data[i+1]<=y_cut :
            T_cut_high=(y_cut-dydx_data[i])/(dydx_data[i+1]-dydx_data[i])+T[i]



    list1[ii,0] = ii * 10
    list1[ii,1] = T_cut_low
    list1[ii,2] = T_cut_high
#print('T_cut_low=',T_cut_low)
#print('T_cut_high=',T_cut_high)
np.savetxt('./pb-Nf2p1.dat',list1)










dmfdT=dydx_data






# Create figure
fig=plt.figure(figsize=(9., 3.5))
ax1=fig.add_subplot(121)

ax1.plot(T,dmfdT,'k^',linewidth=2,markersize=5,label=r'$T=0$')
#ax1.plot(TMeV,dmfdT_qti,'r<',linewidth=2,markersize=5,label=r'$\mu_B=150\,\mathrm{MeV}$')
#ax1.plot(k_T200_muB0,GA_T200_muB0,'b-.',linewidth=2,markersize=5,label=r'$\mu_B=200$')
#ax1.plot(k_T300_muB0,GA_T300_muB0,'g:',linewidth=2,markersize=5,label=r'$\mu_B=300$')
#ax1.axis([0.01,20000,0,0.2])
#ax1.set_xscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$G_A\,[{\mathrm{MeV}}^{-2}]$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

# Plot two
ax2=fig.add_subplot(122)

ax2.plot(muB,T_low,'k-',linewidth=2,markersize=5,label=r'$T=0$')
ax2.plot(muB,T_high,'r-',linewidth=1,markersize=5,label=r'$T=150\,\mathrm{MeV}$')
ax2.plot(muB,Tc,'b-',linewidth=1,markersize=5)
#ax2.plot(muB,Tc1,'g-',linewidth=1,markersize=5)
ax2.axis([0,900,0,200])
#ax2.set_xscale('log')

ax2.set_xlabel('$k\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$G_A\,[{\mathrm{MeV}}^{-2}]$', fontsize=14, color='black')

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
#fig.subplots_adjust(top=0.95, bottom=0.1, left=0.10, right=0.95, hspace=0.35,
#                    wspace=0.35)


fig.savefig("cep.pdf")

#plt.show()

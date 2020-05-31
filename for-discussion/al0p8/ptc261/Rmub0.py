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
chi2mub0=np.loadtxt(r'./fluc/final/buffer/chi2.dat')
chi4mub0=np.loadtxt(r'./fluc/final/buffer/chi4.dat')
chi6mub0=np.loadtxt(r'./fluc/final/buffer/chi6.dat')
chi8mub0=np.loadtxt(r'./fluc/final/buffer/chi8.dat')
r42mub0=chi4mub0/chi2mub0
r62mub0=chi6mub0/chi2mub0
r82mub0=chi8mub0/chi2mub0

hotQCDR42=np.loadtxt('./fluc/data1/hotQCD_R42.dat')
WBR42=np.loadtxt('./fluc/data1/WB_R42.dat')
WBchi2=np.loadtxt('./fluc/data1/WB_chi2.dat')
WBchi6=np.loadtxt('./fluc/data1/WB_chi6.dat')
WBchi6erro=np.loadtxt('./fluc/data1/WB_chi6erro.dat')
WBchi8=np.loadtxt('./fluc/data1/WB_chi8.dat')
WBchi8erro=np.loadtxt('./fluc/data1/WB_chi8erro.dat')
WBchix=np.loadtxt('./fluc/data1/WB_chix.dat')
hotQCDR62=np.loadtxt('./fluc/data1/hotQCD_R62.dat')
hotQCDb=np.loadtxt('./fluc/data1/hotQCDR62_b.dat')
hotQCDg=np.loadtxt('./fluc/data1/hotQCDR62_g.dat')
T=np.loadtxt('TMeV.dat')
R62erro=WBchi6erro/WBchi2
R82erro=WBchi8erro/WBchi2

T1=T/194
# Create figure
fig=plt.figure(figsize=(13., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
ax1.plot(T1,r42mub0,'k-',linewidth=1,markersize=5,label=r'$FRG,\mu_B=0\,\mathrm{MeV}$')
#ax1.plot(T1,r42mub20,'r-',linewidth=1,markersize=5,label=r'$\mu_B=20\,\mathrm{MeV}$')
#ax1.plot(T1,r42mub40,'b-',linewidth=1,markersize=5,label=r'$\mu_B=40\,\mathrm{MeV}$')
#ax1.plot(T1,r42mub60,'y-',linewidth=1,markersize=5,label=r'$\mu_B=60\,\mathrm{MeV}$')
#ax1.plot(T1,r42mub80,'orange',linewidth=1,markersize=5,label=r'$\mu_B=80\,\mathrm{MeV}$')
#ax1.plot(T1,r42mub100,'gray',linewidth=1,markersize=5,label=r'$\mu_B=100\,\mathrm{MeV}$')
#ax1.plot(T1,r42mub120,'g-',linewidth=1,markersize=5,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax1.fill_between(hotQCDR42[:,0]/156,hotQCDR42[:,1]+hotQCDR42[:,2],hotQCDR42[:,1]-hotQCDR42[:,2],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD')
ax1.errorbar(WBR42[:,0]/156,WBR42[:,1],yerr=WBR42[:,2],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax1.axis([0.5,1.5,0,1.2])
#ax1.set_xscale('log')

ax1.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=8,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(132)
ax2.plot(T1,r62mub0,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
#ax2.plot(T1,r62mub20,'r-',linewidth=1,markersize=5)#,label=r'$\mu_B=20\,\mathrm{MeV}$')
#ax2.plot(T1,r62mub40,'b-',linewidth=1,markersize=5)#,label=r'$\mu_B=40\,\mathrm{MeV}$')
#ax2.plot(T1,r62mub60,'y-',linewidth=1,markersize=5)#,label=r'$\mu_B=60\,\mathrm{MeV}$')
#ax2.plot(T1,r62mub80,'orange',linewidth=1,markersize=5)#,label=r'$\mu_B=80\,\mathrm{MeV}$')
#ax2.plot(T1,r62mub100,'gray',linewidth=1,markersize=5)#,label=r'$\mu_B=100\,\mathrm{MeV}$')
#ax2.plot(T1,r62mub120,'g-',linewidth=1,markersize=5)#,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax2.fill_between(hotQCDR62[:,0]/156,hotQCDR62[:,1],hotQCDR62[:,2],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD cont. est')
#ax2.errorbar(hotQCDb[:,0]/156,hotQCDb[:,1],yerr=hotQCDb[:,2],color='blue',marker='s',linestyle='',linewidth=2,markersize=5,alpha=1,label=r'$N_\tau=8$')
#ax2.errorbar(hotQCDg[:,0]/156,hotQCDg[:,1],yerr=hotQCDg[:,2],color='green',marker='^',linestyle='',linewidth=2,markersize=5,alpha=1,label=r'$N_\tau=6$')
ax2.errorbar(WBchix/156,WBchi6/WBchi2,yerr=R62erro,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax2.axis([0.5,1.5,-1.2,1.9])
#ax2.set_xscale('log')

ax2.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize=7.5,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(133)
ax3.plot(T1,r82mub0,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
#ax3.plot(T1,r82mub20,'r-',linewidth=1,markersize=5)#,label=r'$\mu_B=20\,\mathrm{MeV}$')
#ax3.plot(T1,r82mub40,'b-',linewidth=1,markersize=5)#,label=r'$\mu_B=40\,\mathrm{MeV}$')
#ax3.plot(T1,r82mub60,'y-',linewidth=1,markersize=5)#,label=r'$\mu_B=60\,\mathrm{MeV}$')
#ax3.plot(T1,r82mub80,'orange',linewidth=1,markersize=5)#,label=r'$\mu_B=80\,\mathrm{MeV}$')
#ax3.plot(T1,r82mub100,'gray',linewidth=1,markersize=5)#,label=r'$\mu_B=100\,\mathrm{MeV}$')
#ax3.plot(T1,r82mub120,'g-',linewidth=1,markersize=5)#,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax3.errorbar(WBchix/156,WBchi8/WBchi2,yerr=R82erro,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax3.axis([0.5,1.5,-3,3])
#ax2.set_xscale('log')

ax3.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.set_ylabel(r'$\chi^B_8/\chi^B_2$', fontsize=14, color='black')

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


fig.savefig("mub0.pdf")

#plt.show()

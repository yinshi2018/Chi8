#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl
import mpl_toolkits.mplot3d as p3d

mpl.style.use('classic')


# Data for plotting
R42=np.loadtxt(r'./R42.dat')
R62=np.loadtxt(r'./R62.dat')
R82=np.loadtxt(r'./R82.dat')
T=np.loadtxt(r'./TMeV.dat')
mub1=np.loadtxt(r'./mub.dat')
mub=np.zeros([300,41])
T1=np.zeros([300,41])
for num in range(0,300):
    mub[num,:]=mub1

print(mub)
T2=T/1.25
for num in range(0,41):
    T1[:,num]=T2

print(T1)
# Create figure
fig=plt.figure(figsize=(13., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
#ax1.plot(T1,R42,mub,linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
cm = plt.cm.get_cmap('Reds')
cs=ax1.contourf(T1, R42,mub,cmap=cm)
plt.colorbar(cs)

#ax1.fill_between(hotQCDR42[:,0]/156,hotQCDR42[:,1]+hotQCDR42[:,2],hotQCDR42[:,1]-hotQCDR42[:,2],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD')
#ax1.errorbar(WBR42[:,0]/156,WBr62[:,1],yerr=WBr62[:,2],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax1.axis([50.,230.,-0.5,1.5])
#ax1.set_xscale('log')

ax1.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(132)

ax2.axis([60.,200.,-16,7])
#ax2.set_xscale('log')

ax2.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(133)

ax3.axis([80.,200.,-270,320])
#ax3.set_xscale('log')

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
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.07, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("finmub.pdf")

#plt.show()

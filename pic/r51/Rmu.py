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
chi1mub20=np.loadtxt(r'./mub20/deltamu250/final/buffer/chi1.dat')
chi3mub20=np.loadtxt(r'./mub20/deltamu250/final/buffer/chi3.dat')
chi5mub20=np.loadtxt(r'./mub20/deltamu250/final/buffer/chi5.dat')
chi7mub20=np.loadtxt(r'./mub20/deltamu250/final/buffer/chi7.dat')
chi2mub20=np.loadtxt(r'./mub20/deltamu250/final/buffer/chi2.dat')
chi4mub20=np.loadtxt(r'./mub20/deltamu250/final/buffer/chi4.dat')
chi6mub20=np.loadtxt(r'./mub20/deltamu250/final/buffer/chi6.dat')
chi8mub20=np.loadtxt(r'./mub20/deltamu250/final/buffer/chi8.dat')
r31mub20=chi3mub20/chi1mub20
r51mub20=chi5mub20/chi1mub20
r71mub20=chi7mub20/chi1mub20
r42mub20=chi4mub20/chi2mub20
r62mub20=chi6mub20/chi2mub20
r82mub20=chi8mub20/chi2mub20
chi1mub40=np.loadtxt(r'./mub40/deltamu250/final/buffer/chi1.dat')
chi3mub40=np.loadtxt(r'./mub40/deltamu250/final/buffer/chi3.dat')
chi5mub40=np.loadtxt(r'./mub40/deltamu250/final/buffer/chi5.dat')
chi7mub40=np.loadtxt(r'./mub40/deltamu250/final/buffer/chi7.dat')
r31mub40=chi3mub40/chi1mub40
r51mub40=chi5mub40/chi1mub40
r71mub40=chi7mub40/chi1mub40
chi1mub60=np.loadtxt(r'./mub60/deltamu250/final/buffer/chi1.dat')
chi3mub60=np.loadtxt(r'./mub60/deltamu250/final/buffer/chi3.dat')
chi5mub60=np.loadtxt(r'./mub60/deltamu250/final/buffer/chi5.dat')
chi7mub60=np.loadtxt(r'./mub60/deltamu250/final/buffer/chi7.dat')
r31mub60=chi3mub60/chi1mub60
r51mub60=chi5mub60/chi1mub60
r71mub60=chi7mub60/chi1mub60
chi1mub80=np.loadtxt(r'./mub80/deltamu250/final/buffer/chi1.dat')
chi3mub80=np.loadtxt(r'./mub80/deltamu250/final/buffer/chi3.dat')
chi5mub80=np.loadtxt(r'./mub80/deltamu250/final/buffer/chi5.dat')
chi7mub80=np.loadtxt(r'./mub80/deltamu250/final/buffer/chi7.dat')
r31mub80=chi3mub80/chi1mub80
r51mub80=chi5mub80/chi1mub80
r71mub80=chi7mub80/chi1mub80
chi1mub100=np.loadtxt(r'./mub100/deltamu250/final/buffer/chi1.dat')
chi3mub100=np.loadtxt(r'./mub100/deltamu250/final/buffer/chi3.dat')
chi5mub100=np.loadtxt(r'./mub100/deltamu250/final/buffer/chi5.dat')
chi7mub100=np.loadtxt(r'./mub100/deltamu250/final/buffer/chi7.dat')
r31mub100=chi3mub100/chi1mub100
r51mub100=chi5mub100/chi1mub100
r71mub100=chi7mub100/chi1mub100
chi1mub120=np.loadtxt(r'./mub120/deltamu250/final/buffer/chi1.dat')
chi3mub120=np.loadtxt(r'./mub120/deltamu250/final/buffer/chi3.dat')
chi5mub120=np.loadtxt(r'./mub120/deltamu250/final/buffer/chi5.dat')
chi7mub120=np.loadtxt(r'./mub120/deltamu250/final/buffer/chi7.dat')
r31mub120=chi3mub120/chi1mub120
r51mub120=chi5mub120/chi1mub120
r71mub120=chi7mub120/chi1mub120

hotQCDR42=np.loadtxt('data1/hotQCD_R42.dat')
WBR42=np.loadtxt('data1/WB_R42.dat')
WBchi2=np.loadtxt('data1/WB_chi2.dat')
WBchi6=np.loadtxt('data1/WB_chi6.dat')
WBchi6erro=np.loadtxt('data1/WB_chi6erro.dat')
WBchi8=np.loadtxt('data1/WB_chi8.dat')
WBchi8erro=np.loadtxt('data1/WB_chi8erro.dat')
WBchix=np.loadtxt('data1/WB_chix.dat')
hotQCDR62=np.loadtxt('data1/hotQCD_R62.dat')
hotQCDb=np.loadtxt('data1/hotQCDR62_b.dat')
hotQCDg=np.loadtxt('data1/hotQCDR62_g.dat')
T=np.loadtxt('TMeV.dat')
R62erro=WBchi6erro/WBchi2
R82erro=WBchi8erro/WBchi2

T1=T/193.7
# Create figure
fig=plt.figure(figsize=(13., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
ax1.plot(T1,r31mub20,color='navy',linewidth=1,markersize=5,label=r'$\mu_B=20\,\mathrm{MeV}$')
ax1.plot(T1,r31mub40,color='mediumblue',linewidth=1,markersize=5,label=r'$\mu_B=40\,\mathrm{MeV}$')
ax1.plot(T1,r31mub60,color='blue',linewidth=1,markersize=5,label=r'$\mu_B=60\,\mathrm{MeV}$')
ax1.plot(T1,r31mub80,color='slateblue',linewidth=1,markersize=5,label=r'$\mu_B=80\,\mathrm{MeV}$')
ax1.plot(T1,r31mub100,color='steelblue',linewidth=1,markersize=5,label=r'$\mu_B=100\,\mathrm{MeV}$')
ax1.plot(T1,r31mub120,color='dodgerblue',linewidth=1,markersize=5,label=r'$\mu_B=120\,\mathrm{MeV}$')


#ax1.fill_between(hotQCDR42[:,0]/156,hotQCDR42[:,1]+hotQCDR42[:,2],hotQCDR42[:,1]-hotQCDR42[:,2],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD')
#ax1.errorbar(WBR42[:,0]/156,WBr62[:,1],yerr=WBr62[:,2],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax1.axis([0.5,1.5,-0,1.2])
#ax1.set_xscale('log')

ax1.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_3/\chi^B_1$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(132)
ax2.plot(T1,r51mub20,color='navy',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax2.plot(T1,r51mub40,color='mediumblue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax2.plot(T1,r51mub60,color='blue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax2.plot(T1,r51mub80,color='slateblue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax2.plot(T1,r51mub100,color='steelblue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax2.plot(T1,r51mub120,color='dodgerblue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax2.axis([0.5,1.5,-0.5,1.2])
#ax2.set_xscale('log')

ax2.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi^B_5/\chi^B_1$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(133)
ax3.plot(T1,r71mub20,color='navy',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax3.plot(T1,r71mub40,color='mediumblue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax3.plot(T1,r71mub60,color='blue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax3.plot(T1,r71mub80,color='slateblue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax3.plot(T1,r71mub100,color='steelblue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax3.plot(T1,r71mub120,color='dodgerblue',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax3.axis([0.5,1.5,-3,2])
#ax3.set_xscale('log')

ax3.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.set_ylabel(r'$\chi^B_7/\chi^B_1$', fontsize=14, color='black')

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


fig.savefig("r51mub.pdf")

#plt.show()

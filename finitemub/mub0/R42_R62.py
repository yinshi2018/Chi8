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
#T=np.loadtxt('Tem1/buffer/TMeV.dat')
chi2=np.loadtxt('./final/buffer/chi2.dat')
chi4=np.loadtxt('./final/buffer/chi4.dat')
chi6=np.loadtxt('./final/buffer/chi6.dat')

hotQCDR42=np.loadtxt('data1/hotQCD_R42.dat')
WBR42=np.loadtxt('data1/WB_R42.dat')
hotQCDR62=np.loadtxt('data1/hotQCD_R62.dat')
hotQCDb=np.loadtxt('data1/hotQCDR62_b.dat')
hotQCDg=np.loadtxt('data1/hotQCDR62_g.dat')
T=np.loadtxt('Tem1/buffer/TMeV.dat')
R42=chi4/chi2
R62=chi6/chi2

T1=T/196

# Create figure
fig=plt.figure(figsize=(9., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(121)

ax1.plot(T1,R42,'k-',linewidth=2,markersize=5,label=r'$FRG,Tc=270,\alpha=0.7$')

ax1.fill_between(hotQCDR42[:,0]/156,hotQCDR42[:,1]+hotQCDR42[:,2],hotQCDR42[:,1]-hotQCDR42[:,2],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD')
ax1.errorbar(WBR42[:,0]/156,WBR42[:,1],yerr=WBR42[:,2],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax1.axis([0.5,1.7,0.,1.2])

ax1.set_xlabel('$T [\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$\chi^B_4/\chi^B_2$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(122)

ax2.plot(T1,R62,'k-',linewidth=2,markersize=5,label=r'$FRG,Tc=270,\alpha=0.7$')
ax2.fill_between(hotQCDR62[:,0]/156,hotQCDR62[:,1],hotQCDR62[:,2],alpha=0.4,facecolor='gray',edgecolor='',label=r'HotQCD cont. est')
ax2.errorbar(hotQCDb[:,0]/156,hotQCDb[:,1],yerr=hotQCDb[:,2],color='blue',marker='s',linestyle='',linewidth=2,markersize=5,alpha=1,label=r'$N_\tau=8$')
ax2.errorbar(hotQCDg[:,0]/156,hotQCDg[:,1],yerr=hotQCDg[:,2],color='green',marker='^',linestyle='',linewidth=2,markersize=5,alpha=1,label=r'$N_\tau=6$')
ax2.axis([0.5,1.6,-2,3.5])
#ax1.set_xscale('log')
#ax2.text(110, 0.025, r'$\mu_S=\mu_Q=0$',fontsize=14, color='k')

ax2.set_xlabel('$T [\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel('$\chi^B_6/\chi^B_2$', fontsize=14, color='black')

ax2.legend(loc=1,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)


for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.17, left=0.10, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("R42R62.pdf")
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
chi2mub0=np.loadtxt(r'./mub0/final/buffer/chi2.dat')
chi4mub0=np.loadtxt(r'./mub0/final/buffer/chi4.dat')
chi6mub0=np.loadtxt(r'./mub0/final/buffer/chi6.dat')
chi8mub0=np.loadtxt(r'./mub0/final/buffer/chi8.dat')
r42mub0=chi4mub0/chi2mub0
r62mub0=chi6mub0/chi2mub0
r82mub0=chi8mub0/chi2mub0
chi2mub20=np.loadtxt(r'./mub20/final/buffer/chi2.dat')
chi4mub20=np.loadtxt(r'./mub20/final/buffer/chi4.dat')
chi6mub20=np.loadtxt(r'./mub20/final/buffer/chi6.dat')
chi8mub20=np.loadtxt(r'./mub20/final/buffer/chi8.dat')
r42mub20=chi4mub20/chi2mub20
r62mub20=chi6mub20/chi2mub20
r82mub20=chi8mub20/chi2mub20
chi2mub40=np.loadtxt(r'./mub40/final/buffer/chi2.dat')
chi4mub40=np.loadtxt(r'./mub40/final/buffer/chi4.dat')
chi6mub40=np.loadtxt(r'./mub40/final/buffer/chi6.dat')
chi8mub40=np.loadtxt(r'./mub40/final/buffer/chi8.dat')
r42mub40=chi4mub40/chi2mub40
r62mub40=chi6mub40/chi2mub40
r82mub40=chi8mub40/chi2mub40
chi2mub60=np.loadtxt(r'./mub60/final/buffer/chi2.dat')
chi4mub60=np.loadtxt(r'./mub60/final/buffer/chi4.dat')
chi6mub60=np.loadtxt(r'./mub60/final/buffer/chi6.dat')
chi8mub60=np.loadtxt(r'./mub60/final/buffer/chi8.dat')
r42mub60=chi4mub60/chi2mub60
r62mub60=chi6mub60/chi2mub60
r82mub60=chi8mub60/chi2mub60
chi2mub80=np.loadtxt(r'./mub80/final/buffer/chi2.dat')
chi4mub80=np.loadtxt(r'./mub80/final/buffer/chi4.dat')
chi6mub80=np.loadtxt(r'./mub80/final/buffer/chi6.dat')
chi8mub80=np.loadtxt(r'./mub80/final/buffer/chi8.dat')
r42mub80=chi4mub80/chi2mub80
r62mub80=chi6mub80/chi2mub80
r82mub80=chi8mub80/chi2mub80
chi2mub100=np.loadtxt(r'./mub100/final/buffer/chi2.dat')
chi4mub100=np.loadtxt(r'./mub100/final/buffer/chi4.dat')
chi6mub100=np.loadtxt(r'./mub100/final/buffer/chi6.dat')
chi8mub100=np.loadtxt(r'./mub100/final/buffer/chi8.dat')
r42mub100=chi4mub100/chi2mub100
r62mub100=chi6mub100/chi2mub100
r82mub100=chi8mub100/chi2mub100
chi2mub120=np.loadtxt(r'./mub120/final/buffer/chi2.dat')
chi4mub120=np.loadtxt(r'./mub120/final/buffer/chi4.dat')
chi6mub120=np.loadtxt(r'./mub120/final/buffer/chi6.dat')
chi8mub120=np.loadtxt(r'./mub120/final/buffer/chi8.dat')
r42mub120=chi4mub120/chi2mub120
r62mub120=chi6mub120/chi2mub120
r82mub120=chi8mub120/chi2mub120
chi2mub140=np.loadtxt(r'./mub140/final/buffer/chi2.dat')
chi4mub140=np.loadtxt(r'./mub140/final/buffer/chi4.dat')
chi6mub140=np.loadtxt(r'./mub140/final/buffer/chi6.dat')
chi8mub140=np.loadtxt(r'./mub140/final/buffer/chi8.dat')
r42mub140=chi4mub140/chi2mub140
r62mub140=chi6mub140/chi2mub140
r82mub140=chi8mub140/chi2mub140
chi2mub160=np.loadtxt(r'./mub160/final/buffer/chi2.dat')
chi4mub160=np.loadtxt(r'./mub160/final/buffer/chi4.dat')
chi6mub160=np.loadtxt(r'./mub160/final/buffer/chi6.dat')
chi8mub160=np.loadtxt(r'./mub160/final/buffer/chi8.dat')
r42mub160=chi4mub160/chi2mub160
r62mub160=chi6mub160/chi2mub160
r82mub160=chi8mub160/chi2mub160
chi2mub180=np.loadtxt(r'./mub180/final/buffer/chi2.dat')
chi4mub180=np.loadtxt(r'./mub180/final/buffer/chi4.dat')
chi6mub180=np.loadtxt(r'./mub180/final/buffer/chi6.dat')
chi8mub180=np.loadtxt(r'./mub180/final/buffer/chi8.dat')
r42mub180=chi4mub180/chi2mub180
r62mub180=chi6mub180/chi2mub180
r82mub180=chi8mub180/chi2mub180
chi2mub200=np.loadtxt(r'./mub200/final/buffer/chi2.dat')
chi4mub200=np.loadtxt(r'./mub200/final/buffer/chi4.dat')
chi6mub200=np.loadtxt(r'./mub200/final/buffer/chi6.dat')
chi8mub200=np.loadtxt(r'./mub200/final/buffer/chi8.dat')
r42mub200=chi4mub200/chi2mub200
r62mub200=chi6mub200/chi2mub200
r82mub200=chi8mub200/chi2mub200
chi2mub220=np.loadtxt(r'./mub220/final/buffer/chi2.dat')
chi4mub220=np.loadtxt(r'./mub220/final/buffer/chi4.dat')
chi6mub220=np.loadtxt(r'./mub220/final/buffer/chi6.dat')
chi8mub220=np.loadtxt(r'./mub220/final/buffer/chi8.dat')
r42mub220=chi4mub220/chi2mub220
r62mub220=chi6mub220/chi2mub220
r82mub220=chi8mub220/chi2mub220
chi2mub240=np.loadtxt(r'./mub240/final/buffer/chi2.dat')
chi4mub240=np.loadtxt(r'./mub240/final/buffer/chi4.dat')
chi6mub240=np.loadtxt(r'./mub240/final/buffer/chi6.dat')
chi8mub240=np.loadtxt(r'./mub240/final/buffer/chi8.dat')
r42mub240=chi4mub240/chi2mub240
r62mub240=chi6mub240/chi2mub240
r82mub240=chi8mub240/chi2mub240
chi2mub260=np.loadtxt(r'./mub260/final/buffer/chi2.dat')
chi4mub260=np.loadtxt(r'./mub260/final/buffer/chi4.dat')
chi6mub260=np.loadtxt(r'./mub260/final/buffer/chi6.dat')
chi8mub260=np.loadtxt(r'./mub260/final/buffer/chi8.dat')
r42mub260=chi4mub260/chi2mub260
r62mub260=chi6mub260/chi2mub260
r82mub260=chi8mub260/chi2mub260
chi2mub280=np.loadtxt(r'./mub280/final/buffer/chi2.dat')
chi4mub280=np.loadtxt(r'./mub280/final/buffer/chi4.dat')
chi6mub280=np.loadtxt(r'./mub280/final/buffer/chi6.dat')
chi8mub280=np.loadtxt(r'./mub280/final/buffer/chi8.dat')
r42mub280=chi4mub280/chi2mub280
r62mub280=chi6mub280/chi2mub280
r82mub280=chi8mub280/chi2mub280
chi2mub300=np.loadtxt(r'./mub300/final/buffer/chi2.dat')
chi4mub300=np.loadtxt(r'./mub300/final/buffer/chi4.dat')
chi6mub300=np.loadtxt(r'./mub300/final/buffer/chi6.dat')
chi8mub300=np.loadtxt(r'./mub300/final/buffer/chi8.dat')
r42mub300=chi4mub300/chi2mub300
r62mub300=chi6mub300/chi2mub300
r82mub300=chi8mub300/chi2mub300
chi2mub320=np.loadtxt(r'./mub320/final/buffer/chi2.dat')
chi4mub320=np.loadtxt(r'./mub320/final/buffer/chi4.dat')
chi6mub320=np.loadtxt(r'./mub320/final/buffer/chi6.dat')
chi8mub320=np.loadtxt(r'./mub320/final/buffer/chi8.dat')
r42mub320=chi4mub320/chi2mub320
r62mub320=chi6mub320/chi2mub320
r82mub320=chi8mub320/chi2mub320
chi2mub340=np.loadtxt(r'./mub340/final/buffer/chi2.dat')
chi4mub340=np.loadtxt(r'./mub340/final/buffer/chi4.dat')
chi6mub340=np.loadtxt(r'./mub340/final/buffer/chi6.dat')
chi8mub340=np.loadtxt(r'./mub340/final/buffer/chi8.dat')
r42mub340=chi4mub340/chi2mub340
r62mub340=chi6mub340/chi2mub340
r82mub340=chi8mub340/chi2mub340
chi2mub360=np.loadtxt(r'./mub360/final/buffer/chi2.dat')
chi4mub360=np.loadtxt(r'./mub360/final/buffer/chi4.dat')
chi6mub360=np.loadtxt(r'./mub360/final/buffer/chi6.dat')
chi8mub360=np.loadtxt(r'./mub360/final/buffer/chi8.dat')
r42mub360=chi4mub360/chi2mub360
r62mub360=chi6mub360/chi2mub360
r82mub360=chi8mub360/chi2mub360
chi2mub380=np.loadtxt(r'./mub380/final/buffer/chi2.dat')
chi4mub380=np.loadtxt(r'./mub380/final/buffer/chi4.dat')
chi6mub380=np.loadtxt(r'./mub380/final/buffer/chi6.dat')
chi8mub380=np.loadtxt(r'./mub380/final/buffer/chi8.dat')
r42mub380=chi4mub380/chi2mub380
r62mub380=chi6mub380/chi2mub380
r82mub380=chi8mub380/chi2mub380
chi2mub400=np.loadtxt(r'./mub400/final/buffer/chi2.dat')
chi4mub400=np.loadtxt(r'./mub400/final/buffer/chi4.dat')
chi6mub400=np.loadtxt(r'./mub400/final/buffer/chi6.dat')
chi8mub400=np.loadtxt(r'./mub400/final/buffer/chi8.dat')
r42mub400=chi4mub400/chi2mub400
r62mub400=chi6mub400/chi2mub400
r82mub400=chi8mub400/chi2mub400
T=np.loadtxt(r'./TMeV.dat')


T1=T/1.25
# Create figure
fig=plt.figure(figsize=(13., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
ax1.plot(T1,r42mub0,color='navy',linewidth=1,markersize=5,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax1.plot(T1,r42mub20,color='mediumblue',linewidth=1,markersize=5,label=r'$\mu_B=20\,\mathrm{MeV}$')
ax1.plot(T1,r42mub40,color='blue',linewidth=1,markersize=5,label=r'$\mu_B=40\,\mathrm{MeV}$')
ax1.plot(T1,r42mub60,color='slateblue',linewidth=1,markersize=5,label=r'$\mu_B=60\,\mathrm{MeV}$')
ax1.plot(T1,r42mub80,color='steelblue',linewidth=1,markersize=5,label=r'$\mu_B=80\,\mathrm{MeV}$')
ax1.plot(T1,r42mub100,color='dodgerblue',linewidth=1,markersize=5,label=r'$\mu_B=100\,\mathrm{MeV}$')
ax1.plot(T1,r42mub120,color='deepskyblue',linewidth=1,markersize=5,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax1.plot(T1,r42mub140,color='mediumturquoise',linewidth=1,markersize=5,label=r'$\mu_B=140\,\mathrm{MeV}$')
ax1.plot(T1,r42mub160,color='mediumspringgreen',linewidth=1,markersize=5,label=r'$\mu_B=160\,\mathrm{MeV}$')
ax1.plot(T1,r42mub180,color='seagreen',linewidth=1,markersize=5,label=r'$\mu_B=180\,\mathrm{MeV}$')
ax1.plot(T1,r42mub200,color='olivedrab',linewidth=1,markersize=5,label=r'$\mu_B=200\,\mathrm{MeV}$')
ax1.plot(T1,r42mub220,color='darkolivegreen',linewidth=1,markersize=5)#,label=r'$\mu_B=220\,\mathrm{MeV}$')
ax1.plot(T1,r42mub240,color='olive',linewidth=1,markersize=5)#,label=r'$\mu_B=240\,\mathrm{MeV}$')
ax1.plot(T1,r42mub260,color='darkgoldenrod',linewidth=1,markersize=5)#,label=r'$\mu_B=260\,\mathrm{MeV}$')
ax1.plot(T1,r42mub280,color='goldenrod',linewidth=1,markersize=5)#,label=r'$\mu_B=280\,\mathrm{MeV}$')
ax1.plot(T1,r42mub300,color='orange',linewidth=1,markersize=5)#,label=r'$\mu_B=300\,\mathrm{MeV}$')
ax1.plot(T1,r42mub320,color='orangered',linewidth=1,markersize=5)#,label=r'$\mu_B=320\,\mathrm{MeV}$')
ax1.plot(T1,r42mub340,color='red',linewidth=1,markersize=5)#,label=r'$\mu_B=340\,\mathrm{MeV}$')
ax1.plot(T1,r42mub360,color='brown',linewidth=1,markersize=5)#,label=r'$\mu_B=360\,\mathrm{MeV}$')
ax1.plot(T1,r42mub380,color='firebrick',linewidth=1,markersize=5)#,label=r'$\mu_B=380\,\mathrm{MeV}$')
ax1.plot(T1,r42mub400,color='darkred',linewidth=1,markersize=5)#,label=r'$\mu_B=400\,\mathrm{MeV}$')

#ax1.fill_between(hotQCDR42[:,0]/156,hotQCDR42[:,1]+hotQCDR42[:,2],hotQCDR42[:,1]-hotQCDR42[:,2],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD')
#ax1.errorbar(WBR42[:,0]/156,WBr62[:,1],yerr=WBr62[:,2],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax1.axis([50.,230.,-1,1.8])
#ax1.set_xscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(132)
ax2.plot(T1,r62mub0,color='navy',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax2.plot(T1,r62mub20,color='mediumblue',linewidth=1,markersize=5)#,label=r'$\mu_B=20\,\mathrm{MeV}$')
ax2.plot(T1,r62mub40,color='blue',linewidth=1,markersize=5)#,label=r'$\mu_B=40\,\mathrm{MeV}$')
ax2.plot(T1,r62mub60,color='slateblue',linewidth=1,markersize=5)#,label=r'$\mu_B=60\,\mathrm{MeV}$')
ax2.plot(T1,r62mub80,color='steelblue',linewidth=1,markersize=5)#,label=r'$\mu_B=80\,\mathrm{MeV}$')
ax2.plot(T1,r62mub100,color='dodgerblue',linewidth=1,markersize=5)#,label=r'$\mu_B=100\,\mathrm{MeV}$')
ax2.plot(T1,r62mub120,color='deepskyblue',linewidth=1,markersize=5)#,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax2.plot(T1,r62mub140,color='mediumturquoise',linewidth=1,markersize=5)#,label=r'$\mu_B=140\,\mathrm{MeV}$')
ax2.plot(T1,r62mub160,color='mediumspringgreen',linewidth=1,markersize=5)#,label=r'$\mu_B=160\,\mathrm{MeV}$')
ax2.plot(T1,r62mub180,color='seagreen',linewidth=1,markersize=5)#,label=r'$\mu_B=180\,\mathrm{MeV}$')
ax2.plot(T1,r62mub200,color='olivedrab',linewidth=1,markersize=5)#,label=r'$\mu_B=200\,\mathrm{MeV}$')
ax2.plot(T1,r62mub220,color='darkolivegreen',linewidth=1,markersize=5,label=r'$\mu_B=220\,\mathrm{MeV}$')
ax2.plot(T1,r62mub240,color='olive',linewidth=1,markersize=5,label=r'$\mu_B=240\,\mathrm{MeV}$')
ax2.plot(T1,r62mub260,color='darkgoldenrod',linewidth=1,markersize=5,label=r'$\mu_B=260\,\mathrm{MeV}$')
ax2.plot(T1,r62mub280,color='goldenrod',linewidth=1,markersize=5,label=r'$\mu_B=280\,\mathrm{MeV}$')
ax2.plot(T1,r62mub300,color='orange',linewidth=1,markersize=5,label=r'$\mu_B=300\,\mathrm{MeV}$')
ax2.plot(T1,r62mub320,color='orangered',linewidth=1,markersize=5,label=r'$\mu_B=320\,\mathrm{MeV}$')
ax2.plot(T1,r62mub340,color='red',linewidth=1,markersize=5,label=r'$\mu_B=340\,\mathrm{MeV}$')
ax2.plot(T1,r62mub360,color='brown',linewidth=1,markersize=5,label=r'$\mu_B=360\,\mathrm{MeV}$')
ax2.plot(T1,r62mub380,color='firebrick',linewidth=1,markersize=5,label=r'$\mu_B=380\,\mathrm{MeV}$')
ax2.plot(T1,r62mub400,color='darkred',linewidth=1,markersize=5,label=r'$\mu_B=400\,\mathrm{MeV}$')
#ax2.fill_between(hotQCDR62[:,0]/156,hotQCDR62[:,1],hotQCDR62[:,2],alpha=0.25,facecolor='green',edgecolor='',label=r'HotQCD cont. est')
#ax2.errorbar(hotQCDb[:,0]/156,hotQCDb[:,1],yerr=hotQCDb[:,2],color='blue',marker='s',linestyle='',linewidth=2,markersize=5,alpha=1,label=r'$N_\tau=8$')
#ax2.errorbar(hotQCDg[:,0]/156,hotQCDg[:,1],yerr=hotQCDg[:,2],color='green',marker='^',linestyle='',linewidth=2,markersize=5,alpha=1,label=r'$N_\tau=6$')
#ax2.errorbar(WBchix/156,WBchi6/WBchi2,yerr=R62erro,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax2.axis([60.,200.,-35,23])
#ax2.set_xscale('log')

ax2.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')

ax2.legend(loc=3,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(133)
ax3.plot(T1,r82mub0,color='navy',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax3.plot(T1,r82mub20,color='mediumblue',linewidth=1,markersize=5)#,label=r'$\mu_B=20\,\mathrm{MeV}$')
ax3.plot(T1,r82mub40,color='blue',linewidth=1,markersize=5)#,label=r'$\mu_B=40\,\mathrm{MeV}$')
ax3.plot(T1,r82mub60,color='slateblue',linewidth=1,markersize=5)#,label=r'$\mu_B=60\,\mathrm{MeV}$')
ax3.plot(T1,r82mub80,color='steelblue',linewidth=1,markersize=5)#,label=r'$\mu_B=80\,\mathrm{MeV}$')
ax3.plot(T1,r82mub100,color='dodgerblue',linewidth=1,markersize=5)#,label=r'$\mu_B=100\,\mathrm{MeV}$')
ax3.plot(T1,r82mub120,color='deepskyblue',linewidth=1,markersize=5)#,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax3.plot(T1,r82mub140,color='mediumturquoise',linewidth=1,markersize=5)#,label=r'$\mu_B=140\,\mathrm{MeV}$')
ax3.plot(T1,r82mub160,color='mediumspringgreen',linewidth=1,markersize=5)#,label=r'$\mu_B=160\,\mathrm{MeV}$')
ax3.plot(T1,r82mub180,color='seagreen',linewidth=1,markersize=5)#,label=r'$\mu_B=180\,\mathrm{MeV}$')
ax3.plot(T1,r82mub200,color='olivedrab',linewidth=1,markersize=5)#,label=r'$\mu_B=200\,\mathrm{MeV}$')
ax3.plot(T1,r82mub220,color='darkolivegreen',linewidth=1,markersize=5)#,label=r'$\mu_B=220\,\mathrm{MeV}$')
ax3.plot(T1,r82mub240,color='olive',linewidth=1,markersize=5)#,label=r'$\mu_B=240\,\mathrm{MeV}$')
ax3.plot(T1,r82mub260,color='darkgoldenrod',linewidth=1,markersize=5)#,label=r'$\mu_B=260\,\mathrm{MeV}$')
ax3.plot(T1,r82mub280,color='goldenrod',linewidth=1,markersize=5)#,label=r'$\mu_B=280\,\mathrm{MeV}$')
ax3.plot(T1,r82mub300,color='orange',linewidth=1,markersize=5)#,label=r'$\mu_B=300\,\mathrm{MeV}$')
ax3.plot(T1,r82mub320,color='orangered',linewidth=1,markersize=5)#,label=r'$\mu_B=320\,\mathrm{MeV}$')
ax3.plot(T1,r82mub340,color='red',linewidth=1,markersize=5)#,label=r'$\mu_B=340\,\mathrm{MeV}$')
ax3.plot(T1,r82mub360,color='brown',linewidth=1,markersize=5)#,label=r'$\mu_B=360\,\mathrm{MeV}$')
ax3.plot(T1,r82mub380,color='firebrick',linewidth=1,markersize=5)#,label=r'$\mu_B=380\,\mathrm{MeV}$')
ax3.plot(T1,r82mub400,color='darkred',linewidth=1,markersize=5)#,label=r'$\mu_B=400\,\mathrm{MeV}$')
#ax3.errorbar(WBchix/156,WBchi8/WBchi2,yerr=R82erro,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,label=r'Wuppertal-Budaspest')
ax3.axis([100.,180.,-900,1400])
#ax3.set_xscale('log')

ax3.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
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


fig.savefig("highmub.pdf")

#plt.show()

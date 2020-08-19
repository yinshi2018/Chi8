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
expdata=np.loadtxt('./andronic-origin2.dat')
paradata=np.loadtxt('./paradata.dat')
intdata=np.loadtxt('./intdata.dat')
stardata=np.loadtxt('./stardata.dat')
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
exppoint=ax1.errorbar(expdata[:,2],expdata[:,1],xerr=[expdata[:,6],expdata[:,7]],yerr=[expdata[:,4],expdata[:,5]],color='b',ecolor='b',marker='p',linestyle='',linewidth=1.,markersize=7,alpha=0.5,fillstyle='full',label=r'Experiment',zorder=1)
starpoint=ax1.errorbar(stardata[:,1],stardata[:,3],xerr=[stardata[:,2],stardata[:,2]],yerr=[stardata[:,4],stardata[:,4]],color='r',ecolor='r',marker='o',linestyle='',linewidth=1.,markersize=7,alpha=0.5,fillstyle='full',label=r'STAR',zorder=1)

paraline,=ax1.plot(muB,T,dashes=[4,2],color='b',alpha=0.5,label=r'Parameterization')
#parapoint=ax1.scatter(paradata[:,0],paradata[:,1],color='r',marker='o',alpha=0.5,label=r'Freeze-out',zorder=2)
intpoint=ax1.scatter(intdata[:,0],intdata[:,1],color='k',marker='s',alpha=0.3,zorder=3)
ax1.axis([0,800,55,200])

ax1.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')

#ax1.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
mpl.rcParams['legend.numpoints'] = 1
ax1.legend([(paraline,exppoint),starpoint,intpoint],[r'Andronic et al.',r'STAR',r'freezeout: Andronic et al.'],loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)
plt.axes([0.245, 0.212, 0.29, 0.27]) #不用figure的形式则无须用set
exppoint=plt.errorbar(expdata[:,2],expdata[:,1],xerr=[expdata[:,6],expdata[:,7]],yerr=[expdata[:,4],expdata[:,5]],color='b',ecolor='b',marker='p',linestyle='',linewidth=1.,markersize=7,alpha=0.5,fillstyle='full',label=r'Experiment',zorder=1)
starpoint=plt.errorbar(stardata[:,1],stardata[:,3],xerr=[stardata[:,2],stardata[:,2]],yerr=[stardata[:,4],stardata[:,4]],color='r',ecolor='r',marker='o',linestyle='',linewidth=1.,markersize=7,alpha=0.5,fillstyle='full',label=r'STAR',zorder=1)
#expline,=plt.plot(expdata[:,2],expdata[:,1],color='r',zorder=1)
paraline,=plt.plot(muB,T,dashes=[4,2],color='b',alpha=0.5,label=r'Parameterization')
#parapoint=plt.scatter(paradata[:,0],paradata[:,1],color='r',marker='o',alpha=0.5,label=r'Freeze-out',zorder=2)
intpoint=plt.scatter(intdata[:,0],intdata[:,1],color='k',marker='s',alpha=0.3,zorder=3)

x=range(150,171,5)
plt.xticks(fontsize=8)
plt.yticks(x,fontsize=8)
plt.axis([0.,200.,150.,170.])
#plt.axis([0.,450.,120.,170.])
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("phasediagram.pdf")

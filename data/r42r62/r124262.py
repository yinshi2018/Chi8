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

r12189=np.loadtxt(r'./r12189.dat')
r42189=np.loadtxt(r'./r42189.dat')
r62189=np.loadtxt(r'./r62189.dat')

r12190=np.loadtxt(r'./r12190.dat')
r42190=np.loadtxt(r'./r42190.dat')
r62190=np.loadtxt(r'./r62190.dat')

r12191=np.loadtxt(r'./r12191.dat')
r42191=np.loadtxt(r'./r42191.dat')
r62191=np.loadtxt(r'./r62191.dat')

r12192=np.loadtxt(r'./r12192.dat')
r42192=np.loadtxt(r'./r42192.dat')
r62192=np.loadtxt(r'./r62192.dat')

r12193=np.loadtxt(r'./r12193.dat')
r42193=np.loadtxt(r'./r42193.dat')
r62193=np.loadtxt(r'./r62193.dat')

r12194=np.loadtxt(r'./r12194.dat')
r42194=np.loadtxt(r'./r42194.dat')
r62194=np.loadtxt(r'./r62194.dat')

r12195=np.loadtxt(r'./r12195.dat')
r42195=np.loadtxt(r'./r42195.dat')
r62195=np.loadtxt(r'./r62195.dat')

r12196=np.loadtxt(r'./r12196.dat')
r42196=np.loadtxt(r'./r42196.dat')
r62196=np.loadtxt(r'./r62196.dat')

r12197=np.loadtxt(r'./r12197.dat')
r42197=np.loadtxt(r'./r42197.dat')
r62197=np.loadtxt(r'./r62197.dat')

r12198=np.loadtxt(r'./r12198.dat')
r42198=np.loadtxt(r'./r42198.dat')
r62198=np.loadtxt(r'./r62198.dat')

r12199=np.loadtxt(r'./r12199.dat')
r42199=np.loadtxt(r'./r42199.dat')
r62199=np.loadtxt(r'./r62199.dat')

mub=np.loadtxt(r'./mub.dat')

r42lat155up=np.loadtxt(r'./r42r62mubtlat/r42lat155up.dat')
r42lat155down=np.loadtxt(r'./r42r62mubtlat/r42lat155down.dat')
r42lat158up=np.loadtxt(r'./r42r62mubtlat/r42lat158up.dat')
r42lat158down=np.loadtxt(r'./r42r62mubtlat/r42lat158down.dat')
latmubt=np.loadtxt(r'./r42r62mubtlat/latmubt.dat')

r62latup=np.loadtxt(r'./r42r62mubtlat/r62latup.dat')
r62latdown=np.loadtxt(r'./r42r62mubtlat/r62latdown.dat')
latmubt2=np.loadtxt(r'./r42r62mubtlat/latmubt2.dat')

r12latup=np.loadtxt(r'./r42r62mubtlat/r12latup.dat')
r12latdown=np.loadtxt(r'./r42r62mubtlat/r12latdown.dat')
latmubtr12=np.loadtxt(r'./r42r62mubtlat/latmubtr12.dat')
# Create figure
fig=plt.figure(figsize=(12., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
ax1.plot(mub/189.0,r12189,'-',color='navy',linewidth=1,label=r'$T=189\,\mathrm{MeV}$')
#ax1.plot(mub/190.0,r12190,'-',color='mediumblue',linewidth=1,label=r'$T=190\,\mathrm{MeV}$')
#ax1.plot(mub/191.0,r12191,'-',color='blue',linewidth=1,label=r'$T=191\,\mathrm{MeV}$')
#ax1.plot(mub/192.0,r12192,'-',color='slateblue',linewidth=1,label=r'$T=192\,\mathrm{MeV}$')
#ax1.plot(mub/193.0,r12193,'-',color='steelblue',linewidth=1,label=r'$T=193\,\mathrm{MeV}$')
ax1.plot(mub/194.0,r12194,'-',color='dodgerblue',linewidth=1,label=r'$T=194\,\mathrm{MeV}$')
#ax1.plot(mub/195.0,r12195,'-',color='mediumturquoise',linewidth=1,label=r'$T=195\,\mathrm{MeV}$')
#ax1.plot(mub/196.0,r12196,'-',color='mediumspringgreen',linewidth=1,label=r'$T=196\,\mathrm{MeV}$')
#ax1.plot(mub/197.0,r12197,'-',color='seagreen',linewidth=1,label=r'$T=197\,\mathrm{MeV}$')
#ax1.plot(mub/198.0,r12198,'-',color='olivedrab',linewidth=1,label=r'$T=198\,\mathrm{MeV}$')
ax1.plot(mub/199.0,r12199,'-',color='darkolivegreen',linewidth=1,label=r'$T=199\,\mathrm{MeV}$')
ax1.fill_between(latmubtr12,r12latup,r12latdown,color='g',alpha=0.25,label=r'$T=152-161\,\mathrm{MeV}$')


ax1.axis([0,1.25,0,1.1])
#ax1.set_xscale('log')
ax1.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax1.set_ylabel(r'$R^B_{12}$', fontsize=14, color='black')
ax1.legend(loc=4,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
#plt.text(233,0.8,r'$\mathrm{\beta}=1.33$')
#plt.text(221,0.6,r'$\mathrm{\sqrt{S}}=200\mathrm{GeV}$')

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(132)

ax2.plot(mub/189.0,r42189,'-',color='navy',linewidth=1,label=r'$T=189\,\mathrm{MeV}$')
#ax2.plot(mub/190.0,r42190,'-',color='mediumblue',linewidth=1,label=r'$T=190\,\mathrm{MeV}$')
#ax2.plot(mub/191.0,r42191,'-',color='blue',linewidth=1,label=r'$T=191\,\mathrm{MeV}$')
#ax2.plot(mub/192.0,r42192,'-',color='slateblue',linewidth=1,label=r'$T=192\,\mathrm{MeV}$')
#ax2.plot(mub/193.0,r42193,'-',color='steelblue',linewidth=1,label=r'$T=193\,\mathrm{MeV}$')
ax2.plot(mub/194.0,r42194,'-',color='dodgerblue',linewidth=1,label=r'$T=194\,\mathrm{MeV}$')
#ax2.plot(mub/195.0,r42195,'-',color='mediumturquoise',linewidth=1,label=r'$T=195\,\mathrm{MeV}$')
#ax2.plot(mub/196.0,r42196,'-',color='mediumspringgreen',linewidth=1,label=r'$T=196\,\mathrm{MeV}$')
#ax2.plot(mub/197.0,r42197,'-',color='seagreen',linewidth=1,label=r'$T=197\,\mathrm{MeV}$')
#ax2.plot(mub/198.0,r42198,'-',color='olivedrab',linewidth=1,label=r'$T=198\,\mathrm{MeV}$')
ax2.plot(mub/199.0,r42199,'-',color='darkolivegreen',linewidth=1,label=r'$T=199\,\mathrm{MeV}$')

ax2.fill_between(latmubt,r42lat155up,r42lat155down,color='g',alpha=0.25,label=r'$T=155\,\mathrm{MeV}$')
ax2.fill_between(latmubt,r42lat158up,r42lat158down,color='pink',alpha=0.25,label=r'$T=158\,\mathrm{MeV}$')
ax2.axis([0,1.25,0,1.1])
#ax1.set_xscale('log')
ax2.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax2.set_ylabel(r'$R^B_{42}$', fontsize=14, color='black')
ax2.legend(loc=4,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
#plt.text(233,0.8,r'$\mathrm{\beta}=1.33$')
#plt.text(221,0.6,r'$\mathrm{\sqrt{S}}=200\mathrm{GeV}$')

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax3=fig.add_subplot(133)
ax3.plot(mub/189.0,r62189,'-',color='navy',linewidth=1,label=r'$T=189\,\mathrm{MeV}$')
#ax3.plot(mub/190.0,r62190,'-',color='mediumblue',linewidth=1,label=r'$T=190\,\mathrm{MeV}$')
#ax3.plot(mub/191.0,r62191,'-',color='blue',linewidth=1,label=r'$T=191\,\mathrm{MeV}$')
#ax3.plot(mub/192.0,r62192,'-',color='slateblue',linewidth=1,label=r'$T=192\,\mathrm{MeV}$')
#ax3.plot(mub/193.0,r62193,'-',color='steelblue',linewidth=1,label=r'$T=193\,\mathrm{MeV}$')
ax3.plot(mub/194.0,r62194,'-',color='dodgerblue',linewidth=1,label=r'$T=194\,\mathrm{MeV}$')
#ax3.plot(mub/195.0,r62195,'-',color='mediumturquoise',linewidth=1,label=r'$T=195\,\mathrm{MeV}$')
#ax3.plot(mub/196.0,r62196,'-',color='mediumspringgreen',linewidth=1,label=r'$T=196\,\mathrm{MeV}$')
#ax3.plot(mub/197.0,r62197,'-',color='seagreen',linewidth=1,label=r'$T=197\,\mathrm{MeV}$')
#ax3.plot(mub/198.0,r62198,'-',color='olivedrab',linewidth=1,label=r'$T=198\,\mathrm{MeV}$')
ax3.plot(mub/199.0,r62199,'-',color='darkolivegreen',linewidth=1,label=r'$T=199\,\mathrm{MeV}$')

ax3.fill_between(latmubt2,r62latup,r62latdown,color='g',alpha=0.25,label=r'$Lattice$')

ax3.axis([0,1,-3,1])
#ax1.set_xscale('log')
ax3.set_xlabel('$\mu_B/T$', fontsize=14, color='black')
ax3.set_ylabel(r'$R^B_{62}$', fontsize=14, color='black')
ax3.legend(loc=4,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
#plt.text(233,0.8,r'$\mathrm{\beta}=1.33$')
#plt.text(221,0.6,r'$\mathrm{\sqrt{S}}=200\mathrm{GeV}$')

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


fig.savefig("r12.pdf")

#plt.show()

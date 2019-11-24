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
chi2mub0=np.loadtxt(r'./mub0/chi2.dat')
chi4mub0=np.loadtxt(r'./mub0/chi4.dat')
chi6mub0=np.loadtxt(r'./mub0/chi6.dat')
chi8mub0=np.loadtxt(r'./mub0/chi8.dat')
r42mub0=chi4mub0/chi2mub0
r62mub0=chi6mub0/chi2mub0
r82mub0=chi8mub0/chi2mub0
chi2mub20=np.loadtxt(r'./mub20/chi2.dat')
chi4mub20=np.loadtxt(r'./mub20/chi4.dat')
chi6mub20=np.loadtxt(r'./mub20/chi6.dat')
chi8mub20=np.loadtxt(r'./mub20/chi8.dat')
r42mub20=chi4mub20/chi2mub20
r62mub20=chi6mub20/chi2mub20
r82mub20=chi8mub20/chi2mub20
chi2mub40=np.loadtxt(r'./mub40/chi2.dat')
chi4mub40=np.loadtxt(r'./mub40/chi4.dat')
chi6mub40=np.loadtxt(r'./mub40/chi6.dat')
chi8mub40=np.loadtxt(r'./mub40/chi8.dat')
r42mub40=chi4mub40/chi2mub40
r62mub40=chi6mub40/chi2mub40
r82mub40=chi8mub40/chi2mub40
chi2mub60=np.loadtxt(r'./mub60/chi2.dat')
chi4mub60=np.loadtxt(r'./mub60/chi4.dat')
chi6mub60=np.loadtxt(r'./mub60/chi6.dat')
chi8mub60=np.loadtxt(r'./mub60/chi8.dat')
r42mub60=chi4mub60/chi2mub60
r62mub60=chi6mub60/chi2mub60
r82mub60=chi8mub60/chi2mub60
chi2mub80=np.loadtxt(r'./mub80/chi2.dat')
chi4mub80=np.loadtxt(r'./mub80/chi4.dat')
chi6mub80=np.loadtxt(r'./mub80/chi6.dat')
chi8mub80=np.loadtxt(r'./mub80/chi8.dat')
r42mub80=chi4mub80/chi2mub80
r62mub80=chi6mub80/chi2mub80
r82mub80=chi8mub80/chi2mub80
chi2mub100=np.loadtxt(r'./mub100/chi2.dat')
chi4mub100=np.loadtxt(r'./mub100/chi4.dat')
chi6mub100=np.loadtxt(r'./mub100/chi6.dat')
chi8mub100=np.loadtxt(r'./mub100/chi8.dat')
r42mub100=chi4mub100/chi2mub100
r62mub100=chi6mub100/chi2mub100
r82mub100=chi8mub100/chi2mub100
chi2mub120=np.loadtxt(r'./mub120/chi2.dat')
chi4mub120=np.loadtxt(r'./mub120/chi4.dat')
chi6mub120=np.loadtxt(r'./mub120/chi6.dat')
chi8mub120=np.loadtxt(r'./mub120/chi8.dat')
r42mub120=chi4mub120/chi2mub120
r62mub120=chi6mub120/chi2mub120
r82mub120=chi8mub120/chi2mub120
# Create figure
fig=plt.figure(figsize=(13., 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
ax1.plot(r42mub0,'k-',linewidth=1,markersize=5,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax1.plot(r42mub20,'r-',linewidth=1,markersize=5,label=r'$\mu_B=20\,\mathrm{MeV}$')
ax1.plot(r42mub40,'b-',linewidth=1,markersize=5,label=r'$\mu_B=40\,\mathrm{MeV}$')
ax1.plot(r42mub60,'y-',linewidth=1,markersize=5,label=r'$\mu_B=60\,\mathrm{MeV}$')
ax1.plot(r42mub80,'orange',linewidth=1,markersize=5,label=r'$\mu_B=80\,\mathrm{MeV}$')
ax1.plot(r42mub100,'gray',linewidth=1,markersize=5,label=r'$\mu_B=100\,\mathrm{MeV}$')
ax1.plot(r42mub120,'g-',linewidth=1,markersize=5,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax1.axis([80,300,0,1.2])
#ax1.set_xscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(132)
ax2.plot(r62mub0,'k-',linewidth=1,markersize=5,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax2.plot(r62mub20,'r-',linewidth=1,markersize=5,label=r'$\mu_B=20\,\mathrm{MeV}$')
ax2.plot(r62mub40,'b-',linewidth=1,markersize=5,label=r'$\mu_B=40\,\mathrm{MeV}$')
ax2.plot(r62mub60,'y-',linewidth=1,markersize=5,label=r'$\mu_B=60\,\mathrm{MeV}$')
ax2.plot(r62mub80,'orange',linewidth=1,markersize=5,label=r'$\mu_B=80\,\mathrm{MeV}$')
ax2.plot(r62mub100,'gray',linewidth=1,markersize=5,label=r'$\mu_B=100\,\mathrm{MeV}$')
ax2.plot(r62mub120,'g-',linewidth=1,markersize=5,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax2.axis([80,300,-0.5,1.2])
#ax2.set_xscale('log')

ax2.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(133)
ax3.plot(r82mub0,'k-',linewidth=1,markersize=5,label=r'$\mu_B=0\,\mathrm{MeV}$')
ax3.plot(r82mub20,'r-',linewidth=1,markersize=5,label=r'$\mu_B=20\,\mathrm{MeV}$')
ax3.plot(r82mub40,'b-',linewidth=1,markersize=5,label=r'$\mu_B=40\,\mathrm{MeV}$')
ax3.plot(r82mub60,'y-',linewidth=1,markersize=5,label=r'$\mu_B=60\,\mathrm{MeV}$')
ax3.plot(r82mub80,'orange',linewidth=1,markersize=5,label=r'$\mu_B=80\,\mathrm{MeV}$')
ax3.plot(r82mub100,'gray',linewidth=1,markersize=5,label=r'$\mu_B=100\,\mathrm{MeV}$')
ax3.plot(r82mub120,'g-',linewidth=1,markersize=5,label=r'$\mu_B=120\,\mathrm{MeV}$')
ax3.axis([80,300,-5.8,3.2])
#ax2.set_xscale('log')

ax3.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

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


fig.savefig("r.pdf")

#plt.show()

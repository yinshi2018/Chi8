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
chi2mub29=np.loadtxt(r'./mub29/final/buffer/chi2.dat')
chi4mub29=np.loadtxt(r'./mub29/final/buffer/chi4.dat')
chi6mub29=np.loadtxt(r'./mub29/final/buffer/chi6.dat')
chi8mub29=np.loadtxt(r'./mub29/final/buffer/chi8.dat')
r42mub29=chi4mub29/chi2mub29
r62mub29=chi6mub29/chi2mub29
r82mub29=chi8mub29/chi2mub29
chi2mub91=np.loadtxt(r'./mub91/final/buffer/chi2.dat')
chi4mub91=np.loadtxt(r'./mub91/final/buffer/chi4.dat')
chi6mub91=np.loadtxt(r'./mub91/final/buffer/chi6.dat')
chi8mub91=np.loadtxt(r'./mub91/final/buffer/chi8.dat')
r42mub91=chi4mub91/chi2mub91
r62mub91=chi6mub91/chi2mub91
r82mub91=chi8mub91/chi2mub91
chi2mub142=np.loadtxt(r'./mub142/final/buffer/chi2.dat')
chi4mub142=np.loadtxt(r'./mub142/final/buffer/chi4.dat')
chi6mub142=np.loadtxt(r'./mub142/final/buffer/chi6.dat')
chi8mub142=np.loadtxt(r'./mub142/final/buffer/chi8.dat')
r42mub142=chi4mub142/chi2mub142
r62mub142=chi6mub142/chi2mub142
r82mub142=chi8mub142/chi2mub142
chi2mub198=np.loadtxt(r'./mub198/final/buffer/chi2.dat')
chi4mub198=np.loadtxt(r'./mub198/final/buffer/chi4.dat')
chi6mub198=np.loadtxt(r'./mub198/final/buffer/chi6.dat')
chi8mub198=np.loadtxt(r'./mub198/final/buffer/chi8.dat')
r42mub198=chi4mub198/chi2mub198
r62mub198=chi6mub198/chi2mub198
r82mub198=chi8mub198/chi2mub198
chi2mub262=np.loadtxt(r'./mub262/final/buffer/chi2.dat')
chi4mub262=np.loadtxt(r'./mub262/final/buffer/chi4.dat')
chi6mub262=np.loadtxt(r'./mub262/final/buffer/chi6.dat')
chi8mub262=np.loadtxt(r'./mub262/final/buffer/chi8.dat')
r42mub262=chi4mub262/chi2mub262
r62mub262=chi6mub262/chi2mub262
r82mub262=chi8mub262/chi2mub262
chi2mub404=np.loadtxt(r'./mub404/final/buffer/chi2.dat')
chi4mub404=np.loadtxt(r'./mub404/final/buffer/chi4.dat')
chi6mub404=np.loadtxt(r'./mub404/final/buffer/chi6.dat')
chi8mub404=np.loadtxt(r'./mub404/final/buffer/chi8.dat')
r42mub404=chi4mub404/chi2mub404
r62mub404=chi6mub404/chi2mub404
r82mub404=chi8mub404/chi2mub404
chi2mub541=np.loadtxt(r'./mub541/final/buffer/chi2.dat')
chi4mub541=np.loadtxt(r'./mub541/final/buffer/chi4.dat')
chi6mub541=np.loadtxt(r'./mub541/final/buffer/chi6.dat')
chi8mub541=np.loadtxt(r'./mub541/final/buffer/chi8.dat')
r42mub541=chi4mub541/chi2mub541
r62mub541=chi6mub541/chi2mub541
r82mub541=chi8mub541/chi2mub541

#hotQCDR42=np.loadtxt('data1/hotQCD_R42.dat')
#WBR42=np.loadtxt('data1/WB_R42.dat')
#WBchi2=np.loadtxt('data1/WB_chi2.dat')
#WBchi6=np.loadtxt('data1/WB_chi6.dat')
#WBchi6erro=np.loadtxt('data1/WB_chi6erro.dat')
#WBchi8=np.loadtxt('data1/WB_chi8.dat')
#WBchi8erro=np.loadtxt('data1/WB_chi8erro.dat')
#WBchix=np.loadtxt('data1/WB_chix.dat')
#hotQCDR62=np.loadtxt('data1/hotQCD_R62.dat')
#hotQCDb=np.loadtxt('data1/hotQCDR62_b.dat')
#hotQCDg=np.loadtxt('data1/hotQCDR62_g.dat')
T=np.loadtxt('TMeV.dat')
#R62erro=WBchi6erro/WBchi2
#R82erro=WBchi8erro/WBchi2

T1=T/1#191.5
# Create figure
fig=plt.figure(figsize=(13., 3.5*6))
#fig=plt.figure()
ax1=fig.add_subplot(731)
ax1.plot(T1,r42mub29,'k-',linewidth=1,markersize=5,label=r'$\mu_B=29\,\mathrm{MeV}$')
ax1.axis([100,300,0,1.2])
#ax1.set_xscale('log')
ax1.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')
ax1.legend(loc=1,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
plt.text(233,0.8,r'$\mathrm{\beta}=1.33$')
plt.text(221,0.6,r'$\mathrm{\sqrt{S}}=200\mathrm{GeV}$')

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(732)
ax2.plot(T1,r62mub29,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax2.axis([100,300,-0.5,1.2])
#ax2.set_xscale('log')

ax2.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize=10,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(733)
ax3.plot(T1,r82mub29,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax3.axis([100,300,-2.5,2])
#ax2.set_xscale('log')

ax3.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

ax3.legend(loc=0,fontsize=10,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax3.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax4=fig.add_subplot(734)
ax4.plot(T1,r42mub91,'k-',linewidth=1,markersize=5,label=r'$\mu_B=91\,\mathrm{MeV}$')
ax4.axis([100,300,0,1.2])
#ax1.set_xscale('log')
ax4.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax4.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')
ax4.legend(loc=1,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
plt.text(233,0.8,r'$\mathrm{\beta}=1.33$')
plt.text(221,0.6,r'$\mathrm{\sqrt{S}}=62.4\mathrm{GeV}$')

for label in ax4.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax4.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax5=fig.add_subplot(735)
ax5.plot(T1,r62mub91,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax5.axis([100,300,-0.5,1.2])
#ax2.set_xscale('log')

ax5.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax5.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax5.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax5.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax5.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax6=fig.add_subplot(736)
ax6.plot(T1,r82mub91,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax6.axis([100,300,-4,2.5])
#ax2.set_xscale('log')

ax6.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax6.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

ax6.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax6.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax6.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax7=fig.add_subplot(737)
ax7.plot(T1,r42mub142,'k-',linewidth=1,markersize=5,label=r'$\mu_B=142\,\mathrm{MeV}$')
ax7.axis([100,300,0,1.2])
#ax1.set_xscale('log')
ax7.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax7.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')
ax7.legend(loc=1,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
plt.text(227,0.8,r'$\mathrm{\beta}=1.33$')
plt.text(215,0.6,r'$\mathrm{\sqrt{S}}=39\mathrm{GeV}$')
for label in ax7.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax7.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax8=fig.add_subplot(738)
ax8.plot(T1,r62mub142,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax8.axis([100,300,-0.7,1.4])
#ax2.set_xscale('log')

ax8.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax8.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax8.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax8.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax8.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax9=fig.add_subplot(739)
ax9.plot(T1,r82mub142,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax9.axis([100,300,-7.3,4])
#ax2.set_xscale('log')

ax9.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax9.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

ax9.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax9.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax9.yaxis.get_ticklabels():
    label.set_fontsize(10)   


ax10=fig.add_subplot(7,3,10)
ax10.plot(T1,r42mub198,'k-',linewidth=1,markersize=5,label=r'$\mu_B=198\,\mathrm{MeV}$')
ax10.axis([100,300,0,1.2])
#ax1.set_xscale('log')
ax10.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax10.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')
ax10.legend(loc=1,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
plt.text(227,0.8,r'$\mathrm{\beta}=1.33$')
plt.text(215,0.6,r'$\mathrm{\sqrt{S}}=27\mathrm{GeV}$')
for label in ax10.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax10.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax11=fig.add_subplot(7,3,11)
ax11.plot(T1,r62mub198,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax11.axis([100,300,-1.5,1.5])
#ax2.set_xscale('log')

ax11.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax11.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax11.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax11.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax11.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax12=fig.add_subplot(7,3,12)
ax12.plot(T1,r82mub198,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax12.axis([100,300,-15,9])
#ax2.set_xscale('log')

ax12.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax12.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

ax12.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax12.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax12.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax13=fig.add_subplot(7,3,13)
ax13.plot(T1,r42mub262,'k-',linewidth=1,markersize=5,label=r'$\mu_B=262\,\mathrm{MeV}$')
ax13.axis([100,300,0,1.2])
#ax1.set_xscale('log')
ax13.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax13.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')
ax13.legend(loc=1,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
plt.text(227,0.8,r'$\mathrm{\beta}=1.33$')
plt.text(216,0.6,r'$\mathrm{\sqrt{S}}=19.6\mathrm{GeV}$')

for label in ax13.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax13.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax14=fig.add_subplot(7,3,14)
ax14.plot(T1,r62mub262,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax14.axis([100,300,-3,1.8])
#ax2.set_xscale('log')

ax14.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax14.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax14.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax14.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax14.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax15=fig.add_subplot(7,3,15)
ax15.plot(T1,r82mub262,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax15.axis([100,300,-37,29])
#ax2.set_xscale('log')

ax15.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax15.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

ax15.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax15.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax15.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax16=fig.add_subplot(7,3,16)
ax16.plot(T1,r42mub404,'k-',linewidth=1,markersize=5,label=r'$\mu_B=404\,\mathrm{MeV}$')
ax16.axis([100,300,-0.5,1.6])
#ax1.set_xscale('log')
ax16.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax16.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')
ax16.legend(loc=1,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
plt.text(227,0.9,r'$\mathrm{\beta}=1.33$')
plt.text(216,0.6,r'$\mathrm{\sqrt{S}}=11.5\mathrm{GeV}$')

for label in ax16.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax16.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax17=fig.add_subplot(7,3,17)
ax17.plot(T1,r62mub404,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax17.axis([100,300,-16,10])
#ax2.set_xscale('log')

ax17.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax17.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax17.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax17.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax17.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax18=fig.add_subplot(7,3,18)
ax18.plot(T1,r82mub404,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax18.axis([100,300,-350,450])
#ax2.set_xscale('log')

ax18.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax18.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

ax18.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax18.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax18.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax19=fig.add_subplot(7,3,19)
ax19.plot(T1,r42mub541,'k-',linewidth=1,markersize=5,label=r'$\mu_B=541\,\mathrm{MeV}$')
ax19.axis([100,300,-3,3.2])
#ax1.set_xscale('log')
ax19.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax19.set_ylabel(r'$\chi_4/\chi_2$', fontsize=14, color='black')
ax19.legend(loc=1,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)
plt.text(227,1.2,r'$\mathrm{\beta}=1.33$')
plt.text(216,0.3,r'$\mathrm{\sqrt{S}}=7.7\mathrm{GeV}$')

for label in ax19.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax19.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax20=fig.add_subplot(7,3,20)
ax20.plot(T1,r62mub541,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax20.axis([100,300,-130,120])
#ax2.set_xscale('log')

ax20.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax20.set_ylabel(r'$\chi_6/\chi_2$', fontsize=14, color='black')

ax20.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax20.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax20.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax21=fig.add_subplot(7,3,21)
ax21.plot(T1,r82mub541,'k-',linewidth=1,markersize=5)#,label=r'$\mu_B=0\,\mathrm{MeV}$')

ax21.axis([100,300,-9000,12000])
#ax2.set_xscale('log')

ax21.set_xlabel('$T/T_c\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax21.set_ylabel(r'$\chi_8/\chi_2$', fontsize=14, color='black')

ax21.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax21.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax21.yaxis.get_ticklabels():
    label.set_fontsize(10)
#for ax in fig.axes:
#    ax.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
#plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
fig.subplots_adjust(top=0.95, bottom=0.05, left=0.07, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("finmub.pdf")

#plt.show()

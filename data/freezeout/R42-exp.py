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

# Data for plotting
chi222=np.loadtxt('./mub22/cmucen/final/buffer/chi2.dat')
chi422=np.loadtxt('./mub22/cmucen/final/buffer/chi4.dat')
chi622=np.loadtxt('./mub22/cmucen/final/buffer/chi6.dat')
r4222=chi422/chi222
r6222=chi622/chi222
chi268=np.loadtxt('./mub68/cmucen/final/buffer/chi2.dat')
chi468=np.loadtxt('./mub68/cmucen/final/buffer/chi4.dat')
chi668=np.loadtxt('./mub68/cmucen/final/buffer/chi6.dat')
r4268=chi468/chi268
r6268=chi668/chi268
chi2106=np.loadtxt('./mub106/cmucen/final/buffer/chi2.dat')
chi4106=np.loadtxt('./mub106/cmucen/final/buffer/chi4.dat')
chi6106=np.loadtxt('./mub106/cmucen/final/buffer/chi6.dat')
r42106=chi4106/chi2106
r62106=chi6106/chi2106
chi2148=np.loadtxt('./mub148/cmucen/final/buffer/chi2.dat')
chi4148=np.loadtxt('./mub148/cmucen/final/buffer/chi4.dat')
chi6148=np.loadtxt('./mub148/cmucen/final/buffer/chi6.dat')
r42148=chi4148/chi2148
r62148=chi6148/chi2148
chi2196=np.loadtxt('./mub196/cmucen/final/buffer/chi2.dat')
chi4196=np.loadtxt('./mub196/cmucen/final/buffer/chi4.dat')
chi6196=np.loadtxt('./mub196/cmucen/final/buffer/chi6.dat')
r42196=chi4196/chi2196
r62196=chi6196/chi2196
chi2252=np.loadtxt('./mub252/cmucen/final/buffer/chi2.dat')
chi4252=np.loadtxt('./mub252/cmucen/final/buffer/chi4.dat')
chi6252=np.loadtxt('./mub252/cmucen/final/buffer/chi6.dat')
r42252=chi4252/chi2252
r62252=chi6252/chi2252
chi2303=np.loadtxt('./mub303/cmucen/final/buffer/chi2.dat')
chi4303=np.loadtxt('./mub303/cmucen/final/buffer/chi4.dat')
chi6303=np.loadtxt('./mub303/cmucen/final/buffer/chi6.dat')
r42303=chi4303/chi2303
r62303=chi6303/chi2303
chi2406=np.loadtxt('./mub406/cmucen/final/buffer/chi2.dat')
chi4406=np.loadtxt('./mub406/cmucen/final/buffer/chi4.dat')
chi6406=np.loadtxt('./mub406/cmucen/final/buffer/chi6.dat')
r42406=chi4406/chi2406
r62406=chi6406/chi2406
T=np.loadtxt('./TMeV.dat')
data=np.zeros(300)
data2=np.zeros(300)
data3=np.zeros(300)
data4=np.zeros(300)
y62=np.linspace(-10,10,100)
T22up=np.zeros(100)
T22down=np.zeros(100)
T106up=np.zeros(100)
T106down=np.zeros(100)
T148up=np.zeros(100)
T148down=np.zeros(100)
T196up=np.zeros(100)
T196down=np.zeros(100)
for num in range(0,300):
    data[num]=0.906665
    data2[num]=0.700494
    data3[num]=0.220035
    data4[num]=0.235239

for num in range(0,100):
    T22up[num]=152
    T22down[num]=149
    T106up[num]=158
    T106down[num]=154
    T148up[num]=178
    T148down[num]=172
    T196up[num]=168
    T196down[num]=160

datavalue=[0.906665,1.170696,0.700494,0.220035,0.235239,1.623427,1.450839,3.475754]
dataerr=[0.111087,0.232281,0.150150,0.221793,0.341411,0.395317,0.604139,1.020652]
energy=[200.,62.4,39.,27.,19.6,14.5,11.5,7.7]
dif22cen=abs(r4222-0.906665)
dif22up=abs(r4222-(datavalue[0]+dataerr[0]))
dif22down=abs(r4222-(datavalue[0]-dataerr[0]))
min22cen_index=np.argmin(dif22cen[80:300])+80
min22up_index=np.argmin(dif22up[80:300])+80
min22down_index=np.argmin(dif22down[80:300])+80
dif68cen=abs(r4268-1.170696)
dif68up=abs(r4268-(datavalue[1]+dataerr[1]))
dif68down=abs(r4268-(datavalue[1]-dataerr[1]))
min68cen_index=np.argmin(dif68cen[80:300])+80
min68up_index=np.argmin(dif68up[80:300])+80
min68down_index=np.argmin(dif68down[80:300])+80
dif106cen=abs(r42106-0.700494)
dif106up=abs(r42106-(datavalue[2]+dataerr[2]))
dif106down=abs(r42106-(datavalue[2]-dataerr[2]))
min106cen_index=np.argmin(dif106cen[80:300])+80
min106up_index=np.argmin(dif106up[80:300])+80
min106down_index=np.argmin(dif106down[80:300])+80
dif148cen=abs(r42148-0.220035)
dif148up=abs(r42148-(datavalue[3]+dataerr[3]))
dif148down=abs(r42148-(datavalue[3]-dataerr[3]))
min148cen_index=np.argmin(dif148cen[80:300])+80
min148up_index=np.argmin(dif148up[80:300])+80
min148down_index=np.argmin(dif148down[80:300])+80
dif196cen=abs(r42196-0.235239)
dif196up=abs(r42196-(datavalue[4]+dataerr[4]))
dif196down=abs(r42196-(datavalue[4]-dataerr[4]))
min196cen_index=np.argmin(dif196cen[80:300])+80
min196up_index=np.argmin(dif196up[80:300])+80
min196down_index=np.argmin(dif196down[80:300])+80
dif252cen=abs(r42252-1.623427)
dif252up=abs(r42252-(datavalue[5]+dataerr[5]))
dif252down=abs(r42252-(datavalue[5]-dataerr[5]))
min252cen_index=np.argmin(dif252cen[80:300])+80
min252up_index=np.argmin(dif252up[80:300])+80
min252down_index=np.argmin(dif252down[80:300])+80
dif303cen=abs(r42303-1.450839)
dif303up=abs(r42303-(datavalue[6]+dataerr[6]))
dif303down=abs(r42303-(datavalue[6]-dataerr[6]))
min303cen_index=np.argmin(dif303cen[80:300])+80
min303up_index=np.argmin(dif303up[80:300])+80
min303down_index=np.argmin(dif303down[80:300])+80
dif406cen=abs(r42406-3.475754)
dif406up=abs(r42406-(datavalue[7]+dataerr[7]))
dif406down=abs(r42406-(datavalue[7]-dataerr[7]))
min406cen_index=np.argmin(dif406cen[80:300])+80
min406up_index=np.argmin(dif406up[80:300])+80
min406down_index=np.argmin(dif406down[80:300])+80

R62cenfit=[r6222[min22cen_index],r62106[min106cen_index],r62148[min148cen_index],r62196[min196cen_index]]
R62upfit=[r6222[min22up_index],r62106[min106up_index],r62148[min148up_index],r62196[min196up_index]]
R62downfit=[r6222[min22down_index],r62106[min106down_index],r62148[min148down_index],r62196[min196down_index]]
energy=[200.,39.,27.,19.6]
#############################################################################################################################################
xsame=np.linspace(0.,299.,300)
ctcen=1.247
ctup=1.259
ctdown=1.235
ct=np.linspace(ctdown,ctup,10)
chi2mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi2.dat')
chi4mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi4.dat')
chi6mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi6.dat')
chi8mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi8.dat')
r42mub22cen=chi4mub22cen/chi2mub22cen
r62mub22cen=chi6mub22cen/chi2mub22cen
r82mub22cen=chi8mub22cen/chi2mub22cen
chi2mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi2.dat')
chi4mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi4.dat')
chi6mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi6.dat')
chi8mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi8.dat')
r42mub22up=chi4mub22up/chi2mub22up
r62mub22up=chi6mub22up/chi2mub22up
r82mub22up=chi8mub22up/chi2mub22up
chi2mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi2.dat')
chi4mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi4.dat')
chi6mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi6.dat')
chi8mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi8.dat')
r42mub22down=chi4mub22down/chi2mub22down
r62mub22down=chi6mub22down/chi2mub22down
r82mub22down=chi8mub22down/chi2mub22down
r4222=np.zeros((300,20))
r6222=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r4222[:,t]=spline(T/ct[t],r42mub22up,xsame)
    else:
       r4222[:,t]=spline(T/ct[t-10],r42mub22down,xsame)


for num in range(1,20):
    if num==1:
       max22=np.maximum(r4222[:,num-1],r4222[:,num])
       min22=np.minimum(r4222[:,num-1],r4222[:,num])
    else:
       max22=np.maximum(max22,r4222[:,num])
       min22=np.minimum(min22,r4222[:,num])

for t in range(0,20):
    if t<10:
       r6222[:,t]=spline(T/ct[t],r62mub22up,xsame)
    else:
       r6222[:,t]=spline(T/ct[t-10],r62mub22down,xsame)


for num in range(1,20):
    if num==1:
       max6222=np.maximum(r6222[:,num-1],r6222[:,num])
       min6222=np.minimum(r6222[:,num-1],r6222[:,num])
    else:
       max6222=np.maximum(max6222,r6222[:,num])
       min6222=np.minimum(min6222,r6222[:,num])

r42mub22cen=spline(T/ctcen,r42mub22cen,xsame)
r62mub22cen=spline(T/ctcen,r62mub22cen,xsame)

dif22cen=abs(r42mub22cen-0.906665)
dif22up=abs(max22-0.906665)
dif22down=abs(min22-0.906665)
min22cen_index=np.argmin(dif22cen[80:300])+80
min22up_index=np.argmin(dif22up[80:300])+80
min22down_index=np.argmin(dif22down[80:300])+80
print(min22up_index)
print(min22down_index)
r62=[max6222[min22up_index],max6222[min22down_index],min6222[min22up_index],min6222[min22down_index]]
r6222up=np.max(r62)
r6222down=np.min(r62)
print(r6222up)
print(r6222down)

####################################################################################################
chi2mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi2.dat')
chi4mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi4.dat')
chi6mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi6.dat')
chi8mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi8.dat')
r42mub68cen=chi4mub68cen/chi2mub68cen
r62mub68cen=chi6mub68cen/chi2mub68cen
r82mub68cen=chi8mub68cen/chi2mub68cen
chi2mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi2.dat')
chi4mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi4.dat')
chi6mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi6.dat')
chi8mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi8.dat')
r42mub68up=chi4mub68up/chi2mub68up
r62mub68up=chi6mub68up/chi2mub68up
r82mub68up=chi8mub68up/chi2mub68up
chi2mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi2.dat')
chi4mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi4.dat')
chi6mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi6.dat')
chi8mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi8.dat')
r42mub68down=chi4mub68down/chi2mub68down
r62mub68down=chi6mub68down/chi2mub68down
r82mub68down=chi8mub68down/chi2mub68down
####################################################################################################
chi2mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi2.dat')
chi4mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi4.dat')
chi6mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi6.dat')
chi8mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi8.dat')
r42mub106cen=chi4mub106cen/chi2mub106cen
r62mub106cen=chi6mub106cen/chi2mub106cen
r82mub106cen=chi8mub106cen/chi2mub106cen
chi2mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi2.dat')
chi4mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi4.dat')
chi6mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi6.dat')
chi8mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi8.dat')
r42mub106up=chi4mub106up/chi2mub106up
r62mub106up=chi6mub106up/chi2mub106up
r82mub106up=chi8mub106up/chi2mub106up
chi2mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi2.dat')
chi4mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi4.dat')
chi6mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi6.dat')
chi8mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi8.dat')
r42mub106down=chi4mub106down/chi2mub106down
r62mub106down=chi6mub106down/chi2mub106down
r82mub106down=chi8mub106down/chi2mub106down
r42106=np.zeros((300,20))
r62106=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r42106[:,t]=spline(T/ct[t],r42mub106up,xsame)
    else:
       r42106[:,t]=spline(T/ct[t-10],r42mub106down,xsame)


for num in range(1,20):
    if num==1:
       max106=np.maximum(r42106[:,num-1],r42106[:,num])
       min106=np.minimum(r42106[:,num-1],r42106[:,num])
    else:
       max106=np.maximum(max106,r42106[:,num])
       min106=np.minimum(min106,r42106[:,num])

for t in range(0,20):
    if t<10:
       r62106[:,t]=spline(T/ct[t],r62mub106up,xsame)
    else:
       r62106[:,t]=spline(T/ct[t-10],r62mub106down,xsame)


for num in range(1,20):
    if num==1:
       max62106=np.maximum(r62106[:,num-1],r62106[:,num])
       min62106=np.minimum(r62106[:,num-1],r62106[:,num])
    else:
       max62106=np.maximum(max62106,r62106[:,num])
       min62106=np.minimum(min62106,r62106[:,num])

r42mub106cen=spline(T/ctcen,r42mub106cen,xsame)
r62mub106cen=spline(T/ctcen,r62mub106cen,xsame)

dif106cen=abs(r42mub106cen-0.700494)
dif106up=abs(max106-0.700494)
dif106down=abs(min106-0.700494)
min106cen_index=np.argmin(dif106cen[80:300])+80
min106up_index=np.argmin(dif106up[80:300])+80
min106down_index=np.argmin(dif106down[80:300])+80
print(min106up_index)
print(min106down_index)
r62=[max62106[min106up_index],max62106[min106down_index],min62106[min106up_index],min62106[min106down_index]]
r62106up=np.max(r62)
r62106down=np.min(r62)
print(r62106up)
print(r62106down)
####################################################################################################
chi2mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi2.dat')
chi4mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi4.dat')
chi6mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi6.dat')
chi8mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi8.dat')
r42mub148cen=chi4mub148cen/chi2mub148cen
r62mub148cen=chi6mub148cen/chi2mub148cen
r82mub148cen=chi8mub148cen/chi2mub148cen
chi2mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi2.dat')
chi4mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi4.dat')
chi6mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi6.dat')
chi8mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi8.dat')
r42mub148up=chi4mub148up/chi2mub148up
r62mub148up=chi6mub148up/chi2mub148up
r82mub148up=chi8mub148up/chi2mub148up
chi2mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi2.dat')
chi4mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi4.dat')
chi6mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi6.dat')
chi8mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi8.dat')
r42mub148down=chi4mub148down/chi2mub148down
r62mub148down=chi6mub148down/chi2mub148down
r82mub148down=chi8mub148down/chi2mub148down
r42148=np.zeros((300,20))
r62148=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r42148[:,t]=spline(T/ct[t],r42mub148up,xsame)
    else:
       r42148[:,t]=spline(T/ct[t-10],r42mub148down,xsame)


for num in range(1,20):
    if num==1:
       max148=np.maximum(r42148[:,num-1],r42148[:,num])
       min148=np.minimum(r42148[:,num-1],r42148[:,num])
    else:
       max148=np.maximum(max148,r42148[:,num])
       min148=np.minimum(min148,r42148[:,num])

for t in range(0,20):
    if t<10:
       r62148[:,t]=spline(T/ct[t],r62mub148up,xsame)
    else:
       r62148[:,t]=spline(T/ct[t-10],r62mub148down,xsame)


for num in range(1,20):
    if num==1:
       max62148=np.maximum(r62148[:,num-1],r62148[:,num])
       min62148=np.minimum(r62148[:,num-1],r62148[:,num])
    else:
       max62148=np.maximum(max62148,r62148[:,num])
       min62148=np.minimum(min62148,r62148[:,num])

r42mub148cen=spline(T/ctcen,r42mub148cen,xsame)
r62mub148cen=spline(T/ctcen,r62mub148cen,xsame)

dif148cen=abs(r42mub148cen-0.220035)
dif148up=abs(max148-0.220035)
dif148down=abs(min148-0.220035)
min148cen_index=np.argmin(dif148cen[80:300])+80
min148up_index=np.argmin(dif148up[80:300])+80
min148down_index=np.argmin(dif148down[80:300])+80
print(min148up_index)
print(min148down_index)
r62=[max62148[min148up_index],max62148[min148down_index],min62148[min148up_index],min62148[min148down_index]]
r62148up=np.max(r62)
r62148down=np.min(r62)
print(r62148up)
print(r62148down)
####################################################################################################
chi2mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi2.dat')
chi4mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi4.dat')
chi6mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi6.dat')
chi8mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi8.dat')
r42mub196cen=chi4mub196cen/chi2mub196cen
r62mub196cen=chi6mub196cen/chi2mub196cen
r82mub196cen=chi8mub196cen/chi2mub196cen
chi2mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi2.dat')
chi4mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi4.dat')
chi6mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi6.dat')
chi8mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi8.dat')
r42mub196up=chi4mub196up/chi2mub196up
r62mub196up=chi6mub196up/chi2mub196up
r82mub196up=chi8mub196up/chi2mub196up
chi2mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi2.dat')
chi4mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi4.dat')
chi6mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi6.dat')
chi8mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi8.dat')
r42mub196up1=chi4mub196up1/chi2mub196up1
r62mub196up1=chi6mub196up1/chi2mub196up1
r82mub196up1=chi8mub196up1/chi2mub196up1
chi2mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi2.dat')
chi4mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi4.dat')
chi6mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi6.dat')
chi8mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi8.dat')
r42mub196up2=chi4mub196up2/chi2mub196up2
r62mub196up2=chi6mub196up2/chi2mub196up2
r82mub196up2=chi8mub196up2/chi2mub196up2
chi2mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi2.dat')
chi4mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi4.dat')
chi6mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi6.dat')
chi8mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi8.dat')
r42mub196up3=chi4mub196up3/chi2mub196up3
r62mub196up3=chi6mub196up3/chi2mub196up3
r82mub196up3=chi8mub196up3/chi2mub196up3
chi2mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi2.dat')
chi4mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi4.dat')
chi6mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi6.dat')
chi8mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi8.dat')
r42mub196up4=chi4mub196up4/chi2mub196up4
r62mub196up4=chi6mub196up4/chi2mub196up4
r82mub196up4=chi8mub196up4/chi2mub196up4
chi2mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi2.dat')
chi4mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi4.dat')
chi6mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi6.dat')
chi8mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi8.dat')
r42mub196down=chi4mub196down/chi2mub196down
r62mub196down=chi6mub196down/chi2mub196down
r82mub196down=chi8mub196down/chi2mub196down
chi2mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi2.dat')
chi4mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi4.dat')
chi6mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi6.dat')
chi8mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi8.dat')
r42mub196down1=chi4mub196down1/chi2mub196down1
r62mub196down1=chi6mub196down1/chi2mub196down1
r82mub196down1=chi8mub196down1/chi2mub196down1
chi2mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi2.dat')
chi4mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi4.dat')
chi6mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi6.dat')
chi8mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi8.dat')
r42mub196down2=chi4mub196down2/chi2mub196down2
r62mub196down2=chi6mub196down2/chi2mub196down2
r82mub196down2=chi8mub196down2/chi2mub196down2
chi2mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi2.dat')
chi4mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi4.dat')
chi6mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi6.dat')
chi8mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi8.dat')
r42mub196down3=chi4mub196down3/chi2mub196down3
r62mub196down3=chi6mub196down3/chi2mub196down3
r82mub196down3=chi8mub196down3/chi2mub196down3
chi2mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi2.dat')
chi4mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi4.dat')
chi6mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi6.dat')
chi8mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi8.dat')
r42mub196down4=chi4mub196down4/chi2mub196down4
r62mub196down4=chi6mub196down4/chi2mub196down4
r82mub196down4=chi8mub196down4/chi2mub196down4
r42196=np.zeros((300,100))
r62196=np.zeros((300,100))
for t in range(0,100):
    if t<10:
       r42196[:,t]=spline(T/ct[t],r42mub196up,xsame)
    else:
       if t>=10 and t<20:
          r42196[:,t]=spline(T/ct[t-10],r42mub196up1,xsame)
       else:
          if t>=20 and t<30:
             r42196[:,t]=spline(T/ct[t-20],r42mub196up2,xsame)
          else: 
             if t>=30 and t<40:
                r42196[:,t]=spline(T/ct[t-30],r42mub196up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42196[:,t]=spline(T/ct[t-40],r42mub196up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42196[:,t]=spline(T/ct[t-50],r42mub196down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42196[:,t]=spline(T/ct[t-60],r42mub196down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42196[:,t]=spline(T/ct[t-70],r42mub196down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42196[:,t]=spline(T/ct[t-80],r42mub196down3,xsame)
                            else:
                                r42196[:,t]=spline(T/ct[t-90],r42mub196down4,xsame)

for t in range(0,100):
    if t<10:
       r62196[:,t]=spline(T/ct[t],r62mub196up,xsame)
    else:
       if t>=10 and t<20:
          r62196[:,t]=spline(T/ct[t-10],r62mub196up1,xsame)
       else:
          if t>=20 and t<30:
             r62196[:,t]=spline(T/ct[t-20],r62mub196up2,xsame)
          else: 
             if t>=30 and t<40:
                r62196[:,t]=spline(T/ct[t-30],r62mub196up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62196[:,t]=spline(T/ct[t-40],r62mub196up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62196[:,t]=spline(T/ct[t-50],r62mub196down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62196[:,t]=spline(T/ct[t-60],r62mub196down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62196[:,t]=spline(T/ct[t-70],r62mub196down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62196[:,t]=spline(T/ct[t-80],r62mub196down3,xsame)
                            else:
                                r62196[:,t]=spline(T/ct[t-90],r62mub196down4,xsame)


for num in range(1,100):
    if num==1:
       max196=np.maximum(r42196[:,num-1],r42196[:,num])
       min196=np.minimum(r42196[:,num-1],r42196[:,num])
    else:
       max196=np.maximum(max196,r42196[:,num])
       min196=np.minimum(min196,r42196[:,num])

for num in range(1,100):
    if num==1:
       max62196=np.maximum(r62196[:,num-1],r62196[:,num])
       min62196=np.minimum(r62196[:,num-1],r62196[:,num])
    else:
       max62196=np.maximum(max62196,r62196[:,num])
       min62196=np.minimum(min62196,r62196[:,num])

r42mub196cen=spline(T/ctcen,r42mub196cen,xsame)
r62mub196cen=spline(T/ctcen,r62mub196cen,xsame)

dif196cen=abs(r42mub196cen-0.235239)
dif196up=abs(max196-0.235239)
dif196down=abs(min196-0.235239)
min196cen_index=np.argmin(dif196cen[80:300])+80
min196up_index=np.argmin(dif196up[80:300])+80
min196down_index=np.argmin(dif196down[80:300])+80
print(min196up_index)
print(min196down_index)
r62=[max62196[min196up_index],max62196[min196down_index],min62196[min196up_index],min62196[min196down_index]]
r62196up=np.max(r62)
r62196down=np.min(r62)
print(r62196up)
print(r62196down)
####################################################################################################
r62up=[r6222up,r62106up,r62148up,r62196up]
r62down=[r6222down,r62106down,r62148down,r62196down]
r62cen=np.zeros(4)
r62err=np.zeros(4)
for i in range(0,4):
    r62cen[i]=(r62up[i]+r62down[i])/2.
    r62err[i]=(r62up[i]-r62down[i])/2.
####################################################################################################
# Create figure
fig=plt.figure(figsize=(12, 10.5))
#fig=plt.figure()
ax1=fig.add_subplot(331)
#band_mub100=ax1.fill_between(xsame,max22,min22,alpha=0.25,facecolor='b',edgecolor='')
#line_mub100,=ax1.plot(xsame,r42mub22cen,'b',linewidth=1,alpha=0.5)
#ax1.plot(energy,r62up)
#ax1.plot(energy,r62down)
ax1.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax1.plot(xsame,data)
#ax1.legend(( ),(r'This work $T=155$ MeV'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax1.set_xscale('log')
plt.axis([10,230,-2.,2.])
ax1.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax2=fig.add_subplot(332)
band_mub=ax2.fill_between(xsame,max22,min22,alpha=0.25,facecolor='b',edgecolor='',label=r'$200$')
line_mub,=ax2.plot(xsame,r42mub22cen,'b',linewidth=1,alpha=0.5)
ax2.plot(xsame,data)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
ax2.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')
for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(333)
band_mub=ax3.fill_between(xsame,max106,min106,alpha=0.25,facecolor='b',edgecolor='',label=r'$39$')
line_mub,=ax3.plot(xsame,r42mub106cen,'b',linewidth=1,alpha=0.5)
ax3.plot(xsame,data2)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
ax3.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax3.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')
for label in ax3.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax4=fig.add_subplot(334)
band_mub=ax4.fill_between(xsame,max148,min148,alpha=0.25,facecolor='b',edgecolor='',label=r'$27$')
line_mub,=ax4.plot(xsame,r42mub148cen,'b',linewidth=1,alpha=0.5)
ax4.plot(xsame,data3)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
ax4.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax4.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')
for label in ax4.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax4.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax5=fig.add_subplot(335)
band_mub=ax5.fill_between(xsame,max196,min196,alpha=0.25,facecolor='b',edgecolor='',label=r'$19.6$')
line_mub,=ax5.plot(xsame,r42mub196cen,'b',linewidth=1,alpha=0.5)
ax5.plot(xsame,data4)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
ax5.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax5.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')
for label in ax5.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax5.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax6=fig.add_subplot(336)
band_mub=ax6.fill_between(xsame,max6222,min6222,alpha=0.25,facecolor='b',edgecolor='',label=r'$200$')
line_mub,=ax6.plot(xsame,r62mub22cen,'b',linewidth=1,alpha=0.5)
ax6.plot(T22up,y62)
ax6.plot(T22down,y62)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
ax6.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-0.5,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax6.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax6.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax6.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax7=fig.add_subplot(337)
band_mub=ax7.fill_between(xsame,max62106,min62106,alpha=0.25,facecolor='b',edgecolor='',label=r'$39$')
line_mub,=ax7.plot(xsame,r62mub106cen,'b',linewidth=1,alpha=0.5)
ax7.plot(T106up,y62)
ax7.plot(T106down,y62)
ax7.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-1,1.4])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax7.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax7.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax7.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax8=fig.add_subplot(338)
band_mub=ax8.fill_between(xsame,max62148,min62148,alpha=0.25,facecolor='b',edgecolor='',label=r'$27$')
line_mub,=ax8.plot(xsame,r62mub148cen,'b',linewidth=1,alpha=0.5)
ax8.plot(T148up,y62)
ax8.plot(T148down,y62)
ax8.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-1,1.5])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax8.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax8.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax8.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax9=fig.add_subplot(339)
band_mub=ax9.fill_between(xsame,max62196,min62196,alpha=0.25,facecolor='b',edgecolor='',label=r'$19.6$')
line_mub,=ax9.plot(xsame,r62mub196cen,'b',linewidth=1,alpha=0.5)
ax9.plot(T196up,y62)
ax9.plot(T196down,y62)
ax9.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-2.2,1.7])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax9.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax9.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax9.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("R62-exp.pdf")

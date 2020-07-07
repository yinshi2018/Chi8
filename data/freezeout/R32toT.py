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
chi322=np.loadtxt('./mub22/cmucen/final/buffer/chi3.dat')
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
data200=np.zeros(300)
data62=np.zeros(300)
data39=np.zeros(300)
data27=np.zeros(300)
data19=np.zeros(300)
data11=np.zeros(300)
data7=np.zeros(300)
y62=np.linspace(-100,100,100)
T22up=np.zeros(100)
T22down=np.zeros(100)
T68up=np.zeros(100)
T68down=np.zeros(100)
T106up=np.zeros(100)
T106down=np.zeros(100)
T148up=np.zeros(100)
T148down=np.zeros(100)
T196up=np.zeros(100)
T196down=np.zeros(100)
T303up=np.zeros(100)
T303down=np.zeros(100)
T406up=np.zeros(100)
T406down=np.zeros(100)
for num in range(0,300):
    data200[num]=0.122195
    data62[num]=0.302545
    data39[num]=0.432666
    data27[num]=0.541676
    data19[num]=0.612299
    data11[num]=0.680635
    data7[num]=0.60824

datavalue=[0.906665,1.170696,0.700494,0.220035,0.235239,1.623427,1.450839,3.475754]
dataerr=[0.111087,0.232281,0.150150,0.221793,0.341411,0.395317,0.604139,1.020652]
energy=[200.,62.4,39.,27.,19.6,11.5,7.7]
#energy=[200.,39.,27.,19.6]
#############################################################################################################################################
xsame=np.linspace(0.,299.,300)
ctcen=1.247
ctup=1.259
ctdown=1.235
ct=np.linspace(ctdown,ctup,10)
chi2mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi2.dat')
chi3mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi3.dat')
chi4mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi4.dat')
chi6mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi6.dat')
chi8mub22cen=np.loadtxt(r'./mub22/cmucen/final/buffer/chi8.dat')
r32mub22cen=chi3mub22cen/chi2mub22cen
r42mub22cen=chi4mub22cen/chi2mub22cen
r62mub22cen=chi6mub22cen/chi2mub22cen
r82mub22cen=chi8mub22cen/chi2mub22cen
chi2mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi2.dat')
chi3mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi3.dat')
chi4mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi4.dat')
chi6mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi6.dat')
chi8mub22up=np.loadtxt(r'./mub22/cmuup/final/buffer/chi8.dat')
r32mub22up=chi3mub22up/chi2mub22up
r42mub22up=chi4mub22up/chi2mub22up
r62mub22up=chi6mub22up/chi2mub22up
r82mub22up=chi8mub22up/chi2mub22up
chi2mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi2.dat')
chi3mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi3.dat')
chi4mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi4.dat')
chi6mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi6.dat')
chi8mub22down=np.loadtxt(r'./mub22/cmudown/final/buffer/chi8.dat')
r32mub22down=chi3mub22down/chi2mub22down
r42mub22down=chi4mub22down/chi2mub22down
r62mub22down=chi6mub22down/chi2mub22down
r82mub22down=chi8mub22down/chi2mub22down
r3222=np.zeros((300,20))
r4222=np.zeros((300,20))
r6222=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r3222[:,t]=spline(T/ct[t],r32mub22up,xsame)
    else:
       r3222[:,t]=spline(T/ct[t-10],r32mub22down,xsame)


for num in range(1,20):
    if num==1:
       max22=np.maximum(r3222[:,num-1],r3222[:,num])
       min22=np.minimum(r3222[:,num-1],r3222[:,num])
    else:
       max22=np.maximum(max22,r3222[:,num])
       min22=np.minimum(min22,r3222[:,num])

for t in range(0,20):
    if t<10:
       r4222[:,t]=spline(T/ct[t],r42mub22up,xsame)
    else:
       r4222[:,t]=spline(T/ct[t-10],r42mub22down,xsame)

for t in range(0,20):
    if t<10:
       r4222[:,t]=spline(T/ct[t],r42mub22up,xsame)
    else:
       r4222[:,t]=spline(T/ct[t-10],r42mub22down,xsame)


for num in range(1,20):
    if num==1:
       max4222=np.maximum(r4222[:,num-1],r4222[:,num])
       min4222=np.minimum(r4222[:,num-1],r4222[:,num])
    else:
       max4222=np.maximum(max4222,r4222[:,num])
       min4222=np.minimum(min4222,r4222[:,num])

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

r32mub22cen=spline(T/ctcen,r32mub22cen,xsame)
r42mub22cen=spline(T/ctcen,r42mub22cen,xsame)
r62mub22cen=spline(T/ctcen,r62mub22cen,xsame)

dif22cen=abs(r32mub22cen-0.122195)
dif22up=abs(max22-0.122195)
dif22down=abs(min22-0.122195)
min22cen_index=np.argmin(dif22cen[80:300])+80
min22up_index=np.argmin(dif22up[80:300])+80
min22down_index=np.argmin(dif22down[80:300])+80
print(min22up_index)
print(min22down_index)
r42=[max4222[min22up_index],max4222[min22down_index],min4222[min22up_index],min4222[min22down_index]]
r42h=[max4222[min22up_index+5],max4222[min22down_index+5],min4222[min22up_index+5],min4222[min22down_index+5]]
r42l=[max4222[min22up_index-5],max4222[min22down_index-5],min4222[min22up_index-5],min4222[min22down_index-5]]
r4222up=np.max(r42)
r4222down=np.min(r42)
r4222uph=np.max(r42h)
r4222downh=np.min(r42h)
r4222upl=np.max(r42l)
r4222downl=np.min(r42l)
r62=[max6222[min22up_index],max6222[min22down_index],min6222[min22up_index],min6222[min22down_index]]
r62h=[max6222[min22up_index+5],max6222[min22down_index+5],min6222[min22up_index+5],min6222[min22down_index+5]]
r62l=[max6222[min22up_index-5],max6222[min22down_index-5],min6222[min22up_index-5],min6222[min22down_index-5]]
r6222up=np.max(r62)
r6222down=np.min(r62)
r6222uph=np.max(r62h)
r6222downh=np.min(r62h)
r6222upl=np.max(r62l)
r6222downl=np.min(r62l)
print(r6222up)
print(r6222down)

####################################################################################################
chi2mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi2.dat')
chi3mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi3.dat')
chi4mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi4.dat')
chi6mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi6.dat')
chi8mub68cen=np.loadtxt(r'./mub68/cmucen/final/buffer/chi8.dat')
r32mub68cen=chi3mub68cen/chi2mub68cen
r42mub68cen=chi4mub68cen/chi2mub68cen
r62mub68cen=chi6mub68cen/chi2mub68cen
r82mub68cen=chi8mub68cen/chi2mub68cen
chi2mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi2.dat')
chi3mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi3.dat')
chi4mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi4.dat')
chi6mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi6.dat')
chi8mub68up=np.loadtxt(r'./mub68/cmuup/final/buffer/chi8.dat')
r32mub68up=chi3mub68up/chi2mub68up
r42mub68up=chi4mub68up/chi2mub68up
r62mub68up=chi6mub68up/chi2mub68up
r82mub68up=chi8mub68up/chi2mub68up
chi2mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi2.dat')
chi3mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi3.dat')
chi4mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi4.dat')
chi6mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi6.dat')
chi8mub68down=np.loadtxt(r'./mub68/cmudown/final/buffer/chi8.dat')
r32mub68down=chi3mub68down/chi2mub68down
r42mub68down=chi4mub68down/chi2mub68down
r62mub68down=chi6mub68down/chi2mub68down
r82mub68down=chi8mub68down/chi2mub68down
r3268=np.zeros((300,20))
r4268=np.zeros((300,20))
r6268=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r3268[:,t]=spline(T/ct[t],r32mub68up,xsame)
    else:
       r3268[:,t]=spline(T/ct[t-10],r32mub68down,xsame)


for num in range(1,20):
    if num==1:
       max68=np.maximum(r3268[:,num-1],r3268[:,num])
       min68=np.minimum(r3268[:,num-1],r3268[:,num])
    else:
       max68=np.maximum(max68,r3268[:,num])
       min68=np.minimum(min68,r3268[:,num])

for t in range(0,20):
    if t<10:
       r4268[:,t]=spline(T/ct[t],r42mub68up,xsame)
    else:
       r4268[:,t]=spline(T/ct[t-10],r42mub68down,xsame)


for num in range(1,20):
    if num==1:
       max4268=np.maximum(r4268[:,num-1],r4268[:,num])
       min4268=np.minimum(r4268[:,num-1],r4268[:,num])
    else:
       max4268=np.maximum(max4268,r4268[:,num])
       min4268=np.minimum(min4268,r4268[:,num])

for t in range(0,20):
    if t<10:
       r6268[:,t]=spline(T/ct[t],r62mub68up,xsame)
    else:
       r6268[:,t]=spline(T/ct[t-10],r62mub68down,xsame)


for num in range(1,20):
    if num==1:
       max6268=np.maximum(r6268[:,num-1],r6268[:,num])
       min6268=np.minimum(r6268[:,num-1],r6268[:,num])
    else:
       max6268=np.maximum(max6268,r6268[:,num])
       min6268=np.minimum(min6268,r6268[:,num])

r32mub68cen=spline(T/ctcen,r32mub68cen,xsame)
r42mub68cen=spline(T/ctcen,r42mub68cen,xsame)
r62mub68cen=spline(T/ctcen,r62mub68cen,xsame)

dif68cen=abs(r32mub68cen-0.302545)
dif68up=abs(max68-0.302545)
dif68down=abs(min68-0.302545)
min68cen_index=np.argmin(dif68cen[80:300])+80
min68up_index=np.argmin(dif68up[80:300])+80
min68down_index=np.argmin(dif68down[80:300])+80
print(min68up_index)
print(min68down_index)
r42=[max4268[min22up_index],max4268[min22down_index],min4268[min22up_index],min4268[min22down_index]]
r42h=[max4268[min22up_index+5],max4268[min22down_index+5],min4268[min22up_index+5],min4268[min22down_index+5]]
r42l=[max4268[min22up_index-5],max4268[min22down_index-5],min4268[min22up_index-5],min4268[min22down_index-5]]
r4268up=np.max(r42)
r4268down=np.min(r42)
r4268uph=np.max(r42h)
r4268downh=np.min(r42h)
r4268upl=np.max(r42l)
r4268downl=np.min(r42l)
r62=[max4268[min22up_index],max4268[min22down_index],min4268[min22up_index],min4268[min22down_index]]
r62h=[max4268[min22up_index+5],max4268[min22down_index+5],min4268[min22up_index+5],min4268[min22down_index+5]]
r62l=[max4268[min22up_index-5],max4268[min22down_index-5],min4268[min22up_index-5],min4268[min22down_index-5]]
r6268up=np.max(r62)
r6268down=np.min(r62)
r6268uph=np.max(r62h)
r6268downh=np.min(r62h)
r6268upl=np.max(r62l)
r6268downl=np.min(r62l)
print(r6268up)
print(r6268down)
####################################################################################################
chi2mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi2.dat')
chi3mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi3.dat')
chi4mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi4.dat')
chi6mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi6.dat')
chi8mub106cen=np.loadtxt(r'./mub106/cmucen/final/buffer/chi8.dat')
r32mub106cen=chi3mub106cen/chi2mub106cen
r42mub106cen=chi4mub106cen/chi2mub106cen
r62mub106cen=chi6mub106cen/chi2mub106cen
r82mub106cen=chi8mub106cen/chi2mub106cen
chi2mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi2.dat')
chi3mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi3.dat')
chi4mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi4.dat')
chi6mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi6.dat')
chi8mub106up=np.loadtxt(r'./mub106/cmuup/final/buffer/chi8.dat')
r32mub106up=chi3mub106up/chi2mub106up
r42mub106up=chi4mub106up/chi2mub106up
r62mub106up=chi6mub106up/chi2mub106up
r82mub106up=chi8mub106up/chi2mub106up
chi2mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi2.dat')
chi3mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi3.dat')
chi4mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi4.dat')
chi6mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi6.dat')
chi8mub106down=np.loadtxt(r'./mub106/cmudown/final/buffer/chi8.dat')
r32mub106down=chi3mub106down/chi2mub106down
r42mub106down=chi4mub106down/chi2mub106down
r62mub106down=chi6mub106down/chi2mub106down
r82mub106down=chi8mub106down/chi2mub106down
r32106=np.zeros((300,20))
r42106=np.zeros((300,20))
r62106=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r32106[:,t]=spline(T/ct[t],r32mub106up,xsame)
    else:
       r32106[:,t]=spline(T/ct[t-10],r32mub106down,xsame)


for num in range(1,20):
    if num==1:
       max106=np.maximum(r32106[:,num-1],r32106[:,num])
       min106=np.minimum(r32106[:,num-1],r32106[:,num])
    else:
       max106=np.maximum(max106,r32106[:,num])
       min106=np.minimum(min106,r32106[:,num])

for t in range(0,20):
    if t<10:
       r42106[:,t]=spline(T/ct[t],r42mub106up,xsame)
    else:
       r42106[:,t]=spline(T/ct[t-10],r42mub106down,xsame)


for num in range(1,20):
    if num==1:
       max42106=np.maximum(r42106[:,num-1],r42106[:,num])
       min42106=np.minimum(r42106[:,num-1],r42106[:,num])
    else:
       max42106=np.maximum(max42106,r42106[:,num])
       min42106=np.minimum(min42106,r42106[:,num])

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

r32mub106cen=spline(T/ctcen,r32mub106cen,xsame)
r42mub106cen=spline(T/ctcen,r42mub106cen,xsame)
r62mub106cen=spline(T/ctcen,r62mub106cen,xsame)

dif106cen=abs(r32mub106cen-0.432666)
dif106up=abs(max106-0.432666)
dif106down=abs(min106-0.432666)
min106cen_index=np.argmin(dif106cen[80:300])+80
min106up_index=np.argmin(dif106up[80:300])+80
min106down_index=np.argmin(dif106down[80:300])+80
print(min106up_index)
print(min106down_index)
r42=[max42106[min22up_index],max42106[min22down_index],min42106[min22up_index],min42106[min22down_index]]
r42h=[max42106[min22up_index+5],max42106[min22down_index+5],min42106[min22up_index+5],min42106[min22down_index+5]]
r42l=[max42106[min22up_index-5],max42106[min22down_index-5],min42106[min22up_index-5],min42106[min22down_index-5]]
r42106up=np.max(r42)
r42106down=np.min(r42)
r42106uph=np.max(r42h)
r42106downh=np.min(r42h)
r42106upl=np.max(r42l)
r42106downl=np.min(r42l)
r62=[max42106[min22up_index],max42106[min22down_index],min42106[min22up_index],min42106[min22down_index]]
r62h=[max42106[min22up_index+5],max42106[min22down_index+5],min42106[min22up_index+5],min42106[min22down_index+5]]
r62l=[max42106[min22up_index-5],max42106[min22down_index-5],min42106[min22up_index-5],min42106[min22down_index-5]]
r62106up=np.max(r62)
r62106down=np.min(r62)
r62106uph=np.max(r62h)
r62106downh=np.min(r62h)
r62106upl=np.max(r62l)
r62106downl=np.min(r62l)
print(r62106up)
print(r62106down)
####################################################################################################
chi2mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi2.dat')
chi3mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi3.dat')
chi4mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi4.dat')
chi6mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi6.dat')
chi8mub148cen=np.loadtxt(r'./mub148/cmucen/final/buffer/chi8.dat')
r32mub148cen=chi3mub148cen/chi2mub148cen
r42mub148cen=chi4mub148cen/chi2mub148cen
r62mub148cen=chi6mub148cen/chi2mub148cen
r82mub148cen=chi8mub148cen/chi2mub148cen
chi2mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi2.dat')
chi3mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi3.dat')
chi4mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi4.dat')
chi6mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi6.dat')
chi8mub148up=np.loadtxt(r'./mub148/cmuup/final/buffer/chi8.dat')
r32mub148up=chi3mub148up/chi2mub148up
r42mub148up=chi4mub148up/chi2mub148up
r62mub148up=chi6mub148up/chi2mub148up
r82mub148up=chi8mub148up/chi2mub148up
chi2mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi2.dat')
chi3mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi3.dat')
chi4mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi4.dat')
chi6mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi6.dat')
chi8mub148down=np.loadtxt(r'./mub148/cmudown/final/buffer/chi8.dat')
r32mub148down=chi3mub148down/chi2mub148down
r42mub148down=chi4mub148down/chi2mub148down
r62mub148down=chi6mub148down/chi2mub148down
r82mub148down=chi8mub148down/chi2mub148down
r32148=np.zeros((300,20))
r42148=np.zeros((300,20))
r62148=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r32148[:,t]=spline(T/ct[t],r32mub148up,xsame)
    else:
       r32148[:,t]=spline(T/ct[t-10],r32mub148down,xsame)


for num in range(1,20):
    if num==1:
       max148=np.maximum(r32148[:,num-1],r32148[:,num])
       min148=np.minimum(r32148[:,num-1],r32148[:,num])
    else:
       max148=np.maximum(max148,r32148[:,num])
       min148=np.minimum(min148,r32148[:,num])

for t in range(0,20):
    if t<10:
       r42148[:,t]=spline(T/ct[t],r42mub148up,xsame)
    else:
       r42148[:,t]=spline(T/ct[t-10],r42mub148down,xsame)


for num in range(1,20):
    if num==1:
       max42148=np.maximum(r42148[:,num-1],r42148[:,num])
       min42148=np.minimum(r42148[:,num-1],r42148[:,num])
    else:
       max42148=np.maximum(max42148,r42148[:,num])
       min42148=np.minimum(min42148,r42148[:,num])

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

r32mub148cen=spline(T/ctcen,r32mub148cen,xsame)
r42mub148cen=spline(T/ctcen,r42mub148cen,xsame)
r62mub148cen=spline(T/ctcen,r62mub148cen,xsame)

dif148cen=abs(r32mub148cen-0.541676)
dif148up=abs(max148-0.541676)
dif148down=abs(min148-0.541676)
min148cen_index=np.argmin(dif148cen[80:300])+80
min148up_index=np.argmin(dif148up[80:300])+80
min148down_index=np.argmin(dif148down[80:300])+80
print(min148up_index)
print(min148down_index)
r42=[max42148[min22up_index],max42148[min22down_index],min42148[min22up_index],min42148[min22down_index]]
r42h=[max42148[min22up_index+5],max42148[min22down_index+5],min42148[min22up_index+5],min42148[min22down_index+5]]
r42l=[max42148[min22up_index-5],max42148[min22down_index-5],min42148[min22up_index-5],min42148[min22down_index-5]]
r42148up=np.max(r42)
r42148down=np.min(r42)
r42148uph=np.max(r42h)
r42148downh=np.min(r42h)
r42148upl=np.max(r42l)
r42148downl=np.min(r42l)
r62=[max42148[min22up_index],max42148[min22down_index],min42148[min22up_index],min42148[min22down_index]]
r62h=[max42148[min22up_index+5],max42148[min22down_index+5],min42148[min22up_index+5],min42148[min22down_index+5]]
r62l=[max42148[min22up_index-5],max42148[min22down_index-5],min42148[min22up_index-5],min42148[min22down_index-5]]
r62148up=np.max(r62)
r62148down=np.min(r62)
r62148uph=np.max(r62h)
r62148downh=np.min(r62h)
r62148upl=np.max(r62l)
r62148downl=np.min(r62l)
print(r62148up)
print(r62148down)
####################################################################################################
chi2mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi2.dat')
chi3mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi3.dat')
chi4mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi4.dat')
chi6mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi6.dat')
chi8mub196cen=np.loadtxt(r'./mub196/cmucen/final/buffer/chi8.dat')
r32mub196cen=chi3mub196cen/chi2mub196cen
r42mub196cen=chi4mub196cen/chi2mub196cen
r62mub196cen=chi6mub196cen/chi2mub196cen
r82mub196cen=chi8mub196cen/chi2mub196cen
chi2mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi2.dat')
chi3mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi3.dat')
chi4mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi4.dat')
chi6mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi6.dat')
chi8mub196up=np.loadtxt(r'./mub196/cmuup/final/buffer/chi8.dat')
r32mub196up=chi3mub196up/chi2mub196up
r42mub196up=chi4mub196up/chi2mub196up
r62mub196up=chi6mub196up/chi2mub196up
r82mub196up=chi8mub196up/chi2mub196up
chi2mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi2.dat')
chi3mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi3.dat')
chi4mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi4.dat')
chi6mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi6.dat')
chi8mub196up1=np.loadtxt(r'./mub196/cmuup1/final/buffer/chi8.dat')
r32mub196up1=chi3mub196up1/chi2mub196up1
r42mub196up1=chi4mub196up1/chi2mub196up1
r62mub196up1=chi6mub196up1/chi2mub196up1
r82mub196up1=chi8mub196up1/chi2mub196up1
chi2mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi2.dat')
chi3mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi3.dat')
chi4mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi4.dat')
chi6mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi6.dat')
chi8mub196up2=np.loadtxt(r'./mub196/cmuup2/final/buffer/chi8.dat')
r32mub196up2=chi3mub196up2/chi2mub196up2
r42mub196up2=chi4mub196up2/chi2mub196up2
r62mub196up2=chi6mub196up2/chi2mub196up2
r82mub196up2=chi8mub196up2/chi2mub196up2
chi2mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi2.dat')
chi3mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi3.dat')
chi4mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi4.dat')
chi6mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi6.dat')
chi8mub196up3=np.loadtxt(r'./mub196/cmuup3/final/buffer/chi8.dat')
r32mub196up3=chi3mub196up3/chi2mub196up3
r42mub196up3=chi4mub196up3/chi2mub196up3
r62mub196up3=chi6mub196up3/chi2mub196up3
r82mub196up3=chi8mub196up3/chi2mub196up3
chi2mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi2.dat')
chi3mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi3.dat')
chi4mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi4.dat')
chi6mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi6.dat')
chi8mub196up4=np.loadtxt(r'./mub196/cmuup4/final/buffer/chi8.dat')
r32mub196up4=chi3mub196up4/chi2mub196up4
r42mub196up4=chi4mub196up4/chi2mub196up4
r62mub196up4=chi6mub196up4/chi2mub196up4
r82mub196up4=chi8mub196up4/chi2mub196up4
chi2mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi2.dat')
chi3mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi3.dat')
chi4mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi4.dat')
chi6mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi6.dat')
chi8mub196down=np.loadtxt(r'./mub196/cmudown/final/buffer/chi8.dat')
r32mub196down=chi3mub196down/chi2mub196down
r42mub196down=chi4mub196down/chi2mub196down
r62mub196down=chi6mub196down/chi2mub196down
r82mub196down=chi8mub196down/chi2mub196down
chi2mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi2.dat')
chi3mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi3.dat')
chi4mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi4.dat')
chi6mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi6.dat')
chi8mub196down1=np.loadtxt(r'./mub196/cmudown1/final/buffer/chi8.dat')
r32mub196down1=chi3mub196down1/chi2mub196down1
r42mub196down1=chi4mub196down1/chi2mub196down1
r62mub196down1=chi6mub196down1/chi2mub196down1
r82mub196down1=chi8mub196down1/chi2mub196down1
chi2mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi2.dat')
chi3mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi3.dat')
chi4mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi4.dat')
chi6mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi6.dat')
chi8mub196down2=np.loadtxt(r'./mub196/cmudown2/final/buffer/chi8.dat')
r32mub196down2=chi3mub196down2/chi2mub196down2
r42mub196down2=chi4mub196down2/chi2mub196down2
r62mub196down2=chi6mub196down2/chi2mub196down2
r82mub196down2=chi8mub196down2/chi2mub196down2
chi2mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi2.dat')
chi3mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi3.dat')
chi4mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi4.dat')
chi6mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi6.dat')
chi8mub196down3=np.loadtxt(r'./mub196/cmudown3/final/buffer/chi8.dat')
r32mub196down3=chi3mub196down3/chi2mub196down3
r42mub196down3=chi4mub196down3/chi2mub196down3
r62mub196down3=chi6mub196down3/chi2mub196down3
r82mub196down3=chi8mub196down3/chi2mub196down3
chi2mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi2.dat')
chi3mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi3.dat')
chi4mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi4.dat')
chi6mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi6.dat')
chi8mub196down4=np.loadtxt(r'./mub196/cmudown4/final/buffer/chi8.dat')
r32mub196down4=chi3mub196down4/chi2mub196down4
r42mub196down4=chi4mub196down4/chi2mub196down4
r62mub196down4=chi6mub196down4/chi2mub196down4
r82mub196down4=chi8mub196down4/chi2mub196down4
r32196=np.zeros((300,100))
r42196=np.zeros((300,100))
r62196=np.zeros((300,100))
for t in range(0,100):
    if t<10:
       r32196[:,t]=spline(T/ct[t],r32mub196up,xsame)
    else:
       if t>=10 and t<20:
          r32196[:,t]=spline(T/ct[t-10],r32mub196up1,xsame)
       else:
          if t>=20 and t<30:
             r32196[:,t]=spline(T/ct[t-20],r32mub196up2,xsame)
          else: 
             if t>=30 and t<40:
                r32196[:,t]=spline(T/ct[t-30],r32mub196up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32196[:,t]=spline(T/ct[t-40],r32mub196up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32196[:,t]=spline(T/ct[t-50],r32mub196down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32196[:,t]=spline(T/ct[t-60],r32mub196down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32196[:,t]=spline(T/ct[t-70],r32mub196down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32196[:,t]=spline(T/ct[t-80],r32mub196down3,xsame)
                            else:
                                r32196[:,t]=spline(T/ct[t-90],r32mub196down4,xsame)

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
       max196=np.maximum(r32196[:,num-1],r32196[:,num])
       min196=np.minimum(r32196[:,num-1],r32196[:,num])
    else:
       max196=np.maximum(max196,r32196[:,num])
       min196=np.minimum(min196,r32196[:,num])

for num in range(1,100):
    if num==1:
       max42196=np.maximum(r42196[:,num-1],r42196[:,num])
       min42196=np.minimum(r42196[:,num-1],r42196[:,num])
    else:
       max42196=np.maximum(max42196,r42196[:,num])
       min42196=np.minimum(min42196,r42196[:,num])

for num in range(1,100):
    if num==1:
       max62196=np.maximum(r62196[:,num-1],r62196[:,num])
       min62196=np.minimum(r62196[:,num-1],r62196[:,num])
    else:
       max62196=np.maximum(max62196,r62196[:,num])
       min62196=np.minimum(min62196,r62196[:,num])

r32mub196cen=spline(T/ctcen,r32mub196cen,xsame)
r42mub196cen=spline(T/ctcen,r42mub196cen,xsame)
r62mub196cen=spline(T/ctcen,r62mub196cen,xsame)

dif196cen=abs(r32mub196cen-0.612299)
dif196up=abs(max196-0.612299)
dif196down=abs(min196-0.612299)
min196cen_index=np.argmin(dif196cen[80:300])+80
min196up_index=np.argmin(dif196up[80:300])+80
min196down_index=np.argmin(dif196down[80:300])+80
print(min196up_index)
print(min196down_index)
r42=[max42196[min22up_index],max42196[min22down_index],min42196[min22up_index],min42196[min22down_index]]
r42h=[max42196[min22up_index+5],max42196[min22down_index+5],min42196[min22up_index+5],min42196[min22down_index+5]]
r42l=[max42196[min22up_index-5],max42196[min22down_index-5],min42196[min22up_index-5],min42196[min22down_index-5]]
r42196up=np.max(r42)
r42196down=np.min(r42)
r42196uph=np.max(r42h)
r42196downh=np.min(r42h)
r42196upl=np.max(r42l)
r42196downl=np.min(r42l)
r62=[max42196[min22up_index],max42196[min22down_index],min42196[min22up_index],min42196[min22down_index]]
r62h=[max42196[min22up_index+5],max42196[min22down_index+5],min42196[min22up_index+5],min42196[min22down_index+5]]
r62l=[max42196[min22up_index-5],max42196[min22down_index-5],min42196[min22up_index-5],min42196[min22down_index-5]]
r62196up=np.max(r62)
r62196down=np.min(r62)
r62196uph=np.max(r62h)
r62196downh=np.min(r62h)
r62196upl=np.max(r62l)
r62196downl=np.min(r62l)
print(r62196up)
print(r62196down)
#####################################################################################################
chi2mub303cen=np.loadtxt(r'./mub303/cmucen/final/buffer/chi2.dat')
chi3mub303cen=np.loadtxt(r'./mub303/cmucen/final/buffer/chi3.dat')
chi4mub303cen=np.loadtxt(r'./mub303/cmucen/final/buffer/chi4.dat')
chi6mub303cen=np.loadtxt(r'./mub303/cmucen/final/buffer/chi6.dat')
chi8mub303cen=np.loadtxt(r'./mub303/cmucen/final/buffer/chi8.dat')
r32mub303cen=chi3mub303cen/chi2mub303cen
r42mub303cen=chi4mub303cen/chi2mub303cen
r62mub303cen=chi6mub303cen/chi2mub303cen
r82mub303cen=chi8mub303cen/chi2mub303cen
chi2mub303up=np.loadtxt(r'./mub303/cmuup/final/buffer/chi2.dat')
chi3mub303up=np.loadtxt(r'./mub303/cmuup/final/buffer/chi3.dat')
chi4mub303up=np.loadtxt(r'./mub303/cmuup/final/buffer/chi4.dat')
chi6mub303up=np.loadtxt(r'./mub303/cmuup/final/buffer/chi6.dat')
chi8mub303up=np.loadtxt(r'./mub303/cmuup/final/buffer/chi8.dat')
r32mub303up=chi3mub303up/chi2mub303up
r42mub303up=chi4mub303up/chi2mub303up
r62mub303up=chi6mub303up/chi2mub303up
r82mub303up=chi8mub303up/chi2mub303up
chi2mub303up1=np.loadtxt(r'./mub303/cmuup1/final/buffer/chi2.dat')
chi3mub303up1=np.loadtxt(r'./mub303/cmuup1/final/buffer/chi3.dat')
chi4mub303up1=np.loadtxt(r'./mub303/cmuup1/final/buffer/chi4.dat')
chi6mub303up1=np.loadtxt(r'./mub303/cmuup1/final/buffer/chi6.dat')
chi8mub303up1=np.loadtxt(r'./mub303/cmuup1/final/buffer/chi8.dat')
r32mub303up1=chi3mub303up1/chi2mub303up1
r42mub303up1=chi4mub303up1/chi2mub303up1
r62mub303up1=chi6mub303up1/chi2mub303up1
r82mub303up1=chi8mub303up1/chi2mub303up1
chi2mub303up2=np.loadtxt(r'./mub303/cmuup2/final/buffer/chi2.dat')
chi3mub303up2=np.loadtxt(r'./mub303/cmuup2/final/buffer/chi3.dat')
chi4mub303up2=np.loadtxt(r'./mub303/cmuup2/final/buffer/chi4.dat')
chi6mub303up2=np.loadtxt(r'./mub303/cmuup2/final/buffer/chi6.dat')
chi8mub303up2=np.loadtxt(r'./mub303/cmuup2/final/buffer/chi8.dat')
r32mub303up2=chi3mub303up2/chi2mub303up2
r42mub303up2=chi4mub303up2/chi2mub303up2
r62mub303up2=chi6mub303up2/chi2mub303up2
r82mub303up2=chi8mub303up2/chi2mub303up2
chi2mub303up3=np.loadtxt(r'./mub303/cmuup3/final/buffer/chi2.dat')
chi3mub303up3=np.loadtxt(r'./mub303/cmuup3/final/buffer/chi3.dat')
chi4mub303up3=np.loadtxt(r'./mub303/cmuup3/final/buffer/chi4.dat')
chi6mub303up3=np.loadtxt(r'./mub303/cmuup3/final/buffer/chi6.dat')
chi8mub303up3=np.loadtxt(r'./mub303/cmuup3/final/buffer/chi8.dat')
r32mub303up3=chi3mub303up3/chi2mub303up3
r42mub303up3=chi4mub303up3/chi2mub303up3
r62mub303up3=chi6mub303up3/chi2mub303up3
r82mub303up3=chi8mub303up3/chi2mub303up3
chi2mub303up4=np.loadtxt(r'./mub303/cmuup4/final/buffer/chi2.dat')
chi3mub303up4=np.loadtxt(r'./mub303/cmuup4/final/buffer/chi3.dat')
chi4mub303up4=np.loadtxt(r'./mub303/cmuup4/final/buffer/chi4.dat')
chi6mub303up4=np.loadtxt(r'./mub303/cmuup4/final/buffer/chi6.dat')
chi8mub303up4=np.loadtxt(r'./mub303/cmuup4/final/buffer/chi8.dat')
r32mub303up4=chi3mub303up4/chi2mub303up4
r42mub303up4=chi4mub303up4/chi2mub303up4
r62mub303up4=chi6mub303up4/chi2mub303up4
r82mub303up4=chi8mub303up4/chi2mub303up4
chi2mub303down=np.loadtxt(r'./mub303/cmudown/final/buffer/chi2.dat')
chi3mub303down=np.loadtxt(r'./mub303/cmudown/final/buffer/chi3.dat')
chi4mub303down=np.loadtxt(r'./mub303/cmudown/final/buffer/chi4.dat')
chi6mub303down=np.loadtxt(r'./mub303/cmudown/final/buffer/chi6.dat')
chi8mub303down=np.loadtxt(r'./mub303/cmudown/final/buffer/chi8.dat')
r32mub303down=chi3mub303down/chi2mub303down
r42mub303down=chi4mub303down/chi2mub303down
r62mub303down=chi6mub303down/chi2mub303down
r82mub303down=chi8mub303down/chi2mub303down
chi2mub303down1=np.loadtxt(r'./mub303/cmudown1/final/buffer/chi2.dat')
chi3mub303down1=np.loadtxt(r'./mub303/cmudown1/final/buffer/chi3.dat')
chi4mub303down1=np.loadtxt(r'./mub303/cmudown1/final/buffer/chi4.dat')
chi6mub303down1=np.loadtxt(r'./mub303/cmudown1/final/buffer/chi6.dat')
chi8mub303down1=np.loadtxt(r'./mub303/cmudown1/final/buffer/chi8.dat')
r32mub303down1=chi3mub303down1/chi2mub303down1
r42mub303down1=chi4mub303down1/chi2mub303down1
r62mub303down1=chi6mub303down1/chi2mub303down1
r82mub303down1=chi8mub303down1/chi2mub303down1
chi2mub303down2=np.loadtxt(r'./mub303/cmudown2/final/buffer/chi2.dat')
chi3mub303down2=np.loadtxt(r'./mub303/cmudown2/final/buffer/chi3.dat')
chi4mub303down2=np.loadtxt(r'./mub303/cmudown2/final/buffer/chi4.dat')
chi6mub303down2=np.loadtxt(r'./mub303/cmudown2/final/buffer/chi6.dat')
chi8mub303down2=np.loadtxt(r'./mub303/cmudown2/final/buffer/chi8.dat')
r32mub303down2=chi3mub303down2/chi2mub303down2
r42mub303down2=chi4mub303down2/chi2mub303down2
r62mub303down2=chi6mub303down2/chi2mub303down2
r82mub303down2=chi8mub303down2/chi2mub303down2
chi2mub303down3=np.loadtxt(r'./mub303/cmudown3/final/buffer/chi2.dat')
chi3mub303down3=np.loadtxt(r'./mub303/cmudown3/final/buffer/chi3.dat')
chi4mub303down3=np.loadtxt(r'./mub303/cmudown3/final/buffer/chi4.dat')
chi6mub303down3=np.loadtxt(r'./mub303/cmudown3/final/buffer/chi6.dat')
chi8mub303down3=np.loadtxt(r'./mub303/cmudown3/final/buffer/chi8.dat')
r32mub303down3=chi3mub303down3/chi2mub303down3
r42mub303down3=chi4mub303down3/chi2mub303down3
r62mub303down3=chi6mub303down3/chi2mub303down3
r82mub303down3=chi8mub303down3/chi2mub303down3
chi2mub303down4=np.loadtxt(r'./mub303/cmudown4/final/buffer/chi2.dat')
chi3mub303down4=np.loadtxt(r'./mub303/cmudown4/final/buffer/chi3.dat')
chi4mub303down4=np.loadtxt(r'./mub303/cmudown4/final/buffer/chi4.dat')
chi6mub303down4=np.loadtxt(r'./mub303/cmudown4/final/buffer/chi6.dat')
chi8mub303down4=np.loadtxt(r'./mub303/cmudown4/final/buffer/chi8.dat')
r32mub303down4=chi3mub303down4/chi2mub303down4
r42mub303down4=chi4mub303down4/chi2mub303down4
r62mub303down4=chi6mub303down4/chi2mub303down4
r82mub303down4=chi8mub303down4/chi2mub303down4
r32303=np.zeros((300,100))
r42303=np.zeros((300,100))
r62303=np.zeros((300,100))
for t in range(0,100):
    if t<10:
       r32303[:,t]=spline(T/ct[t],r32mub303up,xsame)
    else:
       if t>=10 and t<20:
          r32303[:,t]=spline(T/ct[t-10],r32mub303up1,xsame)
       else:
          if t>=20 and t<30:
             r32303[:,t]=spline(T/ct[t-20],r32mub303up2,xsame)
          else: 
             if t>=30 and t<40:
                r32303[:,t]=spline(T/ct[t-30],r32mub303up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32303[:,t]=spline(T/ct[t-40],r32mub303up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32303[:,t]=spline(T/ct[t-50],r32mub303down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32303[:,t]=spline(T/ct[t-60],r32mub303down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32303[:,t]=spline(T/ct[t-70],r32mub303down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32303[:,t]=spline(T/ct[t-80],r32mub303down3,xsame)
                            else:
                                r32303[:,t]=spline(T/ct[t-90],r32mub303down4,xsame)

for t in range(0,100):
    if t<10:
       r42303[:,t]=spline(T/ct[t],r42mub303up,xsame)
    else:
       if t>=10 and t<20:
          r42303[:,t]=spline(T/ct[t-10],r42mub303up1,xsame)
       else:
          if t>=20 and t<30:
             r42303[:,t]=spline(T/ct[t-20],r42mub303up2,xsame)
          else: 
             if t>=30 and t<40:
                r42303[:,t]=spline(T/ct[t-30],r42mub303up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42303[:,t]=spline(T/ct[t-40],r42mub303up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42303[:,t]=spline(T/ct[t-50],r42mub303down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42303[:,t]=spline(T/ct[t-60],r42mub303down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42303[:,t]=spline(T/ct[t-70],r42mub303down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42303[:,t]=spline(T/ct[t-80],r42mub303down3,xsame)
                            else:
                                r42303[:,t]=spline(T/ct[t-90],r42mub303down4,xsame)

for t in range(0,100):
    if t<10:
       r62303[:,t]=spline(T/ct[t],r62mub303up,xsame)
    else:
       if t>=10 and t<20:
          r62303[:,t]=spline(T/ct[t-10],r62mub303up1,xsame)
       else:
          if t>=20 and t<30:
             r62303[:,t]=spline(T/ct[t-20],r62mub303up2,xsame)
          else: 
             if t>=30 and t<40:
                r62303[:,t]=spline(T/ct[t-30],r62mub303up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62303[:,t]=spline(T/ct[t-40],r62mub303up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62303[:,t]=spline(T/ct[t-50],r62mub303down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62303[:,t]=spline(T/ct[t-60],r62mub303down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62303[:,t]=spline(T/ct[t-70],r62mub303down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62303[:,t]=spline(T/ct[t-80],r62mub303down3,xsame)
                            else:
                                r62303[:,t]=spline(T/ct[t-90],r62mub303down4,xsame)


for num in range(1,100):
    if num==1:
       max303=np.maximum(r32303[:,num-1],r32303[:,num])
       min303=np.minimum(r32303[:,num-1],r32303[:,num])
    else:
       max303=np.maximum(max303,r32303[:,num])
       min303=np.minimum(min303,r32303[:,num])

for num in range(1,100):
    if num==1:
       max42303=np.maximum(r42303[:,num-1],r42303[:,num])
       min42303=np.minimum(r42303[:,num-1],r42303[:,num])
    else:
       max42303=np.maximum(max42303,r42303[:,num])
       min42303=np.minimum(min42303,r42303[:,num])

for num in range(1,100):
    if num==1:
       max62303=np.maximum(r62303[:,num-1],r62303[:,num])
       min62303=np.minimum(r62303[:,num-1],r62303[:,num])
    else:
       max62303=np.maximum(max62303,r62303[:,num])
       min62303=np.minimum(min62303,r62303[:,num])

r32mub303cen=spline(T/ctcen,r32mub303cen,xsame)
r42mub303cen=spline(T/ctcen,r42mub303cen,xsame)
r62mub303cen=spline(T/ctcen,r62mub303cen,xsame)

dif303cen=abs(r32mub303cen-0.680635)
dif303up=abs(max303-0.680635)
dif303down=abs(min303-0.680635)
min303cen_index=np.argmin(dif303cen[80:300])+80
min303up_index=np.argmin(dif303up[80:300])+80
min303down_index=np.argmin(dif303down[80:300])+80
print(min303up_index)
print(min303down_index)
r42=[max42303[min22up_index],max42303[min22down_index],min42303[min22up_index],min42303[min22down_index]]
r42h=[max42303[min22up_index+5],max42303[min22down_index+5],min42303[min22up_index+5],min42303[min22down_index+5]]
r42l=[max42303[min22up_index-5],max42303[min22down_index-5],min42303[min22up_index-5],min42303[min22down_index-5]]
r42303up=np.max(r42)
r42303down=np.min(r42)
r42303uph=np.max(r42h)
r42303downh=np.min(r42h)
r42303upl=np.max(r42l)
r42303downl=np.min(r42l)
r62=[max42303[min22up_index],max42303[min22down_index],min42303[min22up_index],min42303[min22down_index]]
r62h=[max42303[min22up_index+5],max42303[min22down_index+5],min42303[min22up_index+5],min42303[min22down_index+5]]
r62l=[max42303[min22up_index-5],max42303[min22down_index-5],min42303[min22up_index-5],min42303[min22down_index-5]]
r62303up=np.max(r62)
r62303down=np.min(r62)
r62303uph=np.max(r62h)
r62303downh=np.min(r62h)
r62303upl=np.max(r62l)
r62303downl=np.min(r62l)
print(r62303up)
print(r62303down)
####################################################################################################
chi2mub406cen=np.loadtxt(r'./mub406/cmucen/final/buffer/chi2.dat')
chi3mub406cen=np.loadtxt(r'./mub406/cmucen/final/buffer/chi3.dat')
chi4mub406cen=np.loadtxt(r'./mub406/cmucen/final/buffer/chi4.dat')
chi6mub406cen=np.loadtxt(r'./mub406/cmucen/final/buffer/chi6.dat')
chi8mub406cen=np.loadtxt(r'./mub406/cmucen/final/buffer/chi8.dat')
r32mub406cen=chi3mub406cen/chi2mub406cen
r42mub406cen=chi4mub406cen/chi2mub406cen
r62mub406cen=chi6mub406cen/chi2mub406cen
r82mub406cen=chi8mub406cen/chi2mub406cen
chi2mub406up=np.loadtxt(r'./mub406/cmuup/final/buffer/chi2.dat')
chi3mub406up=np.loadtxt(r'./mub406/cmuup/final/buffer/chi3.dat')
chi4mub406up=np.loadtxt(r'./mub406/cmuup/final/buffer/chi4.dat')
chi6mub406up=np.loadtxt(r'./mub406/cmuup/final/buffer/chi6.dat')
chi8mub406up=np.loadtxt(r'./mub406/cmuup/final/buffer/chi8.dat')
r32mub406up=chi3mub406up/chi2mub406up
r42mub406up=chi4mub406up/chi2mub406up
r62mub406up=chi6mub406up/chi2mub406up
r82mub406up=chi8mub406up/chi2mub406up
chi2mub406up1=np.loadtxt(r'./mub406/cmuup1/final/buffer/chi2.dat')
chi3mub406up1=np.loadtxt(r'./mub406/cmuup1/final/buffer/chi3.dat')
chi4mub406up1=np.loadtxt(r'./mub406/cmuup1/final/buffer/chi4.dat')
chi6mub406up1=np.loadtxt(r'./mub406/cmuup1/final/buffer/chi6.dat')
chi8mub406up1=np.loadtxt(r'./mub406/cmuup1/final/buffer/chi8.dat')
r32mub406up1=chi3mub406up1/chi2mub406up1
r42mub406up1=chi4mub406up1/chi2mub406up1
r62mub406up1=chi6mub406up1/chi2mub406up1
r82mub406up1=chi8mub406up1/chi2mub406up1
chi2mub406up2=np.loadtxt(r'./mub406/cmuup2/final/buffer/chi2.dat')
chi3mub406up2=np.loadtxt(r'./mub406/cmuup2/final/buffer/chi3.dat')
chi4mub406up2=np.loadtxt(r'./mub406/cmuup2/final/buffer/chi4.dat')
chi6mub406up2=np.loadtxt(r'./mub406/cmuup2/final/buffer/chi6.dat')
chi8mub406up2=np.loadtxt(r'./mub406/cmuup2/final/buffer/chi8.dat')
r32mub406up2=chi3mub406up2/chi2mub406up2
r42mub406up2=chi4mub406up2/chi2mub406up2
r62mub406up2=chi6mub406up2/chi2mub406up2
r82mub406up2=chi8mub406up2/chi2mub406up2
chi2mub406up3=np.loadtxt(r'./mub406/cmuup3/final/buffer/chi2.dat')
chi3mub406up3=np.loadtxt(r'./mub406/cmuup3/final/buffer/chi3.dat')
chi4mub406up3=np.loadtxt(r'./mub406/cmuup3/final/buffer/chi4.dat')
chi6mub406up3=np.loadtxt(r'./mub406/cmuup3/final/buffer/chi6.dat')
chi8mub406up3=np.loadtxt(r'./mub406/cmuup3/final/buffer/chi8.dat')
r32mub406up3=chi3mub406up3/chi2mub406up3
r42mub406up3=chi4mub406up3/chi2mub406up3
r62mub406up3=chi6mub406up3/chi2mub406up3
r82mub406up3=chi8mub406up3/chi2mub406up3
chi2mub406up4=np.loadtxt(r'./mub406/cmuup4/final/buffer/chi2.dat')
chi3mub406up4=np.loadtxt(r'./mub406/cmuup4/final/buffer/chi3.dat')
chi4mub406up4=np.loadtxt(r'./mub406/cmuup4/final/buffer/chi4.dat')
chi6mub406up4=np.loadtxt(r'./mub406/cmuup4/final/buffer/chi6.dat')
chi8mub406up4=np.loadtxt(r'./mub406/cmuup4/final/buffer/chi8.dat')
r32mub406up4=chi3mub406up4/chi2mub406up4
r42mub406up4=chi4mub406up4/chi2mub406up4
r62mub406up4=chi6mub406up4/chi2mub406up4
r82mub406up4=chi8mub406up4/chi2mub406up4
chi2mub406down=np.loadtxt(r'./mub406/cmudown/final/buffer/chi2.dat')
chi3mub406down=np.loadtxt(r'./mub406/cmudown/final/buffer/chi3.dat')
chi4mub406down=np.loadtxt(r'./mub406/cmudown/final/buffer/chi4.dat')
chi6mub406down=np.loadtxt(r'./mub406/cmudown/final/buffer/chi6.dat')
chi8mub406down=np.loadtxt(r'./mub406/cmudown/final/buffer/chi8.dat')
r32mub406down=chi3mub406down/chi2mub406down
r42mub406down=chi4mub406down/chi2mub406down
r62mub406down=chi6mub406down/chi2mub406down
r82mub406down=chi8mub406down/chi2mub406down
chi2mub406down1=np.loadtxt(r'./mub406/cmudown1/final/buffer/chi2.dat')
chi3mub406down1=np.loadtxt(r'./mub406/cmudown1/final/buffer/chi3.dat')
chi4mub406down1=np.loadtxt(r'./mub406/cmudown1/final/buffer/chi4.dat')
chi6mub406down1=np.loadtxt(r'./mub406/cmudown1/final/buffer/chi6.dat')
chi8mub406down1=np.loadtxt(r'./mub406/cmudown1/final/buffer/chi8.dat')
r32mub406down1=chi3mub406down1/chi2mub406down1
r42mub406down1=chi4mub406down1/chi2mub406down1
r62mub406down1=chi6mub406down1/chi2mub406down1
r82mub406down1=chi8mub406down1/chi2mub406down1
chi2mub406down2=np.loadtxt(r'./mub406/cmudown2/final/buffer/chi2.dat')
chi3mub406down2=np.loadtxt(r'./mub406/cmudown2/final/buffer/chi3.dat')
chi4mub406down2=np.loadtxt(r'./mub406/cmudown2/final/buffer/chi4.dat')
chi6mub406down2=np.loadtxt(r'./mub406/cmudown2/final/buffer/chi6.dat')
chi8mub406down2=np.loadtxt(r'./mub406/cmudown2/final/buffer/chi8.dat')
r32mub406down2=chi3mub406down2/chi2mub406down2
r42mub406down2=chi4mub406down2/chi2mub406down2
r62mub406down2=chi6mub406down2/chi2mub406down2
r82mub406down2=chi8mub406down2/chi2mub406down2
chi2mub406down3=np.loadtxt(r'./mub406/cmudown3/final/buffer/chi2.dat')
chi3mub406down3=np.loadtxt(r'./mub406/cmudown3/final/buffer/chi3.dat')
chi4mub406down3=np.loadtxt(r'./mub406/cmudown3/final/buffer/chi4.dat')
chi6mub406down3=np.loadtxt(r'./mub406/cmudown3/final/buffer/chi6.dat')
chi8mub406down3=np.loadtxt(r'./mub406/cmudown3/final/buffer/chi8.dat')
r32mub406down3=chi3mub406down3/chi2mub406down3
r42mub406down3=chi4mub406down3/chi2mub406down3
r62mub406down3=chi6mub406down3/chi2mub406down3
r82mub406down3=chi8mub406down3/chi2mub406down3
chi2mub406down4=np.loadtxt(r'./mub406/cmudown4/final/buffer/chi2.dat')
chi3mub406down4=np.loadtxt(r'./mub406/cmudown4/final/buffer/chi3.dat')
chi4mub406down4=np.loadtxt(r'./mub406/cmudown4/final/buffer/chi4.dat')
chi6mub406down4=np.loadtxt(r'./mub406/cmudown4/final/buffer/chi6.dat')
chi8mub406down4=np.loadtxt(r'./mub406/cmudown4/final/buffer/chi8.dat')
r32mub406down4=chi3mub406down4/chi2mub406down4
r42mub406down4=chi4mub406down4/chi2mub406down4
r62mub406down4=chi6mub406down4/chi2mub406down4
r82mub406down4=chi8mub406down4/chi2mub406down4
r32406=np.zeros((300,100))
r42406=np.zeros((300,100))
r62406=np.zeros((300,100))
for t in range(0,100):
    if t<10:
       r32406[:,t]=spline(T/ct[t],r32mub406up,xsame)
    else:
       if t>=10 and t<20:
          r32406[:,t]=spline(T/ct[t-10],r32mub406up1,xsame)
       else:
          if t>=20 and t<30:
             r32406[:,t]=spline(T/ct[t-20],r32mub406up2,xsame)
          else: 
             if t>=30 and t<40:
                r32406[:,t]=spline(T/ct[t-30],r32mub406up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32406[:,t]=spline(T/ct[t-40],r32mub406up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32406[:,t]=spline(T/ct[t-50],r32mub406down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32406[:,t]=spline(T/ct[t-60],r32mub406down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32406[:,t]=spline(T/ct[t-70],r32mub406down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32406[:,t]=spline(T/ct[t-80],r32mub406down3,xsame)
                            else:
                                r32406[:,t]=spline(T/ct[t-90],r32mub406down4,xsame)

for t in range(0,100):
    if t<10:
       r42406[:,t]=spline(T/ct[t],r42mub406up,xsame)
    else:
       if t>=10 and t<20:
          r42406[:,t]=spline(T/ct[t-10],r42mub406up1,xsame)
       else:
          if t>=20 and t<30:
             r42406[:,t]=spline(T/ct[t-20],r42mub406up2,xsame)
          else: 
             if t>=30 and t<40:
                r42406[:,t]=spline(T/ct[t-30],r42mub406up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42406[:,t]=spline(T/ct[t-40],r42mub406up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42406[:,t]=spline(T/ct[t-50],r42mub406down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42406[:,t]=spline(T/ct[t-60],r42mub406down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42406[:,t]=spline(T/ct[t-70],r42mub406down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42406[:,t]=spline(T/ct[t-80],r42mub406down3,xsame)
                            else:
                                r42406[:,t]=spline(T/ct[t-90],r42mub406down4,xsame)

for t in range(0,100):
    if t<10:
       r62406[:,t]=spline(T/ct[t],r62mub406up,xsame)
    else:
       if t>=10 and t<20:
          r62406[:,t]=spline(T/ct[t-10],r62mub406up1,xsame)
       else:
          if t>=20 and t<30:
             r62406[:,t]=spline(T/ct[t-20],r62mub406up2,xsame)
          else: 
             if t>=30 and t<40:
                r62406[:,t]=spline(T/ct[t-30],r62mub406up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62406[:,t]=spline(T/ct[t-40],r62mub406up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62406[:,t]=spline(T/ct[t-50],r62mub406down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62406[:,t]=spline(T/ct[t-60],r62mub406down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62406[:,t]=spline(T/ct[t-70],r62mub406down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62406[:,t]=spline(T/ct[t-80],r62mub406down3,xsame)
                            else:
                                r62406[:,t]=spline(T/ct[t-90],r62mub406down4,xsame)


for num in range(1,100):
    if num==1:
       max406=np.maximum(r32406[:,num-1],r32406[:,num])
       min406=np.minimum(r32406[:,num-1],r32406[:,num])
    else:
       max406=np.maximum(max406,r32406[:,num])
       min406=np.minimum(min406,r32406[:,num])

for num in range(1,100):
    if num==1:
       max42406=np.maximum(r42406[:,num-1],r42406[:,num])
       min42406=np.minimum(r42406[:,num-1],r42406[:,num])
    else:
       max42406=np.maximum(max42406,r42406[:,num])
       min42406=np.minimum(min42406,r42406[:,num])

for num in range(1,100):
    if num==1:
       max62406=np.maximum(r62406[:,num-1],r62406[:,num])
       min62406=np.minimum(r62406[:,num-1],r62406[:,num])
    else:
       max62406=np.maximum(max62406,r62406[:,num])
       min62406=np.minimum(min62406,r62406[:,num])

r32mub406cen=spline(T/ctcen,r32mub406cen,xsame)
r42mub406cen=spline(T/ctcen,r42mub406cen,xsame)
r62mub406cen=spline(T/ctcen,r62mub406cen,xsame)

dif406cen=abs(r32mub406cen-0.60824)
dif406up=abs(max406-0.60824)
dif406down=abs(min406-0.60824)
min406cen_index=np.argmin(dif406cen[80:300])+80
min406up_index=np.argmin(dif406up[80:300])+80
min406down_index=np.argmin(dif406down[80:300])+80
print(min406up_index)
print(min406down_index)
r42=[max42406[min22up_index],max42406[min22down_index],min42406[min22up_index],min42406[min22down_index]]
r42h=[max42406[min22up_index+5],max42406[min22down_index+5],min42406[min22up_index+5],min42406[min22down_index+5]]
r42l=[max42406[min22up_index-5],max42406[min22down_index-5],min42406[min22up_index-5],min42406[min22down_index-5]]
r42406up=np.max(r42)
r42406down=np.min(r42)
r42406uph=np.max(r42h)
r42406downh=np.min(r42h)
r42406upl=np.max(r42l)
r42406downl=np.min(r42l)
r62=[max42406[min22up_index],max42406[min22down_index],min42406[min22up_index],min42406[min22down_index]]
r62h=[max42406[min22up_index+5],max42406[min22down_index+5],min42406[min22up_index+5],min42406[min22down_index+5]]
r62l=[max42406[min22up_index-5],max42406[min22down_index-5],min42406[min22up_index-5],min42406[min22down_index-5]]
r62406up=np.max(r62)
r62406down=np.min(r62)
r62406uph=np.max(r62h)
r62406downh=np.min(r62h)
r62406upl=np.max(r62l)
r62406downl=np.min(r62l)
print(r62406up)
print(r62406down)
####################################################################################################
r62up=[r6222up,r6268up,r62106up,r62148up,r62196up,r62303up,r62406up]
r62down=[r6222down,r6268down,r62106down,r62148down,r62196down,r62303down,r62406down]
r42up=[r4222up,r4268up,r42106up,r42148up,r42196up,r42303up,r42406up]
r42down=[r4222down,r4268down,r42106down,r42148down,r42196down,r42303down,r42406down]
r62uph=[r6222uph,r6268uph,r62106uph,r62148uph,r62196uph,r62303uph,r62406uph]
r62downh=[r6222downh,r6268downh,r62106downh,r62148downh,r62196downh,r62303downh,r62406downh]
r42uph=[r4222uph,r4268uph,r42106uph,r42148uph,r42196uph,r42303uph,r42406uph]
r42downh=[r4222downh,r4268downh,r42106downh,r42148downh,r42196downh,r42303downh,r42406downh]
r62upl=[r6222upl,r6268upl,r62106upl,r62148upl,r62196upl,r62303upl,r62406upl]
r62downl=[r6222downl,r6268downl,r62106downl,r62148downl,r62196downl,r62303downl,r62406downl]
r42upl=[r4222upl,r4268upl,r42106upl,r42148upl,r42196upl,r42303upl,r42406upl]
r42downl=[r4222downl,r4268downl,r42106downl,r42148downl,r42196downl,r42303downl,r42406downl]
r62cen=np.zeros(7)
r62err=np.zeros(7)
r42cen=np.zeros(7)
r42err=np.zeros(7)
r62cenh=np.zeros(7)
r62errh=np.zeros(7)
r42cenh=np.zeros(7)
r42errh=np.zeros(7)
r62cenl=np.zeros(7)
r62errl=np.zeros(7)
r42cenl=np.zeros(7)
r42errl=np.zeros(7)
for i in range(0,7):
    r62cen[i]=(r62up[i]+r62down[i])/2.
    r62err[i]=(r62up[i]-r62down[i])/2.
    r42cen[i]=(r42up[i]+r42down[i])/2.
    r42err[i]=(r42up[i]-r42down[i])/2.
    r62cenh[i]=(r62uph[i]+r62downh[i])/2.
    r62errh[i]=(r62uph[i]-r62downh[i])/2.
    r42cenh[i]=(r42uph[i]+r42downh[i])/2.
    r42errh[i]=(r42uph[i]-r42downh[i])/2.
    r62cenl[i]=(r62upl[i]+r62downl[i])/2.
    r62errl[i]=(r62upl[i]-r62downl[i])/2.
    r42cenl[i]=(r42upl[i]+r42downl[i])/2.
    r42errl[i]=(r42upl[i]-r42downl[i])/2.

for num in range(0,100):
    T22up[num]=min22up_index
    T22down[num]=min22down_index
    T68up[num]=min68up_index
    T68down[num]=min68down_index
    T106up[num]=min106up_index
    T106down[num]=min106down_index
    T148up[num]=min148up_index
    T148down[num]=min148down_index
    T196up[num]=min196up_index
    T196down[num]=min196down_index
    T303up[num]=min303up_index
    T303down[num]=min303down_index
    T406up[num]=min406up_index
    T406down[num]=min406down_index
####################################################################################################
# Create figure
fig=plt.figure(figsize=(12, 18.5))
#fig=plt.figure()
ax1=fig.add_subplot(631)
ax1.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax1.plot(energy,r62cen,color='blue',label=r'$T_f$')
ax1.errorbar(energy,r62cenh,yerr=r62errh,color='green',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax1.plot(energy,r62cenh,color='green',label=r'$T_f+5$')
ax1.errorbar(energy,r62cenl,yerr=r62errl,color='red',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax1.plot(energy,r62cenl,color='red',label=r'$T_f-5$')
ax1.set_xscale('log')
ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
plt.axis([5,230,-2.,2.])
ax1.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax2=fig.add_subplot(632)
band_mub=ax2.fill_between(xsame,max22,min22,alpha=0.25,facecolor='b',edgecolor='',label=r'$200$')
line_mub,=ax2.plot(xsame,r32mub22cen,'b',linewidth=1,alpha=0.5)
ax2.plot(xsame,data200)
ax2.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,0.4])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi^B_3/\chi^B_2$', fontsize=14, color='black')
for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax3=fig.add_subplot(633)
band_mub=ax3.fill_between(xsame,max68,min68,alpha=0.25,facecolor='b',edgecolor='',label=r'$62.4$')
line_mub,=ax3.plot(xsame,r32mub68cen,'b',linewidth=1,alpha=0.5)
ax3.plot(xsame,data62)

ax3.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,0.8])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax3.set_ylabel(r'$\chi^B_3/\chi^B_2$', fontsize=14, color='black')
for label in ax3.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax4=fig.add_subplot(634)
band_mub=ax4.fill_between(xsame,max106,min106,alpha=0.25,facecolor='b',edgecolor='',label=r'$39$')
line_mub,=ax4.plot(xsame,r32mub106cen,'b',linewidth=1,alpha=0.5)
ax4.plot(xsame,data39)
ax4.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax4.set_ylabel(r'$\chi^B_3/\chi^B_2$', fontsize=14, color='black')
for label in ax4.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax4.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax5=fig.add_subplot(635)
band_mub=ax5.fill_between(xsame,max148,min148,alpha=0.25,facecolor='b',edgecolor='',label=r'$27$')
line_mub,=ax5.plot(xsame,r32mub148cen,'b',linewidth=1,alpha=0.5)
ax5.plot(xsame,data27)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
ax5.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax5.set_ylabel(r'$\chi^B_3/\chi^B_2$', fontsize=14, color='black')
for label in ax5.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax5.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax6=fig.add_subplot(636)
band_mub=ax6.fill_between(xsame,max196,min196,alpha=0.25,facecolor='b',edgecolor='',label=r'$19.6$')
line_mub,=ax6.plot(xsame,r32mub196cen,'b',linewidth=1,alpha=0.5)
ax6.plot(xsame,data19)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
ax6.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax6.set_ylabel(r'$\chi^B_3/\chi^B_2$', fontsize=14, color='black')
for label in ax6.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax6.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax7=fig.add_subplot(637)
band_mub=ax7.fill_between(xsame,max303,min303,alpha=0.25,facecolor='b',edgecolor='',label=r'$11.5$')
line_mub,=ax7.plot(xsame,r32mub303cen,'b',linewidth=1,alpha=0.5)
ax7.plot(xsame,data11)
ax7.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax7.set_ylabel(r'$\chi^B_3/\chi^B_2$', fontsize=14, color='black')
for label in ax7.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax7.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax8=fig.add_subplot(638)
band_mub=ax8.fill_between(xsame,max406,min406,alpha=0.25,facecolor='b',edgecolor='',label=r'$7.7$')
line_mub,=ax8.plot(xsame,r32mub406cen,'b',linewidth=1,alpha=0.5)
ax8.plot(xsame,data7)
ax8.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax8.set_ylabel(r'$\chi^B_3/\chi^B_2$', fontsize=14, color='black')
for label in ax8.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax8.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax9=fig.add_subplot(639)
band_mub=ax9.fill_between(xsame,max6222,min6222,alpha=0.25,facecolor='b',edgecolor='',label=r'$200$')
line_mub,=ax9.plot(xsame,r62mub22cen,'b',linewidth=1,alpha=0.5)
ax9.plot(T22up,y62)
ax9.plot(T22down,y62)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
ax9.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-0.5,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax9.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax9.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax9.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax10=fig.add_subplot(6,3,10)
band_mub=ax10.fill_between(xsame,max6268,min6268,alpha=0.25,facecolor='b',edgecolor='',label=r'$62.4$')
line_mub,=ax10.plot(xsame,r62mub68cen,'b',linewidth=1,alpha=0.5)
ax10.plot(T68up,y62)
ax10.plot(T68down,y62)
ax10.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-0.5,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax10.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax10.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax10.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax11=fig.add_subplot(6,3,11)
band_mub=ax11.fill_between(xsame,max62106,min62106,alpha=0.25,facecolor='b',edgecolor='',label=r'$39$')
line_mub,=ax11.plot(xsame,r62mub106cen,'b',linewidth=1,alpha=0.5)
ax11.plot(T106up,y62)
ax11.plot(T106down,y62)
ax11.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-1,1.4])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax11.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax11.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax11.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax12=fig.add_subplot(6,3,12)
band_mub=ax12.fill_between(xsame,max62148,min62148,alpha=0.25,facecolor='b',edgecolor='',label=r'$27$')
line_mub,=ax12.plot(xsame,r62mub148cen,'b',linewidth=1,alpha=0.5)
ax12.plot(T148up,y62)
ax12.plot(T148down,y62)
ax12.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-1,1.5])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax12.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax12.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax12.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax13=fig.add_subplot(6,3,13)
band_mub=ax13.fill_between(xsame,max62196,min62196,alpha=0.25,facecolor='b',edgecolor='',label=r'$19.6$')
line_mub,=ax13.plot(xsame,r62mub196cen,'b',linewidth=1,alpha=0.5)
ax13.plot(T196up,y62)
ax13.plot(T196down,y62)
ax13.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-2.2,1.7])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax13.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax13.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax13.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax14=fig.add_subplot(6,3,14)
band_mub=ax14.fill_between(xsame,max62303,min62303,alpha=0.25,facecolor='b',edgecolor='',label=r'$11.5$')
line_mub,=ax14.plot(xsame,r62mub303cen,'b',linewidth=1,alpha=0.5)
ax14.plot(T303up,y62)
ax14.plot(T303down,y62)
ax14.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-10,5])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax14.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax14.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax14.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax15=fig.add_subplot(6,3,15)
band_mub=ax15.fill_between(xsame,max62406,min62406,alpha=0.25,facecolor='b',edgecolor='',label=r'$7.7$')
line_mub,=ax15.plot(xsame,r62mub406cen,'b',linewidth=1,alpha=0.5)
ax15.plot(T406up,y62)
ax15.plot(T406down,y62)
ax15.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-60,50])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax15.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax15.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax15.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax16=fig.add_subplot(6,3,16)
ax16.errorbar(energy,r42cen,yerr=r42err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax16.errorbar(energy,r42cen,color='blue')
ax16.errorbar(energy,r42cenh,yerr=r42errh,color='green',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax16.errorbar(energy,r42cenh,color='green')
ax16.errorbar(energy,r42cenl,yerr=r42errl,color='red',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax16.errorbar(energy,r42cenl,color='red')
ax16.set_xscale('log')
plt.axis([5,230,-2.,2.])
ax16.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax16.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')
for label in ax16.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax16.yaxis.get_ticklabels():
    label.set_fontsize(10)


fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("R32toR62.pdf")

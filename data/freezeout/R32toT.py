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
T=np.loadtxt('./TMeV.dat')
kurtosis=np.loadtxt('./RHICdatakurtosis.dat')
data200=np.zeros(300)
data62=np.zeros(300)
data54=np.zeros(300)
data39=np.zeros(300)
data27=np.zeros(300)
data19=np.zeros(300)
data14=np.zeros(300)
data11=np.zeros(300)
data7=np.zeros(300)
y62=np.linspace(-100,100,100)
T22up=np.zeros(100)
T22down=np.zeros(100)
T68up=np.zeros(100)
T68down=np.zeros(100)
T78up=np.zeros(100)
T78down=np.zeros(100)
T106up=np.zeros(100)
T106down=np.zeros(100)
T148up=np.zeros(100)
T148down=np.zeros(100)
T196up=np.zeros(100)
T196down=np.zeros(100)
T252up=np.zeros(100)
T252down=np.zeros(100)
T303up=np.zeros(100)
T303down=np.zeros(100)
T406up=np.zeros(100)
T406down=np.zeros(100)
for num in range(0,300):
    data200[num]=0.122302
    data62[num]=0.325439
    data54[num]=0.346852
    data39[num]=0.441900
    data27[num]=0.553053
    data19[num]=0.642055
    data14[num]=0.782208
    data11[num]=0.783562
    data7[num]=0.798587


energy=[200.,62.4,54.4,39.,27.,19.6,14.5,11.5,7.7]

#############################################################################################################################################
xsame=np.linspace(0.,299.,300)
deltat=0.05
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

dif22cen=abs(r32mub22cen-0.122302)
dif22up=abs(max22-0.122302)
dif22down=abs(min22-0.122302)
min22cen_index=np.argmin(dif22cen[80:300])+80
min22up_index=np.argmin(dif22up[80:300])+80
min22down_index=np.argmin(dif22down[80:300])+80
print(min22up_index)
print(min22down_index)
r4222cen=r42mub22cen[min22cen_index]
r6222cen=r62mub22cen[min22cen_index]
r4222hcen=r42mub22cen[min22cen_index+int(min22cen_index*deltat)]
r6222hcen=r62mub22cen[min22cen_index+int(min22cen_index*deltat)]
r4222lcen=r42mub22cen[min22cen_index-5]
r6222lcen=r62mub22cen[min22cen_index-5]
r42=[max4222[min22up_index],max4222[min22down_index],min4222[min22up_index],min4222[min22down_index]]
r42h=[max4222[min22up_index+int(min22up_index*deltat)],max4222[min22down_index+int(min22down_index*deltat)],min4222[min22up_index+int(min22up_index*deltat)],min4222[min22down_index+int(min22down_index*deltat)]]
r42l=[max4222[min22up_index-5],max4222[min22down_index-5],min4222[min22up_index-5],min4222[min22down_index-5]]
r4222up=np.max(r42)
r4222down=np.min(r42)
r4222uph=np.max(r42h)
r4222downh=np.min(r42h)
r4222upl=np.max(r42l)
r4222downl=np.min(r42l)
r62=[max6222[min22up_index],max6222[min22down_index],min6222[min22up_index],min6222[min22down_index]]
r62h=[max6222[min22up_index+int(min22up_index*deltat)],max6222[min22down_index+int(min22down_index*deltat)],min6222[min22up_index+int(min22up_index*deltat)],min6222[min22down_index+int(min22down_index*deltat)]]
r62l=[max6222[min22up_index-5],max6222[min22down_index-5],min6222[min22up_index-5],min6222[min22down_index-5]]
r6222up=np.max(r62)
r6222down=np.min(r62)
r6222uph=np.max(r62h)
r6222downh=np.min(r62h)
r6222upl=np.max(r62l)
r6222downl=np.min(r62l)
print(r6222up)
print(r6222down)
print(r6222uph)
print(r6222downh)
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

dif68cen=abs(r32mub68cen-0.325439)
dif68up=abs(max68-0.325439)
dif68down=abs(min68-0.325439)
min68cen_index=np.argmin(dif68cen[80:300])+80
min68up_index=np.argmin(dif68up[80:300])+80
min68down_index=np.argmin(dif68down[80:300])+80
print(min68up_index)
print(min68down_index)
r4268cen=r42mub68cen[min68cen_index]
r6268cen=r62mub68cen[min68cen_index]
r4268hcen=r42mub68cen[min68cen_index+int(min68cen_index*deltat)]
r6268hcen=r62mub68cen[min68cen_index+int(min68cen_index*deltat)]
r4268lcen=r42mub68cen[min68cen_index-5]
r6268lcen=r62mub68cen[min68cen_index-5]
r42=[max4268[min68up_index],max4268[min68down_index],min4268[min68up_index],min4268[min68down_index]]
r42h=[max4268[min68up_index+int(min68up_index*deltat)],max4268[min68down_index+int(min68down_index*deltat)],min4268[min68up_index+int(min68up_index*deltat)],min4268[min68down_index+int(min68down_index*deltat)]]
r42l=[max4268[min68up_index-5],max4268[min68down_index-5],min4268[min68up_index-5],min4268[min68down_index-5]]
r4268up=np.max(r42)
r4268down=np.min(r42)
r4268uph=np.max(r42h)
r4268downh=np.min(r42h)
r4268upl=np.max(r42l)
r4268downl=np.min(r42l)
r62=[max6268[min68up_index],max6268[min68down_index],min6268[min68up_index],min6268[min68down_index]]
r62h=[max6268[min68up_index+int(min68up_index*deltat)],max6268[min68down_index+int(min68down_index*deltat)],min6268[min68up_index+int(min68up_index*deltat)],min6268[min68down_index+int(min68down_index*deltat)]]
r62l=[max6268[min68up_index-5],max6268[min68down_index-5],min6268[min68up_index-5],min6268[min68down_index-5]]
r6268up=np.max(r62)
r6268down=np.min(r62)
r6268uph=np.max(r62h)
r6268downh=np.min(r62h)
r6268upl=np.max(r62l)
r6268downl=np.min(r62l)
print(r6268up)
print(r6268down)
####################################################################################################
chi2mub78cen=np.loadtxt(r'./mub78/cmucen/final/buffer/chi2.dat')
chi3mub78cen=np.loadtxt(r'./mub78/cmucen/final/buffer/chi3.dat')
chi4mub78cen=np.loadtxt(r'./mub78/cmucen/final/buffer/chi4.dat')
chi6mub78cen=np.loadtxt(r'./mub78/cmucen/final/buffer/chi6.dat')
chi8mub78cen=np.loadtxt(r'./mub78/cmucen/final/buffer/chi8.dat')
r32mub78cen=chi3mub78cen/chi2mub78cen
r42mub78cen=chi4mub78cen/chi2mub78cen
r62mub78cen=chi6mub78cen/chi2mub78cen
r82mub78cen=chi8mub78cen/chi2mub78cen
chi2mub78up=np.loadtxt(r'./mub78/cmuup/final/buffer/chi2.dat')
chi3mub78up=np.loadtxt(r'./mub78/cmuup/final/buffer/chi3.dat')
chi4mub78up=np.loadtxt(r'./mub78/cmuup/final/buffer/chi4.dat')
chi6mub78up=np.loadtxt(r'./mub78/cmuup/final/buffer/chi6.dat')
chi8mub78up=np.loadtxt(r'./mub78/cmuup/final/buffer/chi8.dat')
r32mub78up=chi3mub78up/chi2mub78up
r42mub78up=chi4mub78up/chi2mub78up
r62mub78up=chi6mub78up/chi2mub78up
r82mub78up=chi8mub78up/chi2mub78up
chi2mub78down=np.loadtxt(r'./mub78/cmudown/final/buffer/chi2.dat')
chi3mub78down=np.loadtxt(r'./mub78/cmudown/final/buffer/chi3.dat')
chi4mub78down=np.loadtxt(r'./mub78/cmudown/final/buffer/chi4.dat')
chi6mub78down=np.loadtxt(r'./mub78/cmudown/final/buffer/chi6.dat')
chi8mub78down=np.loadtxt(r'./mub78/cmudown/final/buffer/chi8.dat')
r32mub78down=chi3mub78down/chi2mub78down
r42mub78down=chi4mub78down/chi2mub78down
r62mub78down=chi6mub78down/chi2mub78down
r82mub78down=chi8mub78down/chi2mub78down
r3278=np.zeros((300,20))
r4278=np.zeros((300,20))
r6278=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r3278[:,t]=spline(T/ct[t],r32mub78up,xsame)
    else:
       r3278[:,t]=spline(T/ct[t-10],r32mub78down,xsame)


for num in range(1,20):
    if num==1:
       max78=np.maximum(r3278[:,num-1],r3278[:,num])
       min78=np.minimum(r3278[:,num-1],r3278[:,num])
    else:
       max78=np.maximum(max78,r3278[:,num])
       min78=np.minimum(min78,r3278[:,num])

for t in range(0,20):
    if t<10:
       r4278[:,t]=spline(T/ct[t],r42mub78up,xsame)
    else:
       r4278[:,t]=spline(T/ct[t-10],r42mub78down,xsame)


for num in range(1,20):
    if num==1:
       max4278=np.maximum(r4278[:,num-1],r4278[:,num])
       min4278=np.minimum(r4278[:,num-1],r4278[:,num])
    else:
       max4278=np.maximum(max4278,r4278[:,num])
       min4278=np.minimum(min4278,r4278[:,num])

for t in range(0,20):
    if t<10:
       r6278[:,t]=spline(T/ct[t],r62mub78up,xsame)
    else:
       r6278[:,t]=spline(T/ct[t-10],r62mub78down,xsame)


for num in range(1,20):
    if num==1:
       max6278=np.maximum(r6278[:,num-1],r6278[:,num])
       min6278=np.minimum(r6278[:,num-1],r6278[:,num])
    else:
       max6278=np.maximum(max6278,r6278[:,num])
       min6278=np.minimum(min6278,r6278[:,num])

r32mub78cen=spline(T/ctcen,r32mub78cen,xsame)
r42mub78cen=spline(T/ctcen,r42mub78cen,xsame)
r62mub78cen=spline(T/ctcen,r62mub78cen,xsame)

dif78cen=abs(r32mub78cen-0.346852)
dif78up=abs(max78-0.346852)
dif78down=abs(min78-0.346852)
min78cen_index=np.argmin(dif78cen[80:300])+80
min78up_index=np.argmin(dif78up[80:300])+80
min78down_index=np.argmin(dif78down[80:300])+80
print(min78up_index)
print(min78down_index)
r4278cen=r42mub78cen[min78cen_index]
r6278cen=r62mub78cen[min78cen_index]
r4278hcen=r42mub78cen[min78cen_index+int(min78cen_index*deltat)]
r6278hcen=r62mub78cen[min78cen_index+int(min78cen_index*deltat)]
r4278lcen=r42mub78cen[min78cen_index-5]
r6278lcen=r62mub78cen[min78cen_index-5]
r42=[max4278[min78up_index],max4278[min78down_index],min4278[min78up_index],min4278[min78down_index]]
r42h=[max4278[min78up_index+int(min78up_index*deltat)],max4278[min78down_index+int(min78down_index*deltat)],min4278[min78up_index+int(min78up_index*deltat)],min4278[min78down_index+int(min78down_index*deltat)]]
r42l=[max4278[min78up_index-5],max4278[min78down_index-5],min4278[min78up_index-5],min4278[min78down_index-5]]
r4278up=np.max(r42)
r4278down=np.min(r42)
r4278uph=np.max(r42h)
r4278downh=np.min(r42h)
r4278upl=np.max(r42l)
r4278downl=np.min(r42l)
r62=[max6278[min78up_index],max6278[min78down_index],min6278[min78up_index],min6278[min78down_index]]
r62h=[max6278[min78up_index+int(min78up_index*deltat)],max6278[min78down_index+int(min78down_index*deltat)],min6278[min78up_index+int(min78up_index*deltat)],min6278[min78down_index+int(min78down_index*deltat)]]
r62l=[max6278[min78up_index-5],max6278[min78down_index-5],min6278[min78up_index-5],min6278[min78down_index-5]]
r6278up=np.max(r62)
r6278down=np.min(r62)
r6278uph=np.max(r62h)
r6278downh=np.min(r62h)
r6278upl=np.max(r62l)
r6278downl=np.min(r62l)
print(r6278up)
print(r6278down)
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

dif106cen=abs(r32mub106cen-0.441900)
dif106up=abs(max106-0.441900)
dif106down=abs(min106-0.441900)
min106cen_index=np.argmin(dif106cen[80:300])+80
min106up_index=np.argmin(dif106up[80:300])+80
min106down_index=np.argmin(dif106down[80:300])+80
print(min106up_index)
print(min106down_index)
r42106cen=r42mub106cen[min106cen_index]
r62106cen=r62mub106cen[min106cen_index]
r42106hcen=r42mub106cen[min106cen_index+int(min106cen_index*deltat)]
r62106hcen=r62mub106cen[min106cen_index+int(min106cen_index*deltat)]
r42106lcen=r42mub106cen[min106cen_index-5]
r62106lcen=r62mub106cen[min106cen_index-5]
r42=[max42106[min106up_index],max42106[min106down_index],min42106[min106up_index],min42106[min106down_index]]
r42h=[max42106[min106up_index+int(min106up_index*deltat)],max42106[min106down_index+int(min106down_index*deltat)],min42106[min106up_index+int(min106up_index*deltat)],min42106[min106down_index+int(min106down_index*deltat)]]
r42l=[max42106[min106up_index-5],max42106[min106down_index-5],min42106[min106up_index-5],min42106[min106down_index-5]]
r42106up=np.max(r42)
r42106down=np.min(r42)
r42106uph=np.max(r42h)
r42106downh=np.min(r42h)
r42106upl=np.max(r42l)
r42106downl=np.min(r42l)
r62=[max62106[min106up_index],max62106[min106down_index],min62106[min106up_index],min62106[min106down_index]]
r62h=[max62106[min106up_index+int(min106up_index*deltat)],max62106[min106down_index+int(min106down_index*deltat)],min62106[min106up_index+int(min106up_index*deltat)],min62106[min106down_index+int(min106down_index*deltat)]]
r62l=[max62106[min106up_index-5],max62106[min106down_index-5],min62106[min106up_index-5],min62106[min106down_index-5]]
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

dif148cen=abs(r32mub148cen-0.553053)
dif148up=abs(max148-0.553053)
dif148down=abs(min148-0.553053)
min148cen_index=np.argmin(dif148cen[80:300])+80
min148up_index=np.argmin(dif148up[80:300])+80
min148down_index=np.argmin(dif148down[80:300])+80
print(min148up_index)
print(min148down_index)
r42148cen=r42mub148cen[min148cen_index]
r62148cen=r62mub148cen[min148cen_index]
r42148hcen=r42mub148cen[min148cen_index+int(min148cen_index*deltat)]
r62148hcen=r62mub148cen[min148cen_index+int(min148cen_index*deltat)]
r42148lcen=r42mub148cen[min148cen_index-5]
r62148lcen=r62mub148cen[min148cen_index-5]
r42=[max42148[min148up_index],max42148[min148down_index],min42148[min148up_index],min42148[min148down_index]]
r42h=[max42148[min148up_index+int(min148up_index*deltat)],max42148[min148down_index+int(min148down_index*deltat)],min42148[min148up_index+int(min148up_index*deltat)],min42148[min148down_index+int(min148down_index*deltat)]]
r42l=[max42148[min148up_index-5],max42148[min148down_index-5],min42148[min148up_index-5],min42148[min148down_index-5]]
r42148up=np.max(r42)
r42148down=np.min(r42)
r42148uph=np.max(r42h)
r42148downh=np.min(r42h)
r42148upl=np.max(r42l)
r42148downl=np.min(r42l)
r62=[max62148[min148up_index],max62148[min148down_index],min62148[min148up_index],min62148[min148down_index]]
r62h=[max62148[min148up_index+int(min148up_index*deltat)],max62148[min148down_index+int(min148down_index*deltat)],min62148[min148up_index+int(min148up_index*deltat)],min62148[min148down_index+int(min148down_index*deltat)]]
r62l=[max62148[min148up_index-5],max62148[min148down_index-5],min62148[min148up_index-5],min62148[min148down_index-5]]
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

dif196cen=abs(r32mub196cen-0.642055)
dif196up=abs(max196-0.642055)
dif196down=abs(min196-0.642055)
min196cen_index=np.argmin(dif196cen[80:300])+80
min196up_index=np.argmin(dif196up[80:300])+80
min196down_index=np.argmin(dif196down[80:300])+80
print(min196up_index)
print(min196down_index)
r42196cen=r42mub196cen[min196cen_index]
r62196cen=r62mub196cen[min196cen_index]
r42196hcen=r42mub196cen[min196cen_index+int(min196cen_index*deltat)]
r62196hcen=r62mub196cen[min196cen_index+int(min196cen_index*deltat)]
r42196lcen=r42mub196cen[min196cen_index-5]
r62196lcen=r62mub196cen[min196cen_index-5]
r42=[max42196[min196up_index],max42196[min196down_index],min42196[min196up_index],min42196[min196down_index]]
r42h=[max42196[min196up_index+int(min196up_index*deltat)],max42196[min196down_index+int(min196down_index*deltat)],min42196[min196up_index+int(min196up_index*deltat)],min42196[min196down_index+int(min196down_index*deltat)]]
r42l=[max42196[min196up_index-5],max42196[min196down_index-5],min42196[min196up_index-5],min42196[min196down_index-5]]
r42196up=np.max(r42)
r42196down=np.min(r42)
r42196uph=np.max(r42h)
r42196downh=np.min(r42h)
r42196upl=np.max(r42l)
r42196downl=np.min(r42l)
r62=[max62196[min196up_index],max62196[min196down_index],min62196[min196up_index],min62196[min196down_index]]
r62h=[max62196[min196up_index+int(min196up_index*deltat)],max62196[min196down_index+int(min196down_index*deltat)],min62196[min196up_index+int(min196up_index*deltat)],min62196[min196down_index+int(min196down_index*deltat)]]
r62l=[max62196[min196up_index-5],max62196[min196down_index-5],min62196[min196up_index-5],min62196[min196down_index-5]]
r62196up=np.max(r62)
r62196down=np.min(r62)
r62196uph=np.max(r62h)
r62196downh=np.min(r62h)
r62196upl=np.max(r62l)
r62196downl=np.min(r62l)
print(r62196up)
print(r62196down)
####################################################################################################
chi2mub252cen=np.loadtxt(r'./mub252/cmucen/final/buffer/chi2.dat')
chi3mub252cen=np.loadtxt(r'./mub252/cmucen/final/buffer/chi3.dat')
chi4mub252cen=np.loadtxt(r'./mub252/cmucen/final/buffer/chi4.dat')
chi6mub252cen=np.loadtxt(r'./mub252/cmucen/final/buffer/chi6.dat')
chi8mub252cen=np.loadtxt(r'./mub252/cmucen/final/buffer/chi8.dat')
r32mub252cen=chi3mub252cen/chi2mub252cen
r42mub252cen=chi4mub252cen/chi2mub252cen
r62mub252cen=chi6mub252cen/chi2mub252cen
r82mub252cen=chi8mub252cen/chi2mub252cen
chi2mub252up=np.loadtxt(r'./mub252/cmuup/final/buffer/chi2.dat')
chi3mub252up=np.loadtxt(r'./mub252/cmuup/final/buffer/chi3.dat')
chi4mub252up=np.loadtxt(r'./mub252/cmuup/final/buffer/chi4.dat')
chi6mub252up=np.loadtxt(r'./mub252/cmuup/final/buffer/chi6.dat')
chi8mub252up=np.loadtxt(r'./mub252/cmuup/final/buffer/chi8.dat')
r32mub252up=chi3mub252up/chi2mub252up
r42mub252up=chi4mub252up/chi2mub252up
r62mub252up=chi6mub252up/chi2mub252up
r82mub252up=chi8mub252up/chi2mub252up
chi2mub252up1=np.loadtxt(r'./mub252/cmuup1/final/buffer/chi2.dat')
chi3mub252up1=np.loadtxt(r'./mub252/cmuup1/final/buffer/chi3.dat')
chi4mub252up1=np.loadtxt(r'./mub252/cmuup1/final/buffer/chi4.dat')
chi6mub252up1=np.loadtxt(r'./mub252/cmuup1/final/buffer/chi6.dat')
chi8mub252up1=np.loadtxt(r'./mub252/cmuup1/final/buffer/chi8.dat')
r32mub252up1=chi3mub252up1/chi2mub252up1
r42mub252up1=chi4mub252up1/chi2mub252up1
r62mub252up1=chi6mub252up1/chi2mub252up1
r82mub252up1=chi8mub252up1/chi2mub252up1
chi2mub252up2=np.loadtxt(r'./mub252/cmuup2/final/buffer/chi2.dat')
chi3mub252up2=np.loadtxt(r'./mub252/cmuup2/final/buffer/chi3.dat')
chi4mub252up2=np.loadtxt(r'./mub252/cmuup2/final/buffer/chi4.dat')
chi6mub252up2=np.loadtxt(r'./mub252/cmuup2/final/buffer/chi6.dat')
chi8mub252up2=np.loadtxt(r'./mub252/cmuup2/final/buffer/chi8.dat')
r32mub252up2=chi3mub252up2/chi2mub252up2
r42mub252up2=chi4mub252up2/chi2mub252up2
r62mub252up2=chi6mub252up2/chi2mub252up2
r82mub252up2=chi8mub252up2/chi2mub252up2
chi2mub252up3=np.loadtxt(r'./mub252/cmuup3/final/buffer/chi2.dat')
chi3mub252up3=np.loadtxt(r'./mub252/cmuup3/final/buffer/chi3.dat')
chi4mub252up3=np.loadtxt(r'./mub252/cmuup3/final/buffer/chi4.dat')
chi6mub252up3=np.loadtxt(r'./mub252/cmuup3/final/buffer/chi6.dat')
chi8mub252up3=np.loadtxt(r'./mub252/cmuup3/final/buffer/chi8.dat')
r32mub252up3=chi3mub252up3/chi2mub252up3
r42mub252up3=chi4mub252up3/chi2mub252up3
r62mub252up3=chi6mub252up3/chi2mub252up3
r82mub252up3=chi8mub252up3/chi2mub252up3
chi2mub252up4=np.loadtxt(r'./mub252/cmuup4/final/buffer/chi2.dat')
chi3mub252up4=np.loadtxt(r'./mub252/cmuup4/final/buffer/chi3.dat')
chi4mub252up4=np.loadtxt(r'./mub252/cmuup4/final/buffer/chi4.dat')
chi6mub252up4=np.loadtxt(r'./mub252/cmuup4/final/buffer/chi6.dat')
chi8mub252up4=np.loadtxt(r'./mub252/cmuup4/final/buffer/chi8.dat')
r32mub252up4=chi3mub252up4/chi2mub252up4
r42mub252up4=chi4mub252up4/chi2mub252up4
r62mub252up4=chi6mub252up4/chi2mub252up4
r82mub252up4=chi8mub252up4/chi2mub252up4
chi2mub252down=np.loadtxt(r'./mub252/cmudown/final/buffer/chi2.dat')
chi3mub252down=np.loadtxt(r'./mub252/cmudown/final/buffer/chi3.dat')
chi4mub252down=np.loadtxt(r'./mub252/cmudown/final/buffer/chi4.dat')
chi6mub252down=np.loadtxt(r'./mub252/cmudown/final/buffer/chi6.dat')
chi8mub252down=np.loadtxt(r'./mub252/cmudown/final/buffer/chi8.dat')
r32mub252down=chi3mub252down/chi2mub252down
r42mub252down=chi4mub252down/chi2mub252down
r62mub252down=chi6mub252down/chi2mub252down
r82mub252down=chi8mub252down/chi2mub252down
chi2mub252down1=np.loadtxt(r'./mub252/cmudown1/final/buffer/chi2.dat')
chi3mub252down1=np.loadtxt(r'./mub252/cmudown1/final/buffer/chi3.dat')
chi4mub252down1=np.loadtxt(r'./mub252/cmudown1/final/buffer/chi4.dat')
chi6mub252down1=np.loadtxt(r'./mub252/cmudown1/final/buffer/chi6.dat')
chi8mub252down1=np.loadtxt(r'./mub252/cmudown1/final/buffer/chi8.dat')
r32mub252down1=chi3mub252down1/chi2mub252down1
r42mub252down1=chi4mub252down1/chi2mub252down1
r62mub252down1=chi6mub252down1/chi2mub252down1
r82mub252down1=chi8mub252down1/chi2mub252down1
chi2mub252down2=np.loadtxt(r'./mub252/cmudown2/final/buffer/chi2.dat')
chi3mub252down2=np.loadtxt(r'./mub252/cmudown2/final/buffer/chi3.dat')
chi4mub252down2=np.loadtxt(r'./mub252/cmudown2/final/buffer/chi4.dat')
chi6mub252down2=np.loadtxt(r'./mub252/cmudown2/final/buffer/chi6.dat')
chi8mub252down2=np.loadtxt(r'./mub252/cmudown2/final/buffer/chi8.dat')
r32mub252down2=chi3mub252down2/chi2mub252down2
r42mub252down2=chi4mub252down2/chi2mub252down2
r62mub252down2=chi6mub252down2/chi2mub252down2
r82mub252down2=chi8mub252down2/chi2mub252down2
chi2mub252down3=np.loadtxt(r'./mub252/cmudown3/final/buffer/chi2.dat')
chi3mub252down3=np.loadtxt(r'./mub252/cmudown3/final/buffer/chi3.dat')
chi4mub252down3=np.loadtxt(r'./mub252/cmudown3/final/buffer/chi4.dat')
chi6mub252down3=np.loadtxt(r'./mub252/cmudown3/final/buffer/chi6.dat')
chi8mub252down3=np.loadtxt(r'./mub252/cmudown3/final/buffer/chi8.dat')
r32mub252down3=chi3mub252down3/chi2mub252down3
r42mub252down3=chi4mub252down3/chi2mub252down3
r62mub252down3=chi6mub252down3/chi2mub252down3
r82mub252down3=chi8mub252down3/chi2mub252down3
chi2mub252down4=np.loadtxt(r'./mub252/cmudown4/final/buffer/chi2.dat')
chi3mub252down4=np.loadtxt(r'./mub252/cmudown4/final/buffer/chi3.dat')
chi4mub252down4=np.loadtxt(r'./mub252/cmudown4/final/buffer/chi4.dat')
chi6mub252down4=np.loadtxt(r'./mub252/cmudown4/final/buffer/chi6.dat')
chi8mub252down4=np.loadtxt(r'./mub252/cmudown4/final/buffer/chi8.dat')
r32mub252down4=chi3mub252down4/chi2mub252down4
r42mub252down4=chi4mub252down4/chi2mub252down4
r62mub252down4=chi6mub252down4/chi2mub252down4
r82mub252down4=chi8mub252down4/chi2mub252down4
r32252=np.zeros((300,100))
r42252=np.zeros((300,100))
r62252=np.zeros((300,100))
for t in range(0,100):
    if t<10:
       r32252[:,t]=spline(T/ct[t],r32mub252up,xsame)
    else:
       if t>=10 and t<20:
          r32252[:,t]=spline(T/ct[t-10],r32mub252up1,xsame)
       else:
          if t>=20 and t<30:
             r32252[:,t]=spline(T/ct[t-20],r32mub252up2,xsame)
          else: 
             if t>=30 and t<40:
                r32252[:,t]=spline(T/ct[t-30],r32mub252up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32252[:,t]=spline(T/ct[t-40],r32mub252up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32252[:,t]=spline(T/ct[t-50],r32mub252down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32252[:,t]=spline(T/ct[t-60],r32mub252down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32252[:,t]=spline(T/ct[t-70],r32mub252down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32252[:,t]=spline(T/ct[t-80],r32mub252down3,xsame)
                            else:
                                r32252[:,t]=spline(T/ct[t-90],r32mub252down4,xsame)

for t in range(0,100):
    if t<10:
       r42252[:,t]=spline(T/ct[t],r42mub252up,xsame)
    else:
       if t>=10 and t<20:
          r42252[:,t]=spline(T/ct[t-10],r42mub252up1,xsame)
       else:
          if t>=20 and t<30:
             r42252[:,t]=spline(T/ct[t-20],r42mub252up2,xsame)
          else: 
             if t>=30 and t<40:
                r42252[:,t]=spline(T/ct[t-30],r42mub252up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42252[:,t]=spline(T/ct[t-40],r42mub252up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42252[:,t]=spline(T/ct[t-50],r42mub252down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42252[:,t]=spline(T/ct[t-60],r42mub252down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42252[:,t]=spline(T/ct[t-70],r42mub252down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42252[:,t]=spline(T/ct[t-80],r42mub252down3,xsame)
                            else:
                                r42252[:,t]=spline(T/ct[t-90],r42mub252down4,xsame)

for t in range(0,100):
    if t<10:
       r62252[:,t]=spline(T/ct[t],r62mub252up,xsame)
    else:
       if t>=10 and t<20:
          r62252[:,t]=spline(T/ct[t-10],r62mub252up1,xsame)
       else:
          if t>=20 and t<30:
             r62252[:,t]=spline(T/ct[t-20],r62mub252up2,xsame)
          else: 
             if t>=30 and t<40:
                r62252[:,t]=spline(T/ct[t-30],r62mub252up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62252[:,t]=spline(T/ct[t-40],r62mub252up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62252[:,t]=spline(T/ct[t-50],r62mub252down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62252[:,t]=spline(T/ct[t-60],r62mub252down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62252[:,t]=spline(T/ct[t-70],r62mub252down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62252[:,t]=spline(T/ct[t-80],r62mub252down3,xsame)
                            else:
                                r62252[:,t]=spline(T/ct[t-90],r62mub252down4,xsame)


for num in range(1,100):
    if num==1:
       max252=np.maximum(r32252[:,num-1],r32252[:,num])
       min252=np.minimum(r32252[:,num-1],r32252[:,num])
    else:
       max252=np.maximum(max252,r32252[:,num])
       min252=np.minimum(min252,r32252[:,num])

for num in range(1,100):
    if num==1:
       max42252=np.maximum(r42252[:,num-1],r42252[:,num])
       min42252=np.minimum(r42252[:,num-1],r42252[:,num])
    else:
       max42252=np.maximum(max42252,r42252[:,num])
       min42252=np.minimum(min42252,r42252[:,num])

for num in range(1,100):
    if num==1:
       max62252=np.maximum(r62252[:,num-1],r62252[:,num])
       min62252=np.minimum(r62252[:,num-1],r62252[:,num])
    else:
       max62252=np.maximum(max62252,r62252[:,num])
       min62252=np.minimum(min62252,r62252[:,num])

r32mub252cen=spline(T/ctcen,r32mub252cen,xsame)
r42mub252cen=spline(T/ctcen,r42mub252cen,xsame)
r62mub252cen=spline(T/ctcen,r62mub252cen,xsame)

dif252cen=abs(r32mub252cen-0.782208)
dif252up=abs(max252-0.782208)
dif252down=abs(min252-0.782208)
min252cen_index=np.argmin(dif252cen[80:300])+80
min252up_index=np.argmin(dif252up[80:300])+80
min252down_index=np.argmin(dif252down[80:300])+80
print(min252up_index)
print(min252down_index)
r42252cen=r42mub252cen[min252cen_index]
r62252cen=r62mub252cen[min252cen_index]
r42252hcen=r42mub252cen[min252cen_index+int(min252cen_index*deltat)]
r62252hcen=r62mub252cen[min252cen_index+int(min252cen_index*deltat)]
r42252lcen=r42mub252cen[min252cen_index-5]
r62252lcen=r62mub252cen[min252cen_index-5]
r42=[max42252[min252up_index],max42252[min252down_index],min42252[min252up_index],min42252[min252down_index]]
r42h=[max42252[min252up_index+int(min252up_index*deltat)],max42252[min252down_index+int(min252down_index*deltat)],min42252[min252up_index+int(min252up_index*deltat)],min42252[min252down_index+int(min252down_index*deltat)]]
r42l=[max42252[min252up_index-5],max42252[min252down_index-5],min42252[min252up_index-5],min42252[min252down_index-5]]
r42252up=np.max(r42)
r42252down=np.min(r42)
r42252uph=np.max(r42h)
r42252downh=np.min(r42h)
r42252upl=np.max(r42l)
r42252downl=np.min(r42l)
r62=[max62252[min252up_index],max62252[min252down_index],min62252[min252up_index],min62252[min252down_index]]
r62h=[max62252[min252up_index+int(min252up_index*deltat)],max62252[min252down_index+int(min252down_index*deltat)],min62252[min252up_index+int(min252up_index*deltat)],min62252[min252down_index+int(min252down_index*deltat)]]
r62l=[max62252[min252up_index-5],max62252[min252down_index-5],min62252[min252up_index-5],min62252[min252down_index-5]]
r62252up=np.max(r62)
r62252down=np.min(r62)
r62252uph=np.max(r62h)
r62252downh=np.min(r62h)
r62252upl=np.max(r62l)
r62252downl=np.min(r62l)
print(r62252up)
print(r62252down)
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

dif303cen=abs(r32mub303cen-0.783562)
dif303up=abs(max303-0.783562)
dif303down=abs(min303-0.783562)
min303cen_index=np.argmin(dif303cen[80:300])+80
min303up_index=np.argmin(dif303up[80:300])+80
min303down_index=np.argmin(dif303down[80:300])+80
print(min303up_index)
print(min303down_index)
r42303cen=r42mub303cen[min303cen_index]
r62303cen=r62mub303cen[min303cen_index]
r42303hcen=r42mub303cen[min303cen_index+int(min303cen_index*deltat)]
r62303hcen=r62mub303cen[min303cen_index+int(min303cen_index*deltat)]
r42303lcen=r42mub303cen[min303cen_index-5]
r62303lcen=r62mub303cen[min303cen_index-5]
r42=[max42303[min303up_index],max42303[min303down_index],min42303[min303up_index],min42303[min303down_index]]
r42h=[max42303[min303up_index+int(min303up_index*deltat)],max42303[min303down_index+int(min303down_index*deltat)],min42303[min303up_index+int(min303up_index*deltat)],min42303[min303down_index+int(min303down_index*deltat)]]
r42l=[max42303[min303up_index-5],max42303[min303down_index-5],min42303[min303up_index-5],min42303[min303down_index-5]]
r42303up=np.max(r42)
r42303down=np.min(r42)
r42303uph=np.max(r42h)
r42303downh=np.min(r42h)
r42303upl=np.max(r42l)
r42303downl=np.min(r42l)
r62=[max62303[min303up_index],max62303[min303down_index],min62303[min303up_index],min62303[min303down_index]]
r62h=[max62303[min303up_index+int(min303up_index*deltat)],max62303[min303down_index+int(min303down_index*deltat)],min62303[min303up_index+int(min303up_index*deltat)],min62303[min303down_index+int(min303down_index*deltat)]]
r62l=[max62303[min303up_index-5],max62303[min303down_index-5],min62303[min303up_index-5],min62303[min303down_index-5]]
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

dif406cen=abs(r32mub406cen-0.798587)
dif406up=abs(max406-0.798587)
dif406down=abs(min406-0.798587)
min406cen_index=np.argmin(dif406cen[80:300])+80
min406up_index=np.argmin(dif406up[80:300])+80
min406down_index=np.argmin(dif406down[80:300])+80
print(min406up_index)
print(min406down_index)
r42406cen=r42mub406cen[min406cen_index]
r62406cen=r62mub406cen[min406cen_index]
r42406hcen=r42mub406cen[min406cen_index+int(min406cen_index*deltat)]
r62406hcen=r62mub406cen[min406cen_index+int(min406cen_index*deltat)]
r42406lcen=r42mub406cen[min406cen_index-5]
r62406lcen=r62mub406cen[min406cen_index-5]
r42=[max42406[min406up_index],max42406[min406down_index],min42406[min406up_index],min42406[min406down_index]]
r42h=[max42406[min406up_index+int(min406up_index*deltat)],max42406[min406down_index+int(min406down_index*deltat)],min42406[min406up_index+int(min406up_index*deltat)],min42406[min406down_index+int(min406down_index*deltat)]]
r42l=[max42406[min406up_index-5],max42406[min406down_index-5],min42406[min406up_index-5],min42406[min406down_index-5]]
r42406up=np.max(r42)
r42406down=np.min(r42)
r42406uph=np.max(r42h)
r42406downh=np.min(r42h)
r42406upl=np.max(r42l)
r42406downl=np.min(r42l)
r62=[max62406[min406up_index],max62406[min406down_index],min62406[min406up_index],min62406[min406down_index]]
r62h=[max62406[min406up_index+int(min406up_index*deltat)],max62406[min406down_index+int(min406down_index*deltat)],min62406[min406up_index+int(min406up_index*deltat)],min62406[min406down_index+int(min406down_index*deltat)]]
r62l=[max62406[min406up_index-5],max62406[min406down_index-5],min62406[min406up_index-5],min62406[min406down_index-5]]
r62406up=np.max(r62)
r62406down=np.min(r62)
r62406uph=np.max(r62h)
r62406downh=np.min(r62h)
r62406upl=np.max(r62l)
r62406downl=np.min(r62l)
print(r62406cen)
print(r62406up)
print(r62406down)
#print(r62406uph)
#print(r62406downh)
####################################################################################################
r62cen=[r6222cen,r6268cen,r6278cen,r62106cen,r62148cen,r62196cen,r62252cen,r62303cen,r62406cen]
r62up=[r6222up,r6268up,r6278up,r62106up,r62148up,r62196up,r62252up,r62303up,r62406up]
r62down=[r6222down,r6268down,r6278down,r62106down,r62148down,r62196down,r62252down,r62303down,r62406down]
r42up=[r4222up,r4268up,r4278up,r42106up,r42148up,r42196up,r42252up,r42303up,r42406up]
r42down=[r4222down,r4268down,r4278down,r42106down,r42148down,r42196down,r42252down,r42303down,r42406down]
r42cen=[r4222cen,r4268cen,r4278cen,r42106cen,r42148cen,r42196cen,r42252cen,r42303cen,r42406cen]
r42lcen=[r4222lcen,r4268lcen,r4278lcen,r42106lcen,r42148lcen,r42196lcen,r42252lcen,r42303lcen,r42406lcen]
r42hcen=[r4222hcen,r4268hcen,r4278hcen,r42106hcen,r42148hcen,r42196hcen,r42252hcen,r42303hcen,r42406hcen]
r62lcen=[r6222lcen,r6268lcen,r6278lcen,r62106lcen,r62148lcen,r62196lcen,r62252lcen,r62303lcen,r62406lcen]
r62hcen=[r6222hcen,r6268hcen,r6278hcen,r62106hcen,r62148hcen,r62196hcen,r62252hcen,r62303hcen,r62406hcen]
r42hup=[r4222uph,r4268uph,r4278uph,r42106uph,r42148uph,r42196uph,r42252uph,r42303uph,r42406uph]
r42hdown=[r4222downh,r4268downh,r4278downh,r42106downh,r42148downh,r42196downh,r42252downh,r42303downh,r42406downh]
r62lup=[r6222upl,r6268upl,r6278upl,r62106upl,r62148upl,r62196upl,r62252upl,r62303upl,r62406upl]
r62ldown=[r6222downl,r6268downl,r6278downl,r62106downl,r62148downl,r62196downl,r62252downl,r62303downl,r62406downl]
r62hup=[r6222uph,r6268uph,r6278uph,r62106uph,r62148uph,r62196uph,r62252uph,r62303uph,r62406uph]
r62hdown=[r6222downh,r6268downh,r6278downh,r62106downh,r62148downh,r62196downh,r62252downh,r62303downh,r62406downh]
r42lup=[r4222upl,r4268upl,r4278upl,r42106upl,r42148upl,r42196upl,r42252upl,r42303upl,r42406upl]
r42ldown=[r4222downl,r4268downl,r4278downl,r42106downl,r42148downl,r42196downl,r42252downl,r42303downl,r42406downl]#r42和r62的上下限与中心值
r62errup=np.zeros(9)
r62errdown=np.zeros(9)
r42errup=np.zeros(9)
r42errdown=np.zeros(9)
r62errhup=np.zeros(9)
r62errhdown=np.zeros(9)
r42errhup=np.zeros(9)
r42errhdown=np.zeros(9)
r62errlup=np.zeros(9)
r62errldown=np.zeros(9)
r42errlup=np.zeros(9)
r42errldown=np.zeros(9)

for i in range(0,9):
    r62errup[i]=r62up[i]-r62cen[i]
    r62errdown[i]=r62cen[i]-r62down[i]
    r42errup[i]=r42up[i]-r42cen[i]
    r42errdown[i]=r42cen[i]-r42down[i]
    r62errhup[i]=r62hup[i]-r62hcen[i]
    r62errhdown[i]=r62hcen[i]-r62hdown[i]
    r42errhup[i]=r42hup[i]-r42hcen[i]
    r42errhdown[i]=r42hcen[i]-r42hdown[i]
    r62errlup[i]=r62lup[i]-r62lcen[i]
    r62errldown[i]=r62lcen[i]-r62ldown[i]
    r42errlup[i]=r42lup[i]-r42lcen[i]
    r42errldown[i]=r42lcen[i]-r42ldown[i]

print(r62errhup)
print(r62errhdown)
print(r62hcen)


for num in range(0,100):
    T22up[num]=min22up_index
    T22down[num]=min22down_index
    T68up[num]=min68up_index
    T68down[num]=min68down_index
    T78up[num]=min78up_index
    T78down[num]=min78down_index
    T106up[num]=min106up_index
    T106down[num]=min106down_index
    T148up[num]=min148up_index
    T148down[num]=min148down_index
    T196up[num]=min196up_index
    T196down[num]=min196down_index
    T252up[num]=min252up_index
    T252down[num]=min252down_index
    T303up[num]=min303up_index
    T303down[num]=min303down_index
    T406up[num]=min406up_index
    T406down[num]=min406down_index
####################################################################################################
# Create figure
fig=plt.figure(figsize=(12, 18.5))
#fig=plt.figure()
ax1=fig.add_subplot(631)
ax1.errorbar(energy,r62cen,yerr=[r62errdown,r62errup],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,zorder=1)
ax1.plot(energy,r62cen,color='blue',label=r'$T_f$')
ax1.errorbar(energy,r62hcen,yerr=[r62errhdown,r62errhup],color='green',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,zorder=2)
ax1.plot(energy,r62hcen,color='green',label=r'$T_f+10$')
y=range(-60,60,10)
ax1.set_xscale('log')
ax1.set_yscale('symlog')
#ax1.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
plt.axis([5,230,-60.,60.])
ax1.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
plt.yticks(y)
#ax1.set_xticks([200.,62.4,54.4,39.,27.,19.6,14.5,11.5,7.7])
ax1.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
ax1.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'])
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(7)
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
band_mub=ax7.fill_between(xsame,max252,min252,alpha=0.25,facecolor='b',edgecolor='',label=r'$14.5$')
line_mub,=ax7.plot(xsame,r32mub252cen,'b',linewidth=1,alpha=0.5)
ax7.plot(xsame,data14)
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
band_mub=ax8.fill_between(xsame,max303,min303,alpha=0.25,facecolor='b',edgecolor='',label=r'$11.5$')
line_mub,=ax8.plot(xsame,r32mub303cen,'b',linewidth=1,alpha=0.5)
ax8.plot(xsame,data11)
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
band_mub=ax9.fill_between(xsame,max406,min406,alpha=0.25,facecolor='b',edgecolor='',label=r'$7.7$')
line_mub,=ax9.plot(xsame,r32mub406cen,'b',linewidth=1,alpha=0.5)
ax9.plot(xsame,data7)
ax9.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,0,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax9.set_ylabel(r'$\chi^B_3/\chi^B_2$', fontsize=14, color='black')
for label in ax9.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax9.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax10=fig.add_subplot(6,3,10)
band_mub=ax10.fill_between(xsame,max6222,min6222,alpha=0.25,facecolor='b',edgecolor='',label=r'$200$')
line_mub,=ax10.plot(xsame,r62mub22cen,'b',linewidth=1,alpha=0.5)
ax10.plot(T22up,y62)
ax10.plot(T22down,y62)
#ax2.plot(energy,r62up)
#ax2.plot(energy,r62down)
#ax2.errorbar(energy,r62cen,yerr=r62err,color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)#,label=r'$$')
#ax2.plot(xsame,data)
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
band_mub=ax11.fill_between(xsame,max6268,min6268,alpha=0.25,facecolor='b',edgecolor='',label=r'$62.4$')
line_mub,=ax11.plot(xsame,r62mub68cen,'b',linewidth=1,alpha=0.5)
ax11.plot(T68up,y62)
ax11.plot(T68down,y62)
ax11.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-0.5,1.2])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax11.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax11.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax11.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax12=fig.add_subplot(6,3,12)
band_mub=ax12.fill_between(xsame,max62106,min62106,alpha=0.25,facecolor='b',edgecolor='',label=r'$39$')
line_mub,=ax12.plot(xsame,r62mub106cen,'b',linewidth=1,alpha=0.5)
ax12.plot(T106up,y62)
ax12.plot(T106down,y62)
ax12.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-1,1.4])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax12.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax12.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax12.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax13=fig.add_subplot(6,3,13)
band_mub=ax13.fill_between(xsame,max62148,min62148,alpha=0.25,facecolor='b',edgecolor='',label=r'$27$')
line_mub,=ax13.plot(xsame,r62mub148cen,'b',linewidth=1,alpha=0.5)
ax13.plot(T148up,y62)
ax13.plot(T148down,y62)
ax13.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-1,1.5])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax13.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax13.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax13.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax14=fig.add_subplot(6,3,14)
band_mub=ax14.fill_between(xsame,max62196,min62196,alpha=0.25,facecolor='b',edgecolor='',label=r'$19.6$')
line_mub,=ax14.plot(xsame,r62mub196cen,'b',linewidth=1,alpha=0.5)
ax14.plot(T196up,y62)
ax14.plot(T196down,y62)
ax14.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-2.2,1.7])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax14.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax14.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax14.yaxis.get_ticklabels():
    label.set_fontsize(10)


ax15=fig.add_subplot(6,3,15)
band_mub=ax15.fill_between(xsame,max62252,min62252,alpha=0.25,facecolor='b',edgecolor='',label=r'$14.5$')
line_mub,=ax15.plot(xsame,r62mub252cen,'b',linewidth=1,alpha=0.5)
ax15.plot(T252up,y62)
ax15.plot(T252down,y62)
ax15.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-10,5])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax15.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax15.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax15.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax16=fig.add_subplot(6,3,16)
band_mub=ax16.fill_between(xsame,max62303,min62303,alpha=0.25,facecolor='b',edgecolor='',label=r'$11.5$')
line_mub,=ax16.plot(xsame,r62mub303cen,'b',linewidth=1,alpha=0.5)
ax16.plot(T303up,y62)
ax16.plot(T303down,y62)
ax16.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-10,5])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax16.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax16.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax16.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax17=fig.add_subplot(6,3,17)
band_mub=ax17.fill_between(xsame,max62406,min62406,alpha=0.25,facecolor='b',edgecolor='',label=r'$7.7$')
line_mub,=ax17.plot(xsame,r62mub406cen,'b',linewidth=1,alpha=0.5)
ax17.plot(T406up,y62)
ax17.plot(T406down,y62)
ax17.legend(loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax2.set_xscale('log')
plt.axis([80,230,-60,50])
#ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax17.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
for label in ax17.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax17.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax18=fig.add_subplot(6,3,18)
ax18.errorbar(energy,r42cen,yerr=[r42errdown,r42errup],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax18.errorbar(energy,r42cen,color='blue')
ax18.errorbar(energy,r42hcen,yerr=[r42errhdown,r42errhup],color='green',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax18.errorbar(energy,r42hcen,color='green')

ax18.set_xscale('log')
plt.axis([5,230,-2.,2.])
ax18.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax18.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')
for label in ax18.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax18.yaxis.get_ticklabels():
    label.set_fontsize(10)


fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("R32toR62.pdf")

energyrhic=[200.,54.4]
value62=[-2.54509,1.20229]
erro62=[1.01682,0.480246]
# Create figure
fig=plt.figure(figsize=(9., 3.5))
#fig=plt.figure()
ax2=fig.add_subplot(122)
point62cen=ax2.errorbar(energy,r62cen,yerr=[r62errdown,r62errup],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,zorder=1)
line62cen,=ax2.plot(energy,r62cen,color='blue',label=r'$T_f$')
point62h=ax2.errorbar(energy,r62hcen,yerr=[r62errhdown,r62errhup],color='green',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,zorder=2)
line62h,=ax2.plot(energy,r62hcen,color='green',label=r'$T_f+10$')
exp=ax2.errorbar(energyrhic,value62,yerr=erro62,color='red',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1,zorder=2)
ax2.legend(((point62cen,line62cen),(point62h,line62h),exp),(r'This work at $T_f$',r'This work at $1.05T_f$',r'RHIC data'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
plt.axis([5.,230.,-60.,60.])
ax2.set_xscale('symlog')
ax2.set_yscale('symlog')
#plt.xticks([])
ax2.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
ax2.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
plt.yticks([-50,-40,-30,-20,-10,-1,0,1,10,20,30,40,50])
ax2.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(7)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(7)
#fig.subplots_adjust(top=0.95, bottom=0.2, left=0.16, right=0.95, hspace=0.35,wspace=0.35)
#fig.savefig("R62.pdf")


# Create figure
#fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(121)
ax1.errorbar(energy,r42cen,yerr=[r42errdown,r42errup],color='blue',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax1.errorbar(energy,r42cen,color='blue')
ax1.errorbar(energy,r42hcen,yerr=[r42errhdown,r42errhup],color='green',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
ax1.errorbar(energy,r42hcen,color='green')
ax1.errorbar(energy,kurtosis[:,0],yerr=kurtosis[:,1],color='red',marker='o',linestyle='',linewidth=2,markersize=5,fillstyle='none',alpha=1)
#ax1.errorbar(energy,kurtosis[:,0],color='red')
ax1.set_xscale('symlog')
plt.axis([5,230,-2.,2.])
ax1.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
ax1.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
ax1.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(7)

fig.subplots_adjust(top=0.95, bottom=0.2, left=0.1, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("R4262.pdf")


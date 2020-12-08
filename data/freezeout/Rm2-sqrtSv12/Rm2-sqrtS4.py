#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl
from scipy.interpolate import spline
from scipy import interpolate
import pylab as pl




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
y62=np.linspace(-5000,5000,100)
T22up=np.zeros(100)
T22down=np.zeros(100)
T68up=np.zeros(100)
T68down=np.zeros(100)
T78up=np.zeros(100)
T78down=np.zeros(100)
T106up=np.zeros(100)
T106down=np.zeros(100)
T120up=np.zeros(100)
T120down=np.zeros(100)
T135up=np.zeros(100)
T135down=np.zeros(100)
T148up=np.zeros(100)
T148down=np.zeros(100)
T165up=np.zeros(100)
T165down=np.zeros(100)
T180up=np.zeros(100)
T180down=np.zeros(100)
T196up=np.zeros(100)
T196down=np.zeros(100)
T215up=np.zeros(100)
T215down=np.zeros(100)
T230up=np.zeros(100)
T230down=np.zeros(100)
T252up=np.zeros(100)
T252down=np.zeros(100)
T265up=np.zeros(100)
T265down=np.zeros(100)
T280up=np.zeros(100)
T280down=np.zeros(100)
T303up=np.zeros(100)
T303down=np.zeros(100)
T310up=np.zeros(100)
T310down=np.zeros(100)
T320up=np.zeros(100)
T320down=np.zeros(100)
T330up=np.zeros(100)
T330down=np.zeros(100)
T340up=np.zeros(100)
T340down=np.zeros(100)
T350up=np.zeros(100)
T350down=np.zeros(100)
T360up=np.zeros(100)
T360down=np.zeros(100)
T370up=np.zeros(100)
T370down=np.zeros(100)
T380up=np.zeros(100)
T380down=np.zeros(100)
T390up=np.zeros(100)
T390down=np.zeros(100)
T406up=np.zeros(100)
T406down=np.zeros(100)

Tf22=np.zeros(100)
Tf68=np.zeros(100)
Tf78=np.zeros(100)
Tf106=np.zeros(100)
Tf148=np.zeros(100)
Tf196=np.zeros(100)
Tf252=np.zeros(100)
Tf303=np.zeros(100)
Tf406=np.zeros(100)
for num in range(0,300):
    data200[num]=0.900669
    data62[num]=0.792955	
    data54[num]=0.632837
    data39[num]=0.739693	
    data27[num]=0.196254	
    data19[num]=0.140553
    data14[num]=1.468760
    data11[num]=0.695796
    data7[num]=	1.766972

for num in range(0,100):
    Tf22[num]=158.
    Tf68[num]=158.
    Tf78[num]=158.
    Tf106[num]=158.
    Tf148[num]=157.
    Tf196[num]=156.
    Tf252[num]=153.
    Tf303[num]=150.
    Tf406[num]=138.




fit7=np.loadtxt(r'./fitSTAR/sevenpointfit.dat')
#print(fit7)
fit4=np.loadtxt(r'./fitSTAR/fourpointfit.dat')
energy=[200.,62.4,54.4,39.,34.2,30.0,27.,23.8,21.5,19.6,17.4,16.0,14.5,13.4,12.4,11.5,10.9,10.4,10.0,9.6,9.2,8.9,8.5,8.2,7.9,7.7]
energyexp=[200.,62.4,54.4,39.,27.,19.6,14.5,11.5,7.7]

#############################################################################################################################################
xsame=np.linspace(1.,300.,2991)
deltat=0.05
ctcen=1.247
ctup=1.259
ctdown=1.235
cmu=1.110
c=ctcen/cmu

Tcup=[int(205/ctdown)-1,int(205/ctdown)-1,int(205/ctdown)-1,int(204/ctdown)-1,int(203/ctdown)-1,int(201/ctdown)-1,int(198/ctdown)-1,int(194/ctdown)-1,int(182/ctdown)-1]
Tcdown=[int(205/ctup)-1,int(205/ctup)-1,int(205/ctup)-1,int(204/ctup)-1,int(203/ctup)-1,int(201/ctup)-1,int(198/ctup)-1,int(194/ctup)-1,int(182/ctup)-1]
Tcen=[int(205/ctcen)-1,int(205/ctcen)-1,int(205/ctcen)-1,int(204/ctcen)-1,int(203/ctcen)-1,int(201/ctcen)-1,int(198/ctcen)-1,int(194/ctcen)-1,int(182/ctcen)-1]
#Tcup=[int(191/ctdown),int(190/ctdown),int(190/ctdown),int(189/ctdown),int(187/ctdown),int(185/ctdown),int(180/ctdown),int(174/ctdown),int(159/ctdown)]
#Tcdown=[int(191/ctup),int(190/ctup),int(190/ctup),int(189/ctup),int(187/ctup),int(185/ctup),int(180/ctup),int(174/ctup),int(159/ctup)]
#Tcen=[int(191/ctcen),int(190/ctcen),int(190/ctcen),int(189/ctcen),int(187/ctcen),int(185/ctcen),int(180/ctcen),int(174/ctcen),int(159/ctcen)]

#print(xsame)
#print(Tcup)
#print(T)

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
r3222=np.zeros((2991,20))
r4222=np.zeros((2991,20))
r6222=np.zeros((2991,20))
r8222=np.zeros((2991,20))
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

for t in range(0,20):
    if t<10:
       r8222[:,t]=spline(T/ct[t],r82mub22up,xsame)
    else:
       r8222[:,t]=spline(T/ct[t-10],r82mub22down,xsame)

for num in range(1,20):
    if num==1:
       max8222=np.maximum(r8222[:,num-1],r8222[:,num])
       min8222=np.minimum(r8222[:,num-1],r8222[:,num])
    else:
       max8222=np.maximum(max8222,r8222[:,num])
       min8222=np.minimum(min8222,r8222[:,num])

r32mub22cen=spline(T/ctcen,r32mub22cen,xsame)*c
max22=max22*c
min22=min22*c
r42mub22cen=spline(T/ctcen,r42mub22cen,xsame)
r62mub22cen=spline(T/ctcen,r62mub22cen,xsame)
r82mub22cen=spline(T/ctcen,r82mub22cen,xsame)
#print(r42mub22cen)

dif6222minc=np.zeros(2991)
dif6222minu=np.zeros(2991)
dif6222mind=np.zeros(2991)
dif6222minc=abs(r62mub22cen+0.5)
dif6222minu=abs(max6222+0.5)
dif6222mind=abs(min6222+0.5)
min6222cindex=np.argmin(dif6222minc[80:2991])+80
min6222uindex=np.argmin(dif6222minu[80:2991])+80
min6222dindex=np.argmin(dif6222mind[80:2991])+80
r62minc=r62mub22cen[min6222cindex]
r62minu=max6222[min6222uindex]
r62mind=min6222[min6222dindex]
erru=r62minu-r62minc
errd=r62minc-r62mind
print(r62minc)
print(erru)
print(errd)



dif22cen=abs(r42mub22cen-0.900669)
dif22up=abs(max4222-0.900669)
dif22down=abs(min4222-0.900669)
#min22cen_index=int(round(fit7[0,2]))
#min22up_index=int(round(fit7[0,1]))
#min22down_index=int(round(fit7[0,0]))
min22cen_index=1605
min22up_index=1605
min22down_index=1605

print(min22cen_index)
#print(min22up_index)
#print(min22down_index)
r3222cen=r32mub22cen[min22cen_index]
r4222cen=r42mub22cen[min22cen_index]
r6222cen=r62mub22cen[min22cen_index]
r8222cen=r82mub22cen[min22cen_index]
#r3222hcen=r32mub22cen[min22cen_index+int(min22cen_index*deltat)]
#r4222hcen=r42mub22cen[min22cen_index+int(min22cen_index*deltat)]
#r6222hcen=r62mub22cen[min22cen_index+int(min22cen_index*deltat)]
#r8222hcen=r82mub22cen[min22cen_index+int(min22cen_index*deltat)]
r3222hcen=r32mub22cen[Tcen[0]]
r4222hcen=r42mub22cen[Tcen[0]]
r6222hcen=r62mub22cen[Tcen[0]]
r8222hcen=r82mub22cen[Tcen[0]]


r32=[max22[min22up_index],max22[min22down_index],min22[min22up_index],min22[min22down_index]]
#r32h=[max22[min22up_index+int(min22up_index*deltat)],max22[min22down_index+int(min22down_index*deltat)],min22[min22up_index+int(min22up_index*deltat)],min22[min22down_index+int(min22down_index*deltat)]]
r32h=[max22[Tcup[0]],max22[Tcdown[0]],min22[Tcup[0]],min22[Tcdown[0]]]
r3222up=np.max(r32)
r3222down=np.min(r32)
r3222uph=np.max(r32h)
r3222downh=np.min(r32h)

r42=[max4222[min22up_index],max4222[min22down_index],min4222[min22up_index],min4222[min22down_index]]
#r42h=[max4222[min22up_index+int(min22up_index*deltat)],max4222[min22down_index+int(min22down_index*deltat)],min4222[min22up_index+int(min22up_index*deltat)],min4222[min22down_index+int(min22down_index*deltat)]]
r42h=[max4222[Tcup[0]],max4222[Tcdown[0]],min4222[Tcup[0]],min4222[Tcdown[0]]]
r4222up=np.max(r42)
r4222down=np.min(r42)
r4222uph=np.max(r42h)
r4222downh=np.min(r42h)


r62=[max6222[min22up_index],max6222[min22down_index],min6222[min22up_index],min6222[min22down_index]]
#r62h=[max6222[min22up_index+int(min22up_index*deltat)],max6222[min22down_index+int(min22down_index*deltat)],min6222[min22up_index+int(min22up_index*deltat)],min6222[min22down_index+int(min22down_index*deltat)]]
r62h=[max6222[Tcup[0]],max6222[Tcdown[0]],min6222[Tcup[0]],min6222[Tcdown[0]]]
r6222up=np.max(r62)
r6222down=np.min(r62)
r6222uph=np.max(r62h)
r6222downh=np.min(r62h)


r82=[max8222[min22up_index],max8222[min22down_index],min8222[min22up_index],min8222[min22down_index]]
#r82h=[max8222[min22up_index+int(min22up_index*deltat)],max8222[min22down_index+int(min22down_index*deltat)],min8222[min22up_index+int(min22up_index*deltat)],min8222[min22down_index+int(min22down_index*deltat)]]
r82h=[max8222[Tcup[0]],max8222[Tcdown[0]],min8222[Tcup[0]],min8222[Tcdown[0]]]
r8222up=np.max(r82)
r8222down=np.min(r82)
r8222uph=np.max(r82h)
r8222downh=np.min(r82h)


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
r3268=np.zeros((2991,20))
r4268=np.zeros((2991,20))
r6268=np.zeros((2991,20))
r8268=np.zeros((2991,20))
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

for t in range(0,20):
    if t<10:
       r8268[:,t]=spline(T/ct[t],r82mub68up,xsame)
    else:
       r8268[:,t]=spline(T/ct[t-10],r82mub68down,xsame)


for num in range(1,20):
    if num==1:
       max8268=np.maximum(r8268[:,num-1],r8268[:,num])
       min8268=np.minimum(r8268[:,num-1],r8268[:,num])
    else:
       max8268=np.maximum(max8268,r8268[:,num])
       min8268=np.minimum(min8268,r8268[:,num])

r32mub68cen=spline(T/ctcen,r32mub68cen,xsame)*c
max68=max68*c
min68=min68*c
r42mub68cen=spline(T/ctcen,r42mub68cen,xsame)
r62mub68cen=spline(T/ctcen,r62mub68cen,xsame)
r82mub68cen=spline(T/ctcen,r82mub68cen,xsame)

dif68cen=abs(r42mub68cen-0.792955)
dif68up=abs(max4268-0.792955)
dif68down=abs(min4268-0.792955)
#min68cen_index=int(round(fit7[1,2]))
#min68up_index=int(round(fit7[1,1]))
#min68down_index=int(round(fit7[1,0]))
min68cen_index=1601
min68up_index=1601
min68down_index=1601
print(min68cen_index)
#print(min68up_index)
#print(min68down_index)
r3268cen=r32mub68cen[min68cen_index]
#r3268hcen=r32mub68cen[min68cen_index+int(min68cen_index*deltat)]
r3268hcen=r32mub68cen[Tcen[1]]
r32=[max68[min68up_index],max68[min68down_index],min68[min68up_index],min68[min68down_index]]
#r32h=[max68[min68up_index+int(min68up_index*deltat)],max68[min68down_index+int(min68down_index*deltat)],min68[min68up_index+int(min68up_index*deltat)],min68[min68down_index+int(min68down_index*deltat)]]
r32h=[max68[Tcup[1]],max68[Tcdown[1]],min68[Tcup[1]],min68[Tcdown[1]]]
r3268up=np.max(r32)
r3268down=np.min(r32)
r3268uph=np.max(r32h)
r3268downh=np.min(r32h)

r4268cen=r42mub68cen[min68cen_index]
r6268cen=r62mub68cen[min68cen_index]
#r4268hcen=r42mub68cen[min68cen_index+int(min68cen_index*deltat)]
#r6268hcen=r62mub68cen[min68cen_index+int(min68cen_index*deltat)]
r4268hcen=r42mub68cen[Tcen[1]]
r6268hcen=r62mub68cen[Tcen[1]]
r42=[max4268[min68up_index],max4268[min68down_index],min4268[min68up_index],min4268[min68down_index]]
#r42h=[max4268[min68up_index+int(min68up_index*deltat)],max4268[min68down_index+int(min68down_index*deltat)],min4268[min68up_index+int(min68up_index*deltat)],min4268[min68down_index+int(min68down_index*deltat)]]
r42h=[max4268[Tcup[1]],max4268[Tcdown[1]],min4268[Tcup[1]],min4268[Tcdown[1]]]
r4268up=np.max(r42)
r4268down=np.min(r42)
r4268uph=np.max(r42h)
r4268downh=np.min(r42h)

r62=[max6268[min68up_index],max6268[min68down_index],min6268[min68up_index],min6268[min68down_index]]
#r62h=[max6268[min68up_index+int(min68up_index*deltat)],max6268[min68down_index+int(min68down_index*deltat)],min6268[min68up_index+int(min68up_index*deltat)],min6268[min68down_index+int(min68down_index*deltat)]]
r62h=[max6268[Tcup[1]],max6268[Tcdown[1]],min6268[Tcup[1]],min6268[Tcdown[1]]]
r6268up=np.max(r62)
r6268down=np.min(r62)
r6268uph=np.max(r62h)
r6268downh=np.min(r62h)

r8268cen=r82mub68cen[min68cen_index]
#r8268hcen=r82mub68cen[min68cen_index+int(min68cen_index*deltat)]
r8268hcen=r82mub68cen[Tcen[1]]
r82=[max8268[min68up_index],max8268[min68down_index],min8268[min68up_index],min8268[min68down_index]]
#r82h=[max8268[min68up_index+int(min68up_index*deltat)],max8268[min68down_index+int(min68down_index*deltat)],min8268[min68up_index+int(min68up_index*deltat)],min8268[min68down_index+int(min68down_index*deltat)]]
r82h=[max8268[Tcup[1]],max8268[Tcdown[1]],min8268[Tcup[1]],min8268[Tcdown[1]]]
r8268up=np.max(r82)
r8268down=np.min(r82)
r8268uph=np.max(r82h)
r8268downh=np.min(r82h)

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
r3278=np.zeros((2991,20))
r4278=np.zeros((2991,20))
r6278=np.zeros((2991,20))
r8278=np.zeros((2991,20))
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

for t in range(0,20):
    if t<10:
       r8278[:,t]=spline(T/ct[t],r82mub78up,xsame)
    else:
       r8278[:,t]=spline(T/ct[t-10],r82mub78down,xsame)


for num in range(1,20):
    if num==1:
       max8278=np.maximum(r8278[:,num-1],r8278[:,num])
       min8278=np.minimum(r8278[:,num-1],r8278[:,num])
    else:
       max8278=np.maximum(max8278,r8278[:,num])
       min8278=np.minimum(min8278,r8278[:,num])

r32mub78cen=spline(T/ctcen,r32mub78cen,xsame)*c
max78=max78*c
min78=min78*c
r42mub78cen=spline(T/ctcen,r42mub78cen,xsame)
r62mub78cen=spline(T/ctcen,r62mub78cen,xsame)
r82mub78cen=spline(T/ctcen,r82mub78cen,xsame)

dif78cen=abs(r42mub78cen-0.632837)
dif78up=abs(max4278-0.632837)
dif78down=abs(min4278-0.632837)
min78cen_index=1600
min78up_index=1600
min78down_index=1600
print(min78cen_index)
#print(min78up_index)
#print(min78down_index)
r3278cen=r32mub78cen[min78cen_index]
#r3278hcen=r32mub78cen[min78cen_index+int(min78cen_index*deltat)]
r3278hcen=r32mub78cen[Tcen[2]]
r32=[max78[min78up_index],max78[min78down_index],min78[min78up_index],min78[min78down_index]]
#r32h=[max78[min78up_index+int(min78up_index*deltat)],max78[min78down_index+int(min78down_index*deltat)],min78[min78up_index+int(min78up_index*deltat)],min78[min78down_index+int(min78down_index*deltat)]]
r32h=[max78[Tcup[2]],max78[Tcdown[2]],min78[Tcup[2]],min78[Tcdown[2]]]
r3278up=np.max(r32)
r3278down=np.min(r32)
r3278uph=np.max(r32h)
r3278downh=np.min(r32h)

r4278cen=r42mub78cen[min78cen_index]
r6278cen=r62mub78cen[min78cen_index]
#r4278hcen=r42mub78cen[min78cen_index+int(min78cen_index*deltat)]
#r6278hcen=r62mub78cen[min78cen_index+int(min78cen_index*deltat)]
r4278hcen=r42mub78cen[Tcen[2]]
r6278hcen=r62mub78cen[Tcen[2]]
r42=[max4278[min78up_index],max4278[min78down_index],min4278[min78up_index],min4278[min78down_index]]
#r42h=[max4278[min78up_index+int(min78up_index*deltat)],max4278[min78down_index+int(min78down_index*deltat)],min4278[min78up_index+int(min78up_index*deltat)],min4278[min78down_index+int(min78down_index*deltat)]]
r42h=[max4278[Tcup[2]],max4278[Tcdown[2]],min4278[Tcup[2]],min4278[Tcdown[2]]]
r4278up=np.max(r42)
r4278down=np.min(r42)
r4278uph=np.max(r42h)
r4278downh=np.min(r42h)


r6278cen=r62mub78cen[min78cen_index]
#r6278hcen=r62mub78cen[min78cen_index+int(min78cen_index*deltat)]
r6278hcen=r62mub78cen[Tcen[2]]
r62=[max6278[min78up_index],max6278[min78down_index],min6278[min78up_index],min6278[min78down_index]]
#r62h=[max6278[min78up_index+int(min78up_index*deltat)],max6278[min78down_index+int(min78down_index*deltat)],min6278[min78up_index+int(min78up_index*deltat)],min6278[min78down_index+int(min78down_index*deltat)]]
r62h=[max6278[Tcup[2]],max6278[Tcdown[2]],min6278[Tcup[2]],min6278[Tcdown[2]]]
r6278up=np.max(r62)
r6278down=np.min(r62)
r6278uph=np.max(r62h)
r6278downh=np.min(r62h)

r8278cen=r82mub78cen[min78cen_index]
#r8278hcen=r82mub78cen[min78cen_index+int(min78cen_index*deltat)]
r8278hcen=r82mub78cen[Tcen[2]]
r82=[max8278[min78up_index],max8278[min78down_index],min8278[min78up_index],min8278[min78down_index]]
#r82h=[max8278[min78up_index+int(min78up_index*deltat)],max8278[min78down_index+int(min78down_index*deltat)],min8278[min78up_index+int(min78up_index*deltat)],min8278[min78down_index+int(min78down_index*deltat)]]
r82h=[max8278[Tcup[2]],max8278[Tcdown[2]],min8278[Tcup[2]],min8278[Tcdown[2]]]
r8278up=np.max(r82)
r8278down=np.min(r82)
r8278uph=np.max(r82h)
r8278downh=np.min(r82h)

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
r32106=np.zeros((2991,20))
r42106=np.zeros((2991,20))
r62106=np.zeros((2991,20))
r82106=np.zeros((2991,20))
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

for t in range(0,20):
    if t<10:
       r82106[:,t]=spline(T/ct[t],r82mub106up,xsame)
    else:
       r82106[:,t]=spline(T/ct[t-10],r82mub106down,xsame)


for num in range(1,20):
    if num==1:
       max82106=np.maximum(r82106[:,num-1],r82106[:,num])
       min82106=np.minimum(r82106[:,num-1],r82106[:,num])
    else:
       max82106=np.maximum(max82106,r82106[:,num])
       min82106=np.minimum(min82106,r82106[:,num])

r32mub106cen=spline(T/ctcen,r32mub106cen,xsame)*c
max106=max106*c
min106=min106*c
r42mub106cen=spline(T/ctcen,r42mub106cen,xsame)
r62mub106cen=spline(T/ctcen,r62mub106cen,xsame)
r82mub106cen=spline(T/ctcen,r82mub106cen,xsame)

dif106cen=abs(r42mub106cen-0.739693)
dif106up=abs(max42106-0.739693)
dif106down=abs(min42106-0.739693)
min106cen_index=1595
min106up_index=1595
min106down_index=1595
print(min106cen_index)
#print(min106up_index)
#print(min106down_index)
r32106cen=r32mub106cen[min106cen_index]
#r32106hcen=r32mub106cen[min106cen_index+int(min106cen_index*deltat)]
r32106hcen=r32mub106cen[Tcen[3]]
r32=[max106[min106up_index],max106[min106down_index],min106[min106up_index],min106[min106down_index]]
#r32h=[max106[min106up_index+int(min106up_index*deltat)],max106[min106down_index+int(min106down_index*deltat)],min106[min106up_index+int(min106up_index*deltat)],min106[min106down_index+int(min106down_index*deltat)]]
r32h=[max106[Tcup[3]],max106[Tcdown[3]],min106[Tcup[3]],min106[Tcdown[3]]]
r32106up=np.max(r32)
r32106down=np.min(r32)
r32106uph=np.max(r32h)
r32106downh=np.min(r32h)

r42106cen=r42mub106cen[min106cen_index]
r62106cen=r62mub106cen[min106cen_index]
#r42106hcen=r42mub106cen[min106cen_index+int(min106cen_index*deltat)]
#r62106hcen=r62mub106cen[min106cen_index+int(min106cen_index*deltat)]
r42106hcen=r42mub106cen[Tcen[3]]
r62106hcen=r62mub106cen[Tcen[3]]
r42=[max42106[min106up_index],max42106[min106down_index],min42106[min106up_index],min42106[min106down_index]]
#r42h=[max42106[min106up_index+int(min106up_index*deltat)],max42106[min106down_index+int(min106down_index*deltat)],min42106[min106up_index+int(min106up_index*deltat)],min42106[min106down_index+int(min106down_index*deltat)]]
r42h=[max42106[Tcup[3]],max42106[Tcdown[3]],min42106[Tcup[3]],min42106[Tcdown[3]]]
r42106up=np.max(r42)
r42106down=np.min(r42)
r42106uph=np.max(r42h)
r42106downh=np.min(r42h)

r62=[max62106[min106up_index],max62106[min106down_index],min62106[min106up_index],min62106[min106down_index]]
#r62h=[max62106[min106up_index+int(min106up_index*deltat)],max62106[min106down_index+int(min106down_index*deltat)],min62106[min106up_index+int(min106up_index*deltat)],min62106[min106down_index+int(min106down_index*deltat)]]
r62h=[max62106[Tcup[3]],max62106[Tcdown[3]],min62106[Tcup[3]],min62106[Tcdown[3]]]
r62106up=np.max(r62)
r62106down=np.min(r62)
r62106uph=np.max(r62h)
r62106downh=np.min(r62h)

r82106cen=r82mub106cen[min106cen_index]
#r82106hcen=r82mub106cen[min106cen_index+int(min106cen_index*deltat)]
r82106hcen=r82mub106cen[Tcen[3]]
r82=[max82106[min106up_index],max82106[min106down_index],min82106[min106up_index],min82106[min106down_index]]
#r82h=[max82106[min106up_index+int(min106up_index*deltat)],max82106[min106down_index+int(min106down_index*deltat)],min82106[min106up_index+int(min106up_index*deltat)],min82106[min106down_index+int(min106down_index*deltat)]]
r82h=[max82106[Tcup[3]],max82106[Tcdown[3]],min82106[Tcup[3]],min82106[Tcdown[3]]]
r82106up=np.max(r82)
r82106down=np.min(r82)
r82106uph=np.max(r82h)
r82106downh=np.min(r82h)
####################################################################################################
chi2mub120cen=np.loadtxt(r'./addition/mub120/cmucen/final/buffer/chi2.dat')
chi3mub120cen=np.loadtxt(r'./addition/mub120/cmucen/final/buffer/chi3.dat')
chi4mub120cen=np.loadtxt(r'./addition/mub120/cmucen/final/buffer/chi4.dat')
chi6mub120cen=np.loadtxt(r'./addition/mub120/cmucen/final/buffer/chi6.dat')
chi8mub120cen=np.loadtxt(r'./addition/mub120/cmucen/final/buffer/chi8.dat')
r32mub120cen=chi3mub120cen/chi2mub120cen
r42mub120cen=chi4mub120cen/chi2mub120cen
r62mub120cen=chi6mub120cen/chi2mub120cen
r82mub120cen=chi8mub120cen/chi2mub120cen
chi2mub120up=np.loadtxt(r'./addition/mub120/cmuup/final/buffer/chi2.dat')
chi3mub120up=np.loadtxt(r'./addition/mub120/cmuup/final/buffer/chi3.dat')
chi4mub120up=np.loadtxt(r'./addition/mub120/cmuup/final/buffer/chi4.dat')
chi6mub120up=np.loadtxt(r'./addition/mub120/cmuup/final/buffer/chi6.dat')
chi8mub120up=np.loadtxt(r'./addition/mub120/cmuup/final/buffer/chi8.dat')
r32mub120up=chi3mub120up/chi2mub120up
r42mub120up=chi4mub120up/chi2mub120up
r62mub120up=chi6mub120up/chi2mub120up
r82mub120up=chi8mub120up/chi2mub120up
chi2mub120down=np.loadtxt(r'./addition/mub120/cmudown/final/buffer/chi2.dat')
chi3mub120down=np.loadtxt(r'./addition/mub120/cmudown/final/buffer/chi3.dat')
chi4mub120down=np.loadtxt(r'./addition/mub120/cmudown/final/buffer/chi4.dat')
chi6mub120down=np.loadtxt(r'./addition/mub120/cmudown/final/buffer/chi6.dat')
chi8mub120down=np.loadtxt(r'./addition/mub120/cmudown/final/buffer/chi8.dat')
r32mub120down=chi3mub120down/chi2mub120down
r42mub120down=chi4mub120down/chi2mub120down
r62mub120down=chi6mub120down/chi2mub120down
r82mub120down=chi8mub120down/chi2mub120down
r32120=np.zeros((2991,20))
r42120=np.zeros((2991,20))
r62120=np.zeros((2991,20))
r82120=np.zeros((2991,20))
for t in range(0,20):
    if t<10:
       r32120[:,t]=spline(T/ct[t],r32mub120up,xsame)
    else:
       r32120[:,t]=spline(T/ct[t-10],r32mub120down,xsame)


for num in range(1,20):
    if num==1:
       max120=np.maximum(r32120[:,num-1],r32120[:,num])
       min120=np.minimum(r32120[:,num-1],r32120[:,num])
    else:
       max120=np.maximum(max120,r32120[:,num])
       min120=np.minimum(min120,r32120[:,num])

for t in range(0,20):
    if t<10:
       r42120[:,t]=spline(T/ct[t],r42mub120up,xsame)
    else:
       r42120[:,t]=spline(T/ct[t-10],r42mub120down,xsame)


for num in range(1,20):
    if num==1:
       max42120=np.maximum(r42120[:,num-1],r42120[:,num])
       min42120=np.minimum(r42120[:,num-1],r42120[:,num])
    else:
       max42120=np.maximum(max42120,r42120[:,num])
       min42120=np.minimum(min42120,r42120[:,num])

for t in range(0,20):
    if t<10:
       r62120[:,t]=spline(T/ct[t],r62mub120up,xsame)
    else:
       r62120[:,t]=spline(T/ct[t-10],r62mub120down,xsame)


for num in range(1,20):
    if num==1:
       max62120=np.maximum(r62120[:,num-1],r62120[:,num])
       min62120=np.minimum(r62120[:,num-1],r62120[:,num])
    else:
       max62120=np.maximum(max62120,r62120[:,num])
       min62120=np.minimum(min62120,r62120[:,num])

for t in range(0,20):
    if t<10:
       r82120[:,t]=spline(T/ct[t],r82mub120up,xsame)
    else:
       r82120[:,t]=spline(T/ct[t-10],r82mub120down,xsame)


for num in range(1,20):
    if num==1:
       max82120=np.maximum(r82120[:,num-1],r82120[:,num])
       min82120=np.minimum(r82120[:,num-1],r82120[:,num])
    else:
       max82120=np.maximum(max82120,r82120[:,num])
       min82120=np.minimum(min82120,r82120[:,num])

r32mub120cen=spline(T/ctcen,r32mub120cen,xsame)
r42mub120cen=spline(T/ctcen,r42mub120cen,xsame)
r62mub120cen=spline(T/ctcen,r62mub120cen,xsame)
r82mub120cen=spline(T/ctcen,r82mub120cen,xsame)

dif120cen=abs(r42mub120cen-0.739693)
dif120up=abs(max42120-0.739693)
dif120down=abs(min42120-0.739693)
min120cen_index=1592#int(round(fit7[3,2]))
min120up_index=1592#int(round(fit7[3,1]))
min120down_index=1592#int(round(fit7[3,0]))
print(min120cen_index)

r32120cen=r32mub120cen[min120cen_index]
r32=[max120[min120up_index],max120[min120down_index],min120[min120up_index],min120[min120down_index]]
r32120up=np.max(r32)
r32120down=np.min(r32)
r32120uph=np.max(r32h)
r32120downh=np.min(r32h)

r42120cen=r42mub120cen[min120cen_index]
r62120cen=r62mub120cen[min120cen_index]
r42=[max42120[min120up_index],max42120[min120down_index],min42120[min120up_index],min42120[min120down_index]]
r42120up=np.max(r42)
r42120down=np.min(r42)

r62=[max62120[min120up_index],max62120[min120down_index],min62120[min120up_index],min62120[min120down_index]]
r62120up=np.max(r62)
r62120down=np.min(r62)

r82120cen=r82mub120cen[min120cen_index]
r82=[max82120[min120up_index],max82120[min120down_index],min82120[min120up_index],min82120[min120down_index]]
r82120up=np.max(r82)
r82120down=np.min(r82)
####################################################################################################
chi2mub135cen=np.loadtxt(r'./addition/mub135/cmucen/final/buffer/chi2.dat')
chi3mub135cen=np.loadtxt(r'./addition/mub135/cmucen/final/buffer/chi3.dat')
chi4mub135cen=np.loadtxt(r'./addition/mub135/cmucen/final/buffer/chi4.dat')
chi6mub135cen=np.loadtxt(r'./addition/mub135/cmucen/final/buffer/chi6.dat')
chi8mub135cen=np.loadtxt(r'./addition/mub135/cmucen/final/buffer/chi8.dat')
r32mub135cen=chi3mub135cen/chi2mub135cen
r42mub135cen=chi4mub135cen/chi2mub135cen
r62mub135cen=chi6mub135cen/chi2mub135cen
r82mub135cen=chi8mub135cen/chi2mub135cen
chi2mub135up=np.loadtxt(r'./addition/mub135/cmuup/final/buffer/chi2.dat')
chi3mub135up=np.loadtxt(r'./addition/mub135/cmuup/final/buffer/chi3.dat')
chi4mub135up=np.loadtxt(r'./addition/mub135/cmuup/final/buffer/chi4.dat')
chi6mub135up=np.loadtxt(r'./addition/mub135/cmuup/final/buffer/chi6.dat')
chi8mub135up=np.loadtxt(r'./addition/mub135/cmuup/final/buffer/chi8.dat')
r32mub135up=chi3mub135up/chi2mub135up
r42mub135up=chi4mub135up/chi2mub135up
r62mub135up=chi6mub135up/chi2mub135up
r82mub135up=chi8mub135up/chi2mub135up
chi2mub135down=np.loadtxt(r'./addition/mub135/cmudown/final/buffer/chi2.dat')
chi3mub135down=np.loadtxt(r'./addition/mub135/cmudown/final/buffer/chi3.dat')
chi4mub135down=np.loadtxt(r'./addition/mub135/cmudown/final/buffer/chi4.dat')
chi6mub135down=np.loadtxt(r'./addition/mub135/cmudown/final/buffer/chi6.dat')
chi8mub135down=np.loadtxt(r'./addition/mub135/cmudown/final/buffer/chi8.dat')
r32mub135down=chi3mub135down/chi2mub135down
r42mub135down=chi4mub135down/chi2mub135down
r62mub135down=chi6mub135down/chi2mub135down
r82mub135down=chi8mub135down/chi2mub135down
r32135=np.zeros((2991,20))
r42135=np.zeros((2991,20))
r62135=np.zeros((2991,20))
r82135=np.zeros((2991,20))
for t in range(0,20):
    if t<10:
       r32135[:,t]=spline(T/ct[t],r32mub135up,xsame)
    else:
       r32135[:,t]=spline(T/ct[t-10],r32mub135down,xsame)


for num in range(1,20):
    if num==1:
       max135=np.maximum(r32135[:,num-1],r32135[:,num])
       min135=np.minimum(r32135[:,num-1],r32135[:,num])
    else:
       max135=np.maximum(max135,r32135[:,num])
       min135=np.minimum(min135,r32135[:,num])

for t in range(0,20):
    if t<10:
       r42135[:,t]=spline(T/ct[t],r42mub135up,xsame)
    else:
       r42135[:,t]=spline(T/ct[t-10],r42mub135down,xsame)


for num in range(1,20):
    if num==1:
       max42135=np.maximum(r42135[:,num-1],r42135[:,num])
       min42135=np.minimum(r42135[:,num-1],r42135[:,num])
    else:
       max42135=np.maximum(max42135,r42135[:,num])
       min42135=np.minimum(min42135,r42135[:,num])

for t in range(0,20):
    if t<10:
       r62135[:,t]=spline(T/ct[t],r62mub135up,xsame)
    else:
       r62135[:,t]=spline(T/ct[t-10],r62mub135down,xsame)


for num in range(1,20):
    if num==1:
       max62135=np.maximum(r62135[:,num-1],r62135[:,num])
       min62135=np.minimum(r62135[:,num-1],r62135[:,num])
    else:
       max62135=np.maximum(max62135,r62135[:,num])
       min62135=np.minimum(min62135,r62135[:,num])

for t in range(0,20):
    if t<10:
       r82135[:,t]=spline(T/ct[t],r82mub135up,xsame)
    else:
       r82135[:,t]=spline(T/ct[t-10],r82mub135down,xsame)


for num in range(1,20):
    if num==1:
       max82135=np.maximum(r82135[:,num-1],r82135[:,num])
       min82135=np.minimum(r82135[:,num-1],r82135[:,num])
    else:
       max82135=np.maximum(max82135,r82135[:,num])
       min82135=np.minimum(min82135,r82135[:,num])


r32mub135cen=spline(T/ctcen,r32mub135cen,xsame)
r42mub135cen=spline(T/ctcen,r42mub135cen,xsame)
r62mub135cen=spline(T/ctcen,r62mub135cen,xsame)
r82mub135cen=spline(T/ctcen,r82mub135cen,xsame)

dif135cen=abs(r42mub135cen-0.739693)
dif135up=abs(max42135-0.739693)
dif135down=abs(min42135-0.739693)
min135cen_index=1588#int(round(fit7[3,2]))
min135up_index=1588#int(round(fit7[3,1]))
min135down_index=1588#int(round(fit7[3,0]))
print(min135cen_index)

r32135cen=r32mub135cen[min135cen_index]
r32=[max135[min135up_index],max135[min135down_index],min135[min135up_index],min135[min135down_index]]
r32135up=np.max(r32)
r32135down=np.min(r32)
r32135uph=np.max(r32h)
r32135downh=np.min(r32h)

r42135cen=r42mub135cen[min135cen_index]
r62135cen=r62mub135cen[min135cen_index]
r42=[max42135[min135up_index],max42135[min135down_index],min42135[min135up_index],min42135[min135down_index]]
r42135up=np.max(r42)
r42135down=np.min(r42)

r62=[max62135[min135up_index],max62135[min135down_index],min62135[min135up_index],min62135[min135down_index]]
r62135up=np.max(r62)
r62135down=np.min(r62)

r82135cen=r82mub135cen[min135cen_index]
r82=[max82135[min135up_index],max82135[min135down_index],min82135[min135up_index],min82135[min135down_index]]
r82135up=np.max(r82)
r82135down=np.min(r82)


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
r32148=np.zeros((2991,20))
r42148=np.zeros((2991,20))
r62148=np.zeros((2991,20))
r82148=np.zeros((2991,20))
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

for t in range(0,20):
    if t<10:
       r82148[:,t]=spline(T/ct[t],r82mub148up,xsame)
    else:
       r82148[:,t]=spline(T/ct[t-10],r82mub148down,xsame)


for num in range(1,20):
    if num==1:
       max82148=np.maximum(r82148[:,num-1],r82148[:,num])
       min82148=np.minimum(r82148[:,num-1],r82148[:,num])
    else:
       max82148=np.maximum(max82148,r82148[:,num])
       min82148=np.minimum(min82148,r82148[:,num])

r32mub148cen=spline(T/ctcen,r32mub148cen,xsame)
r42mub148cen=spline(T/ctcen,r42mub148cen,xsame)
r62mub148cen=spline(T/ctcen,r62mub148cen,xsame)
r82mub148cen=spline(T/ctcen,r82mub148cen,xsame)

dif148cen=abs(r42mub148cen-0.196254)
dif148up=abs(max42148-0.196254)
dif148down=abs(min42148-0.196254)
min148cen_index=1584#int(round(fit7[4,2]))
min148up_index=1584#int(round(fit7[4,1]))
min148down_index=1584#int(round(fit7[4,0]))
print(min148cen_index)
#print(min148up_index)
#print(min148down_index)
r32148cen=r32mub148cen[min148cen_index]
#r32148hcen=r32mub148cen[min148cen_index+int(min148cen_index*deltat)]
r32148hcen=r32mub148cen[Tcen[4]]
r32=[max148[min148up_index],max148[min148down_index],min148[min148up_index],min148[min148down_index]]
#r32h=[max148[min148up_index+int(min148up_index*deltat)],max148[min148down_index+int(min148down_index*deltat)],min148[min148up_index+int(min148up_index*deltat)],min148[min148down_index+int(min148down_index*deltat)]]
r32h=[max148[Tcup[4]],max148[Tcdown[4]],min148[Tcup[4]],min148[Tcdown[4]]]
r32148up=np.max(r32)
r32148down=np.min(r32)
r32148uph=np.max(r32h)
r32148downh=np.min(r32h)

r42148cen=r42mub148cen[min148cen_index]
r62148cen=r62mub148cen[min148cen_index]
#r42148hcen=r42mub148cen[min148cen_index+int(min148cen_index*deltat)]
#r62148hcen=r62mub148cen[min148cen_index+int(min148cen_index*deltat)]
r42148hcen=r42mub148cen[Tcen[4]]
r62148hcen=r62mub148cen[Tcen[4]]
r42=[max42148[min148up_index],max42148[min148down_index],min42148[min148up_index],min42148[min148down_index]]
#r42h=[max42148[min148up_index+int(min148up_index*deltat)],max42148[min148down_index+int(min148down_index*deltat)],min42148[min148up_index+int(min148up_index*deltat)],min42148[min148down_index+int(min148down_index*deltat)]]
r42h=[max42148[Tcup[4]],max42148[Tcdown[4]],min42148[Tcup[4]],min42148[Tcdown[4]]]
r42148up=np.max(r42)
r42148down=np.min(r42)
r42148uph=np.max(r42h)
r42148downh=np.min(r42h)

r62=[max62148[min148up_index],max62148[min148down_index],min62148[min148up_index],min62148[min148down_index]]
#r62h=[max62148[min148up_index+int(min148up_index*deltat)],max62148[min148down_index+int(min148down_index*deltat)],min62148[min148up_index+int(min148up_index*deltat)],min62148[min148down_index+int(min148down_index*deltat)]]
r62h=[max62148[Tcup[4]],max62148[Tcdown[4]],min62148[Tcup[4]],min62148[Tcdown[4]]]
r62148up=np.max(r62)
r62148down=np.min(r62)
r62148uph=np.max(r62h)
r62148downh=np.min(r62h)

r82148cen=r82mub148cen[min148cen_index]
#r82148hcen=r82mub148cen[min148cen_index+int(min148cen_index*deltat)]
r82148hcen=r82mub148cen[Tcen[4]]
r82=[max82148[min148up_index],max82148[min148down_index],min82148[min148up_index],min82148[min148down_index]]
#r82h=[max82148[min148up_index+int(min148up_index*deltat)],max82148[min148down_index+int(min148down_index*deltat)],min82148[min148up_index+int(min148up_index*deltat)],min82148[min148down_index+int(min148down_index*deltat)]]
r82h=[max82148[Tcup[4]],max82148[Tcdown[4]],min82148[Tcup[4]],min82148[Tcdown[4]]]
r82148up=np.max(r82)
r82148down=np.min(r82)
r82148uph=np.max(r82h)
r82148downh=np.min(r82h)
####################################################################################################
chi2mub165cen=np.loadtxt(r'./addition/mub165/cmucen/final/buffer/chi2.dat')
chi3mub165cen=np.loadtxt(r'./addition/mub165/cmucen/final/buffer/chi3.dat')
chi4mub165cen=np.loadtxt(r'./addition/mub165/cmucen/final/buffer/chi4.dat')
chi6mub165cen=np.loadtxt(r'./addition/mub165/cmucen/final/buffer/chi6.dat')
chi8mub165cen=np.loadtxt(r'./addition/mub165/cmucen/final/buffer/chi8.dat')
r32mub165cen=chi3mub165cen/chi2mub165cen
r42mub165cen=chi4mub165cen/chi2mub165cen
r62mub165cen=chi6mub165cen/chi2mub165cen
r82mub165cen=chi8mub165cen/chi2mub165cen
chi2mub165up=np.loadtxt(r'./addition/mub165/cmuup/final/buffer/chi2.dat')
chi3mub165up=np.loadtxt(r'./addition/mub165/cmuup/final/buffer/chi3.dat')
chi4mub165up=np.loadtxt(r'./addition/mub165/cmuup/final/buffer/chi4.dat')
chi6mub165up=np.loadtxt(r'./addition/mub165/cmuup/final/buffer/chi6.dat')
chi8mub165up=np.loadtxt(r'./addition/mub165/cmuup/final/buffer/chi8.dat')
r32mub165up=chi3mub165up/chi2mub165up
r42mub165up=chi4mub165up/chi2mub165up
r62mub165up=chi6mub165up/chi2mub165up
r82mub165up=chi8mub165up/chi2mub165up
chi2mub165up1=np.loadtxt(r'./addition/mub165/cmuup1/final/buffer/chi2.dat')
chi3mub165up1=np.loadtxt(r'./addition/mub165/cmuup1/final/buffer/chi3.dat')
chi4mub165up1=np.loadtxt(r'./addition/mub165/cmuup1/final/buffer/chi4.dat')
chi6mub165up1=np.loadtxt(r'./addition/mub165/cmuup1/final/buffer/chi6.dat')
chi8mub165up1=np.loadtxt(r'./addition/mub165/cmuup1/final/buffer/chi8.dat')
r32mub165up1=chi3mub165up1/chi2mub165up1
r42mub165up1=chi4mub165up1/chi2mub165up1
r62mub165up1=chi6mub165up1/chi2mub165up1
r82mub165up1=chi8mub165up1/chi2mub165up1
chi2mub165up2=np.loadtxt(r'./addition/mub165/cmuup2/final/buffer/chi2.dat')
chi3mub165up2=np.loadtxt(r'./addition/mub165/cmuup2/final/buffer/chi3.dat')
chi4mub165up2=np.loadtxt(r'./addition/mub165/cmuup2/final/buffer/chi4.dat')
chi6mub165up2=np.loadtxt(r'./addition/mub165/cmuup2/final/buffer/chi6.dat')
chi8mub165up2=np.loadtxt(r'./addition/mub165/cmuup2/final/buffer/chi8.dat')
r32mub165up2=chi3mub165up2/chi2mub165up2
r42mub165up2=chi4mub165up2/chi2mub165up2
r62mub165up2=chi6mub165up2/chi2mub165up2
r82mub165up2=chi8mub165up2/chi2mub165up2
chi2mub165up3=np.loadtxt(r'./addition/mub165/cmuup3/final/buffer/chi2.dat')
chi3mub165up3=np.loadtxt(r'./addition/mub165/cmuup3/final/buffer/chi3.dat')
chi4mub165up3=np.loadtxt(r'./addition/mub165/cmuup3/final/buffer/chi4.dat')
chi6mub165up3=np.loadtxt(r'./addition/mub165/cmuup3/final/buffer/chi6.dat')
chi8mub165up3=np.loadtxt(r'./addition/mub165/cmuup3/final/buffer/chi8.dat')
r32mub165up3=chi3mub165up3/chi2mub165up3
r42mub165up3=chi4mub165up3/chi2mub165up3
r62mub165up3=chi6mub165up3/chi2mub165up3
r82mub165up3=chi8mub165up3/chi2mub165up3
chi2mub165up4=np.loadtxt(r'./addition/mub165/cmuup4/final/buffer/chi2.dat')
chi3mub165up4=np.loadtxt(r'./addition/mub165/cmuup4/final/buffer/chi3.dat')
chi4mub165up4=np.loadtxt(r'./addition/mub165/cmuup4/final/buffer/chi4.dat')
chi6mub165up4=np.loadtxt(r'./addition/mub165/cmuup4/final/buffer/chi6.dat')
chi8mub165up4=np.loadtxt(r'./addition/mub165/cmuup4/final/buffer/chi8.dat')
r32mub165up4=chi3mub165up4/chi2mub165up4
r42mub165up4=chi4mub165up4/chi2mub165up4
r62mub165up4=chi6mub165up4/chi2mub165up4
r82mub165up4=chi8mub165up4/chi2mub165up4
chi2mub165down=np.loadtxt(r'./addition/mub165/cmudown/final/buffer/chi2.dat')
chi3mub165down=np.loadtxt(r'./addition/mub165/cmudown/final/buffer/chi3.dat')
chi4mub165down=np.loadtxt(r'./addition/mub165/cmudown/final/buffer/chi4.dat')
chi6mub165down=np.loadtxt(r'./addition/mub165/cmudown/final/buffer/chi6.dat')
chi8mub165down=np.loadtxt(r'./addition/mub165/cmudown/final/buffer/chi8.dat')
r32mub165down=chi3mub165down/chi2mub165down
r42mub165down=chi4mub165down/chi2mub165down
r62mub165down=chi6mub165down/chi2mub165down
r82mub165down=chi8mub165down/chi2mub165down
chi2mub165down1=np.loadtxt(r'./addition/mub165/cmudown1/final/buffer/chi2.dat')
chi3mub165down1=np.loadtxt(r'./addition/mub165/cmudown1/final/buffer/chi3.dat')
chi4mub165down1=np.loadtxt(r'./addition/mub165/cmudown1/final/buffer/chi4.dat')
chi6mub165down1=np.loadtxt(r'./addition/mub165/cmudown1/final/buffer/chi6.dat')
chi8mub165down1=np.loadtxt(r'./addition/mub165/cmudown1/final/buffer/chi8.dat')
r32mub165down1=chi3mub165down1/chi2mub165down1
r42mub165down1=chi4mub165down1/chi2mub165down1
r62mub165down1=chi6mub165down1/chi2mub165down1
r82mub165down1=chi8mub165down1/chi2mub165down1
chi2mub165down2=np.loadtxt(r'./addition/mub165/cmudown2/final/buffer/chi2.dat')
chi3mub165down2=np.loadtxt(r'./addition/mub165/cmudown2/final/buffer/chi3.dat')
chi4mub165down2=np.loadtxt(r'./addition/mub165/cmudown2/final/buffer/chi4.dat')
chi6mub165down2=np.loadtxt(r'./addition/mub165/cmudown2/final/buffer/chi6.dat')
chi8mub165down2=np.loadtxt(r'./addition/mub165/cmudown2/final/buffer/chi8.dat')
r32mub165down2=chi3mub165down2/chi2mub165down2
r42mub165down2=chi4mub165down2/chi2mub165down2
r62mub165down2=chi6mub165down2/chi2mub165down2
r82mub165down2=chi8mub165down2/chi2mub165down2
chi2mub165down3=np.loadtxt(r'./addition/mub165/cmudown3/final/buffer/chi2.dat')
chi3mub165down3=np.loadtxt(r'./addition/mub165/cmudown3/final/buffer/chi3.dat')
chi4mub165down3=np.loadtxt(r'./addition/mub165/cmudown3/final/buffer/chi4.dat')
chi6mub165down3=np.loadtxt(r'./addition/mub165/cmudown3/final/buffer/chi6.dat')
chi8mub165down3=np.loadtxt(r'./addition/mub165/cmudown3/final/buffer/chi8.dat')
r32mub165down3=chi3mub165down3/chi2mub165down3
r42mub165down3=chi4mub165down3/chi2mub165down3
r62mub165down3=chi6mub165down3/chi2mub165down3
r82mub165down3=chi8mub165down3/chi2mub165down3
chi2mub165down4=np.loadtxt(r'./addition/mub165/cmudown4/final/buffer/chi2.dat')
chi3mub165down4=np.loadtxt(r'./addition/mub165/cmudown4/final/buffer/chi3.dat')
chi4mub165down4=np.loadtxt(r'./addition/mub165/cmudown4/final/buffer/chi4.dat')
chi6mub165down4=np.loadtxt(r'./addition/mub165/cmudown4/final/buffer/chi6.dat')
chi8mub165down4=np.loadtxt(r'./addition/mub165/cmudown4/final/buffer/chi8.dat')
r32mub165down4=chi3mub165down4/chi2mub165down4
r42mub165down4=chi4mub165down4/chi2mub165down4
r62mub165down4=chi6mub165down4/chi2mub165down4
r82mub165down4=chi8mub165down4/chi2mub165down4
r32165=np.zeros((2991,100))
r42165=np.zeros((2991,100))
r62165=np.zeros((2991,100))
r82165=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32165[:,t]=spline(T/ct[t],r32mub165up,xsame)
    else:
       if t>=10 and t<20:
          r32165[:,t]=spline(T/ct[t-10],r32mub165up1,xsame)
       else:
          if t>=20 and t<30:
             r32165[:,t]=spline(T/ct[t-20],r32mub165up2,xsame)
          else: 
             if t>=30 and t<40:
                r32165[:,t]=spline(T/ct[t-30],r32mub165up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32165[:,t]=spline(T/ct[t-40],r32mub165up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32165[:,t]=spline(T/ct[t-50],r32mub165down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32165[:,t]=spline(T/ct[t-60],r32mub165down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32165[:,t]=spline(T/ct[t-70],r32mub165down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32165[:,t]=spline(T/ct[t-80],r32mub165down3,xsame)
                            else:
                                r32165[:,t]=spline(T/ct[t-90],r32mub165down4,xsame)

for t in range(0,100):
    if t<10:
       r42165[:,t]=spline(T/ct[t],r42mub165up,xsame)
    else:
       if t>=10 and t<20:
          r42165[:,t]=spline(T/ct[t-10],r42mub165up1,xsame)
       else:
          if t>=20 and t<30:
             r42165[:,t]=spline(T/ct[t-20],r42mub165up2,xsame)
          else: 
             if t>=30 and t<40:
                r42165[:,t]=spline(T/ct[t-30],r42mub165up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42165[:,t]=spline(T/ct[t-40],r42mub165up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42165[:,t]=spline(T/ct[t-50],r42mub165down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42165[:,t]=spline(T/ct[t-60],r42mub165down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42165[:,t]=spline(T/ct[t-70],r42mub165down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42165[:,t]=spline(T/ct[t-80],r42mub165down3,xsame)
                            else:
                                r42165[:,t]=spline(T/ct[t-90],r42mub165down4,xsame)

for t in range(0,100):
    if t<10:
       r62165[:,t]=spline(T/ct[t],r62mub165up,xsame)
    else:
       if t>=10 and t<20:
          r62165[:,t]=spline(T/ct[t-10],r62mub165up1,xsame)
       else:
          if t>=20 and t<30:
             r62165[:,t]=spline(T/ct[t-20],r62mub165up2,xsame)
          else: 
             if t>=30 and t<40:
                r62165[:,t]=spline(T/ct[t-30],r62mub165up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62165[:,t]=spline(T/ct[t-40],r62mub165up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62165[:,t]=spline(T/ct[t-50],r62mub165down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62165[:,t]=spline(T/ct[t-60],r62mub165down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62165[:,t]=spline(T/ct[t-70],r62mub165down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62165[:,t]=spline(T/ct[t-80],r62mub165down3,xsame)
                            else:
                                r62165[:,t]=spline(T/ct[t-90],r62mub165down4,xsame)

for t in range(0,100):
    if t<10:
       r82165[:,t]=spline(T/ct[t],r82mub165up,xsame)
    else:
       if t>=10 and t<20:
          r82165[:,t]=spline(T/ct[t-10],r82mub165up1,xsame)
       else:
          if t>=20 and t<30:
             r82165[:,t]=spline(T/ct[t-20],r82mub165up2,xsame)
          else: 
             if t>=30 and t<40:
                r82165[:,t]=spline(T/ct[t-30],r82mub165up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82165[:,t]=spline(T/ct[t-40],r82mub165up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82165[:,t]=spline(T/ct[t-50],r82mub165down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82165[:,t]=spline(T/ct[t-60],r82mub165down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82165[:,t]=spline(T/ct[t-70],r82mub165down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82165[:,t]=spline(T/ct[t-80],r82mub165down3,xsame)
                            else:
                                r82165[:,t]=spline(T/ct[t-90],r82mub165down4,xsame)


for num in range(1,100):
    if num==1:
       max165=np.maximum(r32165[:,num-1],r32165[:,num])
       min165=np.minimum(r32165[:,num-1],r32165[:,num])
    else:
       max165=np.maximum(max165,r32165[:,num])
       min165=np.minimum(min165,r32165[:,num])

for num in range(1,100):
    if num==1:
       max42165=np.maximum(r42165[:,num-1],r42165[:,num])
       min42165=np.minimum(r42165[:,num-1],r42165[:,num])
    else:
       max42165=np.maximum(max42165,r42165[:,num])
       min42165=np.minimum(min42165,r42165[:,num])

for num in range(1,100):
    if num==1:
       max62165=np.maximum(r62165[:,num-1],r62165[:,num])
       min62165=np.minimum(r62165[:,num-1],r62165[:,num])
    else:
       max62165=np.maximum(max62165,r62165[:,num])
       min62165=np.minimum(min62165,r62165[:,num])

for num in range(1,100):
    if num==1:
       max82165=np.maximum(r82165[:,num-1],r82165[:,num])
       min82165=np.minimum(r82165[:,num-1],r82165[:,num])
    else:
       max82165=np.maximum(max82165,r82165[:,num])
       min82165=np.minimum(min82165,r82165[:,num])

r32mub165cen=spline(T/ctcen,r32mub165cen,xsame)
r42mub165cen=spline(T/ctcen,r42mub165cen,xsame)
r62mub165cen=spline(T/ctcen,r62mub165cen,xsame)
r82mub165cen=spline(T/ctcen,r82mub165cen,xsame)

dif165cen=abs(r42mub165cen-0.140553)
dif165up=abs(max42165-0.140553)
dif165down=abs(min42165-0.140553)
min165cen_index=1579#int(round(fit7[5,2]))
min165up_index=1579#int(round(fit7[5,1]))
min165down_index=1579#int(round(fit7[5,0]))
print(min165cen_index)
r32165cen=r32mub165cen[min165cen_index]
r32165hcen=r32mub165cen[Tcen[5]]
r32=[max165[min165up_index],max165[min165down_index],min165[min165up_index],min165[min165down_index]]
r32165up=np.max(r32)
r32165down=np.min(r32)

r42165cen=r42mub165cen[min165cen_index]
r62165cen=r62mub165cen[min165cen_index]
r42=[max42165[min165up_index],max42165[min165down_index],min42165[min165up_index],min42165[min165down_index]]
r42165up=np.max(r42)
r42165down=np.min(r42)

r62=[max62165[min165up_index],max62165[min165down_index],min62165[min165up_index],min62165[min165down_index]]
r62165up=np.max(r62)
r62165down=np.min(r62)

r82165cen=r82mub165cen[min165cen_index]
r82=[max82165[min165up_index],max82165[min165down_index],min82165[min165up_index],min82165[min165down_index]]
r82165up=np.max(r82)
r82165down=np.min(r82)
####################################################################################################
chi2mub180cen=np.loadtxt(r'./addition/mub180/cmucen/final/buffer/chi2.dat')
chi3mub180cen=np.loadtxt(r'./addition/mub180/cmucen/final/buffer/chi3.dat')
chi4mub180cen=np.loadtxt(r'./addition/mub180/cmucen/final/buffer/chi4.dat')
chi6mub180cen=np.loadtxt(r'./addition/mub180/cmucen/final/buffer/chi6.dat')
chi8mub180cen=np.loadtxt(r'./addition/mub180/cmucen/final/buffer/chi8.dat')
r32mub180cen=chi3mub180cen/chi2mub180cen
r42mub180cen=chi4mub180cen/chi2mub180cen
r62mub180cen=chi6mub180cen/chi2mub180cen
r82mub180cen=chi8mub180cen/chi2mub180cen
chi2mub180up=np.loadtxt(r'./addition/mub180/cmuup/final/buffer/chi2.dat')
chi3mub180up=np.loadtxt(r'./addition/mub180/cmuup/final/buffer/chi3.dat')
chi4mub180up=np.loadtxt(r'./addition/mub180/cmuup/final/buffer/chi4.dat')
chi6mub180up=np.loadtxt(r'./addition/mub180/cmuup/final/buffer/chi6.dat')
chi8mub180up=np.loadtxt(r'./addition/mub180/cmuup/final/buffer/chi8.dat')
r32mub180up=chi3mub180up/chi2mub180up
r42mub180up=chi4mub180up/chi2mub180up
r62mub180up=chi6mub180up/chi2mub180up
r82mub180up=chi8mub180up/chi2mub180up
chi2mub180up1=np.loadtxt(r'./addition/mub180/cmuup1/final/buffer/chi2.dat')
chi3mub180up1=np.loadtxt(r'./addition/mub180/cmuup1/final/buffer/chi3.dat')
chi4mub180up1=np.loadtxt(r'./addition/mub180/cmuup1/final/buffer/chi4.dat')
chi6mub180up1=np.loadtxt(r'./addition/mub180/cmuup1/final/buffer/chi6.dat')
chi8mub180up1=np.loadtxt(r'./addition/mub180/cmuup1/final/buffer/chi8.dat')
r32mub180up1=chi3mub180up1/chi2mub180up1
r42mub180up1=chi4mub180up1/chi2mub180up1
r62mub180up1=chi6mub180up1/chi2mub180up1
r82mub180up1=chi8mub180up1/chi2mub180up1
chi2mub180up2=np.loadtxt(r'./addition/mub180/cmuup2/final/buffer/chi2.dat')
chi3mub180up2=np.loadtxt(r'./addition/mub180/cmuup2/final/buffer/chi3.dat')
chi4mub180up2=np.loadtxt(r'./addition/mub180/cmuup2/final/buffer/chi4.dat')
chi6mub180up2=np.loadtxt(r'./addition/mub180/cmuup2/final/buffer/chi6.dat')
chi8mub180up2=np.loadtxt(r'./addition/mub180/cmuup2/final/buffer/chi8.dat')
r32mub180up2=chi3mub180up2/chi2mub180up2
r42mub180up2=chi4mub180up2/chi2mub180up2
r62mub180up2=chi6mub180up2/chi2mub180up2
r82mub180up2=chi8mub180up2/chi2mub180up2
chi2mub180up3=np.loadtxt(r'./addition/mub180/cmuup3/final/buffer/chi2.dat')
chi3mub180up3=np.loadtxt(r'./addition/mub180/cmuup3/final/buffer/chi3.dat')
chi4mub180up3=np.loadtxt(r'./addition/mub180/cmuup3/final/buffer/chi4.dat')
chi6mub180up3=np.loadtxt(r'./addition/mub180/cmuup3/final/buffer/chi6.dat')
chi8mub180up3=np.loadtxt(r'./addition/mub180/cmuup3/final/buffer/chi8.dat')
r32mub180up3=chi3mub180up3/chi2mub180up3
r42mub180up3=chi4mub180up3/chi2mub180up3
r62mub180up3=chi6mub180up3/chi2mub180up3
r82mub180up3=chi8mub180up3/chi2mub180up3
chi2mub180up4=np.loadtxt(r'./addition/mub180/cmuup4/final/buffer/chi2.dat')
chi3mub180up4=np.loadtxt(r'./addition/mub180/cmuup4/final/buffer/chi3.dat')
chi4mub180up4=np.loadtxt(r'./addition/mub180/cmuup4/final/buffer/chi4.dat')
chi6mub180up4=np.loadtxt(r'./addition/mub180/cmuup4/final/buffer/chi6.dat')
chi8mub180up4=np.loadtxt(r'./addition/mub180/cmuup4/final/buffer/chi8.dat')
r32mub180up4=chi3mub180up4/chi2mub180up4
r42mub180up4=chi4mub180up4/chi2mub180up4
r62mub180up4=chi6mub180up4/chi2mub180up4
r82mub180up4=chi8mub180up4/chi2mub180up4
chi2mub180down=np.loadtxt(r'./addition/mub180/cmudown/final/buffer/chi2.dat')
chi3mub180down=np.loadtxt(r'./addition/mub180/cmudown/final/buffer/chi3.dat')
chi4mub180down=np.loadtxt(r'./addition/mub180/cmudown/final/buffer/chi4.dat')
chi6mub180down=np.loadtxt(r'./addition/mub180/cmudown/final/buffer/chi6.dat')
chi8mub180down=np.loadtxt(r'./addition/mub180/cmudown/final/buffer/chi8.dat')
r32mub180down=chi3mub180down/chi2mub180down
r42mub180down=chi4mub180down/chi2mub180down
r62mub180down=chi6mub180down/chi2mub180down
r82mub180down=chi8mub180down/chi2mub180down
chi2mub180down1=np.loadtxt(r'./addition/mub180/cmudown1/final/buffer/chi2.dat')
chi3mub180down1=np.loadtxt(r'./addition/mub180/cmudown1/final/buffer/chi3.dat')
chi4mub180down1=np.loadtxt(r'./addition/mub180/cmudown1/final/buffer/chi4.dat')
chi6mub180down1=np.loadtxt(r'./addition/mub180/cmudown1/final/buffer/chi6.dat')
chi8mub180down1=np.loadtxt(r'./addition/mub180/cmudown1/final/buffer/chi8.dat')
r32mub180down1=chi3mub180down1/chi2mub180down1
r42mub180down1=chi4mub180down1/chi2mub180down1
r62mub180down1=chi6mub180down1/chi2mub180down1
r82mub180down1=chi8mub180down1/chi2mub180down1
chi2mub180down2=np.loadtxt(r'./addition/mub180/cmudown2/final/buffer/chi2.dat')
chi3mub180down2=np.loadtxt(r'./addition/mub180/cmudown2/final/buffer/chi3.dat')
chi4mub180down2=np.loadtxt(r'./addition/mub180/cmudown2/final/buffer/chi4.dat')
chi6mub180down2=np.loadtxt(r'./addition/mub180/cmudown2/final/buffer/chi6.dat')
chi8mub180down2=np.loadtxt(r'./addition/mub180/cmudown2/final/buffer/chi8.dat')
r32mub180down2=chi3mub180down2/chi2mub180down2
r42mub180down2=chi4mub180down2/chi2mub180down2
r62mub180down2=chi6mub180down2/chi2mub180down2
r82mub180down2=chi8mub180down2/chi2mub180down2
chi2mub180down3=np.loadtxt(r'./addition/mub180/cmudown3/final/buffer/chi2.dat')
chi3mub180down3=np.loadtxt(r'./addition/mub180/cmudown3/final/buffer/chi3.dat')
chi4mub180down3=np.loadtxt(r'./addition/mub180/cmudown3/final/buffer/chi4.dat')
chi6mub180down3=np.loadtxt(r'./addition/mub180/cmudown3/final/buffer/chi6.dat')
chi8mub180down3=np.loadtxt(r'./addition/mub180/cmudown3/final/buffer/chi8.dat')
r32mub180down3=chi3mub180down3/chi2mub180down3
r42mub180down3=chi4mub180down3/chi2mub180down3
r62mub180down3=chi6mub180down3/chi2mub180down3
r82mub180down3=chi8mub180down3/chi2mub180down3
chi2mub180down4=np.loadtxt(r'./addition/mub180/cmudown4/final/buffer/chi2.dat')
chi3mub180down4=np.loadtxt(r'./addition/mub180/cmudown4/final/buffer/chi3.dat')
chi4mub180down4=np.loadtxt(r'./addition/mub180/cmudown4/final/buffer/chi4.dat')
chi6mub180down4=np.loadtxt(r'./addition/mub180/cmudown4/final/buffer/chi6.dat')
chi8mub180down4=np.loadtxt(r'./addition/mub180/cmudown4/final/buffer/chi8.dat')
r32mub180down4=chi3mub180down4/chi2mub180down4
r42mub180down4=chi4mub180down4/chi2mub180down4
r62mub180down4=chi6mub180down4/chi2mub180down4
r82mub180down4=chi8mub180down4/chi2mub180down4
r32180=np.zeros((2991,100))
r42180=np.zeros((2991,100))
r62180=np.zeros((2991,100))
r82180=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32180[:,t]=spline(T/ct[t],r32mub180up,xsame)
    else:
       if t>=10 and t<20:
          r32180[:,t]=spline(T/ct[t-10],r32mub180up1,xsame)
       else:
          if t>=20 and t<30:
             r32180[:,t]=spline(T/ct[t-20],r32mub180up2,xsame)
          else: 
             if t>=30 and t<40:
                r32180[:,t]=spline(T/ct[t-30],r32mub180up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32180[:,t]=spline(T/ct[t-40],r32mub180up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32180[:,t]=spline(T/ct[t-50],r32mub180down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32180[:,t]=spline(T/ct[t-60],r32mub180down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32180[:,t]=spline(T/ct[t-70],r32mub180down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32180[:,t]=spline(T/ct[t-80],r32mub180down3,xsame)
                            else:
                                r32180[:,t]=spline(T/ct[t-90],r32mub180down4,xsame)

for t in range(0,100):
    if t<10:
       r42180[:,t]=spline(T/ct[t],r42mub180up,xsame)
    else:
       if t>=10 and t<20:
          r42180[:,t]=spline(T/ct[t-10],r42mub180up1,xsame)
       else:
          if t>=20 and t<30:
             r42180[:,t]=spline(T/ct[t-20],r42mub180up2,xsame)
          else: 
             if t>=30 and t<40:
                r42180[:,t]=spline(T/ct[t-30],r42mub180up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42180[:,t]=spline(T/ct[t-40],r42mub180up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42180[:,t]=spline(T/ct[t-50],r42mub180down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42180[:,t]=spline(T/ct[t-60],r42mub180down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42180[:,t]=spline(T/ct[t-70],r42mub180down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42180[:,t]=spline(T/ct[t-80],r42mub180down3,xsame)
                            else:
                                r42180[:,t]=spline(T/ct[t-90],r42mub180down4,xsame)

for t in range(0,100):
    if t<10:
       r62180[:,t]=spline(T/ct[t],r62mub180up,xsame)
    else:
       if t>=10 and t<20:
          r62180[:,t]=spline(T/ct[t-10],r62mub180up1,xsame)
       else:
          if t>=20 and t<30:
             r62180[:,t]=spline(T/ct[t-20],r62mub180up2,xsame)
          else: 
             if t>=30 and t<40:
                r62180[:,t]=spline(T/ct[t-30],r62mub180up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62180[:,t]=spline(T/ct[t-40],r62mub180up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62180[:,t]=spline(T/ct[t-50],r62mub180down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62180[:,t]=spline(T/ct[t-60],r62mub180down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62180[:,t]=spline(T/ct[t-70],r62mub180down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62180[:,t]=spline(T/ct[t-80],r62mub180down3,xsame)
                            else:
                                r62180[:,t]=spline(T/ct[t-90],r62mub180down4,xsame)

for t in range(0,100):
    if t<10:
       r82180[:,t]=spline(T/ct[t],r82mub180up,xsame)
    else:
       if t>=10 and t<20:
          r82180[:,t]=spline(T/ct[t-10],r82mub180up1,xsame)
       else:
          if t>=20 and t<30:
             r82180[:,t]=spline(T/ct[t-20],r82mub180up2,xsame)
          else: 
             if t>=30 and t<40:
                r82180[:,t]=spline(T/ct[t-30],r82mub180up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82180[:,t]=spline(T/ct[t-40],r82mub180up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82180[:,t]=spline(T/ct[t-50],r82mub180down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82180[:,t]=spline(T/ct[t-60],r82mub180down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82180[:,t]=spline(T/ct[t-70],r82mub180down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82180[:,t]=spline(T/ct[t-80],r82mub180down3,xsame)
                            else:
                                r82180[:,t]=spline(T/ct[t-90],r82mub180down4,xsame)


for num in range(1,100):
    if num==1:
       max180=np.maximum(r32180[:,num-1],r32180[:,num])
       min180=np.minimum(r32180[:,num-1],r32180[:,num])
    else:
       max180=np.maximum(max180,r32180[:,num])
       min180=np.minimum(min180,r32180[:,num])

for num in range(1,100):
    if num==1:
       max42180=np.maximum(r42180[:,num-1],r42180[:,num])
       min42180=np.minimum(r42180[:,num-1],r42180[:,num])
    else:
       max42180=np.maximum(max42180,r42180[:,num])
       min42180=np.minimum(min42180,r42180[:,num])

for num in range(1,100):
    if num==1:
       max62180=np.maximum(r62180[:,num-1],r62180[:,num])
       min62180=np.minimum(r62180[:,num-1],r62180[:,num])
    else:
       max62180=np.maximum(max62180,r62180[:,num])
       min62180=np.minimum(min62180,r62180[:,num])

for num in range(1,100):
    if num==1:
       max82180=np.maximum(r82180[:,num-1],r82180[:,num])
       min82180=np.minimum(r82180[:,num-1],r82180[:,num])
    else:
       max82180=np.maximum(max82180,r82180[:,num])
       min82180=np.minimum(min82180,r82180[:,num])

r32mub180cen=spline(T/ctcen,r32mub180cen,xsame)
r42mub180cen=spline(T/ctcen,r42mub180cen,xsame)
r62mub180cen=spline(T/ctcen,r62mub180cen,xsame)
r82mub180cen=spline(T/ctcen,r82mub180cen,xsame)

dif180cen=abs(r42mub180cen-0.140553)
dif180up=abs(max42180-0.140553)
dif180down=abs(min42180-0.140553)
min180cen_index=1572#int(round(fit7[5,2]))
min180up_index=1572#int(round(fit7[5,1]))
min180down_index=1572#int(round(fit7[5,0]))
print(min180cen_index)
r32180cen=r32mub180cen[min180cen_index]
r32180hcen=r32mub180cen[Tcen[5]]
r32=[max180[min180up_index],max180[min180down_index],min180[min180up_index],min180[min180down_index]]
r32180up=np.max(r32)
r32180down=np.min(r32)

r42180cen=r42mub180cen[min180cen_index]
r62180cen=r62mub180cen[min180cen_index]
r42=[max42180[min180up_index],max42180[min180down_index],min42180[min180up_index],min42180[min180down_index]]
r42180up=np.max(r42)
r42180down=np.min(r42)

r62=[max62180[min180up_index],max62180[min180down_index],min62180[min180up_index],min62180[min180down_index]]
r62180up=np.max(r62)
r62180down=np.min(r62)

r82180cen=r82mub180cen[min180cen_index]
r82=[max82180[min180up_index],max82180[min180down_index],min82180[min180up_index],min82180[min180down_index]]
r82180up=np.max(r82)
r82180down=np.min(r82)
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
r32196=np.zeros((2991,100))
r42196=np.zeros((2991,100))
r62196=np.zeros((2991,100))
r82196=np.zeros((2991,100))
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

for t in range(0,100):
    if t<10:
       r82196[:,t]=spline(T/ct[t],r82mub196up,xsame)
    else:
       if t>=10 and t<20:
          r82196[:,t]=spline(T/ct[t-10],r82mub196up1,xsame)
       else:
          if t>=20 and t<30:
             r82196[:,t]=spline(T/ct[t-20],r82mub196up2,xsame)
          else: 
             if t>=30 and t<40:
                r82196[:,t]=spline(T/ct[t-30],r82mub196up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82196[:,t]=spline(T/ct[t-40],r82mub196up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82196[:,t]=spline(T/ct[t-50],r82mub196down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82196[:,t]=spline(T/ct[t-60],r82mub196down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82196[:,t]=spline(T/ct[t-70],r82mub196down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82196[:,t]=spline(T/ct[t-80],r82mub196down3,xsame)
                            else:
                                r82196[:,t]=spline(T/ct[t-90],r82mub196down4,xsame)


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

for num in range(1,100):
    if num==1:
       max82196=np.maximum(r82196[:,num-1],r82196[:,num])
       min82196=np.minimum(r82196[:,num-1],r82196[:,num])
    else:
       max82196=np.maximum(max82196,r82196[:,num])
       min82196=np.minimum(min82196,r82196[:,num])

r32mub196cen=spline(T/ctcen,r32mub196cen,xsame)
r42mub196cen=spline(T/ctcen,r42mub196cen,xsame)
r62mub196cen=spline(T/ctcen,r62mub196cen,xsame)
r82mub196cen=spline(T/ctcen,r82mub196cen,xsame)

dif196cen=abs(r42mub196cen-0.140553)
dif196up=abs(max42196-0.140553)
dif196down=abs(min42196-0.140553)
min196cen_index=1565#int(round(fit7[5,2]))
min196up_index=1565#int(round(fit7[5,1]))
min196down_index=1565#int(round(fit7[5,0]))
print(min196cen_index)
#print(min196up_index)
#print(min196down_index)
r32196cen=r32mub196cen[min196cen_index]
#r32196hcen=r32mub196cen[min196cen_index+int(min196cen_index*deltat)]
r32196hcen=r32mub196cen[Tcen[5]]
r32=[max196[min196up_index],max196[min196down_index],min196[min196up_index],min196[min196down_index]]
#r32h=[max196[min196up_index+int(min196up_index*deltat)],max196[min196down_index+int(min196down_index*deltat)],min196[min196up_index+int(min196up_index*deltat)],min196[min196down_index+int(min196down_index*deltat)]]
r32h=[max196[Tcup[5]],max196[Tcdown[5]],min196[Tcup[5]],min196[Tcdown[5]]]
r32196up=np.max(r32)
r32196down=np.min(r32)
r32196uph=np.max(r32h)
r32196downh=np.min(r32h)

r42196cen=r42mub196cen[min196cen_index]
r62196cen=r62mub196cen[min196cen_index]
#r42196hcen=r42mub196cen[min196cen_index+int(min196cen_index*deltat)]
#r62196hcen=r62mub196cen[min196cen_index+int(min196cen_index*deltat)]
r42196hcen=r42mub196cen[Tcen[5]]
r62196hcen=r62mub196cen[Tcen[5]]
r42=[max42196[min196up_index],max42196[min196down_index],min42196[min196up_index],min42196[min196down_index]]
#r42h=[max42196[min196up_index+int(min196up_index*deltat)],max42196[min196down_index+int(min196down_index*deltat)],min42196[min196up_index+int(min196up_index*deltat)],min42196[min196down_index+int(min196down_index*deltat)]]
r42h=[max42196[Tcup[5]],max42196[Tcdown[5]],min42196[Tcup[5]],min42196[Tcdown[5]]]
r42196up=np.max(r42)
r42196down=np.min(r42)
r42196uph=np.max(r42h)
r42196downh=np.min(r42h)

r62=[max62196[min196up_index],max62196[min196down_index],min62196[min196up_index],min62196[min196down_index]]
#r62h=[max62196[min196up_index+int(min196up_index*deltat)],max62196[min196down_index+int(min196down_index*deltat)],min62196[min196up_index+int(min196up_index*deltat)],min62196[min196down_index+int(min196down_index*deltat)]]
r62h=[max62196[Tcup[5]],max62196[Tcdown[5]],min62196[Tcup[5]],min62196[Tcdown[5]]]
r62196up=np.max(r62)
r62196down=np.min(r62)
r62196uph=np.max(r62h)
r62196downh=np.min(r62h)

r82196cen=r82mub196cen[min196cen_index]
#r82196hcen=r82mub196cen[min196cen_index+int(min196cen_index*deltat)]
r82196hcen=r82mub196cen[Tcen[5]]
r82=[max82196[min196up_index],max82196[min196down_index],min82196[min196up_index],min82196[min196down_index]]
#r82h=[max82196[min196up_index+int(min196up_index*deltat)],max82196[min196down_index+int(min196down_index*deltat)],min82196[min196up_index+int(min196up_index*deltat)],min82196[min196down_index+int(min196down_index*deltat)]]
r82h=[max82196[Tcup[5]],max82196[Tcdown[5]],min82196[Tcup[5]],min82196[Tcdown[5]]]
r82196up=np.max(r82)
r82196down=np.min(r82)
r82196uph=np.max(r82h)
r82196downh=np.min(r82h)
####################################################################################################
chi2mub215cen=np.loadtxt(r'./addition/mub215/cmucen/final/buffer/chi2.dat')
chi3mub215cen=np.loadtxt(r'./addition/mub215/cmucen/final/buffer/chi3.dat')
chi4mub215cen=np.loadtxt(r'./addition/mub215/cmucen/final/buffer/chi4.dat')
chi6mub215cen=np.loadtxt(r'./addition/mub215/cmucen/final/buffer/chi6.dat')
chi8mub215cen=np.loadtxt(r'./addition/mub215/cmucen/final/buffer/chi8.dat')
r32mub215cen=chi3mub215cen/chi2mub215cen
r42mub215cen=chi4mub215cen/chi2mub215cen
r62mub215cen=chi6mub215cen/chi2mub215cen
r82mub215cen=chi8mub215cen/chi2mub215cen
chi2mub215up=np.loadtxt(r'./addition/mub215/cmuup/final/buffer/chi2.dat')
chi3mub215up=np.loadtxt(r'./addition/mub215/cmuup/final/buffer/chi3.dat')
chi4mub215up=np.loadtxt(r'./addition/mub215/cmuup/final/buffer/chi4.dat')
chi6mub215up=np.loadtxt(r'./addition/mub215/cmuup/final/buffer/chi6.dat')
chi8mub215up=np.loadtxt(r'./addition/mub215/cmuup/final/buffer/chi8.dat')
r32mub215up=chi3mub215up/chi2mub215up
r42mub215up=chi4mub215up/chi2mub215up
r62mub215up=chi6mub215up/chi2mub215up
r82mub215up=chi8mub215up/chi2mub215up
chi2mub215up1=np.loadtxt(r'./addition/mub215/cmuup1/final/buffer/chi2.dat')
chi3mub215up1=np.loadtxt(r'./addition/mub215/cmuup1/final/buffer/chi3.dat')
chi4mub215up1=np.loadtxt(r'./addition/mub215/cmuup1/final/buffer/chi4.dat')
chi6mub215up1=np.loadtxt(r'./addition/mub215/cmuup1/final/buffer/chi6.dat')
chi8mub215up1=np.loadtxt(r'./addition/mub215/cmuup1/final/buffer/chi8.dat')
r32mub215up1=chi3mub215up1/chi2mub215up1
r42mub215up1=chi4mub215up1/chi2mub215up1
r62mub215up1=chi6mub215up1/chi2mub215up1
r82mub215up1=chi8mub215up1/chi2mub215up1
chi2mub215up2=np.loadtxt(r'./addition/mub215/cmuup2/final/buffer/chi2.dat')
chi3mub215up2=np.loadtxt(r'./addition/mub215/cmuup2/final/buffer/chi3.dat')
chi4mub215up2=np.loadtxt(r'./addition/mub215/cmuup2/final/buffer/chi4.dat')
chi6mub215up2=np.loadtxt(r'./addition/mub215/cmuup2/final/buffer/chi6.dat')
chi8mub215up2=np.loadtxt(r'./addition/mub215/cmuup2/final/buffer/chi8.dat')
r32mub215up2=chi3mub215up2/chi2mub215up2
r42mub215up2=chi4mub215up2/chi2mub215up2
r62mub215up2=chi6mub215up2/chi2mub215up2
r82mub215up2=chi8mub215up2/chi2mub215up2
chi2mub215up3=np.loadtxt(r'./addition/mub215/cmuup3/final/buffer/chi2.dat')
chi3mub215up3=np.loadtxt(r'./addition/mub215/cmuup3/final/buffer/chi3.dat')
chi4mub215up3=np.loadtxt(r'./addition/mub215/cmuup3/final/buffer/chi4.dat')
chi6mub215up3=np.loadtxt(r'./addition/mub215/cmuup3/final/buffer/chi6.dat')
chi8mub215up3=np.loadtxt(r'./addition/mub215/cmuup3/final/buffer/chi8.dat')
r32mub215up3=chi3mub215up3/chi2mub215up3
r42mub215up3=chi4mub215up3/chi2mub215up3
r62mub215up3=chi6mub215up3/chi2mub215up3
r82mub215up3=chi8mub215up3/chi2mub215up3
chi2mub215up4=np.loadtxt(r'./addition/mub215/cmuup4/final/buffer/chi2.dat')
chi3mub215up4=np.loadtxt(r'./addition/mub215/cmuup4/final/buffer/chi3.dat')
chi4mub215up4=np.loadtxt(r'./addition/mub215/cmuup4/final/buffer/chi4.dat')
chi6mub215up4=np.loadtxt(r'./addition/mub215/cmuup4/final/buffer/chi6.dat')
chi8mub215up4=np.loadtxt(r'./addition/mub215/cmuup4/final/buffer/chi8.dat')
r32mub215up4=chi3mub215up4/chi2mub215up4
r42mub215up4=chi4mub215up4/chi2mub215up4
r62mub215up4=chi6mub215up4/chi2mub215up4
r82mub215up4=chi8mub215up4/chi2mub215up4
chi2mub215down=np.loadtxt(r'./addition/mub215/cmudown/final/buffer/chi2.dat')
chi3mub215down=np.loadtxt(r'./addition/mub215/cmudown/final/buffer/chi3.dat')
chi4mub215down=np.loadtxt(r'./addition/mub215/cmudown/final/buffer/chi4.dat')
chi6mub215down=np.loadtxt(r'./addition/mub215/cmudown/final/buffer/chi6.dat')
chi8mub215down=np.loadtxt(r'./addition/mub215/cmudown/final/buffer/chi8.dat')
r32mub215down=chi3mub215down/chi2mub215down
r42mub215down=chi4mub215down/chi2mub215down
r62mub215down=chi6mub215down/chi2mub215down
r82mub215down=chi8mub215down/chi2mub215down
chi2mub215down1=np.loadtxt(r'./addition/mub215/cmudown1/final/buffer/chi2.dat')
chi3mub215down1=np.loadtxt(r'./addition/mub215/cmudown1/final/buffer/chi3.dat')
chi4mub215down1=np.loadtxt(r'./addition/mub215/cmudown1/final/buffer/chi4.dat')
chi6mub215down1=np.loadtxt(r'./addition/mub215/cmudown1/final/buffer/chi6.dat')
chi8mub215down1=np.loadtxt(r'./addition/mub215/cmudown1/final/buffer/chi8.dat')
r32mub215down1=chi3mub215down1/chi2mub215down1
r42mub215down1=chi4mub215down1/chi2mub215down1
r62mub215down1=chi6mub215down1/chi2mub215down1
r82mub215down1=chi8mub215down1/chi2mub215down1
chi2mub215down2=np.loadtxt(r'./addition/mub215/cmudown2/final/buffer/chi2.dat')
chi3mub215down2=np.loadtxt(r'./addition/mub215/cmudown2/final/buffer/chi3.dat')
chi4mub215down2=np.loadtxt(r'./addition/mub215/cmudown2/final/buffer/chi4.dat')
chi6mub215down2=np.loadtxt(r'./addition/mub215/cmudown2/final/buffer/chi6.dat')
chi8mub215down2=np.loadtxt(r'./addition/mub215/cmudown2/final/buffer/chi8.dat')
r32mub215down2=chi3mub215down2/chi2mub215down2
r42mub215down2=chi4mub215down2/chi2mub215down2
r62mub215down2=chi6mub215down2/chi2mub215down2
r82mub215down2=chi8mub215down2/chi2mub215down2
chi2mub215down3=np.loadtxt(r'./addition/mub215/cmudown3/final/buffer/chi2.dat')
chi3mub215down3=np.loadtxt(r'./addition/mub215/cmudown3/final/buffer/chi3.dat')
chi4mub215down3=np.loadtxt(r'./addition/mub215/cmudown3/final/buffer/chi4.dat')
chi6mub215down3=np.loadtxt(r'./addition/mub215/cmudown3/final/buffer/chi6.dat')
chi8mub215down3=np.loadtxt(r'./addition/mub215/cmudown3/final/buffer/chi8.dat')
r32mub215down3=chi3mub215down3/chi2mub215down3
r42mub215down3=chi4mub215down3/chi2mub215down3
r62mub215down3=chi6mub215down3/chi2mub215down3
r82mub215down3=chi8mub215down3/chi2mub215down3
chi2mub215down4=np.loadtxt(r'./addition/mub215/cmudown4/final/buffer/chi2.dat')
chi3mub215down4=np.loadtxt(r'./addition/mub215/cmudown4/final/buffer/chi3.dat')
chi4mub215down4=np.loadtxt(r'./addition/mub215/cmudown4/final/buffer/chi4.dat')
chi6mub215down4=np.loadtxt(r'./addition/mub215/cmudown4/final/buffer/chi6.dat')
chi8mub215down4=np.loadtxt(r'./addition/mub215/cmudown4/final/buffer/chi8.dat')
r32mub215down4=chi3mub215down4/chi2mub215down4
r42mub215down4=chi4mub215down4/chi2mub215down4
r62mub215down4=chi6mub215down4/chi2mub215down4
r82mub215down4=chi8mub215down4/chi2mub215down4
r32215=np.zeros((2991,100))
r42215=np.zeros((2991,100))
r62215=np.zeros((2991,100))
r82215=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32215[:,t]=spline(T/ct[t],r32mub215up,xsame)
    else:
       if t>=10 and t<20:
          r32215[:,t]=spline(T/ct[t-10],r32mub215up1,xsame)
       else:
          if t>=20 and t<30:
             r32215[:,t]=spline(T/ct[t-20],r32mub215up2,xsame)
          else: 
             if t>=30 and t<40:
                r32215[:,t]=spline(T/ct[t-30],r32mub215up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32215[:,t]=spline(T/ct[t-40],r32mub215up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32215[:,t]=spline(T/ct[t-50],r32mub215down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32215[:,t]=spline(T/ct[t-60],r32mub215down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32215[:,t]=spline(T/ct[t-70],r32mub215down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32215[:,t]=spline(T/ct[t-80],r32mub215down3,xsame)
                            else:
                                r32215[:,t]=spline(T/ct[t-90],r32mub215down4,xsame)

for t in range(0,100):
    if t<10:
       r42215[:,t]=spline(T/ct[t],r42mub215up,xsame)
    else:
       if t>=10 and t<20:
          r42215[:,t]=spline(T/ct[t-10],r42mub215up1,xsame)
       else:
          if t>=20 and t<30:
             r42215[:,t]=spline(T/ct[t-20],r42mub215up2,xsame)
          else: 
             if t>=30 and t<40:
                r42215[:,t]=spline(T/ct[t-30],r42mub215up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42215[:,t]=spline(T/ct[t-40],r42mub215up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42215[:,t]=spline(T/ct[t-50],r42mub215down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42215[:,t]=spline(T/ct[t-60],r42mub215down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42215[:,t]=spline(T/ct[t-70],r42mub215down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42215[:,t]=spline(T/ct[t-80],r42mub215down3,xsame)
                            else:
                                r42215[:,t]=spline(T/ct[t-90],r42mub215down4,xsame)

for t in range(0,100):
    if t<10:
       r62215[:,t]=spline(T/ct[t],r62mub215up,xsame)
    else:
       if t>=10 and t<20:
          r62215[:,t]=spline(T/ct[t-10],r62mub215up1,xsame)
       else:
          if t>=20 and t<30:
             r62215[:,t]=spline(T/ct[t-20],r62mub215up2,xsame)
          else: 
             if t>=30 and t<40:
                r62215[:,t]=spline(T/ct[t-30],r62mub215up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62215[:,t]=spline(T/ct[t-40],r62mub215up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62215[:,t]=spline(T/ct[t-50],r62mub215down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62215[:,t]=spline(T/ct[t-60],r62mub215down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62215[:,t]=spline(T/ct[t-70],r62mub215down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62215[:,t]=spline(T/ct[t-80],r62mub215down3,xsame)
                            else:
                                r62215[:,t]=spline(T/ct[t-90],r62mub215down4,xsame)

for t in range(0,100):
    if t<10:
       r82215[:,t]=spline(T/ct[t],r82mub215up,xsame)
    else:
       if t>=10 and t<20:
          r82215[:,t]=spline(T/ct[t-10],r82mub215up1,xsame)
       else:
          if t>=20 and t<30:
             r82215[:,t]=spline(T/ct[t-20],r82mub215up2,xsame)
          else: 
             if t>=30 and t<40:
                r82215[:,t]=spline(T/ct[t-30],r82mub215up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82215[:,t]=spline(T/ct[t-40],r82mub215up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82215[:,t]=spline(T/ct[t-50],r82mub215down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82215[:,t]=spline(T/ct[t-60],r82mub215down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82215[:,t]=spline(T/ct[t-70],r82mub215down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82215[:,t]=spline(T/ct[t-80],r82mub215down3,xsame)
                            else:
                                r82215[:,t]=spline(T/ct[t-90],r82mub215down4,xsame)


for num in range(1,100):
    if num==1:
       max215=np.maximum(r32215[:,num-1],r32215[:,num])
       min215=np.minimum(r32215[:,num-1],r32215[:,num])
    else:
       max215=np.maximum(max215,r32215[:,num])
       min215=np.minimum(min215,r32215[:,num])

for num in range(1,100):
    if num==1:
       max42215=np.maximum(r42215[:,num-1],r42215[:,num])
       min42215=np.minimum(r42215[:,num-1],r42215[:,num])
    else:
       max42215=np.maximum(max42215,r42215[:,num])
       min42215=np.minimum(min42215,r42215[:,num])

for num in range(1,100):
    if num==1:
       max62215=np.maximum(r62215[:,num-1],r62215[:,num])
       min62215=np.minimum(r62215[:,num-1],r62215[:,num])
    else:
       max62215=np.maximum(max62215,r62215[:,num])
       min62215=np.minimum(min62215,r62215[:,num])

for num in range(1,100):
    if num==1:
       max82215=np.maximum(r82215[:,num-1],r82215[:,num])
       min82215=np.minimum(r82215[:,num-1],r82215[:,num])
    else:
       max82215=np.maximum(max82215,r82215[:,num])
       min82215=np.minimum(min82215,r82215[:,num])

r32mub215cen=spline(T/ctcen,r32mub215cen,xsame)
r42mub215cen=spline(T/ctcen,r42mub215cen,xsame)
r62mub215cen=spline(T/ctcen,r62mub215cen,xsame)
r82mub215cen=spline(T/ctcen,r82mub215cen,xsame)

dif215cen=abs(r42mub215cen-0.140553)
dif215up=abs(max42215-0.140553)
dif215down=abs(min42215-0.140553)
min215cen_index=1555#int(round(fit7[5,2]))
min215up_index=1555#int(round(fit7[5,1]))
min215down_index=1555#int(round(fit7[5,0]))
print(min215cen_index)
r32215cen=r32mub215cen[min215cen_index]
r32215hcen=r32mub215cen[Tcen[5]]
r32=[max215[min215up_index],max215[min215down_index],min215[min215up_index],min215[min215down_index]]
r32215up=np.max(r32)
r32215down=np.min(r32)

r42215cen=r42mub215cen[min215cen_index]
r62215cen=r62mub215cen[min215cen_index]
r42=[max42215[min215up_index],max42215[min215down_index],min42215[min215up_index],min42215[min215down_index]]
r42215up=np.max(r42)
r42215down=np.min(r42)

r62=[max62215[min215up_index],max62215[min215down_index],min62215[min215up_index],min62215[min215down_index]]
r62215up=np.max(r62)
r62215down=np.min(r62)

r82215cen=r82mub215cen[min215cen_index]
r82=[max82215[min215up_index],max82215[min215down_index],min82215[min215up_index],min82215[min215down_index]]
r82215up=np.max(r82)
r82215down=np.min(r82)
####################################################################################################
chi2mub230cen=np.loadtxt(r'./addition/mub230/cmucen/final/buffer/chi2.dat')
chi3mub230cen=np.loadtxt(r'./addition/mub230/cmucen/final/buffer/chi3.dat')
chi4mub230cen=np.loadtxt(r'./addition/mub230/cmucen/final/buffer/chi4.dat')
chi6mub230cen=np.loadtxt(r'./addition/mub230/cmucen/final/buffer/chi6.dat')
chi8mub230cen=np.loadtxt(r'./addition/mub230/cmucen/final/buffer/chi8.dat')
r32mub230cen=chi3mub230cen/chi2mub230cen
r42mub230cen=chi4mub230cen/chi2mub230cen
r62mub230cen=chi6mub230cen/chi2mub230cen
r82mub230cen=chi8mub230cen/chi2mub230cen
chi2mub230up=np.loadtxt(r'./addition/mub230/cmuup/final/buffer/chi2.dat')
chi3mub230up=np.loadtxt(r'./addition/mub230/cmuup/final/buffer/chi3.dat')
chi4mub230up=np.loadtxt(r'./addition/mub230/cmuup/final/buffer/chi4.dat')
chi6mub230up=np.loadtxt(r'./addition/mub230/cmuup/final/buffer/chi6.dat')
chi8mub230up=np.loadtxt(r'./addition/mub230/cmuup/final/buffer/chi8.dat')
r32mub230up=chi3mub230up/chi2mub230up
r42mub230up=chi4mub230up/chi2mub230up
r62mub230up=chi6mub230up/chi2mub230up
r82mub230up=chi8mub230up/chi2mub230up
chi2mub230up1=np.loadtxt(r'./addition/mub230/cmuup1/final/buffer/chi2.dat')
chi3mub230up1=np.loadtxt(r'./addition/mub230/cmuup1/final/buffer/chi3.dat')
chi4mub230up1=np.loadtxt(r'./addition/mub230/cmuup1/final/buffer/chi4.dat')
chi6mub230up1=np.loadtxt(r'./addition/mub230/cmuup1/final/buffer/chi6.dat')
chi8mub230up1=np.loadtxt(r'./addition/mub230/cmuup1/final/buffer/chi8.dat')
r32mub230up1=chi3mub230up1/chi2mub230up1
r42mub230up1=chi4mub230up1/chi2mub230up1
r62mub230up1=chi6mub230up1/chi2mub230up1
r82mub230up1=chi8mub230up1/chi2mub230up1
chi2mub230up2=np.loadtxt(r'./addition/mub230/cmuup2/final/buffer/chi2.dat')
chi3mub230up2=np.loadtxt(r'./addition/mub230/cmuup2/final/buffer/chi3.dat')
chi4mub230up2=np.loadtxt(r'./addition/mub230/cmuup2/final/buffer/chi4.dat')
chi6mub230up2=np.loadtxt(r'./addition/mub230/cmuup2/final/buffer/chi6.dat')
chi8mub230up2=np.loadtxt(r'./addition/mub230/cmuup2/final/buffer/chi8.dat')
r32mub230up2=chi3mub230up2/chi2mub230up2
r42mub230up2=chi4mub230up2/chi2mub230up2
r62mub230up2=chi6mub230up2/chi2mub230up2
r82mub230up2=chi8mub230up2/chi2mub230up2
chi2mub230up3=np.loadtxt(r'./addition/mub230/cmuup3/final/buffer/chi2.dat')
chi3mub230up3=np.loadtxt(r'./addition/mub230/cmuup3/final/buffer/chi3.dat')
chi4mub230up3=np.loadtxt(r'./addition/mub230/cmuup3/final/buffer/chi4.dat')
chi6mub230up3=np.loadtxt(r'./addition/mub230/cmuup3/final/buffer/chi6.dat')
chi8mub230up3=np.loadtxt(r'./addition/mub230/cmuup3/final/buffer/chi8.dat')
r32mub230up3=chi3mub230up3/chi2mub230up3
r42mub230up3=chi4mub230up3/chi2mub230up3
r62mub230up3=chi6mub230up3/chi2mub230up3
r82mub230up3=chi8mub230up3/chi2mub230up3
chi2mub230up4=np.loadtxt(r'./addition/mub230/cmuup4/final/buffer/chi2.dat')
chi3mub230up4=np.loadtxt(r'./addition/mub230/cmuup4/final/buffer/chi3.dat')
chi4mub230up4=np.loadtxt(r'./addition/mub230/cmuup4/final/buffer/chi4.dat')
chi6mub230up4=np.loadtxt(r'./addition/mub230/cmuup4/final/buffer/chi6.dat')
chi8mub230up4=np.loadtxt(r'./addition/mub230/cmuup4/final/buffer/chi8.dat')
r32mub230up4=chi3mub230up4/chi2mub230up4
r42mub230up4=chi4mub230up4/chi2mub230up4
r62mub230up4=chi6mub230up4/chi2mub230up4
r82mub230up4=chi8mub230up4/chi2mub230up4
chi2mub230down=np.loadtxt(r'./addition/mub230/cmudown/final/buffer/chi2.dat')
chi3mub230down=np.loadtxt(r'./addition/mub230/cmudown/final/buffer/chi3.dat')
chi4mub230down=np.loadtxt(r'./addition/mub230/cmudown/final/buffer/chi4.dat')
chi6mub230down=np.loadtxt(r'./addition/mub230/cmudown/final/buffer/chi6.dat')
chi8mub230down=np.loadtxt(r'./addition/mub230/cmudown/final/buffer/chi8.dat')
r32mub230down=chi3mub230down/chi2mub230down
r42mub230down=chi4mub230down/chi2mub230down
r62mub230down=chi6mub230down/chi2mub230down
r82mub230down=chi8mub230down/chi2mub230down
chi2mub230down1=np.loadtxt(r'./addition/mub230/cmudown1/final/buffer/chi2.dat')
chi3mub230down1=np.loadtxt(r'./addition/mub230/cmudown1/final/buffer/chi3.dat')
chi4mub230down1=np.loadtxt(r'./addition/mub230/cmudown1/final/buffer/chi4.dat')
chi6mub230down1=np.loadtxt(r'./addition/mub230/cmudown1/final/buffer/chi6.dat')
chi8mub230down1=np.loadtxt(r'./addition/mub230/cmudown1/final/buffer/chi8.dat')
r32mub230down1=chi3mub230down1/chi2mub230down1
r42mub230down1=chi4mub230down1/chi2mub230down1
r62mub230down1=chi6mub230down1/chi2mub230down1
r82mub230down1=chi8mub230down1/chi2mub230down1
chi2mub230down2=np.loadtxt(r'./addition/mub230/cmudown2/final/buffer/chi2.dat')
chi3mub230down2=np.loadtxt(r'./addition/mub230/cmudown2/final/buffer/chi3.dat')
chi4mub230down2=np.loadtxt(r'./addition/mub230/cmudown2/final/buffer/chi4.dat')
chi6mub230down2=np.loadtxt(r'./addition/mub230/cmudown2/final/buffer/chi6.dat')
chi8mub230down2=np.loadtxt(r'./addition/mub230/cmudown2/final/buffer/chi8.dat')
r32mub230down2=chi3mub230down2/chi2mub230down2
r42mub230down2=chi4mub230down2/chi2mub230down2
r62mub230down2=chi6mub230down2/chi2mub230down2
r82mub230down2=chi8mub230down2/chi2mub230down2
chi2mub230down3=np.loadtxt(r'./addition/mub230/cmudown3/final/buffer/chi2.dat')
chi3mub230down3=np.loadtxt(r'./addition/mub230/cmudown3/final/buffer/chi3.dat')
chi4mub230down3=np.loadtxt(r'./addition/mub230/cmudown3/final/buffer/chi4.dat')
chi6mub230down3=np.loadtxt(r'./addition/mub230/cmudown3/final/buffer/chi6.dat')
chi8mub230down3=np.loadtxt(r'./addition/mub230/cmudown3/final/buffer/chi8.dat')
r32mub230down3=chi3mub230down3/chi2mub230down3
r42mub230down3=chi4mub230down3/chi2mub230down3
r62mub230down3=chi6mub230down3/chi2mub230down3
r82mub230down3=chi8mub230down3/chi2mub230down3
chi2mub230down4=np.loadtxt(r'./addition/mub230/cmudown4/final/buffer/chi2.dat')
chi3mub230down4=np.loadtxt(r'./addition/mub230/cmudown4/final/buffer/chi3.dat')
chi4mub230down4=np.loadtxt(r'./addition/mub230/cmudown4/final/buffer/chi4.dat')
chi6mub230down4=np.loadtxt(r'./addition/mub230/cmudown4/final/buffer/chi6.dat')
chi8mub230down4=np.loadtxt(r'./addition/mub230/cmudown4/final/buffer/chi8.dat')
r32mub230down4=chi3mub230down4/chi2mub230down4
r42mub230down4=chi4mub230down4/chi2mub230down4
r62mub230down4=chi6mub230down4/chi2mub230down4
r82mub230down4=chi8mub230down4/chi2mub230down4
r32230=np.zeros((2991,100))
r42230=np.zeros((2991,100))
r62230=np.zeros((2991,100))
r82230=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32230[:,t]=spline(T/ct[t],r32mub230up,xsame)
    else:
       if t>=10 and t<20:
          r32230[:,t]=spline(T/ct[t-10],r32mub230up1,xsame)
       else:
          if t>=20 and t<30:
             r32230[:,t]=spline(T/ct[t-20],r32mub230up2,xsame)
          else: 
             if t>=30 and t<40:
                r32230[:,t]=spline(T/ct[t-30],r32mub230up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32230[:,t]=spline(T/ct[t-40],r32mub230up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32230[:,t]=spline(T/ct[t-50],r32mub230down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32230[:,t]=spline(T/ct[t-60],r32mub230down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32230[:,t]=spline(T/ct[t-70],r32mub230down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32230[:,t]=spline(T/ct[t-80],r32mub230down3,xsame)
                            else:
                                r32230[:,t]=spline(T/ct[t-90],r32mub230down4,xsame)

for t in range(0,100):
    if t<10:
       r42230[:,t]=spline(T/ct[t],r42mub230up,xsame)
    else:
       if t>=10 and t<20:
          r42230[:,t]=spline(T/ct[t-10],r42mub230up1,xsame)
       else:
          if t>=20 and t<30:
             r42230[:,t]=spline(T/ct[t-20],r42mub230up2,xsame)
          else: 
             if t>=30 and t<40:
                r42230[:,t]=spline(T/ct[t-30],r42mub230up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42230[:,t]=spline(T/ct[t-40],r42mub230up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42230[:,t]=spline(T/ct[t-50],r42mub230down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42230[:,t]=spline(T/ct[t-60],r42mub230down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42230[:,t]=spline(T/ct[t-70],r42mub230down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42230[:,t]=spline(T/ct[t-80],r42mub230down3,xsame)
                            else:
                                r42230[:,t]=spline(T/ct[t-90],r42mub230down4,xsame)

for t in range(0,100):
    if t<10:
       r62230[:,t]=spline(T/ct[t],r62mub230up,xsame)
    else:
       if t>=10 and t<20:
          r62230[:,t]=spline(T/ct[t-10],r62mub230up1,xsame)
       else:
          if t>=20 and t<30:
             r62230[:,t]=spline(T/ct[t-20],r62mub230up2,xsame)
          else: 
             if t>=30 and t<40:
                r62230[:,t]=spline(T/ct[t-30],r62mub230up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62230[:,t]=spline(T/ct[t-40],r62mub230up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62230[:,t]=spline(T/ct[t-50],r62mub230down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62230[:,t]=spline(T/ct[t-60],r62mub230down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62230[:,t]=spline(T/ct[t-70],r62mub230down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62230[:,t]=spline(T/ct[t-80],r62mub230down3,xsame)
                            else:
                                r62230[:,t]=spline(T/ct[t-90],r62mub230down4,xsame)

for t in range(0,100):
    if t<10:
       r82230[:,t]=spline(T/ct[t],r82mub230up,xsame)
    else:
       if t>=10 and t<20:
          r82230[:,t]=spline(T/ct[t-10],r82mub230up1,xsame)
       else:
          if t>=20 and t<30:
             r82230[:,t]=spline(T/ct[t-20],r82mub230up2,xsame)
          else: 
             if t>=30 and t<40:
                r82230[:,t]=spline(T/ct[t-30],r82mub230up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82230[:,t]=spline(T/ct[t-40],r82mub230up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82230[:,t]=spline(T/ct[t-50],r82mub230down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82230[:,t]=spline(T/ct[t-60],r82mub230down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82230[:,t]=spline(T/ct[t-70],r82mub230down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82230[:,t]=spline(T/ct[t-80],r82mub230down3,xsame)
                            else:
                                r82230[:,t]=spline(T/ct[t-90],r82mub230down4,xsame)


for num in range(1,100):
    if num==1:
       max230=np.maximum(r32230[:,num-1],r32230[:,num])
       min230=np.minimum(r32230[:,num-1],r32230[:,num])
    else:
       max230=np.maximum(max230,r32230[:,num])
       min230=np.minimum(min230,r32230[:,num])

for num in range(1,100):
    if num==1:
       max42230=np.maximum(r42230[:,num-1],r42230[:,num])
       min42230=np.minimum(r42230[:,num-1],r42230[:,num])
    else:
       max42230=np.maximum(max42230,r42230[:,num])
       min42230=np.minimum(min42230,r42230[:,num])

for num in range(1,100):
    if num==1:
       max62230=np.maximum(r62230[:,num-1],r62230[:,num])
       min62230=np.minimum(r62230[:,num-1],r62230[:,num])
    else:
       max62230=np.maximum(max62230,r62230[:,num])
       min62230=np.minimum(min62230,r62230[:,num])

for num in range(1,100):
    if num==1:
       max82230=np.maximum(r82230[:,num-1],r82230[:,num])
       min82230=np.minimum(r82230[:,num-1],r82230[:,num])
    else:
       max82230=np.maximum(max82230,r82230[:,num])
       min82230=np.minimum(min82230,r82230[:,num])

r32mub230cen=spline(T/ctcen,r32mub230cen,xsame)
r42mub230cen=spline(T/ctcen,r42mub230cen,xsame)
r62mub230cen=spline(T/ctcen,r62mub230cen,xsame)
r82mub230cen=spline(T/ctcen,r82mub230cen,xsame)

dif230cen=abs(r42mub230cen-0.140553)
dif230up=abs(max42230-0.140553)
dif230down=abs(min42230-0.140553)
min230cen_index=1546#int(round(fit7[5,2]))
min230up_index=1546#int(round(fit7[5,1]))
min230down_index=1546#int(round(fit7[5,0]))
print(min230cen_index)
r32230cen=r32mub230cen[min230cen_index]
r32230hcen=r32mub230cen[Tcen[5]]
r32=[max230[min230up_index],max230[min230down_index],min230[min230up_index],min230[min230down_index]]
r32230up=np.max(r32)
r32230down=np.min(r32)

r42230cen=r42mub230cen[min230cen_index]
r62230cen=r62mub230cen[min230cen_index]
r42=[max42230[min230up_index],max42230[min230down_index],min42230[min230up_index],min42230[min230down_index]]
r42230up=np.max(r42)
r42230down=np.min(r42)

r62=[max62230[min230up_index],max62230[min230down_index],min62230[min230up_index],min62230[min230down_index]]
r62230up=np.max(r62)
r62230down=np.min(r62)

r82230cen=r82mub230cen[min230cen_index]
r82=[max82230[min230up_index],max82230[min230down_index],min82230[min230up_index],min82230[min230down_index]]
r82230up=np.max(r82)
r82230down=np.min(r82)

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
r32252=np.zeros((2991,100))
r42252=np.zeros((2991,100))
r62252=np.zeros((2991,100))
r82252=np.zeros((2991,100))
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


for t in range(0,100):
    if t<10:
       r82252[:,t]=spline(T/ct[t],r82mub252up,xsame)
    else:
       if t>=10 and t<20:
          r82252[:,t]=spline(T/ct[t-10],r82mub252up1,xsame)
       else:
          if t>=20 and t<30:
             r82252[:,t]=spline(T/ct[t-20],r82mub252up2,xsame)
          else: 
             if t>=30 and t<40:
                r82252[:,t]=spline(T/ct[t-30],r82mub252up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82252[:,t]=spline(T/ct[t-40],r82mub252up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82252[:,t]=spline(T/ct[t-50],r82mub252down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82252[:,t]=spline(T/ct[t-60],r82mub252down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82252[:,t]=spline(T/ct[t-70],r82mub252down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82252[:,t]=spline(T/ct[t-80],r82mub252down3,xsame)
                            else:
                                r82252[:,t]=spline(T/ct[t-90],r82mub252down4,xsame)


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

for num in range(1,100):
    if num==1:
       max82252=np.maximum(r82252[:,num-1],r82252[:,num])
       min82252=np.minimum(r82252[:,num-1],r82252[:,num])
    else:
       max82252=np.maximum(max82252,r82252[:,num])
       min82252=np.minimum(min82252,r82252[:,num])

r32mub252cen=spline(T/ctcen,r32mub252cen,xsame)
r42mub252cen=spline(T/ctcen,r42mub252cen,xsame)
r62mub252cen=spline(T/ctcen,r62mub252cen,xsame)
r82mub252cen=spline(T/ctcen,r82mub252cen,xsame)

dif252cen=abs(r42mub252cen-1.468760)
dif252up=abs(max42252-1.468760)
dif252down=abs(min42252-1.468760)
min252cen_index=1531#int(round(fit7[6,2]))
min252up_index=1531#int(round(fit7[6,1]))
min252down_index=1531#int(round(fit7[6,0]))
print(min252cen_index)
#print(min252up_index)
#print(min252down_index)
r32252cen=r32mub252cen[min252cen_index]
#r32252hcen=r32mub252cen[min252cen_index+int(min252cen_index*deltat)]
r32252hcen=r32mub252cen[Tcen[6]]
r32=[max252[min252up_index],max252[min252down_index],min252[min252up_index],min252[min252down_index]]
#r32h=[max252[min252up_index+int(min252up_index*deltat)],max252[min252down_index+int(min252down_index*deltat)],min252[min252up_index+int(min252up_index*deltat)],min252[min252down_index+int(min252down_index*deltat)]]
r32h=[max252[Tcup[6]],max252[Tcdown[6]],min252[Tcup[6]],min252[Tcdown[6]]]
r32252up=np.max(r32)
r32252down=np.min(r32)
r32252uph=np.max(r32h)
r32252downh=np.min(r32h)

r42252cen=r42mub252cen[min252cen_index]
r62252cen=r62mub252cen[min252cen_index]
#r42252hcen=r42mub252cen[min252cen_index+int(min252cen_index*deltat)]
#r62252hcen=r62mub252cen[min252cen_index+int(min252cen_index*deltat)]
r42252hcen=r42mub252cen[Tcen[6]]
r62252hcen=r62mub252cen[Tcen[6]]
r42=[max42252[min252up_index],max42252[min252down_index],min42252[min252up_index],min42252[min252down_index]]
#r42h=[max42252[min252up_index+int(min252up_index*deltat)],max42252[min252down_index+int(min252down_index*deltat)],min42252[min252up_index+int(min252up_index*deltat)],min42252[min252down_index+int(min252down_index*deltat)]]
r42h=[max42252[Tcup[6]],max42252[Tcdown[6]],min42252[Tcup[6]],min42252[Tcdown[6]]]
r42252up=np.max(r42)
r42252down=np.min(r42)
r42252uph=np.max(r42h)
r42252downh=np.min(r42h)

r62=[max62252[min252up_index],max62252[min252down_index],min62252[min252up_index],min62252[min252down_index]]
#r62h=[max62252[min252up_index+int(min252up_index*deltat)],max62252[min252down_index+int(min252down_index*deltat)],min62252[min252up_index+int(min252up_index*deltat)],min62252[min252down_index+int(min252down_index*deltat)]]
r62h=[max62252[Tcup[6]],max62252[Tcdown[6]],min62252[Tcup[6]],min62252[Tcdown[6]]]
r62252up=np.max(r62)
r62252down=np.min(r62)
r62252uph=np.max(r62h)
r62252downh=np.min(r62h)

r82252cen=r82mub252cen[min252cen_index]
#r82252hcen=r82mub252cen[min252cen_index+int(min252cen_index*deltat)]
r82252hcen=r82mub252cen[Tcen[6]]
r82=[max82252[min252up_index],max82252[min252down_index],min82252[min252up_index],min82252[min252down_index]]
#r82h=[max82252[min252up_index+int(min252up_index*deltat)],max82252[min252down_index+int(min252down_index*deltat)],min82252[min252up_index+int(min252up_index*deltat)],min82252[min252down_index+int(min252down_index*deltat)]]
r82h=[max82252[Tcup[6]],max82252[Tcdown[6]],min82252[Tcup[6]],min82252[Tcdown[6]]]
r82252up=np.max(r82)
r82252down=np.min(r82)
r82252uph=np.max(r82h)
r82252downh=np.min(r82h)
####################################################################################################
chi2mub265cen=np.loadtxt(r'./addition/mub265/cmucen/final/buffer/chi2.dat')
chi3mub265cen=np.loadtxt(r'./addition/mub265/cmucen/final/buffer/chi3.dat')
chi4mub265cen=np.loadtxt(r'./addition/mub265/cmucen/final/buffer/chi4.dat')
chi6mub265cen=np.loadtxt(r'./addition/mub265/cmucen/final/buffer/chi6.dat')
chi8mub265cen=np.loadtxt(r'./addition/mub265/cmucen/final/buffer/chi8.dat')
r32mub265cen=chi3mub265cen/chi2mub265cen
r42mub265cen=chi4mub265cen/chi2mub265cen
r62mub265cen=chi6mub265cen/chi2mub265cen
r82mub265cen=chi8mub265cen/chi2mub265cen
chi2mub265up=np.loadtxt(r'./addition/mub265/cmuup/final/buffer/chi2.dat')
chi3mub265up=np.loadtxt(r'./addition/mub265/cmuup/final/buffer/chi3.dat')
chi4mub265up=np.loadtxt(r'./addition/mub265/cmuup/final/buffer/chi4.dat')
chi6mub265up=np.loadtxt(r'./addition/mub265/cmuup/final/buffer/chi6.dat')
chi8mub265up=np.loadtxt(r'./addition/mub265/cmuup/final/buffer/chi8.dat')
r32mub265up=chi3mub265up/chi2mub265up
r42mub265up=chi4mub265up/chi2mub265up
r62mub265up=chi6mub265up/chi2mub265up
r82mub265up=chi8mub265up/chi2mub265up
chi2mub265up1=np.loadtxt(r'./addition/mub265/cmuup1/final/buffer/chi2.dat')
chi3mub265up1=np.loadtxt(r'./addition/mub265/cmuup1/final/buffer/chi3.dat')
chi4mub265up1=np.loadtxt(r'./addition/mub265/cmuup1/final/buffer/chi4.dat')
chi6mub265up1=np.loadtxt(r'./addition/mub265/cmuup1/final/buffer/chi6.dat')
chi8mub265up1=np.loadtxt(r'./addition/mub265/cmuup1/final/buffer/chi8.dat')
r32mub265up1=chi3mub265up1/chi2mub265up1
r42mub265up1=chi4mub265up1/chi2mub265up1
r62mub265up1=chi6mub265up1/chi2mub265up1
r82mub265up1=chi8mub265up1/chi2mub265up1
chi2mub265up2=np.loadtxt(r'./addition/mub265/cmuup2/final/buffer/chi2.dat')
chi3mub265up2=np.loadtxt(r'./addition/mub265/cmuup2/final/buffer/chi3.dat')
chi4mub265up2=np.loadtxt(r'./addition/mub265/cmuup2/final/buffer/chi4.dat')
chi6mub265up2=np.loadtxt(r'./addition/mub265/cmuup2/final/buffer/chi6.dat')
chi8mub265up2=np.loadtxt(r'./addition/mub265/cmuup2/final/buffer/chi8.dat')
r32mub265up2=chi3mub265up2/chi2mub265up2
r42mub265up2=chi4mub265up2/chi2mub265up2
r62mub265up2=chi6mub265up2/chi2mub265up2
r82mub265up2=chi8mub265up2/chi2mub265up2
chi2mub265up3=np.loadtxt(r'./addition/mub265/cmuup3/final/buffer/chi2.dat')
chi3mub265up3=np.loadtxt(r'./addition/mub265/cmuup3/final/buffer/chi3.dat')
chi4mub265up3=np.loadtxt(r'./addition/mub265/cmuup3/final/buffer/chi4.dat')
chi6mub265up3=np.loadtxt(r'./addition/mub265/cmuup3/final/buffer/chi6.dat')
chi8mub265up3=np.loadtxt(r'./addition/mub265/cmuup3/final/buffer/chi8.dat')
r32mub265up3=chi3mub265up3/chi2mub265up3
r42mub265up3=chi4mub265up3/chi2mub265up3
r62mub265up3=chi6mub265up3/chi2mub265up3
r82mub265up3=chi8mub265up3/chi2mub265up3
chi2mub265up4=np.loadtxt(r'./addition/mub265/cmuup4/final/buffer/chi2.dat')
chi3mub265up4=np.loadtxt(r'./addition/mub265/cmuup4/final/buffer/chi3.dat')
chi4mub265up4=np.loadtxt(r'./addition/mub265/cmuup4/final/buffer/chi4.dat')
chi6mub265up4=np.loadtxt(r'./addition/mub265/cmuup4/final/buffer/chi6.dat')
chi8mub265up4=np.loadtxt(r'./addition/mub265/cmuup4/final/buffer/chi8.dat')
r32mub265up4=chi3mub265up4/chi2mub265up4
r42mub265up4=chi4mub265up4/chi2mub265up4
r62mub265up4=chi6mub265up4/chi2mub265up4
r82mub265up4=chi8mub265up4/chi2mub265up4
chi2mub265down=np.loadtxt(r'./addition/mub265/cmudown/final/buffer/chi2.dat')
chi3mub265down=np.loadtxt(r'./addition/mub265/cmudown/final/buffer/chi3.dat')
chi4mub265down=np.loadtxt(r'./addition/mub265/cmudown/final/buffer/chi4.dat')
chi6mub265down=np.loadtxt(r'./addition/mub265/cmudown/final/buffer/chi6.dat')
chi8mub265down=np.loadtxt(r'./addition/mub265/cmudown/final/buffer/chi8.dat')
r32mub265down=chi3mub265down/chi2mub265down
r42mub265down=chi4mub265down/chi2mub265down
r62mub265down=chi6mub265down/chi2mub265down
r82mub265down=chi8mub265down/chi2mub265down
chi2mub265down1=np.loadtxt(r'./addition/mub265/cmudown1/final/buffer/chi2.dat')
chi3mub265down1=np.loadtxt(r'./addition/mub265/cmudown1/final/buffer/chi3.dat')
chi4mub265down1=np.loadtxt(r'./addition/mub265/cmudown1/final/buffer/chi4.dat')
chi6mub265down1=np.loadtxt(r'./addition/mub265/cmudown1/final/buffer/chi6.dat')
chi8mub265down1=np.loadtxt(r'./addition/mub265/cmudown1/final/buffer/chi8.dat')
r32mub265down1=chi3mub265down1/chi2mub265down1
r42mub265down1=chi4mub265down1/chi2mub265down1
r62mub265down1=chi6mub265down1/chi2mub265down1
r82mub265down1=chi8mub265down1/chi2mub265down1
chi2mub265down2=np.loadtxt(r'./addition/mub265/cmudown2/final/buffer/chi2.dat')
chi3mub265down2=np.loadtxt(r'./addition/mub265/cmudown2/final/buffer/chi3.dat')
chi4mub265down2=np.loadtxt(r'./addition/mub265/cmudown2/final/buffer/chi4.dat')
chi6mub265down2=np.loadtxt(r'./addition/mub265/cmudown2/final/buffer/chi6.dat')
chi8mub265down2=np.loadtxt(r'./addition/mub265/cmudown2/final/buffer/chi8.dat')
r32mub265down2=chi3mub265down2/chi2mub265down2
r42mub265down2=chi4mub265down2/chi2mub265down2
r62mub265down2=chi6mub265down2/chi2mub265down2
r82mub265down2=chi8mub265down2/chi2mub265down2
chi2mub265down3=np.loadtxt(r'./addition/mub265/cmudown3/final/buffer/chi2.dat')
chi3mub265down3=np.loadtxt(r'./addition/mub265/cmudown3/final/buffer/chi3.dat')
chi4mub265down3=np.loadtxt(r'./addition/mub265/cmudown3/final/buffer/chi4.dat')
chi6mub265down3=np.loadtxt(r'./addition/mub265/cmudown3/final/buffer/chi6.dat')
chi8mub265down3=np.loadtxt(r'./addition/mub265/cmudown3/final/buffer/chi8.dat')
r32mub265down3=chi3mub265down3/chi2mub265down3
r42mub265down3=chi4mub265down3/chi2mub265down3
r62mub265down3=chi6mub265down3/chi2mub265down3
r82mub265down3=chi8mub265down3/chi2mub265down3
chi2mub265down4=np.loadtxt(r'./addition/mub265/cmudown4/final/buffer/chi2.dat')
chi3mub265down4=np.loadtxt(r'./addition/mub265/cmudown4/final/buffer/chi3.dat')
chi4mub265down4=np.loadtxt(r'./addition/mub265/cmudown4/final/buffer/chi4.dat')
chi6mub265down4=np.loadtxt(r'./addition/mub265/cmudown4/final/buffer/chi6.dat')
chi8mub265down4=np.loadtxt(r'./addition/mub265/cmudown4/final/buffer/chi8.dat')
r32mub265down4=chi3mub265down4/chi2mub265down4
r42mub265down4=chi4mub265down4/chi2mub265down4
r62mub265down4=chi6mub265down4/chi2mub265down4
r82mub265down4=chi8mub265down4/chi2mub265down4
r32265=np.zeros((2991,100))
r42265=np.zeros((2991,100))
r62265=np.zeros((2991,100))
r82265=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32265[:,t]=spline(T/ct[t],r32mub265up,xsame)
    else:
       if t>=10 and t<20:
          r32265[:,t]=spline(T/ct[t-10],r32mub265up1,xsame)
       else:
          if t>=20 and t<30:
             r32265[:,t]=spline(T/ct[t-20],r32mub265up2,xsame)
          else: 
             if t>=30 and t<40:
                r32265[:,t]=spline(T/ct[t-30],r32mub265up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32265[:,t]=spline(T/ct[t-40],r32mub265up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32265[:,t]=spline(T/ct[t-50],r32mub265down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32265[:,t]=spline(T/ct[t-60],r32mub265down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32265[:,t]=spline(T/ct[t-70],r32mub265down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32265[:,t]=spline(T/ct[t-80],r32mub265down3,xsame)
                            else:
                                r32265[:,t]=spline(T/ct[t-90],r32mub265down4,xsame)

for t in range(0,100):
    if t<10:
       r42265[:,t]=spline(T/ct[t],r42mub265up,xsame)
    else:
       if t>=10 and t<20:
          r42265[:,t]=spline(T/ct[t-10],r42mub265up1,xsame)
       else:
          if t>=20 and t<30:
             r42265[:,t]=spline(T/ct[t-20],r42mub265up2,xsame)
          else: 
             if t>=30 and t<40:
                r42265[:,t]=spline(T/ct[t-30],r42mub265up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42265[:,t]=spline(T/ct[t-40],r42mub265up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42265[:,t]=spline(T/ct[t-50],r42mub265down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42265[:,t]=spline(T/ct[t-60],r42mub265down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42265[:,t]=spline(T/ct[t-70],r42mub265down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42265[:,t]=spline(T/ct[t-80],r42mub265down3,xsame)
                            else:
                                r42265[:,t]=spline(T/ct[t-90],r42mub265down4,xsame)

for t in range(0,100):
    if t<10:
       r62265[:,t]=spline(T/ct[t],r62mub265up,xsame)
    else:
       if t>=10 and t<20:
          r62265[:,t]=spline(T/ct[t-10],r62mub265up1,xsame)
       else:
          if t>=20 and t<30:
             r62265[:,t]=spline(T/ct[t-20],r62mub265up2,xsame)
          else: 
             if t>=30 and t<40:
                r62265[:,t]=spline(T/ct[t-30],r62mub265up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62265[:,t]=spline(T/ct[t-40],r62mub265up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62265[:,t]=spline(T/ct[t-50],r62mub265down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62265[:,t]=spline(T/ct[t-60],r62mub265down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62265[:,t]=spline(T/ct[t-70],r62mub265down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62265[:,t]=spline(T/ct[t-80],r62mub265down3,xsame)
                            else:
                                r62265[:,t]=spline(T/ct[t-90],r62mub265down4,xsame)

for t in range(0,100):
    if t<10:
       r82265[:,t]=spline(T/ct[t],r82mub265up,xsame)
    else:
       if t>=10 and t<20:
          r82265[:,t]=spline(T/ct[t-10],r82mub265up1,xsame)
       else:
          if t>=20 and t<30:
             r82265[:,t]=spline(T/ct[t-20],r82mub265up2,xsame)
          else: 
             if t>=30 and t<40:
                r82265[:,t]=spline(T/ct[t-30],r82mub265up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82265[:,t]=spline(T/ct[t-40],r82mub265up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82265[:,t]=spline(T/ct[t-50],r82mub265down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82265[:,t]=spline(T/ct[t-60],r82mub265down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82265[:,t]=spline(T/ct[t-70],r82mub265down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82265[:,t]=spline(T/ct[t-80],r82mub265down3,xsame)
                            else:
                                r82265[:,t]=spline(T/ct[t-90],r82mub265down4,xsame)


for num in range(1,100):
    if num==1:
       max265=np.maximum(r32265[:,num-1],r32265[:,num])
       min265=np.minimum(r32265[:,num-1],r32265[:,num])
    else:
       max265=np.maximum(max265,r32265[:,num])
       min265=np.minimum(min265,r32265[:,num])

for num in range(1,100):
    if num==1:
       max42265=np.maximum(r42265[:,num-1],r42265[:,num])
       min42265=np.minimum(r42265[:,num-1],r42265[:,num])
    else:
       max42265=np.maximum(max42265,r42265[:,num])
       min42265=np.minimum(min42265,r42265[:,num])

for num in range(1,100):
    if num==1:
       max62265=np.maximum(r62265[:,num-1],r62265[:,num])
       min62265=np.minimum(r62265[:,num-1],r62265[:,num])
    else:
       max62265=np.maximum(max62265,r62265[:,num])
       min62265=np.minimum(min62265,r62265[:,num])

for num in range(1,100):
    if num==1:
       max82265=np.maximum(r82265[:,num-1],r82265[:,num])
       min82265=np.minimum(r82265[:,num-1],r82265[:,num])
    else:
       max82265=np.maximum(max82265,r82265[:,num])
       min82265=np.minimum(min82265,r82265[:,num])

r32mub265cen=spline(T/ctcen,r32mub265cen,xsame)
r42mub265cen=spline(T/ctcen,r42mub265cen,xsame)
r62mub265cen=spline(T/ctcen,r62mub265cen,xsame)
r82mub265cen=spline(T/ctcen,r82mub265cen,xsame)

dif265cen=abs(r42mub265cen-0.140553)
dif265up=abs(max42265-0.140553)
dif265down=abs(min42265-0.140553)
min265cen_index=1521#int(round(fit7[5,2]))
min265up_index=1521#int(round(fit7[5,1]))
min265down_index=1521#int(round(fit7[5,0]))
print(min265cen_index)
r32265cen=r32mub265cen[min265cen_index]
r32265hcen=r32mub265cen[Tcen[5]]
r32=[max265[min265up_index],max265[min265down_index],min265[min265up_index],min265[min265down_index]]
r32265up=np.max(r32)
r32265down=np.min(r32)

r42265cen=r42mub265cen[min265cen_index]
r62265cen=r62mub265cen[min265cen_index]
r42=[max42265[min265up_index],max42265[min265down_index],min42265[min265up_index],min42265[min265down_index]]
r42265up=np.max(r42)
r42265down=np.min(r42)

r62=[max62265[min265up_index],max62265[min265down_index],min62265[min265up_index],min62265[min265down_index]]
r62265up=np.max(r62)
r62265down=np.min(r62)

r82265cen=r82mub265cen[min265cen_index]
r82=[max82265[min265up_index],max82265[min265down_index],min82265[min265up_index],min82265[min265down_index]]
r82265up=np.max(r82)
r82265down=np.min(r82)
####################################################################################################
chi2mub280cen=np.loadtxt(r'./addition/mub280/cmucen/final/buffer/chi2.dat')
chi3mub280cen=np.loadtxt(r'./addition/mub280/cmucen/final/buffer/chi3.dat')
chi4mub280cen=np.loadtxt(r'./addition/mub280/cmucen/final/buffer/chi4.dat')
chi6mub280cen=np.loadtxt(r'./addition/mub280/cmucen/final/buffer/chi6.dat')
chi8mub280cen=np.loadtxt(r'./addition/mub280/cmucen/final/buffer/chi8.dat')
r32mub280cen=chi3mub280cen/chi2mub280cen
r42mub280cen=chi4mub280cen/chi2mub280cen
r62mub280cen=chi6mub280cen/chi2mub280cen
r82mub280cen=chi8mub280cen/chi2mub280cen
chi2mub280up=np.loadtxt(r'./addition/mub280/cmuup/final/buffer/chi2.dat')
chi3mub280up=np.loadtxt(r'./addition/mub280/cmuup/final/buffer/chi3.dat')
chi4mub280up=np.loadtxt(r'./addition/mub280/cmuup/final/buffer/chi4.dat')
chi6mub280up=np.loadtxt(r'./addition/mub280/cmuup/final/buffer/chi6.dat')
chi8mub280up=np.loadtxt(r'./addition/mub280/cmuup/final/buffer/chi8.dat')
r32mub280up=chi3mub280up/chi2mub280up
r42mub280up=chi4mub280up/chi2mub280up
r62mub280up=chi6mub280up/chi2mub280up
r82mub280up=chi8mub280up/chi2mub280up
chi2mub280up1=np.loadtxt(r'./addition/mub280/cmuup1/final/buffer/chi2.dat')
chi3mub280up1=np.loadtxt(r'./addition/mub280/cmuup1/final/buffer/chi3.dat')
chi4mub280up1=np.loadtxt(r'./addition/mub280/cmuup1/final/buffer/chi4.dat')
chi6mub280up1=np.loadtxt(r'./addition/mub280/cmuup1/final/buffer/chi6.dat')
chi8mub280up1=np.loadtxt(r'./addition/mub280/cmuup1/final/buffer/chi8.dat')
r32mub280up1=chi3mub280up1/chi2mub280up1
r42mub280up1=chi4mub280up1/chi2mub280up1
r62mub280up1=chi6mub280up1/chi2mub280up1
r82mub280up1=chi8mub280up1/chi2mub280up1
chi2mub280up2=np.loadtxt(r'./addition/mub280/cmuup2/final/buffer/chi2.dat')
chi3mub280up2=np.loadtxt(r'./addition/mub280/cmuup2/final/buffer/chi3.dat')
chi4mub280up2=np.loadtxt(r'./addition/mub280/cmuup2/final/buffer/chi4.dat')
chi6mub280up2=np.loadtxt(r'./addition/mub280/cmuup2/final/buffer/chi6.dat')
chi8mub280up2=np.loadtxt(r'./addition/mub280/cmuup2/final/buffer/chi8.dat')
r32mub280up2=chi3mub280up2/chi2mub280up2
r42mub280up2=chi4mub280up2/chi2mub280up2
r62mub280up2=chi6mub280up2/chi2mub280up2
r82mub280up2=chi8mub280up2/chi2mub280up2
chi2mub280up3=np.loadtxt(r'./addition/mub280/cmuup3/final/buffer/chi2.dat')
chi3mub280up3=np.loadtxt(r'./addition/mub280/cmuup3/final/buffer/chi3.dat')
chi4mub280up3=np.loadtxt(r'./addition/mub280/cmuup3/final/buffer/chi4.dat')
chi6mub280up3=np.loadtxt(r'./addition/mub280/cmuup3/final/buffer/chi6.dat')
chi8mub280up3=np.loadtxt(r'./addition/mub280/cmuup3/final/buffer/chi8.dat')
r32mub280up3=chi3mub280up3/chi2mub280up3
r42mub280up3=chi4mub280up3/chi2mub280up3
r62mub280up3=chi6mub280up3/chi2mub280up3
r82mub280up3=chi8mub280up3/chi2mub280up3
chi2mub280up4=np.loadtxt(r'./addition/mub280/cmuup4/final/buffer/chi2.dat')
chi3mub280up4=np.loadtxt(r'./addition/mub280/cmuup4/final/buffer/chi3.dat')
chi4mub280up4=np.loadtxt(r'./addition/mub280/cmuup4/final/buffer/chi4.dat')
chi6mub280up4=np.loadtxt(r'./addition/mub280/cmuup4/final/buffer/chi6.dat')
chi8mub280up4=np.loadtxt(r'./addition/mub280/cmuup4/final/buffer/chi8.dat')
r32mub280up4=chi3mub280up4/chi2mub280up4
r42mub280up4=chi4mub280up4/chi2mub280up4
r62mub280up4=chi6mub280up4/chi2mub280up4
r82mub280up4=chi8mub280up4/chi2mub280up4
chi2mub280down=np.loadtxt(r'./addition/mub280/cmudown/final/buffer/chi2.dat')
chi3mub280down=np.loadtxt(r'./addition/mub280/cmudown/final/buffer/chi3.dat')
chi4mub280down=np.loadtxt(r'./addition/mub280/cmudown/final/buffer/chi4.dat')
chi6mub280down=np.loadtxt(r'./addition/mub280/cmudown/final/buffer/chi6.dat')
chi8mub280down=np.loadtxt(r'./addition/mub280/cmudown/final/buffer/chi8.dat')
r32mub280down=chi3mub280down/chi2mub280down
r42mub280down=chi4mub280down/chi2mub280down
r62mub280down=chi6mub280down/chi2mub280down
r82mub280down=chi8mub280down/chi2mub280down
chi2mub280down1=np.loadtxt(r'./addition/mub280/cmudown1/final/buffer/chi2.dat')
chi3mub280down1=np.loadtxt(r'./addition/mub280/cmudown1/final/buffer/chi3.dat')
chi4mub280down1=np.loadtxt(r'./addition/mub280/cmudown1/final/buffer/chi4.dat')
chi6mub280down1=np.loadtxt(r'./addition/mub280/cmudown1/final/buffer/chi6.dat')
chi8mub280down1=np.loadtxt(r'./addition/mub280/cmudown1/final/buffer/chi8.dat')
r32mub280down1=chi3mub280down1/chi2mub280down1
r42mub280down1=chi4mub280down1/chi2mub280down1
r62mub280down1=chi6mub280down1/chi2mub280down1
r82mub280down1=chi8mub280down1/chi2mub280down1
chi2mub280down2=np.loadtxt(r'./addition/mub280/cmudown2/final/buffer/chi2.dat')
chi3mub280down2=np.loadtxt(r'./addition/mub280/cmudown2/final/buffer/chi3.dat')
chi4mub280down2=np.loadtxt(r'./addition/mub280/cmudown2/final/buffer/chi4.dat')
chi6mub280down2=np.loadtxt(r'./addition/mub280/cmudown2/final/buffer/chi6.dat')
chi8mub280down2=np.loadtxt(r'./addition/mub280/cmudown2/final/buffer/chi8.dat')
r32mub280down2=chi3mub280down2/chi2mub280down2
r42mub280down2=chi4mub280down2/chi2mub280down2
r62mub280down2=chi6mub280down2/chi2mub280down2
r82mub280down2=chi8mub280down2/chi2mub280down2
chi2mub280down3=np.loadtxt(r'./addition/mub280/cmudown3/final/buffer/chi2.dat')
chi3mub280down3=np.loadtxt(r'./addition/mub280/cmudown3/final/buffer/chi3.dat')
chi4mub280down3=np.loadtxt(r'./addition/mub280/cmudown3/final/buffer/chi4.dat')
chi6mub280down3=np.loadtxt(r'./addition/mub280/cmudown3/final/buffer/chi6.dat')
chi8mub280down3=np.loadtxt(r'./addition/mub280/cmudown3/final/buffer/chi8.dat')
r32mub280down3=chi3mub280down3/chi2mub280down3
r42mub280down3=chi4mub280down3/chi2mub280down3
r62mub280down3=chi6mub280down3/chi2mub280down3
r82mub280down3=chi8mub280down3/chi2mub280down3
chi2mub280down4=np.loadtxt(r'./addition/mub280/cmudown4/final/buffer/chi2.dat')
chi3mub280down4=np.loadtxt(r'./addition/mub280/cmudown4/final/buffer/chi3.dat')
chi4mub280down4=np.loadtxt(r'./addition/mub280/cmudown4/final/buffer/chi4.dat')
chi6mub280down4=np.loadtxt(r'./addition/mub280/cmudown4/final/buffer/chi6.dat')
chi8mub280down4=np.loadtxt(r'./addition/mub280/cmudown4/final/buffer/chi8.dat')
r32mub280down4=chi3mub280down4/chi2mub280down4
r42mub280down4=chi4mub280down4/chi2mub280down4
r62mub280down4=chi6mub280down4/chi2mub280down4
r82mub280down4=chi8mub280down4/chi2mub280down4
r32280=np.zeros((2991,100))
r42280=np.zeros((2991,100))
r62280=np.zeros((2991,100))
r82280=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32280[:,t]=spline(T/ct[t],r32mub280up,xsame)
    else:
       if t>=10 and t<20:
          r32280[:,t]=spline(T/ct[t-10],r32mub280up1,xsame)
       else:
          if t>=20 and t<30:
             r32280[:,t]=spline(T/ct[t-20],r32mub280up2,xsame)
          else: 
             if t>=30 and t<40:
                r32280[:,t]=spline(T/ct[t-30],r32mub280up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32280[:,t]=spline(T/ct[t-40],r32mub280up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32280[:,t]=spline(T/ct[t-50],r32mub280down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32280[:,t]=spline(T/ct[t-60],r32mub280down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32280[:,t]=spline(T/ct[t-70],r32mub280down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32280[:,t]=spline(T/ct[t-80],r32mub280down3,xsame)
                            else:
                                r32280[:,t]=spline(T/ct[t-90],r32mub280down4,xsame)

for t in range(0,100):
    if t<10:
       r42280[:,t]=spline(T/ct[t],r42mub280up,xsame)
    else:
       if t>=10 and t<20:
          r42280[:,t]=spline(T/ct[t-10],r42mub280up1,xsame)
       else:
          if t>=20 and t<30:
             r42280[:,t]=spline(T/ct[t-20],r42mub280up2,xsame)
          else: 
             if t>=30 and t<40:
                r42280[:,t]=spline(T/ct[t-30],r42mub280up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42280[:,t]=spline(T/ct[t-40],r42mub280up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42280[:,t]=spline(T/ct[t-50],r42mub280down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42280[:,t]=spline(T/ct[t-60],r42mub280down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42280[:,t]=spline(T/ct[t-70],r42mub280down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42280[:,t]=spline(T/ct[t-80],r42mub280down3,xsame)
                            else:
                                r42280[:,t]=spline(T/ct[t-90],r42mub280down4,xsame)

for t in range(0,100):
    if t<10:
       r62280[:,t]=spline(T/ct[t],r62mub280up,xsame)
    else:
       if t>=10 and t<20:
          r62280[:,t]=spline(T/ct[t-10],r62mub280up1,xsame)
       else:
          if t>=20 and t<30:
             r62280[:,t]=spline(T/ct[t-20],r62mub280up2,xsame)
          else: 
             if t>=30 and t<40:
                r62280[:,t]=spline(T/ct[t-30],r62mub280up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62280[:,t]=spline(T/ct[t-40],r62mub280up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62280[:,t]=spline(T/ct[t-50],r62mub280down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62280[:,t]=spline(T/ct[t-60],r62mub280down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62280[:,t]=spline(T/ct[t-70],r62mub280down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62280[:,t]=spline(T/ct[t-80],r62mub280down3,xsame)
                            else:
                                r62280[:,t]=spline(T/ct[t-90],r62mub280down4,xsame)

for t in range(0,100):
    if t<10:
       r82280[:,t]=spline(T/ct[t],r82mub280up,xsame)
    else:
       if t>=10 and t<20:
          r82280[:,t]=spline(T/ct[t-10],r82mub280up1,xsame)
       else:
          if t>=20 and t<30:
             r82280[:,t]=spline(T/ct[t-20],r82mub280up2,xsame)
          else: 
             if t>=30 and t<40:
                r82280[:,t]=spline(T/ct[t-30],r82mub280up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82280[:,t]=spline(T/ct[t-40],r82mub280up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82280[:,t]=spline(T/ct[t-50],r82mub280down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82280[:,t]=spline(T/ct[t-60],r82mub280down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82280[:,t]=spline(T/ct[t-70],r82mub280down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82280[:,t]=spline(T/ct[t-80],r82mub280down3,xsame)
                            else:
                                r82280[:,t]=spline(T/ct[t-90],r82mub280down4,xsame)


for num in range(1,100):
    if num==1:
       max280=np.maximum(r32280[:,num-1],r32280[:,num])
       min280=np.minimum(r32280[:,num-1],r32280[:,num])
    else:
       max280=np.maximum(max280,r32280[:,num])
       min280=np.minimum(min280,r32280[:,num])

for num in range(1,100):
    if num==1:
       max42280=np.maximum(r42280[:,num-1],r42280[:,num])
       min42280=np.minimum(r42280[:,num-1],r42280[:,num])
    else:
       max42280=np.maximum(max42280,r42280[:,num])
       min42280=np.minimum(min42280,r42280[:,num])

for num in range(1,100):
    if num==1:
       max62280=np.maximum(r62280[:,num-1],r62280[:,num])
       min62280=np.minimum(r62280[:,num-1],r62280[:,num])
    else:
       max62280=np.maximum(max62280,r62280[:,num])
       min62280=np.minimum(min62280,r62280[:,num])

for num in range(1,100):
    if num==1:
       max82280=np.maximum(r82280[:,num-1],r82280[:,num])
       min82280=np.minimum(r82280[:,num-1],r82280[:,num])
    else:
       max82280=np.maximum(max82280,r82280[:,num])
       min82280=np.minimum(min82280,r82280[:,num])

r32mub280cen=spline(T/ctcen,r32mub280cen,xsame)
r42mub280cen=spline(T/ctcen,r42mub280cen,xsame)
r62mub280cen=spline(T/ctcen,r62mub280cen,xsame)
r82mub280cen=spline(T/ctcen,r82mub280cen,xsame)

dif280cen=abs(r42mub280cen-0.140553)
dif280up=abs(max42280-0.140553)
dif280down=abs(min42280-0.140553)
min280cen_index=1509#int(round(fit7[5,2]))
min280up_index=1509#int(round(fit7[5,1]))
min280down_index=1509#int(round(fit7[5,0]))
print(min280cen_index)
r32280cen=r32mub280cen[min280cen_index]
r32280hcen=r32mub280cen[Tcen[5]]
r32=[max280[min280up_index],max280[min280down_index],min280[min280up_index],min280[min280down_index]]
r32280up=np.max(r32)
r32280down=np.min(r32)

r42280cen=r42mub280cen[min280cen_index]
r62280cen=r62mub280cen[min280cen_index]
r42=[max42280[min280up_index],max42280[min280down_index],min42280[min280up_index],min42280[min280down_index]]
r42280up=np.max(r42)
r42280down=np.min(r42)

r62=[max62280[min280up_index],max62280[min280down_index],min62280[min280up_index],min62280[min280down_index]]
r62280up=np.max(r62)
r62280down=np.min(r62)

r82280cen=r82mub280cen[min280cen_index]
r82=[max82280[min280up_index],max82280[min280down_index],min82280[min280up_index],min82280[min280down_index]]
r82280up=np.max(r82)
r82280down=np.min(r82)

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
r32303=np.zeros((2991,100))
r42303=np.zeros((2991,100))
r62303=np.zeros((2991,100))
r82303=np.zeros((2991,100))
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

for t in range(0,100):
    if t<10:
       r82303[:,t]=spline(T/ct[t],r82mub303up,xsame)
    else:
       if t>=10 and t<20:
          r82303[:,t]=spline(T/ct[t-10],r82mub303up1,xsame)
       else:
          if t>=20 and t<30:
             r82303[:,t]=spline(T/ct[t-20],r82mub303up2,xsame)
          else: 
             if t>=30 and t<40:
                r82303[:,t]=spline(T/ct[t-30],r82mub303up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82303[:,t]=spline(T/ct[t-40],r82mub303up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82303[:,t]=spline(T/ct[t-50],r82mub303down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82303[:,t]=spline(T/ct[t-60],r82mub303down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82303[:,t]=spline(T/ct[t-70],r82mub303down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82303[:,t]=spline(T/ct[t-80],r82mub303down3,xsame)
                            else:
                                r82303[:,t]=spline(T/ct[t-90],r82mub303down4,xsame)


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

for num in range(1,100):
    if num==1:
       max82303=np.maximum(r82303[:,num-1],r82303[:,num])
       min82303=np.minimum(r82303[:,num-1],r82303[:,num])
    else:
       max82303=np.maximum(max82303,r82303[:,num])
       min82303=np.minimum(min82303,r82303[:,num])

r32mub303cen=spline(T/ctcen,r32mub303cen,xsame)
r42mub303cen=spline(T/ctcen,r42mub303cen,xsame)
r62mub303cen=spline(T/ctcen,r62mub303cen,xsame)
r82mub303cen=spline(T/ctcen,r82mub303cen,xsame)

dif303cen=abs(r42mub303cen-0.695796)
dif303up=abs(max42303-0.695796)
dif303down=abs(min42303-0.695796)
min303cen_index=1487#int(round(fit7[7,2]))
min303up_index=1487#int(round(fit7[7,1]))
min303down_index=1487#int(round(fit7[7,0]))
print(min303cen_index)
#print(min303up_index)
#print(min303down_index)
r32303cen=r32mub303cen[min303cen_index]
#r32303hcen=r32mub303cen[min303cen_index+int(min303cen_index*deltat)]
r32303hcen=r32mub303cen[Tcen[7]]
r32=[max303[min303up_index],max303[min303down_index],min303[min303up_index],min303[min303down_index]]
#r32h=[max303[min303up_index+int(min303up_index*deltat)],max303[min303down_index+int(min303down_index*deltat)],min303[min303up_index+int(min303up_index*deltat)],min303[min303down_index+int(min303down_index*deltat)]]
r32h=[max303[Tcup[7]],max303[Tcdown[7]],min303[Tcup[7]],min303[Tcdown[7]]]
r32303up=np.max(r32)
r32303down=np.min(r32)
r32303uph=np.max(r32h)
r32303downh=np.min(r32h)

r42303cen=r42mub303cen[min303cen_index]
r62303cen=r62mub303cen[min303cen_index]
#r42303hcen=r42mub303cen[min303cen_index+int(min303cen_index*deltat)]
#r62303hcen=r62mub303cen[min303cen_index+int(min303cen_index*deltat)]
r42303hcen=r42mub303cen[Tcen[7]]
r62303hcen=r62mub303cen[Tcen[7]]
r42=[max42303[min303up_index],max42303[min303down_index],min42303[min303up_index],min42303[min303down_index]]
#r42h=[max42303[min303up_index+int(min303up_index*deltat)],max42303[min303down_index+int(min303down_index*deltat)],min42303[min303up_index+int(min303up_index*deltat)],min42303[min303down_index+int(min303down_index*deltat)]]
r42h=[max42303[Tcup[7]],max42303[Tcdown[7]],min42303[Tcup[7]],min42303[Tcdown[7]]]
r42303up=np.max(r42)
r42303down=np.min(r42)
r42303uph=np.max(r42h)
r42303downh=np.min(r42h)

r62=[max62303[min303up_index],max62303[min303down_index],min62303[min303up_index],min62303[min303down_index]]
#r62h=[max62303[min303up_index+int(min303up_index*deltat)],max62303[min303down_index+int(min303down_index*deltat)],min62303[min303up_index+int(min303up_index*deltat)],min62303[min303down_index+int(min303down_index*deltat)]]
r62h=[max62303[Tcup[7]],max62303[Tcdown[7]],min62303[Tcup[7]],min62303[Tcdown[7]]]
r62303up=np.max(r62)
r62303down=np.min(r62)
r62303uph=np.max(r62h)
r62303downh=np.min(r62h)

r82303cen=r82mub303cen[min303cen_index]
#r82303hcen=r82mub303cen[min303cen_index+int(min303cen_index*deltat)]
r82303hcen=r82mub303cen[Tcen[7]]
r82=[max82303[min303up_index],max82303[min303down_index],min82303[min303up_index],min82303[min303down_index]]
#r82h=[max82303[min303up_index+int(min303up_index*deltat)],max82303[min303down_index+int(min303down_index*deltat)],min82303[min303up_index+int(min303up_index*deltat)],min82303[min303down_index+int(min303down_index*deltat)]]
r82h=[max82303[Tcup[7]],max82303[Tcdown[7]],min82303[Tcup[7]],min82303[Tcdown[7]]]
r82303up=np.max(r82)
r82303down=np.min(r82)
r82303uph=np.max(r82h)
r82303downh=np.min(r82h)
####################################################################################################
chi2mub310cen=np.loadtxt(r'./addition/mub310/cmucen/final/buffer/chi2.dat')
chi3mub310cen=np.loadtxt(r'./addition/mub310/cmucen/final/buffer/chi3.dat')
chi4mub310cen=np.loadtxt(r'./addition/mub310/cmucen/final/buffer/chi4.dat')
chi6mub310cen=np.loadtxt(r'./addition/mub310/cmucen/final/buffer/chi6.dat')
chi8mub310cen=np.loadtxt(r'./addition/mub310/cmucen/final/buffer/chi8.dat')
r32mub310cen=chi3mub310cen/chi2mub310cen
r42mub310cen=chi4mub310cen/chi2mub310cen
r62mub310cen=chi6mub310cen/chi2mub310cen
r82mub310cen=chi8mub310cen/chi2mub310cen
chi2mub310up=np.loadtxt(r'./addition/mub310/cmuup/final/buffer/chi2.dat')
chi3mub310up=np.loadtxt(r'./addition/mub310/cmuup/final/buffer/chi3.dat')
chi4mub310up=np.loadtxt(r'./addition/mub310/cmuup/final/buffer/chi4.dat')
chi6mub310up=np.loadtxt(r'./addition/mub310/cmuup/final/buffer/chi6.dat')
chi8mub310up=np.loadtxt(r'./addition/mub310/cmuup/final/buffer/chi8.dat')
r32mub310up=chi3mub310up/chi2mub310up
r42mub310up=chi4mub310up/chi2mub310up
r62mub310up=chi6mub310up/chi2mub310up
r82mub310up=chi8mub310up/chi2mub310up
chi2mub310up1=np.loadtxt(r'./addition/mub310/cmuup1/final/buffer/chi2.dat')
chi3mub310up1=np.loadtxt(r'./addition/mub310/cmuup1/final/buffer/chi3.dat')
chi4mub310up1=np.loadtxt(r'./addition/mub310/cmuup1/final/buffer/chi4.dat')
chi6mub310up1=np.loadtxt(r'./addition/mub310/cmuup1/final/buffer/chi6.dat')
chi8mub310up1=np.loadtxt(r'./addition/mub310/cmuup1/final/buffer/chi8.dat')
r32mub310up1=chi3mub310up1/chi2mub310up1
r42mub310up1=chi4mub310up1/chi2mub310up1
r62mub310up1=chi6mub310up1/chi2mub310up1
r82mub310up1=chi8mub310up1/chi2mub310up1
chi2mub310up2=np.loadtxt(r'./addition/mub310/cmuup2/final/buffer/chi2.dat')
chi3mub310up2=np.loadtxt(r'./addition/mub310/cmuup2/final/buffer/chi3.dat')
chi4mub310up2=np.loadtxt(r'./addition/mub310/cmuup2/final/buffer/chi4.dat')
chi6mub310up2=np.loadtxt(r'./addition/mub310/cmuup2/final/buffer/chi6.dat')
chi8mub310up2=np.loadtxt(r'./addition/mub310/cmuup2/final/buffer/chi8.dat')
r32mub310up2=chi3mub310up2/chi2mub310up2
r42mub310up2=chi4mub310up2/chi2mub310up2
r62mub310up2=chi6mub310up2/chi2mub310up2
r82mub310up2=chi8mub310up2/chi2mub310up2
chi2mub310up3=np.loadtxt(r'./addition/mub310/cmuup3/final/buffer/chi2.dat')
chi3mub310up3=np.loadtxt(r'./addition/mub310/cmuup3/final/buffer/chi3.dat')
chi4mub310up3=np.loadtxt(r'./addition/mub310/cmuup3/final/buffer/chi4.dat')
chi6mub310up3=np.loadtxt(r'./addition/mub310/cmuup3/final/buffer/chi6.dat')
chi8mub310up3=np.loadtxt(r'./addition/mub310/cmuup3/final/buffer/chi8.dat')
r32mub310up3=chi3mub310up3/chi2mub310up3
r42mub310up3=chi4mub310up3/chi2mub310up3
r62mub310up3=chi6mub310up3/chi2mub310up3
r82mub310up3=chi8mub310up3/chi2mub310up3
chi2mub310up4=np.loadtxt(r'./addition/mub310/cmuup4/final/buffer/chi2.dat')
chi3mub310up4=np.loadtxt(r'./addition/mub310/cmuup4/final/buffer/chi3.dat')
chi4mub310up4=np.loadtxt(r'./addition/mub310/cmuup4/final/buffer/chi4.dat')
chi6mub310up4=np.loadtxt(r'./addition/mub310/cmuup4/final/buffer/chi6.dat')
chi8mub310up4=np.loadtxt(r'./addition/mub310/cmuup4/final/buffer/chi8.dat')
r32mub310up4=chi3mub310up4/chi2mub310up4
r42mub310up4=chi4mub310up4/chi2mub310up4
r62mub310up4=chi6mub310up4/chi2mub310up4
r82mub310up4=chi8mub310up4/chi2mub310up4
chi2mub310down=np.loadtxt(r'./addition/mub310/cmudown/final/buffer/chi2.dat')
chi3mub310down=np.loadtxt(r'./addition/mub310/cmudown/final/buffer/chi3.dat')
chi4mub310down=np.loadtxt(r'./addition/mub310/cmudown/final/buffer/chi4.dat')
chi6mub310down=np.loadtxt(r'./addition/mub310/cmudown/final/buffer/chi6.dat')
chi8mub310down=np.loadtxt(r'./addition/mub310/cmudown/final/buffer/chi8.dat')
r32mub310down=chi3mub310down/chi2mub310down
r42mub310down=chi4mub310down/chi2mub310down
r62mub310down=chi6mub310down/chi2mub310down
r82mub310down=chi8mub310down/chi2mub310down
chi2mub310down1=np.loadtxt(r'./addition/mub310/cmudown1/final/buffer/chi2.dat')
chi3mub310down1=np.loadtxt(r'./addition/mub310/cmudown1/final/buffer/chi3.dat')
chi4mub310down1=np.loadtxt(r'./addition/mub310/cmudown1/final/buffer/chi4.dat')
chi6mub310down1=np.loadtxt(r'./addition/mub310/cmudown1/final/buffer/chi6.dat')
chi8mub310down1=np.loadtxt(r'./addition/mub310/cmudown1/final/buffer/chi8.dat')
r32mub310down1=chi3mub310down1/chi2mub310down1
r42mub310down1=chi4mub310down1/chi2mub310down1
r62mub310down1=chi6mub310down1/chi2mub310down1
r82mub310down1=chi8mub310down1/chi2mub310down1
chi2mub310down2=np.loadtxt(r'./addition/mub310/cmudown2/final/buffer/chi2.dat')
chi3mub310down2=np.loadtxt(r'./addition/mub310/cmudown2/final/buffer/chi3.dat')
chi4mub310down2=np.loadtxt(r'./addition/mub310/cmudown2/final/buffer/chi4.dat')
chi6mub310down2=np.loadtxt(r'./addition/mub310/cmudown2/final/buffer/chi6.dat')
chi8mub310down2=np.loadtxt(r'./addition/mub310/cmudown2/final/buffer/chi8.dat')
r32mub310down2=chi3mub310down2/chi2mub310down2
r42mub310down2=chi4mub310down2/chi2mub310down2
r62mub310down2=chi6mub310down2/chi2mub310down2
r82mub310down2=chi8mub310down2/chi2mub310down2
chi2mub310down3=np.loadtxt(r'./addition/mub310/cmudown3/final/buffer/chi2.dat')
chi3mub310down3=np.loadtxt(r'./addition/mub310/cmudown3/final/buffer/chi3.dat')
chi4mub310down3=np.loadtxt(r'./addition/mub310/cmudown3/final/buffer/chi4.dat')
chi6mub310down3=np.loadtxt(r'./addition/mub310/cmudown3/final/buffer/chi6.dat')
chi8mub310down3=np.loadtxt(r'./addition/mub310/cmudown3/final/buffer/chi8.dat')
r32mub310down3=chi3mub310down3/chi2mub310down3
r42mub310down3=chi4mub310down3/chi2mub310down3
r62mub310down3=chi6mub310down3/chi2mub310down3
r82mub310down3=chi8mub310down3/chi2mub310down3
chi2mub310down4=np.loadtxt(r'./addition/mub310/cmudown4/final/buffer/chi2.dat')
chi3mub310down4=np.loadtxt(r'./addition/mub310/cmudown4/final/buffer/chi3.dat')
chi4mub310down4=np.loadtxt(r'./addition/mub310/cmudown4/final/buffer/chi4.dat')
chi6mub310down4=np.loadtxt(r'./addition/mub310/cmudown4/final/buffer/chi6.dat')
chi8mub310down4=np.loadtxt(r'./addition/mub310/cmudown4/final/buffer/chi8.dat')
r32mub310down4=chi3mub310down4/chi2mub310down4
r42mub310down4=chi4mub310down4/chi2mub310down4
r62mub310down4=chi6mub310down4/chi2mub310down4
r82mub310down4=chi8mub310down4/chi2mub310down4
r32310=np.zeros((2991,100))
r42310=np.zeros((2991,100))
r62310=np.zeros((2991,100))
r82310=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32310[:,t]=spline(T/ct[t],r32mub310up,xsame)
    else:
       if t>=10 and t<20:
          r32310[:,t]=spline(T/ct[t-10],r32mub310up1,xsame)
       else:
          if t>=20 and t<30:
             r32310[:,t]=spline(T/ct[t-20],r32mub310up2,xsame)
          else: 
             if t>=30 and t<40:
                r32310[:,t]=spline(T/ct[t-30],r32mub310up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32310[:,t]=spline(T/ct[t-40],r32mub310up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32310[:,t]=spline(T/ct[t-50],r32mub310down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32310[:,t]=spline(T/ct[t-60],r32mub310down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32310[:,t]=spline(T/ct[t-70],r32mub310down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32310[:,t]=spline(T/ct[t-80],r32mub310down3,xsame)
                            else:
                                r32310[:,t]=spline(T/ct[t-90],r32mub310down4,xsame)

for t in range(0,100):
    if t<10:
       r42310[:,t]=spline(T/ct[t],r42mub310up,xsame)
    else:
       if t>=10 and t<20:
          r42310[:,t]=spline(T/ct[t-10],r42mub310up1,xsame)
       else:
          if t>=20 and t<30:
             r42310[:,t]=spline(T/ct[t-20],r42mub310up2,xsame)
          else: 
             if t>=30 and t<40:
                r42310[:,t]=spline(T/ct[t-30],r42mub310up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42310[:,t]=spline(T/ct[t-40],r42mub310up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42310[:,t]=spline(T/ct[t-50],r42mub310down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42310[:,t]=spline(T/ct[t-60],r42mub310down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42310[:,t]=spline(T/ct[t-70],r42mub310down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42310[:,t]=spline(T/ct[t-80],r42mub310down3,xsame)
                            else:
                                r42310[:,t]=spline(T/ct[t-90],r42mub310down4,xsame)

for t in range(0,100):
    if t<10:
       r62310[:,t]=spline(T/ct[t],r62mub310up,xsame)
    else:
       if t>=10 and t<20:
          r62310[:,t]=spline(T/ct[t-10],r62mub310up1,xsame)
       else:
          if t>=20 and t<30:
             r62310[:,t]=spline(T/ct[t-20],r62mub310up2,xsame)
          else: 
             if t>=30 and t<40:
                r62310[:,t]=spline(T/ct[t-30],r62mub310up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62310[:,t]=spline(T/ct[t-40],r62mub310up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62310[:,t]=spline(T/ct[t-50],r62mub310down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62310[:,t]=spline(T/ct[t-60],r62mub310down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62310[:,t]=spline(T/ct[t-70],r62mub310down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62310[:,t]=spline(T/ct[t-80],r62mub310down3,xsame)
                            else:
                                r62310[:,t]=spline(T/ct[t-90],r62mub310down4,xsame)

for t in range(0,100):
    if t<10:
       r82310[:,t]=spline(T/ct[t],r82mub310up,xsame)
    else:
       if t>=10 and t<20:
          r82310[:,t]=spline(T/ct[t-10],r82mub310up1,xsame)
       else:
          if t>=20 and t<30:
             r82310[:,t]=spline(T/ct[t-20],r82mub310up2,xsame)
          else: 
             if t>=30 and t<40:
                r82310[:,t]=spline(T/ct[t-30],r82mub310up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82310[:,t]=spline(T/ct[t-40],r82mub310up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82310[:,t]=spline(T/ct[t-50],r82mub310down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82310[:,t]=spline(T/ct[t-60],r82mub310down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82310[:,t]=spline(T/ct[t-70],r82mub310down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82310[:,t]=spline(T/ct[t-80],r82mub310down3,xsame)
                            else:
                                r82310[:,t]=spline(T/ct[t-90],r82mub310down4,xsame)


for num in range(1,100):
    if num==1:
       max310=np.maximum(r32310[:,num-1],r32310[:,num])
       min310=np.minimum(r32310[:,num-1],r32310[:,num])
    else:
       max310=np.maximum(max310,r32310[:,num])
       min310=np.minimum(min310,r32310[:,num])

for num in range(1,100):
    if num==1:
       max42310=np.maximum(r42310[:,num-1],r42310[:,num])
       min42310=np.minimum(r42310[:,num-1],r42310[:,num])
    else:
       max42310=np.maximum(max42310,r42310[:,num])
       min42310=np.minimum(min42310,r42310[:,num])

for num in range(1,100):
    if num==1:
       max62310=np.maximum(r62310[:,num-1],r62310[:,num])
       min62310=np.minimum(r62310[:,num-1],r62310[:,num])
    else:
       max62310=np.maximum(max62310,r62310[:,num])
       min62310=np.minimum(min62310,r62310[:,num])

for num in range(1,100):
    if num==1:
       max82310=np.maximum(r82310[:,num-1],r82310[:,num])
       min82310=np.minimum(r82310[:,num-1],r82310[:,num])
    else:
       max82310=np.maximum(max82310,r82310[:,num])
       min82310=np.minimum(min82310,r82310[:,num])

r32mub310cen=spline(T/ctcen,r32mub310cen,xsame)
r42mub310cen=spline(T/ctcen,r42mub310cen,xsame)
r62mub310cen=spline(T/ctcen,r62mub310cen,xsame)
r82mub310cen=spline(T/ctcen,r82mub310cen,xsame)

dif310cen=abs(r42mub310cen-0.140553)
dif310up=abs(max42310-0.140553)
dif310down=abs(min42310-0.140553)
min310cen_index=1481#int(round(fit7[5,2]))
min310up_index=1481#int(round(fit7[5,1]))
min310down_index=1481#int(round(fit7[5,0]))
print(min310cen_index)
r32310cen=r32mub310cen[min310cen_index]
r32310hcen=r32mub310cen[Tcen[5]]
r32=[max310[min310up_index],max310[min310down_index],min310[min310up_index],min310[min310down_index]]
r32310up=np.max(r32)
r32310down=np.min(r32)

r42310cen=r42mub310cen[min310cen_index]
r62310cen=r62mub310cen[min310cen_index]
r42=[max42310[min310up_index],max42310[min310down_index],min42310[min310up_index],min42310[min310down_index]]
r42310up=np.max(r42)
r42310down=np.min(r42)

r62=[max62310[min310up_index],max62310[min310down_index],min62310[min310up_index],min62310[min310down_index]]
r62310up=np.max(r62)
r62310down=np.min(r62)

r82310cen=r82mub310cen[min310cen_index]
r82=[max82310[min310up_index],max82310[min310down_index],min82310[min310up_index],min82310[min310down_index]]
r82310up=np.max(r82)
r82310down=np.min(r82)
####################################################################################################
chi2mub320cen=np.loadtxt(r'./addition/mub320/cmucen/final/buffer/chi2.dat')
chi3mub320cen=np.loadtxt(r'./addition/mub320/cmucen/final/buffer/chi3.dat')
chi4mub320cen=np.loadtxt(r'./addition/mub320/cmucen/final/buffer/chi4.dat')
chi6mub320cen=np.loadtxt(r'./addition/mub320/cmucen/final/buffer/chi6.dat')
chi8mub320cen=np.loadtxt(r'./addition/mub320/cmucen/final/buffer/chi8.dat')
r32mub320cen=chi3mub320cen/chi2mub320cen
r42mub320cen=chi4mub320cen/chi2mub320cen
r62mub320cen=chi6mub320cen/chi2mub320cen
r82mub320cen=chi8mub320cen/chi2mub320cen
chi2mub320up=np.loadtxt(r'./addition/mub320/cmuup/final/buffer/chi2.dat')
chi3mub320up=np.loadtxt(r'./addition/mub320/cmuup/final/buffer/chi3.dat')
chi4mub320up=np.loadtxt(r'./addition/mub320/cmuup/final/buffer/chi4.dat')
chi6mub320up=np.loadtxt(r'./addition/mub320/cmuup/final/buffer/chi6.dat')
chi8mub320up=np.loadtxt(r'./addition/mub320/cmuup/final/buffer/chi8.dat')
r32mub320up=chi3mub320up/chi2mub320up
r42mub320up=chi4mub320up/chi2mub320up
r62mub320up=chi6mub320up/chi2mub320up
r82mub320up=chi8mub320up/chi2mub320up
chi2mub320up1=np.loadtxt(r'./addition/mub320/cmuup1/final/buffer/chi2.dat')
chi3mub320up1=np.loadtxt(r'./addition/mub320/cmuup1/final/buffer/chi3.dat')
chi4mub320up1=np.loadtxt(r'./addition/mub320/cmuup1/final/buffer/chi4.dat')
chi6mub320up1=np.loadtxt(r'./addition/mub320/cmuup1/final/buffer/chi6.dat')
chi8mub320up1=np.loadtxt(r'./addition/mub320/cmuup1/final/buffer/chi8.dat')
r32mub320up1=chi3mub320up1/chi2mub320up1
r42mub320up1=chi4mub320up1/chi2mub320up1
r62mub320up1=chi6mub320up1/chi2mub320up1
r82mub320up1=chi8mub320up1/chi2mub320up1
chi2mub320up2=np.loadtxt(r'./addition/mub320/cmuup2/final/buffer/chi2.dat')
chi3mub320up2=np.loadtxt(r'./addition/mub320/cmuup2/final/buffer/chi3.dat')
chi4mub320up2=np.loadtxt(r'./addition/mub320/cmuup2/final/buffer/chi4.dat')
chi6mub320up2=np.loadtxt(r'./addition/mub320/cmuup2/final/buffer/chi6.dat')
chi8mub320up2=np.loadtxt(r'./addition/mub320/cmuup2/final/buffer/chi8.dat')
r32mub320up2=chi3mub320up2/chi2mub320up2
r42mub320up2=chi4mub320up2/chi2mub320up2
r62mub320up2=chi6mub320up2/chi2mub320up2
r82mub320up2=chi8mub320up2/chi2mub320up2
chi2mub320up3=np.loadtxt(r'./addition/mub320/cmuup3/final/buffer/chi2.dat')
chi3mub320up3=np.loadtxt(r'./addition/mub320/cmuup3/final/buffer/chi3.dat')
chi4mub320up3=np.loadtxt(r'./addition/mub320/cmuup3/final/buffer/chi4.dat')
chi6mub320up3=np.loadtxt(r'./addition/mub320/cmuup3/final/buffer/chi6.dat')
chi8mub320up3=np.loadtxt(r'./addition/mub320/cmuup3/final/buffer/chi8.dat')
r32mub320up3=chi3mub320up3/chi2mub320up3
r42mub320up3=chi4mub320up3/chi2mub320up3
r62mub320up3=chi6mub320up3/chi2mub320up3
r82mub320up3=chi8mub320up3/chi2mub320up3
chi2mub320up4=np.loadtxt(r'./addition/mub320/cmuup4/final/buffer/chi2.dat')
chi3mub320up4=np.loadtxt(r'./addition/mub320/cmuup4/final/buffer/chi3.dat')
chi4mub320up4=np.loadtxt(r'./addition/mub320/cmuup4/final/buffer/chi4.dat')
chi6mub320up4=np.loadtxt(r'./addition/mub320/cmuup4/final/buffer/chi6.dat')
chi8mub320up4=np.loadtxt(r'./addition/mub320/cmuup4/final/buffer/chi8.dat')
r32mub320up4=chi3mub320up4/chi2mub320up4
r42mub320up4=chi4mub320up4/chi2mub320up4
r62mub320up4=chi6mub320up4/chi2mub320up4
r82mub320up4=chi8mub320up4/chi2mub320up4
chi2mub320down=np.loadtxt(r'./addition/mub320/cmudown/final/buffer/chi2.dat')
chi3mub320down=np.loadtxt(r'./addition/mub320/cmudown/final/buffer/chi3.dat')
chi4mub320down=np.loadtxt(r'./addition/mub320/cmudown/final/buffer/chi4.dat')
chi6mub320down=np.loadtxt(r'./addition/mub320/cmudown/final/buffer/chi6.dat')
chi8mub320down=np.loadtxt(r'./addition/mub320/cmudown/final/buffer/chi8.dat')
r32mub320down=chi3mub320down/chi2mub320down
r42mub320down=chi4mub320down/chi2mub320down
r62mub320down=chi6mub320down/chi2mub320down
r82mub320down=chi8mub320down/chi2mub320down
chi2mub320down1=np.loadtxt(r'./addition/mub320/cmudown1/final/buffer/chi2.dat')
chi3mub320down1=np.loadtxt(r'./addition/mub320/cmudown1/final/buffer/chi3.dat')
chi4mub320down1=np.loadtxt(r'./addition/mub320/cmudown1/final/buffer/chi4.dat')
chi6mub320down1=np.loadtxt(r'./addition/mub320/cmudown1/final/buffer/chi6.dat')
chi8mub320down1=np.loadtxt(r'./addition/mub320/cmudown1/final/buffer/chi8.dat')
r32mub320down1=chi3mub320down1/chi2mub320down1
r42mub320down1=chi4mub320down1/chi2mub320down1
r62mub320down1=chi6mub320down1/chi2mub320down1
r82mub320down1=chi8mub320down1/chi2mub320down1
chi2mub320down2=np.loadtxt(r'./addition/mub320/cmudown2/final/buffer/chi2.dat')
chi3mub320down2=np.loadtxt(r'./addition/mub320/cmudown2/final/buffer/chi3.dat')
chi4mub320down2=np.loadtxt(r'./addition/mub320/cmudown2/final/buffer/chi4.dat')
chi6mub320down2=np.loadtxt(r'./addition/mub320/cmudown2/final/buffer/chi6.dat')
chi8mub320down2=np.loadtxt(r'./addition/mub320/cmudown2/final/buffer/chi8.dat')
r32mub320down2=chi3mub320down2/chi2mub320down2
r42mub320down2=chi4mub320down2/chi2mub320down2
r62mub320down2=chi6mub320down2/chi2mub320down2
r82mub320down2=chi8mub320down2/chi2mub320down2
chi2mub320down3=np.loadtxt(r'./addition/mub320/cmudown3/final/buffer/chi2.dat')
chi3mub320down3=np.loadtxt(r'./addition/mub320/cmudown3/final/buffer/chi3.dat')
chi4mub320down3=np.loadtxt(r'./addition/mub320/cmudown3/final/buffer/chi4.dat')
chi6mub320down3=np.loadtxt(r'./addition/mub320/cmudown3/final/buffer/chi6.dat')
chi8mub320down3=np.loadtxt(r'./addition/mub320/cmudown3/final/buffer/chi8.dat')
r32mub320down3=chi3mub320down3/chi2mub320down3
r42mub320down3=chi4mub320down3/chi2mub320down3
r62mub320down3=chi6mub320down3/chi2mub320down3
r82mub320down3=chi8mub320down3/chi2mub320down3
chi2mub320down4=np.loadtxt(r'./addition/mub320/cmudown4/final/buffer/chi2.dat')
chi3mub320down4=np.loadtxt(r'./addition/mub320/cmudown4/final/buffer/chi3.dat')
chi4mub320down4=np.loadtxt(r'./addition/mub320/cmudown4/final/buffer/chi4.dat')
chi6mub320down4=np.loadtxt(r'./addition/mub320/cmudown4/final/buffer/chi6.dat')
chi8mub320down4=np.loadtxt(r'./addition/mub320/cmudown4/final/buffer/chi8.dat')
r32mub320down4=chi3mub320down4/chi2mub320down4
r42mub320down4=chi4mub320down4/chi2mub320down4
r62mub320down4=chi6mub320down4/chi2mub320down4
r82mub320down4=chi8mub320down4/chi2mub320down4
r32320=np.zeros((2991,100))
r42320=np.zeros((2991,100))
r62320=np.zeros((2991,100))
r82320=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32320[:,t]=spline(T/ct[t],r32mub320up,xsame)
    else:
       if t>=10 and t<20:
          r32320[:,t]=spline(T/ct[t-10],r32mub320up1,xsame)
       else:
          if t>=20 and t<30:
             r32320[:,t]=spline(T/ct[t-20],r32mub320up2,xsame)
          else: 
             if t>=30 and t<40:
                r32320[:,t]=spline(T/ct[t-30],r32mub320up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32320[:,t]=spline(T/ct[t-40],r32mub320up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32320[:,t]=spline(T/ct[t-50],r32mub320down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32320[:,t]=spline(T/ct[t-60],r32mub320down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32320[:,t]=spline(T/ct[t-70],r32mub320down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32320[:,t]=spline(T/ct[t-80],r32mub320down3,xsame)
                            else:
                                r32320[:,t]=spline(T/ct[t-90],r32mub320down4,xsame)

for t in range(0,100):
    if t<10:
       r42320[:,t]=spline(T/ct[t],r42mub320up,xsame)
    else:
       if t>=10 and t<20:
          r42320[:,t]=spline(T/ct[t-10],r42mub320up1,xsame)
       else:
          if t>=20 and t<30:
             r42320[:,t]=spline(T/ct[t-20],r42mub320up2,xsame)
          else: 
             if t>=30 and t<40:
                r42320[:,t]=spline(T/ct[t-30],r42mub320up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42320[:,t]=spline(T/ct[t-40],r42mub320up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42320[:,t]=spline(T/ct[t-50],r42mub320down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42320[:,t]=spline(T/ct[t-60],r42mub320down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42320[:,t]=spline(T/ct[t-70],r42mub320down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42320[:,t]=spline(T/ct[t-80],r42mub320down3,xsame)
                            else:
                                r42320[:,t]=spline(T/ct[t-90],r42mub320down4,xsame)

for t in range(0,100):
    if t<10:
       r62320[:,t]=spline(T/ct[t],r62mub320up,xsame)
    else:
       if t>=10 and t<20:
          r62320[:,t]=spline(T/ct[t-10],r62mub320up1,xsame)
       else:
          if t>=20 and t<30:
             r62320[:,t]=spline(T/ct[t-20],r62mub320up2,xsame)
          else: 
             if t>=30 and t<40:
                r62320[:,t]=spline(T/ct[t-30],r62mub320up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62320[:,t]=spline(T/ct[t-40],r62mub320up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62320[:,t]=spline(T/ct[t-50],r62mub320down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62320[:,t]=spline(T/ct[t-60],r62mub320down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62320[:,t]=spline(T/ct[t-70],r62mub320down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62320[:,t]=spline(T/ct[t-80],r62mub320down3,xsame)
                            else:
                                r62320[:,t]=spline(T/ct[t-90],r62mub320down4,xsame)

for t in range(0,100):
    if t<10:
       r82320[:,t]=spline(T/ct[t],r82mub320up,xsame)
    else:
       if t>=10 and t<20:
          r82320[:,t]=spline(T/ct[t-10],r82mub320up1,xsame)
       else:
          if t>=20 and t<30:
             r82320[:,t]=spline(T/ct[t-20],r82mub320up2,xsame)
          else: 
             if t>=30 and t<40:
                r82320[:,t]=spline(T/ct[t-30],r82mub320up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82320[:,t]=spline(T/ct[t-40],r82mub320up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82320[:,t]=spline(T/ct[t-50],r82mub320down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82320[:,t]=spline(T/ct[t-60],r82mub320down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82320[:,t]=spline(T/ct[t-70],r82mub320down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82320[:,t]=spline(T/ct[t-80],r82mub320down3,xsame)
                            else:
                                r82320[:,t]=spline(T/ct[t-90],r82mub320down4,xsame)


for num in range(1,100):
    if num==1:
       max320=np.maximum(r32320[:,num-1],r32320[:,num])
       min320=np.minimum(r32320[:,num-1],r32320[:,num])
    else:
       max320=np.maximum(max320,r32320[:,num])
       min320=np.minimum(min320,r32320[:,num])

for num in range(1,100):
    if num==1:
       max42320=np.maximum(r42320[:,num-1],r42320[:,num])
       min42320=np.minimum(r42320[:,num-1],r42320[:,num])
    else:
       max42320=np.maximum(max42320,r42320[:,num])
       min42320=np.minimum(min42320,r42320[:,num])

for num in range(1,100):
    if num==1:
       max62320=np.maximum(r62320[:,num-1],r62320[:,num])
       min62320=np.minimum(r62320[:,num-1],r62320[:,num])
    else:
       max62320=np.maximum(max62320,r62320[:,num])
       min62320=np.minimum(min62320,r62320[:,num])

for num in range(1,100):
    if num==1:
       max82320=np.maximum(r82320[:,num-1],r82320[:,num])
       min82320=np.minimum(r82320[:,num-1],r82320[:,num])
    else:
       max82320=np.maximum(max82320,r82320[:,num])
       min82320=np.minimum(min82320,r82320[:,num])

r32mub320cen=spline(T/ctcen,r32mub320cen,xsame)
r42mub320cen=spline(T/ctcen,r42mub320cen,xsame)
r62mub320cen=spline(T/ctcen,r62mub320cen,xsame)
r82mub320cen=spline(T/ctcen,r82mub320cen,xsame)

dif320cen=abs(r42mub320cen-0.140553)
dif320up=abs(max42320-0.140553)
dif320down=abs(min42320-0.140553)
min320cen_index=1470#int(round(fit7[5,2]))
min320up_index=1470#int(round(fit7[5,1]))
min320down_index=1470#int(round(fit7[5,0]))
print(min320cen_index)
r32320cen=r32mub320cen[min320cen_index]
r32320hcen=r32mub320cen[Tcen[5]]
r32=[max320[min320up_index],max320[min320down_index],min320[min320up_index],min320[min320down_index]]
r32320up=np.max(r32)
r32320down=np.min(r32)

r42320cen=r42mub320cen[min320cen_index]
r62320cen=r62mub320cen[min320cen_index]
r42=[max42320[min320up_index],max42320[min320down_index],min42320[min320up_index],min42320[min320down_index]]
r42320up=np.max(r42)
r42320down=np.min(r42)

r62=[max62320[min320up_index],max62320[min320down_index],min62320[min320up_index],min62320[min320down_index]]
r62320up=np.max(r62)
r62320down=np.min(r62)

r82320cen=r82mub320cen[min320cen_index]
r82=[max82320[min320up_index],max82320[min320down_index],min82320[min320up_index],min82320[min320down_index]]
r82320up=np.max(r82)
r82320down=np.min(r82)
####################################################################################################
chi2mub330cen=np.loadtxt(r'./addition/mub330/cmucen/final/buffer/chi2.dat')
chi3mub330cen=np.loadtxt(r'./addition/mub330/cmucen/final/buffer/chi3.dat')
chi4mub330cen=np.loadtxt(r'./addition/mub330/cmucen/final/buffer/chi4.dat')
chi6mub330cen=np.loadtxt(r'./addition/mub330/cmucen/final/buffer/chi6.dat')
chi8mub330cen=np.loadtxt(r'./addition/mub330/cmucen/final/buffer/chi8.dat')
r32mub330cen=chi3mub330cen/chi2mub330cen
r42mub330cen=chi4mub330cen/chi2mub330cen
r62mub330cen=chi6mub330cen/chi2mub330cen
r82mub330cen=chi8mub330cen/chi2mub330cen
chi2mub330up=np.loadtxt(r'./addition/mub330/cmuup/final/buffer/chi2.dat')
chi3mub330up=np.loadtxt(r'./addition/mub330/cmuup/final/buffer/chi3.dat')
chi4mub330up=np.loadtxt(r'./addition/mub330/cmuup/final/buffer/chi4.dat')
chi6mub330up=np.loadtxt(r'./addition/mub330/cmuup/final/buffer/chi6.dat')
chi8mub330up=np.loadtxt(r'./addition/mub330/cmuup/final/buffer/chi8.dat')
r32mub330up=chi3mub330up/chi2mub330up
r42mub330up=chi4mub330up/chi2mub330up
r62mub330up=chi6mub330up/chi2mub330up
r82mub330up=chi8mub330up/chi2mub330up
chi2mub330up1=np.loadtxt(r'./addition/mub330/cmuup1/final/buffer/chi2.dat')
chi3mub330up1=np.loadtxt(r'./addition/mub330/cmuup1/final/buffer/chi3.dat')
chi4mub330up1=np.loadtxt(r'./addition/mub330/cmuup1/final/buffer/chi4.dat')
chi6mub330up1=np.loadtxt(r'./addition/mub330/cmuup1/final/buffer/chi6.dat')
chi8mub330up1=np.loadtxt(r'./addition/mub330/cmuup1/final/buffer/chi8.dat')
r32mub330up1=chi3mub330up1/chi2mub330up1
r42mub330up1=chi4mub330up1/chi2mub330up1
r62mub330up1=chi6mub330up1/chi2mub330up1
r82mub330up1=chi8mub330up1/chi2mub330up1
chi2mub330up2=np.loadtxt(r'./addition/mub330/cmuup2/final/buffer/chi2.dat')
chi3mub330up2=np.loadtxt(r'./addition/mub330/cmuup2/final/buffer/chi3.dat')
chi4mub330up2=np.loadtxt(r'./addition/mub330/cmuup2/final/buffer/chi4.dat')
chi6mub330up2=np.loadtxt(r'./addition/mub330/cmuup2/final/buffer/chi6.dat')
chi8mub330up2=np.loadtxt(r'./addition/mub330/cmuup2/final/buffer/chi8.dat')
r32mub330up2=chi3mub330up2/chi2mub330up2
r42mub330up2=chi4mub330up2/chi2mub330up2
r62mub330up2=chi6mub330up2/chi2mub330up2
r82mub330up2=chi8mub330up2/chi2mub330up2
chi2mub330up3=np.loadtxt(r'./addition/mub330/cmuup3/final/buffer/chi2.dat')
chi3mub330up3=np.loadtxt(r'./addition/mub330/cmuup3/final/buffer/chi3.dat')
chi4mub330up3=np.loadtxt(r'./addition/mub330/cmuup3/final/buffer/chi4.dat')
chi6mub330up3=np.loadtxt(r'./addition/mub330/cmuup3/final/buffer/chi6.dat')
chi8mub330up3=np.loadtxt(r'./addition/mub330/cmuup3/final/buffer/chi8.dat')
r32mub330up3=chi3mub330up3/chi2mub330up3
r42mub330up3=chi4mub330up3/chi2mub330up3
r62mub330up3=chi6mub330up3/chi2mub330up3
r82mub330up3=chi8mub330up3/chi2mub330up3
chi2mub330up4=np.loadtxt(r'./addition/mub330/cmuup4/final/buffer/chi2.dat')
chi3mub330up4=np.loadtxt(r'./addition/mub330/cmuup4/final/buffer/chi3.dat')
chi4mub330up4=np.loadtxt(r'./addition/mub330/cmuup4/final/buffer/chi4.dat')
chi6mub330up4=np.loadtxt(r'./addition/mub330/cmuup4/final/buffer/chi6.dat')
chi8mub330up4=np.loadtxt(r'./addition/mub330/cmuup4/final/buffer/chi8.dat')
r32mub330up4=chi3mub330up4/chi2mub330up4
r42mub330up4=chi4mub330up4/chi2mub330up4
r62mub330up4=chi6mub330up4/chi2mub330up4
r82mub330up4=chi8mub330up4/chi2mub330up4
chi2mub330down=np.loadtxt(r'./addition/mub330/cmudown/final/buffer/chi2.dat')
chi3mub330down=np.loadtxt(r'./addition/mub330/cmudown/final/buffer/chi3.dat')
chi4mub330down=np.loadtxt(r'./addition/mub330/cmudown/final/buffer/chi4.dat')
chi6mub330down=np.loadtxt(r'./addition/mub330/cmudown/final/buffer/chi6.dat')
chi8mub330down=np.loadtxt(r'./addition/mub330/cmudown/final/buffer/chi8.dat')
r32mub330down=chi3mub330down/chi2mub330down
r42mub330down=chi4mub330down/chi2mub330down
r62mub330down=chi6mub330down/chi2mub330down
r82mub330down=chi8mub330down/chi2mub330down
chi2mub330down1=np.loadtxt(r'./addition/mub330/cmudown1/final/buffer/chi2.dat')
chi3mub330down1=np.loadtxt(r'./addition/mub330/cmudown1/final/buffer/chi3.dat')
chi4mub330down1=np.loadtxt(r'./addition/mub330/cmudown1/final/buffer/chi4.dat')
chi6mub330down1=np.loadtxt(r'./addition/mub330/cmudown1/final/buffer/chi6.dat')
chi8mub330down1=np.loadtxt(r'./addition/mub330/cmudown1/final/buffer/chi8.dat')
r32mub330down1=chi3mub330down1/chi2mub330down1
r42mub330down1=chi4mub330down1/chi2mub330down1
r62mub330down1=chi6mub330down1/chi2mub330down1
r82mub330down1=chi8mub330down1/chi2mub330down1
chi2mub330down2=np.loadtxt(r'./addition/mub330/cmudown2/final/buffer/chi2.dat')
chi3mub330down2=np.loadtxt(r'./addition/mub330/cmudown2/final/buffer/chi3.dat')
chi4mub330down2=np.loadtxt(r'./addition/mub330/cmudown2/final/buffer/chi4.dat')
chi6mub330down2=np.loadtxt(r'./addition/mub330/cmudown2/final/buffer/chi6.dat')
chi8mub330down2=np.loadtxt(r'./addition/mub330/cmudown2/final/buffer/chi8.dat')
r32mub330down2=chi3mub330down2/chi2mub330down2
r42mub330down2=chi4mub330down2/chi2mub330down2
r62mub330down2=chi6mub330down2/chi2mub330down2
r82mub330down2=chi8mub330down2/chi2mub330down2
chi2mub330down3=np.loadtxt(r'./addition/mub330/cmudown3/final/buffer/chi2.dat')
chi3mub330down3=np.loadtxt(r'./addition/mub330/cmudown3/final/buffer/chi3.dat')
chi4mub330down3=np.loadtxt(r'./addition/mub330/cmudown3/final/buffer/chi4.dat')
chi6mub330down3=np.loadtxt(r'./addition/mub330/cmudown3/final/buffer/chi6.dat')
chi8mub330down3=np.loadtxt(r'./addition/mub330/cmudown3/final/buffer/chi8.dat')
r32mub330down3=chi3mub330down3/chi2mub330down3
r42mub330down3=chi4mub330down3/chi2mub330down3
r62mub330down3=chi6mub330down3/chi2mub330down3
r82mub330down3=chi8mub330down3/chi2mub330down3
chi2mub330down4=np.loadtxt(r'./addition/mub330/cmudown4/final/buffer/chi2.dat')
chi3mub330down4=np.loadtxt(r'./addition/mub330/cmudown4/final/buffer/chi3.dat')
chi4mub330down4=np.loadtxt(r'./addition/mub330/cmudown4/final/buffer/chi4.dat')
chi6mub330down4=np.loadtxt(r'./addition/mub330/cmudown4/final/buffer/chi6.dat')
chi8mub330down4=np.loadtxt(r'./addition/mub330/cmudown4/final/buffer/chi8.dat')
r32mub330down4=chi3mub330down4/chi2mub330down4
r42mub330down4=chi4mub330down4/chi2mub330down4
r62mub330down4=chi6mub330down4/chi2mub330down4
r82mub330down4=chi8mub330down4/chi2mub330down4
r32330=np.zeros((2991,100))
r42330=np.zeros((2991,100))
r62330=np.zeros((2991,100))
r82330=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32330[:,t]=spline(T/ct[t],r32mub330up,xsame)
    else:
       if t>=10 and t<20:
          r32330[:,t]=spline(T/ct[t-10],r32mub330up1,xsame)
       else:
          if t>=20 and t<30:
             r32330[:,t]=spline(T/ct[t-20],r32mub330up2,xsame)
          else: 
             if t>=30 and t<40:
                r32330[:,t]=spline(T/ct[t-30],r32mub330up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32330[:,t]=spline(T/ct[t-40],r32mub330up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32330[:,t]=spline(T/ct[t-50],r32mub330down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32330[:,t]=spline(T/ct[t-60],r32mub330down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32330[:,t]=spline(T/ct[t-70],r32mub330down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32330[:,t]=spline(T/ct[t-80],r32mub330down3,xsame)
                            else:
                                r32330[:,t]=spline(T/ct[t-90],r32mub330down4,xsame)

for t in range(0,100):
    if t<10:
       r42330[:,t]=spline(T/ct[t],r42mub330up,xsame)
    else:
       if t>=10 and t<20:
          r42330[:,t]=spline(T/ct[t-10],r42mub330up1,xsame)
       else:
          if t>=20 and t<30:
             r42330[:,t]=spline(T/ct[t-20],r42mub330up2,xsame)
          else: 
             if t>=30 and t<40:
                r42330[:,t]=spline(T/ct[t-30],r42mub330up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42330[:,t]=spline(T/ct[t-40],r42mub330up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42330[:,t]=spline(T/ct[t-50],r42mub330down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42330[:,t]=spline(T/ct[t-60],r42mub330down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42330[:,t]=spline(T/ct[t-70],r42mub330down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42330[:,t]=spline(T/ct[t-80],r42mub330down3,xsame)
                            else:
                                r42330[:,t]=spline(T/ct[t-90],r42mub330down4,xsame)

for t in range(0,100):
    if t<10:
       r62330[:,t]=spline(T/ct[t],r62mub330up,xsame)
    else:
       if t>=10 and t<20:
          r62330[:,t]=spline(T/ct[t-10],r62mub330up1,xsame)
       else:
          if t>=20 and t<30:
             r62330[:,t]=spline(T/ct[t-20],r62mub330up2,xsame)
          else: 
             if t>=30 and t<40:
                r62330[:,t]=spline(T/ct[t-30],r62mub330up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62330[:,t]=spline(T/ct[t-40],r62mub330up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62330[:,t]=spline(T/ct[t-50],r62mub330down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62330[:,t]=spline(T/ct[t-60],r62mub330down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62330[:,t]=spline(T/ct[t-70],r62mub330down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62330[:,t]=spline(T/ct[t-80],r62mub330down3,xsame)
                            else:
                                r62330[:,t]=spline(T/ct[t-90],r62mub330down4,xsame)

for t in range(0,100):
    if t<10:
       r82330[:,t]=spline(T/ct[t],r82mub330up,xsame)
    else:
       if t>=10 and t<20:
          r82330[:,t]=spline(T/ct[t-10],r82mub330up1,xsame)
       else:
          if t>=20 and t<30:
             r82330[:,t]=spline(T/ct[t-20],r82mub330up2,xsame)
          else: 
             if t>=30 and t<40:
                r82330[:,t]=spline(T/ct[t-30],r82mub330up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82330[:,t]=spline(T/ct[t-40],r82mub330up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82330[:,t]=spline(T/ct[t-50],r82mub330down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82330[:,t]=spline(T/ct[t-60],r82mub330down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82330[:,t]=spline(T/ct[t-70],r82mub330down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82330[:,t]=spline(T/ct[t-80],r82mub330down3,xsame)
                            else:
                                r82330[:,t]=spline(T/ct[t-90],r82mub330down4,xsame)


for num in range(1,100):
    if num==1:
       max330=np.maximum(r32330[:,num-1],r32330[:,num])
       min330=np.minimum(r32330[:,num-1],r32330[:,num])
    else:
       max330=np.maximum(max330,r32330[:,num])
       min330=np.minimum(min330,r32330[:,num])

for num in range(1,100):
    if num==1:
       max42330=np.maximum(r42330[:,num-1],r42330[:,num])
       min42330=np.minimum(r42330[:,num-1],r42330[:,num])
    else:
       max42330=np.maximum(max42330,r42330[:,num])
       min42330=np.minimum(min42330,r42330[:,num])

for num in range(1,100):
    if num==1:
       max62330=np.maximum(r62330[:,num-1],r62330[:,num])
       min62330=np.minimum(r62330[:,num-1],r62330[:,num])
    else:
       max62330=np.maximum(max62330,r62330[:,num])
       min62330=np.minimum(min62330,r62330[:,num])

for num in range(1,100):
    if num==1:
       max82330=np.maximum(r82330[:,num-1],r82330[:,num])
       min82330=np.minimum(r82330[:,num-1],r82330[:,num])
    else:
       max82330=np.maximum(max82330,r82330[:,num])
       min82330=np.minimum(min82330,r82330[:,num])

r32mub330cen=spline(T/ctcen,r32mub330cen,xsame)
r42mub330cen=spline(T/ctcen,r42mub330cen,xsame)
r62mub330cen=spline(T/ctcen,r62mub330cen,xsame)
r82mub330cen=spline(T/ctcen,r82mub330cen,xsame)

dif330cen=abs(r42mub330cen-0.140553)
dif330up=abs(max42330-0.140553)
dif330down=abs(min42330-0.140553)
min330cen_index=1459#int(round(fit7[5,2]))
min330up_index=1459#int(round(fit7[5,1]))
min330down_index=1459#int(round(fit7[5,0]))
print(min330cen_index)
r32330cen=r32mub330cen[min330cen_index]
r32330hcen=r32mub330cen[Tcen[5]]
r32=[max330[min330up_index],max330[min330down_index],min330[min330up_index],min330[min330down_index]]
r32330up=np.max(r32)
r32330down=np.min(r32)

r42330cen=r42mub330cen[min330cen_index]
r62330cen=r62mub330cen[min330cen_index]
r42=[max42330[min330up_index],max42330[min330down_index],min42330[min330up_index],min42330[min330down_index]]
r42330up=np.max(r42)
r42330down=np.min(r42)

r62=[max62330[min330up_index],max62330[min330down_index],min62330[min330up_index],min62330[min330down_index]]
r62330up=np.max(r62)
r62330down=np.min(r62)

r82330cen=r82mub330cen[min330cen_index]
r82=[max82330[min330up_index],max82330[min330down_index],min82330[min330up_index],min82330[min330down_index]]
r82330up=np.max(r82)
r82330down=np.min(r82)
####################################################################################################
chi2mub340cen=np.loadtxt(r'./addition/mub340/cmucen/final/buffer/chi2.dat')
chi3mub340cen=np.loadtxt(r'./addition/mub340/cmucen/final/buffer/chi3.dat')
chi4mub340cen=np.loadtxt(r'./addition/mub340/cmucen/final/buffer/chi4.dat')
chi6mub340cen=np.loadtxt(r'./addition/mub340/cmucen/final/buffer/chi6.dat')
chi8mub340cen=np.loadtxt(r'./addition/mub340/cmucen/final/buffer/chi8.dat')
r32mub340cen=chi3mub340cen/chi2mub340cen
r42mub340cen=chi4mub340cen/chi2mub340cen
r62mub340cen=chi6mub340cen/chi2mub340cen
r82mub340cen=chi8mub340cen/chi2mub340cen
chi2mub340up=np.loadtxt(r'./addition/mub340/cmuup/final/buffer/chi2.dat')
chi3mub340up=np.loadtxt(r'./addition/mub340/cmuup/final/buffer/chi3.dat')
chi4mub340up=np.loadtxt(r'./addition/mub340/cmuup/final/buffer/chi4.dat')
chi6mub340up=np.loadtxt(r'./addition/mub340/cmuup/final/buffer/chi6.dat')
chi8mub340up=np.loadtxt(r'./addition/mub340/cmuup/final/buffer/chi8.dat')
r32mub340up=chi3mub340up/chi2mub340up
r42mub340up=chi4mub340up/chi2mub340up
r62mub340up=chi6mub340up/chi2mub340up
r82mub340up=chi8mub340up/chi2mub340up
chi2mub340up1=np.loadtxt(r'./addition/mub340/cmuup1/final/buffer/chi2.dat')
chi3mub340up1=np.loadtxt(r'./addition/mub340/cmuup1/final/buffer/chi3.dat')
chi4mub340up1=np.loadtxt(r'./addition/mub340/cmuup1/final/buffer/chi4.dat')
chi6mub340up1=np.loadtxt(r'./addition/mub340/cmuup1/final/buffer/chi6.dat')
chi8mub340up1=np.loadtxt(r'./addition/mub340/cmuup1/final/buffer/chi8.dat')
r32mub340up1=chi3mub340up1/chi2mub340up1
r42mub340up1=chi4mub340up1/chi2mub340up1
r62mub340up1=chi6mub340up1/chi2mub340up1
r82mub340up1=chi8mub340up1/chi2mub340up1
chi2mub340up2=np.loadtxt(r'./addition/mub340/cmuup2/final/buffer/chi2.dat')
chi3mub340up2=np.loadtxt(r'./addition/mub340/cmuup2/final/buffer/chi3.dat')
chi4mub340up2=np.loadtxt(r'./addition/mub340/cmuup2/final/buffer/chi4.dat')
chi6mub340up2=np.loadtxt(r'./addition/mub340/cmuup2/final/buffer/chi6.dat')
chi8mub340up2=np.loadtxt(r'./addition/mub340/cmuup2/final/buffer/chi8.dat')
r32mub340up2=chi3mub340up2/chi2mub340up2
r42mub340up2=chi4mub340up2/chi2mub340up2
r62mub340up2=chi6mub340up2/chi2mub340up2
r82mub340up2=chi8mub340up2/chi2mub340up2
chi2mub340up3=np.loadtxt(r'./addition/mub340/cmuup3/final/buffer/chi2.dat')
chi3mub340up3=np.loadtxt(r'./addition/mub340/cmuup3/final/buffer/chi3.dat')
chi4mub340up3=np.loadtxt(r'./addition/mub340/cmuup3/final/buffer/chi4.dat')
chi6mub340up3=np.loadtxt(r'./addition/mub340/cmuup3/final/buffer/chi6.dat')
chi8mub340up3=np.loadtxt(r'./addition/mub340/cmuup3/final/buffer/chi8.dat')
r32mub340up3=chi3mub340up3/chi2mub340up3
r42mub340up3=chi4mub340up3/chi2mub340up3
r62mub340up3=chi6mub340up3/chi2mub340up3
r82mub340up3=chi8mub340up3/chi2mub340up3
chi2mub340up4=np.loadtxt(r'./addition/mub340/cmuup4/final/buffer/chi2.dat')
chi3mub340up4=np.loadtxt(r'./addition/mub340/cmuup4/final/buffer/chi3.dat')
chi4mub340up4=np.loadtxt(r'./addition/mub340/cmuup4/final/buffer/chi4.dat')
chi6mub340up4=np.loadtxt(r'./addition/mub340/cmuup4/final/buffer/chi6.dat')
chi8mub340up4=np.loadtxt(r'./addition/mub340/cmuup4/final/buffer/chi8.dat')
r32mub340up4=chi3mub340up4/chi2mub340up4
r42mub340up4=chi4mub340up4/chi2mub340up4
r62mub340up4=chi6mub340up4/chi2mub340up4
r82mub340up4=chi8mub340up4/chi2mub340up4
chi2mub340down=np.loadtxt(r'./addition/mub340/cmudown/final/buffer/chi2.dat')
chi3mub340down=np.loadtxt(r'./addition/mub340/cmudown/final/buffer/chi3.dat')
chi4mub340down=np.loadtxt(r'./addition/mub340/cmudown/final/buffer/chi4.dat')
chi6mub340down=np.loadtxt(r'./addition/mub340/cmudown/final/buffer/chi6.dat')
chi8mub340down=np.loadtxt(r'./addition/mub340/cmudown/final/buffer/chi8.dat')
r32mub340down=chi3mub340down/chi2mub340down
r42mub340down=chi4mub340down/chi2mub340down
r62mub340down=chi6mub340down/chi2mub340down
r82mub340down=chi8mub340down/chi2mub340down
chi2mub340down1=np.loadtxt(r'./addition/mub340/cmudown1/final/buffer/chi2.dat')
chi3mub340down1=np.loadtxt(r'./addition/mub340/cmudown1/final/buffer/chi3.dat')
chi4mub340down1=np.loadtxt(r'./addition/mub340/cmudown1/final/buffer/chi4.dat')
chi6mub340down1=np.loadtxt(r'./addition/mub340/cmudown1/final/buffer/chi6.dat')
chi8mub340down1=np.loadtxt(r'./addition/mub340/cmudown1/final/buffer/chi8.dat')
r32mub340down1=chi3mub340down1/chi2mub340down1
r42mub340down1=chi4mub340down1/chi2mub340down1
r62mub340down1=chi6mub340down1/chi2mub340down1
r82mub340down1=chi8mub340down1/chi2mub340down1
chi2mub340down2=np.loadtxt(r'./addition/mub340/cmudown2/final/buffer/chi2.dat')
chi3mub340down2=np.loadtxt(r'./addition/mub340/cmudown2/final/buffer/chi3.dat')
chi4mub340down2=np.loadtxt(r'./addition/mub340/cmudown2/final/buffer/chi4.dat')
chi6mub340down2=np.loadtxt(r'./addition/mub340/cmudown2/final/buffer/chi6.dat')
chi8mub340down2=np.loadtxt(r'./addition/mub340/cmudown2/final/buffer/chi8.dat')
r32mub340down2=chi3mub340down2/chi2mub340down2
r42mub340down2=chi4mub340down2/chi2mub340down2
r62mub340down2=chi6mub340down2/chi2mub340down2
r82mub340down2=chi8mub340down2/chi2mub340down2
chi2mub340down3=np.loadtxt(r'./addition/mub340/cmudown3/final/buffer/chi2.dat')
chi3mub340down3=np.loadtxt(r'./addition/mub340/cmudown3/final/buffer/chi3.dat')
chi4mub340down3=np.loadtxt(r'./addition/mub340/cmudown3/final/buffer/chi4.dat')
chi6mub340down3=np.loadtxt(r'./addition/mub340/cmudown3/final/buffer/chi6.dat')
chi8mub340down3=np.loadtxt(r'./addition/mub340/cmudown3/final/buffer/chi8.dat')
r32mub340down3=chi3mub340down3/chi2mub340down3
r42mub340down3=chi4mub340down3/chi2mub340down3
r62mub340down3=chi6mub340down3/chi2mub340down3
r82mub340down3=chi8mub340down3/chi2mub340down3
chi2mub340down4=np.loadtxt(r'./addition/mub340/cmudown4/final/buffer/chi2.dat')
chi3mub340down4=np.loadtxt(r'./addition/mub340/cmudown4/final/buffer/chi3.dat')
chi4mub340down4=np.loadtxt(r'./addition/mub340/cmudown4/final/buffer/chi4.dat')
chi6mub340down4=np.loadtxt(r'./addition/mub340/cmudown4/final/buffer/chi6.dat')
chi8mub340down4=np.loadtxt(r'./addition/mub340/cmudown4/final/buffer/chi8.dat')
r32mub340down4=chi3mub340down4/chi2mub340down4
r42mub340down4=chi4mub340down4/chi2mub340down4
r62mub340down4=chi6mub340down4/chi2mub340down4
r82mub340down4=chi8mub340down4/chi2mub340down4
r32340=np.zeros((2991,100))
r42340=np.zeros((2991,100))
r62340=np.zeros((2991,100))
r82340=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32340[:,t]=spline(T/ct[t],r32mub340up,xsame)
    else:
       if t>=10 and t<20:
          r32340[:,t]=spline(T/ct[t-10],r32mub340up1,xsame)
       else:
          if t>=20 and t<30:
             r32340[:,t]=spline(T/ct[t-20],r32mub340up2,xsame)
          else: 
             if t>=30 and t<40:
                r32340[:,t]=spline(T/ct[t-30],r32mub340up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32340[:,t]=spline(T/ct[t-40],r32mub340up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32340[:,t]=spline(T/ct[t-50],r32mub340down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32340[:,t]=spline(T/ct[t-60],r32mub340down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32340[:,t]=spline(T/ct[t-70],r32mub340down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32340[:,t]=spline(T/ct[t-80],r32mub340down3,xsame)
                            else:
                                r32340[:,t]=spline(T/ct[t-90],r32mub340down4,xsame)

for t in range(0,100):
    if t<10:
       r42340[:,t]=spline(T/ct[t],r42mub340up,xsame)
    else:
       if t>=10 and t<20:
          r42340[:,t]=spline(T/ct[t-10],r42mub340up1,xsame)
       else:
          if t>=20 and t<30:
             r42340[:,t]=spline(T/ct[t-20],r42mub340up2,xsame)
          else: 
             if t>=30 and t<40:
                r42340[:,t]=spline(T/ct[t-30],r42mub340up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42340[:,t]=spline(T/ct[t-40],r42mub340up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42340[:,t]=spline(T/ct[t-50],r42mub340down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42340[:,t]=spline(T/ct[t-60],r42mub340down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42340[:,t]=spline(T/ct[t-70],r42mub340down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42340[:,t]=spline(T/ct[t-80],r42mub340down3,xsame)
                            else:
                                r42340[:,t]=spline(T/ct[t-90],r42mub340down4,xsame)

for t in range(0,100):
    if t<10:
       r62340[:,t]=spline(T/ct[t],r62mub340up,xsame)
    else:
       if t>=10 and t<20:
          r62340[:,t]=spline(T/ct[t-10],r62mub340up1,xsame)
       else:
          if t>=20 and t<30:
             r62340[:,t]=spline(T/ct[t-20],r62mub340up2,xsame)
          else: 
             if t>=30 and t<40:
                r62340[:,t]=spline(T/ct[t-30],r62mub340up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62340[:,t]=spline(T/ct[t-40],r62mub340up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62340[:,t]=spline(T/ct[t-50],r62mub340down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62340[:,t]=spline(T/ct[t-60],r62mub340down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62340[:,t]=spline(T/ct[t-70],r62mub340down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62340[:,t]=spline(T/ct[t-80],r62mub340down3,xsame)
                            else:
                                r62340[:,t]=spline(T/ct[t-90],r62mub340down4,xsame)

for t in range(0,100):
    if t<10:
       r82340[:,t]=spline(T/ct[t],r82mub340up,xsame)
    else:
       if t>=10 and t<20:
          r82340[:,t]=spline(T/ct[t-10],r82mub340up1,xsame)
       else:
          if t>=20 and t<30:
             r82340[:,t]=spline(T/ct[t-20],r82mub340up2,xsame)
          else: 
             if t>=30 and t<40:
                r82340[:,t]=spline(T/ct[t-30],r82mub340up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82340[:,t]=spline(T/ct[t-40],r82mub340up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82340[:,t]=spline(T/ct[t-50],r82mub340down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82340[:,t]=spline(T/ct[t-60],r82mub340down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82340[:,t]=spline(T/ct[t-70],r82mub340down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82340[:,t]=spline(T/ct[t-80],r82mub340down3,xsame)
                            else:
                                r82340[:,t]=spline(T/ct[t-90],r82mub340down4,xsame)


for num in range(1,100):
    if num==1:
       max340=np.maximum(r32340[:,num-1],r32340[:,num])
       min340=np.minimum(r32340[:,num-1],r32340[:,num])
    else:
       max340=np.maximum(max340,r32340[:,num])
       min340=np.minimum(min340,r32340[:,num])

for num in range(1,100):
    if num==1:
       max42340=np.maximum(r42340[:,num-1],r42340[:,num])
       min42340=np.minimum(r42340[:,num-1],r42340[:,num])
    else:
       max42340=np.maximum(max42340,r42340[:,num])
       min42340=np.minimum(min42340,r42340[:,num])

for num in range(1,100):
    if num==1:
       max62340=np.maximum(r62340[:,num-1],r62340[:,num])
       min62340=np.minimum(r62340[:,num-1],r62340[:,num])
    else:
       max62340=np.maximum(max62340,r62340[:,num])
       min62340=np.minimum(min62340,r62340[:,num])

for num in range(1,100):
    if num==1:
       max82340=np.maximum(r82340[:,num-1],r82340[:,num])
       min82340=np.minimum(r82340[:,num-1],r82340[:,num])
    else:
       max82340=np.maximum(max82340,r82340[:,num])
       min82340=np.minimum(min82340,r82340[:,num])

r32mub340cen=spline(T/ctcen,r32mub340cen,xsame)
r42mub340cen=spline(T/ctcen,r42mub340cen,xsame)
r62mub340cen=spline(T/ctcen,r62mub340cen,xsame)
r82mub340cen=spline(T/ctcen,r82mub340cen,xsame)

dif340cen=abs(r42mub340cen-0.140553)
dif340up=abs(max42340-0.140553)
dif340down=abs(min42340-0.140553)
min340cen_index=1447#int(round(fit7[5,2]))
min340up_index=1447#int(round(fit7[5,1]))
min340down_index=1447#int(round(fit7[5,0]))
print(min340cen_index)
r32340cen=r32mub340cen[min340cen_index]
r32340hcen=r32mub340cen[Tcen[5]]
r32=[max340[min340up_index],max340[min340down_index],min340[min340up_index],min340[min340down_index]]
r32340up=np.max(r32)
r32340down=np.min(r32)

r42340cen=r42mub340cen[min340cen_index]
r62340cen=r62mub340cen[min340cen_index]
r42=[max42340[min340up_index],max42340[min340down_index],min42340[min340up_index],min42340[min340down_index]]
r42340up=np.max(r42)
r42340down=np.min(r42)

r62=[max62340[min340up_index],max62340[min340down_index],min62340[min340up_index],min62340[min340down_index]]
r62340up=np.max(r62)
r62340down=np.min(r62)

r82340cen=r82mub340cen[min340cen_index]
r82=[max82340[min340up_index],max82340[min340down_index],min82340[min340up_index],min82340[min340down_index]]
r82340up=np.max(r82)
r82340down=np.min(r82)
####################################################################################################
chi2mub350cen=np.loadtxt(r'./addition/mub350/cmucen/final/buffer/chi2.dat')
chi3mub350cen=np.loadtxt(r'./addition/mub350/cmucen/final/buffer/chi3.dat')
chi4mub350cen=np.loadtxt(r'./addition/mub350/cmucen/final/buffer/chi4.dat')
chi6mub350cen=np.loadtxt(r'./addition/mub350/cmucen/final/buffer/chi6.dat')
chi8mub350cen=np.loadtxt(r'./addition/mub350/cmucen/final/buffer/chi8.dat')
r32mub350cen=chi3mub350cen/chi2mub350cen
r42mub350cen=chi4mub350cen/chi2mub350cen
r62mub350cen=chi6mub350cen/chi2mub350cen
r82mub350cen=chi8mub350cen/chi2mub350cen
chi2mub350up=np.loadtxt(r'./addition/mub350/cmuup/final/buffer/chi2.dat')
chi3mub350up=np.loadtxt(r'./addition/mub350/cmuup/final/buffer/chi3.dat')
chi4mub350up=np.loadtxt(r'./addition/mub350/cmuup/final/buffer/chi4.dat')
chi6mub350up=np.loadtxt(r'./addition/mub350/cmuup/final/buffer/chi6.dat')
chi8mub350up=np.loadtxt(r'./addition/mub350/cmuup/final/buffer/chi8.dat')
r32mub350up=chi3mub350up/chi2mub350up
r42mub350up=chi4mub350up/chi2mub350up
r62mub350up=chi6mub350up/chi2mub350up
r82mub350up=chi8mub350up/chi2mub350up
chi2mub350up1=np.loadtxt(r'./addition/mub350/cmuup1/final/buffer/chi2.dat')
chi3mub350up1=np.loadtxt(r'./addition/mub350/cmuup1/final/buffer/chi3.dat')
chi4mub350up1=np.loadtxt(r'./addition/mub350/cmuup1/final/buffer/chi4.dat')
chi6mub350up1=np.loadtxt(r'./addition/mub350/cmuup1/final/buffer/chi6.dat')
chi8mub350up1=np.loadtxt(r'./addition/mub350/cmuup1/final/buffer/chi8.dat')
r32mub350up1=chi3mub350up1/chi2mub350up1
r42mub350up1=chi4mub350up1/chi2mub350up1
r62mub350up1=chi6mub350up1/chi2mub350up1
r82mub350up1=chi8mub350up1/chi2mub350up1
chi2mub350up2=np.loadtxt(r'./addition/mub350/cmuup2/final/buffer/chi2.dat')
chi3mub350up2=np.loadtxt(r'./addition/mub350/cmuup2/final/buffer/chi3.dat')
chi4mub350up2=np.loadtxt(r'./addition/mub350/cmuup2/final/buffer/chi4.dat')
chi6mub350up2=np.loadtxt(r'./addition/mub350/cmuup2/final/buffer/chi6.dat')
chi8mub350up2=np.loadtxt(r'./addition/mub350/cmuup2/final/buffer/chi8.dat')
r32mub350up2=chi3mub350up2/chi2mub350up2
r42mub350up2=chi4mub350up2/chi2mub350up2
r62mub350up2=chi6mub350up2/chi2mub350up2
r82mub350up2=chi8mub350up2/chi2mub350up2
chi2mub350up3=np.loadtxt(r'./addition/mub350/cmuup3/final/buffer/chi2.dat')
chi3mub350up3=np.loadtxt(r'./addition/mub350/cmuup3/final/buffer/chi3.dat')
chi4mub350up3=np.loadtxt(r'./addition/mub350/cmuup3/final/buffer/chi4.dat')
chi6mub350up3=np.loadtxt(r'./addition/mub350/cmuup3/final/buffer/chi6.dat')
chi8mub350up3=np.loadtxt(r'./addition/mub350/cmuup3/final/buffer/chi8.dat')
r32mub350up3=chi3mub350up3/chi2mub350up3
r42mub350up3=chi4mub350up3/chi2mub350up3
r62mub350up3=chi6mub350up3/chi2mub350up3
r82mub350up3=chi8mub350up3/chi2mub350up3
chi2mub350up4=np.loadtxt(r'./addition/mub350/cmuup4/final/buffer/chi2.dat')
chi3mub350up4=np.loadtxt(r'./addition/mub350/cmuup4/final/buffer/chi3.dat')
chi4mub350up4=np.loadtxt(r'./addition/mub350/cmuup4/final/buffer/chi4.dat')
chi6mub350up4=np.loadtxt(r'./addition/mub350/cmuup4/final/buffer/chi6.dat')
chi8mub350up4=np.loadtxt(r'./addition/mub350/cmuup4/final/buffer/chi8.dat')
r32mub350up4=chi3mub350up4/chi2mub350up4
r42mub350up4=chi4mub350up4/chi2mub350up4
r62mub350up4=chi6mub350up4/chi2mub350up4
r82mub350up4=chi8mub350up4/chi2mub350up4
chi2mub350down=np.loadtxt(r'./addition/mub350/cmudown/final/buffer/chi2.dat')
chi3mub350down=np.loadtxt(r'./addition/mub350/cmudown/final/buffer/chi3.dat')
chi4mub350down=np.loadtxt(r'./addition/mub350/cmudown/final/buffer/chi4.dat')
chi6mub350down=np.loadtxt(r'./addition/mub350/cmudown/final/buffer/chi6.dat')
chi8mub350down=np.loadtxt(r'./addition/mub350/cmudown/final/buffer/chi8.dat')
r32mub350down=chi3mub350down/chi2mub350down
r42mub350down=chi4mub350down/chi2mub350down
r62mub350down=chi6mub350down/chi2mub350down
r82mub350down=chi8mub350down/chi2mub350down
chi2mub350down1=np.loadtxt(r'./addition/mub350/cmudown1/final/buffer/chi2.dat')
chi3mub350down1=np.loadtxt(r'./addition/mub350/cmudown1/final/buffer/chi3.dat')
chi4mub350down1=np.loadtxt(r'./addition/mub350/cmudown1/final/buffer/chi4.dat')
chi6mub350down1=np.loadtxt(r'./addition/mub350/cmudown1/final/buffer/chi6.dat')
chi8mub350down1=np.loadtxt(r'./addition/mub350/cmudown1/final/buffer/chi8.dat')
r32mub350down1=chi3mub350down1/chi2mub350down1
r42mub350down1=chi4mub350down1/chi2mub350down1
r62mub350down1=chi6mub350down1/chi2mub350down1
r82mub350down1=chi8mub350down1/chi2mub350down1
chi2mub350down2=np.loadtxt(r'./addition/mub350/cmudown2/final/buffer/chi2.dat')
chi3mub350down2=np.loadtxt(r'./addition/mub350/cmudown2/final/buffer/chi3.dat')
chi4mub350down2=np.loadtxt(r'./addition/mub350/cmudown2/final/buffer/chi4.dat')
chi6mub350down2=np.loadtxt(r'./addition/mub350/cmudown2/final/buffer/chi6.dat')
chi8mub350down2=np.loadtxt(r'./addition/mub350/cmudown2/final/buffer/chi8.dat')
r32mub350down2=chi3mub350down2/chi2mub350down2
r42mub350down2=chi4mub350down2/chi2mub350down2
r62mub350down2=chi6mub350down2/chi2mub350down2
r82mub350down2=chi8mub350down2/chi2mub350down2
chi2mub350down3=np.loadtxt(r'./addition/mub350/cmudown3/final/buffer/chi2.dat')
chi3mub350down3=np.loadtxt(r'./addition/mub350/cmudown3/final/buffer/chi3.dat')
chi4mub350down3=np.loadtxt(r'./addition/mub350/cmudown3/final/buffer/chi4.dat')
chi6mub350down3=np.loadtxt(r'./addition/mub350/cmudown3/final/buffer/chi6.dat')
chi8mub350down3=np.loadtxt(r'./addition/mub350/cmudown3/final/buffer/chi8.dat')
r32mub350down3=chi3mub350down3/chi2mub350down3
r42mub350down3=chi4mub350down3/chi2mub350down3
r62mub350down3=chi6mub350down3/chi2mub350down3
r82mub350down3=chi8mub350down3/chi2mub350down3
chi2mub350down4=np.loadtxt(r'./addition/mub350/cmudown4/final/buffer/chi2.dat')
chi3mub350down4=np.loadtxt(r'./addition/mub350/cmudown4/final/buffer/chi3.dat')
chi4mub350down4=np.loadtxt(r'./addition/mub350/cmudown4/final/buffer/chi4.dat')
chi6mub350down4=np.loadtxt(r'./addition/mub350/cmudown4/final/buffer/chi6.dat')
chi8mub350down4=np.loadtxt(r'./addition/mub350/cmudown4/final/buffer/chi8.dat')
r32mub350down4=chi3mub350down4/chi2mub350down4
r42mub350down4=chi4mub350down4/chi2mub350down4
r62mub350down4=chi6mub350down4/chi2mub350down4
r82mub350down4=chi8mub350down4/chi2mub350down4
r32350=np.zeros((2991,100))
r42350=np.zeros((2991,100))
r62350=np.zeros((2991,100))
r82350=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32350[:,t]=spline(T/ct[t],r32mub350up,xsame)
    else:
       if t>=10 and t<20:
          r32350[:,t]=spline(T/ct[t-10],r32mub350up1,xsame)
       else:
          if t>=20 and t<30:
             r32350[:,t]=spline(T/ct[t-20],r32mub350up2,xsame)
          else: 
             if t>=30 and t<40:
                r32350[:,t]=spline(T/ct[t-30],r32mub350up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32350[:,t]=spline(T/ct[t-40],r32mub350up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32350[:,t]=spline(T/ct[t-50],r32mub350down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32350[:,t]=spline(T/ct[t-60],r32mub350down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32350[:,t]=spline(T/ct[t-70],r32mub350down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32350[:,t]=spline(T/ct[t-80],r32mub350down3,xsame)
                            else:
                                r32350[:,t]=spline(T/ct[t-90],r32mub350down4,xsame)

for t in range(0,100):
    if t<10:
       r42350[:,t]=spline(T/ct[t],r42mub350up,xsame)
    else:
       if t>=10 and t<20:
          r42350[:,t]=spline(T/ct[t-10],r42mub350up1,xsame)
       else:
          if t>=20 and t<30:
             r42350[:,t]=spline(T/ct[t-20],r42mub350up2,xsame)
          else: 
             if t>=30 and t<40:
                r42350[:,t]=spline(T/ct[t-30],r42mub350up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42350[:,t]=spline(T/ct[t-40],r42mub350up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42350[:,t]=spline(T/ct[t-50],r42mub350down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42350[:,t]=spline(T/ct[t-60],r42mub350down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42350[:,t]=spline(T/ct[t-70],r42mub350down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42350[:,t]=spline(T/ct[t-80],r42mub350down3,xsame)
                            else:
                                r42350[:,t]=spline(T/ct[t-90],r42mub350down4,xsame)

for t in range(0,100):
    if t<10:
       r62350[:,t]=spline(T/ct[t],r62mub350up,xsame)
    else:
       if t>=10 and t<20:
          r62350[:,t]=spline(T/ct[t-10],r62mub350up1,xsame)
       else:
          if t>=20 and t<30:
             r62350[:,t]=spline(T/ct[t-20],r62mub350up2,xsame)
          else: 
             if t>=30 and t<40:
                r62350[:,t]=spline(T/ct[t-30],r62mub350up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62350[:,t]=spline(T/ct[t-40],r62mub350up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62350[:,t]=spline(T/ct[t-50],r62mub350down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62350[:,t]=spline(T/ct[t-60],r62mub350down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62350[:,t]=spline(T/ct[t-70],r62mub350down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62350[:,t]=spline(T/ct[t-80],r62mub350down3,xsame)
                            else:
                                r62350[:,t]=spline(T/ct[t-90],r62mub350down4,xsame)

for t in range(0,100):
    if t<10:
       r82350[:,t]=spline(T/ct[t],r82mub350up,xsame)
    else:
       if t>=10 and t<20:
          r82350[:,t]=spline(T/ct[t-10],r82mub350up1,xsame)
       else:
          if t>=20 and t<30:
             r82350[:,t]=spline(T/ct[t-20],r82mub350up2,xsame)
          else: 
             if t>=30 and t<40:
                r82350[:,t]=spline(T/ct[t-30],r82mub350up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82350[:,t]=spline(T/ct[t-40],r82mub350up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82350[:,t]=spline(T/ct[t-50],r82mub350down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82350[:,t]=spline(T/ct[t-60],r82mub350down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82350[:,t]=spline(T/ct[t-70],r82mub350down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82350[:,t]=spline(T/ct[t-80],r82mub350down3,xsame)
                            else:
                                r82350[:,t]=spline(T/ct[t-90],r82mub350down4,xsame)


for num in range(1,100):
    if num==1:
       max350=np.maximum(r32350[:,num-1],r32350[:,num])
       min350=np.minimum(r32350[:,num-1],r32350[:,num])
    else:
       max350=np.maximum(max350,r32350[:,num])
       min350=np.minimum(min350,r32350[:,num])

for num in range(1,100):
    if num==1:
       max42350=np.maximum(r42350[:,num-1],r42350[:,num])
       min42350=np.minimum(r42350[:,num-1],r42350[:,num])
    else:
       max42350=np.maximum(max42350,r42350[:,num])
       min42350=np.minimum(min42350,r42350[:,num])

for num in range(1,100):
    if num==1:
       max62350=np.maximum(r62350[:,num-1],r62350[:,num])
       min62350=np.minimum(r62350[:,num-1],r62350[:,num])
    else:
       max62350=np.maximum(max62350,r62350[:,num])
       min62350=np.minimum(min62350,r62350[:,num])

for num in range(1,100):
    if num==1:
       max82350=np.maximum(r82350[:,num-1],r82350[:,num])
       min82350=np.minimum(r82350[:,num-1],r82350[:,num])
    else:
       max82350=np.maximum(max82350,r82350[:,num])
       min82350=np.minimum(min82350,r82350[:,num])

r32mub350cen=spline(T/ctcen,r32mub350cen,xsame)
r42mub350cen=spline(T/ctcen,r42mub350cen,xsame)
r62mub350cen=spline(T/ctcen,r62mub350cen,xsame)
r82mub350cen=spline(T/ctcen,r82mub350cen,xsame)

dif350cen=abs(r42mub350cen-0.140553)
dif350up=abs(max42350-0.140553)
dif350down=abs(min42350-0.140553)
min350cen_index=1435#int(round(fit7[5,2]))
min350up_index=1435#int(round(fit7[5,1]))
min350down_index=1435#int(round(fit7[5,0]))
print(min350cen_index)
r32350cen=r32mub350cen[min350cen_index]
r32350hcen=r32mub350cen[Tcen[5]]
r32=[max350[min350up_index],max350[min350down_index],min350[min350up_index],min350[min350down_index]]
r32350up=np.max(r32)
r32350down=np.min(r32)

r42350cen=r42mub350cen[min350cen_index]
r62350cen=r62mub350cen[min350cen_index]
r42=[max42350[min350up_index],max42350[min350down_index],min42350[min350up_index],min42350[min350down_index]]
r42350up=np.max(r42)
r42350down=np.min(r42)

r62=[max62350[min350up_index],max62350[min350down_index],min62350[min350up_index],min62350[min350down_index]]
r62350up=np.max(r62)
r62350down=np.min(r62)

r82350cen=r82mub350cen[min350cen_index]
r82=[max82350[min350up_index],max82350[min350down_index],min82350[min350up_index],min82350[min350down_index]]
r82350up=np.max(r82)
r82350down=np.min(r82)
####################################################################################################
chi2mub360cen=np.loadtxt(r'./addition/mub360/cmucen/final/buffer/chi2.dat')
chi3mub360cen=np.loadtxt(r'./addition/mub360/cmucen/final/buffer/chi3.dat')
chi4mub360cen=np.loadtxt(r'./addition/mub360/cmucen/final/buffer/chi4.dat')
chi6mub360cen=np.loadtxt(r'./addition/mub360/cmucen/final/buffer/chi6.dat')
chi8mub360cen=np.loadtxt(r'./addition/mub360/cmucen/final/buffer/chi8.dat')
r32mub360cen=chi3mub360cen/chi2mub360cen
r42mub360cen=chi4mub360cen/chi2mub360cen
r62mub360cen=chi6mub360cen/chi2mub360cen
r82mub360cen=chi8mub360cen/chi2mub360cen
chi2mub360up=np.loadtxt(r'./addition/mub360/cmuup/final/buffer/chi2.dat')
chi3mub360up=np.loadtxt(r'./addition/mub360/cmuup/final/buffer/chi3.dat')
chi4mub360up=np.loadtxt(r'./addition/mub360/cmuup/final/buffer/chi4.dat')
chi6mub360up=np.loadtxt(r'./addition/mub360/cmuup/final/buffer/chi6.dat')
chi8mub360up=np.loadtxt(r'./addition/mub360/cmuup/final/buffer/chi8.dat')
r32mub360up=chi3mub360up/chi2mub360up
r42mub360up=chi4mub360up/chi2mub360up
r62mub360up=chi6mub360up/chi2mub360up
r82mub360up=chi8mub360up/chi2mub360up
chi2mub360up1=np.loadtxt(r'./addition/mub360/cmuup1/final/buffer/chi2.dat')
chi3mub360up1=np.loadtxt(r'./addition/mub360/cmuup1/final/buffer/chi3.dat')
chi4mub360up1=np.loadtxt(r'./addition/mub360/cmuup1/final/buffer/chi4.dat')
chi6mub360up1=np.loadtxt(r'./addition/mub360/cmuup1/final/buffer/chi6.dat')
chi8mub360up1=np.loadtxt(r'./addition/mub360/cmuup1/final/buffer/chi8.dat')
r32mub360up1=chi3mub360up1/chi2mub360up1
r42mub360up1=chi4mub360up1/chi2mub360up1
r62mub360up1=chi6mub360up1/chi2mub360up1
r82mub360up1=chi8mub360up1/chi2mub360up1
chi2mub360up2=np.loadtxt(r'./addition/mub360/cmuup2/final/buffer/chi2.dat')
chi3mub360up2=np.loadtxt(r'./addition/mub360/cmuup2/final/buffer/chi3.dat')
chi4mub360up2=np.loadtxt(r'./addition/mub360/cmuup2/final/buffer/chi4.dat')
chi6mub360up2=np.loadtxt(r'./addition/mub360/cmuup2/final/buffer/chi6.dat')
chi8mub360up2=np.loadtxt(r'./addition/mub360/cmuup2/final/buffer/chi8.dat')
r32mub360up2=chi3mub360up2/chi2mub360up2
r42mub360up2=chi4mub360up2/chi2mub360up2
r62mub360up2=chi6mub360up2/chi2mub360up2
r82mub360up2=chi8mub360up2/chi2mub360up2
chi2mub360up3=np.loadtxt(r'./addition/mub360/cmuup3/final/buffer/chi2.dat')
chi3mub360up3=np.loadtxt(r'./addition/mub360/cmuup3/final/buffer/chi3.dat')
chi4mub360up3=np.loadtxt(r'./addition/mub360/cmuup3/final/buffer/chi4.dat')
chi6mub360up3=np.loadtxt(r'./addition/mub360/cmuup3/final/buffer/chi6.dat')
chi8mub360up3=np.loadtxt(r'./addition/mub360/cmuup3/final/buffer/chi8.dat')
r32mub360up3=chi3mub360up3/chi2mub360up3
r42mub360up3=chi4mub360up3/chi2mub360up3
r62mub360up3=chi6mub360up3/chi2mub360up3
r82mub360up3=chi8mub360up3/chi2mub360up3
chi2mub360up4=np.loadtxt(r'./addition/mub360/cmuup4/final/buffer/chi2.dat')
chi3mub360up4=np.loadtxt(r'./addition/mub360/cmuup4/final/buffer/chi3.dat')
chi4mub360up4=np.loadtxt(r'./addition/mub360/cmuup4/final/buffer/chi4.dat')
chi6mub360up4=np.loadtxt(r'./addition/mub360/cmuup4/final/buffer/chi6.dat')
chi8mub360up4=np.loadtxt(r'./addition/mub360/cmuup4/final/buffer/chi8.dat')
r32mub360up4=chi3mub360up4/chi2mub360up4
r42mub360up4=chi4mub360up4/chi2mub360up4
r62mub360up4=chi6mub360up4/chi2mub360up4
r82mub360up4=chi8mub360up4/chi2mub360up4
chi2mub360down=np.loadtxt(r'./addition/mub360/cmudown/final/buffer/chi2.dat')
chi3mub360down=np.loadtxt(r'./addition/mub360/cmudown/final/buffer/chi3.dat')
chi4mub360down=np.loadtxt(r'./addition/mub360/cmudown/final/buffer/chi4.dat')
chi6mub360down=np.loadtxt(r'./addition/mub360/cmudown/final/buffer/chi6.dat')
chi8mub360down=np.loadtxt(r'./addition/mub360/cmudown/final/buffer/chi8.dat')
r32mub360down=chi3mub360down/chi2mub360down
r42mub360down=chi4mub360down/chi2mub360down
r62mub360down=chi6mub360down/chi2mub360down
r82mub360down=chi8mub360down/chi2mub360down
chi2mub360down1=np.loadtxt(r'./addition/mub360/cmudown1/final/buffer/chi2.dat')
chi3mub360down1=np.loadtxt(r'./addition/mub360/cmudown1/final/buffer/chi3.dat')
chi4mub360down1=np.loadtxt(r'./addition/mub360/cmudown1/final/buffer/chi4.dat')
chi6mub360down1=np.loadtxt(r'./addition/mub360/cmudown1/final/buffer/chi6.dat')
chi8mub360down1=np.loadtxt(r'./addition/mub360/cmudown1/final/buffer/chi8.dat')
r32mub360down1=chi3mub360down1/chi2mub360down1
r42mub360down1=chi4mub360down1/chi2mub360down1
r62mub360down1=chi6mub360down1/chi2mub360down1
r82mub360down1=chi8mub360down1/chi2mub360down1
chi2mub360down2=np.loadtxt(r'./addition/mub360/cmudown2/final/buffer/chi2.dat')
chi3mub360down2=np.loadtxt(r'./addition/mub360/cmudown2/final/buffer/chi3.dat')
chi4mub360down2=np.loadtxt(r'./addition/mub360/cmudown2/final/buffer/chi4.dat')
chi6mub360down2=np.loadtxt(r'./addition/mub360/cmudown2/final/buffer/chi6.dat')
chi8mub360down2=np.loadtxt(r'./addition/mub360/cmudown2/final/buffer/chi8.dat')
r32mub360down2=chi3mub360down2/chi2mub360down2
r42mub360down2=chi4mub360down2/chi2mub360down2
r62mub360down2=chi6mub360down2/chi2mub360down2
r82mub360down2=chi8mub360down2/chi2mub360down2
chi2mub360down3=np.loadtxt(r'./addition/mub360/cmudown3/final/buffer/chi2.dat')
chi3mub360down3=np.loadtxt(r'./addition/mub360/cmudown3/final/buffer/chi3.dat')
chi4mub360down3=np.loadtxt(r'./addition/mub360/cmudown3/final/buffer/chi4.dat')
chi6mub360down3=np.loadtxt(r'./addition/mub360/cmudown3/final/buffer/chi6.dat')
chi8mub360down3=np.loadtxt(r'./addition/mub360/cmudown3/final/buffer/chi8.dat')
r32mub360down3=chi3mub360down3/chi2mub360down3
r42mub360down3=chi4mub360down3/chi2mub360down3
r62mub360down3=chi6mub360down3/chi2mub360down3
r82mub360down3=chi8mub360down3/chi2mub360down3
chi2mub360down4=np.loadtxt(r'./addition/mub360/cmudown4/final/buffer/chi2.dat')
chi3mub360down4=np.loadtxt(r'./addition/mub360/cmudown4/final/buffer/chi3.dat')
chi4mub360down4=np.loadtxt(r'./addition/mub360/cmudown4/final/buffer/chi4.dat')
chi6mub360down4=np.loadtxt(r'./addition/mub360/cmudown4/final/buffer/chi6.dat')
chi8mub360down4=np.loadtxt(r'./addition/mub360/cmudown4/final/buffer/chi8.dat')
r32mub360down4=chi3mub360down4/chi2mub360down4
r42mub360down4=chi4mub360down4/chi2mub360down4
r62mub360down4=chi6mub360down4/chi2mub360down4
r82mub360down4=chi8mub360down4/chi2mub360down4
r32360=np.zeros((2991,100))
r42360=np.zeros((2991,100))
r62360=np.zeros((2991,100))
r82360=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32360[:,t]=spline(T/ct[t],r32mub360up,xsame)
    else:
       if t>=10 and t<20:
          r32360[:,t]=spline(T/ct[t-10],r32mub360up1,xsame)
       else:
          if t>=20 and t<30:
             r32360[:,t]=spline(T/ct[t-20],r32mub360up2,xsame)
          else: 
             if t>=30 and t<40:
                r32360[:,t]=spline(T/ct[t-30],r32mub360up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32360[:,t]=spline(T/ct[t-40],r32mub360up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32360[:,t]=spline(T/ct[t-50],r32mub360down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32360[:,t]=spline(T/ct[t-60],r32mub360down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32360[:,t]=spline(T/ct[t-70],r32mub360down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32360[:,t]=spline(T/ct[t-80],r32mub360down3,xsame)
                            else:
                                r32360[:,t]=spline(T/ct[t-90],r32mub360down4,xsame)

for t in range(0,100):
    if t<10:
       r42360[:,t]=spline(T/ct[t],r42mub360up,xsame)
    else:
       if t>=10 and t<20:
          r42360[:,t]=spline(T/ct[t-10],r42mub360up1,xsame)
       else:
          if t>=20 and t<30:
             r42360[:,t]=spline(T/ct[t-20],r42mub360up2,xsame)
          else: 
             if t>=30 and t<40:
                r42360[:,t]=spline(T/ct[t-30],r42mub360up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42360[:,t]=spline(T/ct[t-40],r42mub360up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42360[:,t]=spline(T/ct[t-50],r42mub360down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42360[:,t]=spline(T/ct[t-60],r42mub360down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42360[:,t]=spline(T/ct[t-70],r42mub360down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42360[:,t]=spline(T/ct[t-80],r42mub360down3,xsame)
                            else:
                                r42360[:,t]=spline(T/ct[t-90],r42mub360down4,xsame)

for t in range(0,100):
    if t<10:
       r62360[:,t]=spline(T/ct[t],r62mub360up,xsame)
    else:
       if t>=10 and t<20:
          r62360[:,t]=spline(T/ct[t-10],r62mub360up1,xsame)
       else:
          if t>=20 and t<30:
             r62360[:,t]=spline(T/ct[t-20],r62mub360up2,xsame)
          else: 
             if t>=30 and t<40:
                r62360[:,t]=spline(T/ct[t-30],r62mub360up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62360[:,t]=spline(T/ct[t-40],r62mub360up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62360[:,t]=spline(T/ct[t-50],r62mub360down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62360[:,t]=spline(T/ct[t-60],r62mub360down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62360[:,t]=spline(T/ct[t-70],r62mub360down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62360[:,t]=spline(T/ct[t-80],r62mub360down3,xsame)
                            else:
                                r62360[:,t]=spline(T/ct[t-90],r62mub360down4,xsame)

for t in range(0,100):
    if t<10:
       r82360[:,t]=spline(T/ct[t],r82mub360up,xsame)
    else:
       if t>=10 and t<20:
          r82360[:,t]=spline(T/ct[t-10],r82mub360up1,xsame)
       else:
          if t>=20 and t<30:
             r82360[:,t]=spline(T/ct[t-20],r82mub360up2,xsame)
          else: 
             if t>=30 and t<40:
                r82360[:,t]=spline(T/ct[t-30],r82mub360up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82360[:,t]=spline(T/ct[t-40],r82mub360up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82360[:,t]=spline(T/ct[t-50],r82mub360down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82360[:,t]=spline(T/ct[t-60],r82mub360down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82360[:,t]=spline(T/ct[t-70],r82mub360down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82360[:,t]=spline(T/ct[t-80],r82mub360down3,xsame)
                            else:
                                r82360[:,t]=spline(T/ct[t-90],r82mub360down4,xsame)


for num in range(1,100):
    if num==1:
       max360=np.maximum(r32360[:,num-1],r32360[:,num])
       min360=np.minimum(r32360[:,num-1],r32360[:,num])
    else:
       max360=np.maximum(max360,r32360[:,num])
       min360=np.minimum(min360,r32360[:,num])

for num in range(1,100):
    if num==1:
       max42360=np.maximum(r42360[:,num-1],r42360[:,num])
       min42360=np.minimum(r42360[:,num-1],r42360[:,num])
    else:
       max42360=np.maximum(max42360,r42360[:,num])
       min42360=np.minimum(min42360,r42360[:,num])

for num in range(1,100):
    if num==1:
       max62360=np.maximum(r62360[:,num-1],r62360[:,num])
       min62360=np.minimum(r62360[:,num-1],r62360[:,num])
    else:
       max62360=np.maximum(max62360,r62360[:,num])
       min62360=np.minimum(min62360,r62360[:,num])

for num in range(1,100):
    if num==1:
       max82360=np.maximum(r82360[:,num-1],r82360[:,num])
       min82360=np.minimum(r82360[:,num-1],r82360[:,num])
    else:
       max82360=np.maximum(max82360,r82360[:,num])
       min82360=np.minimum(min82360,r82360[:,num])

r32mub360cen=spline(T/ctcen,r32mub360cen,xsame)
r42mub360cen=spline(T/ctcen,r42mub360cen,xsame)
r62mub360cen=spline(T/ctcen,r62mub360cen,xsame)
r82mub360cen=spline(T/ctcen,r82mub360cen,xsame)

dif360cen=abs(r42mub360cen-0.140553)
dif360up=abs(max42360-0.140553)
dif360down=abs(min42360-0.140553)
min360cen_index=1422#int(round(fit7[5,2]))
min360up_index=1422#int(round(fit7[5,1]))
min360down_index=1422#int(round(fit7[5,0]))
print(min360cen_index)
r32360cen=r32mub360cen[min360cen_index]
r32360hcen=r32mub360cen[Tcen[5]]
r32=[max360[min360up_index],max360[min360down_index],min360[min360up_index],min360[min360down_index]]
r32360up=np.max(r32)
r32360down=np.min(r32)

r42360cen=r42mub360cen[min360cen_index]
r62360cen=r62mub360cen[min360cen_index]
r42=[max42360[min360up_index],max42360[min360down_index],min42360[min360up_index],min42360[min360down_index]]
r42360up=np.max(r42)
r42360down=np.min(r42)

r62=[max62360[min360up_index],max62360[min360down_index],min62360[min360up_index],min62360[min360down_index]]
r62360up=np.max(r62)
r62360down=np.min(r62)

r82360cen=r82mub360cen[min360cen_index]
r82=[max82360[min360up_index],max82360[min360down_index],min82360[min360up_index],min82360[min360down_index]]
r82360up=np.max(r82)
r82360down=np.min(r82)
####################################################################################################
chi2mub370cen=np.loadtxt(r'./addition/mub370/cmucen/final/buffer/chi2.dat')
chi3mub370cen=np.loadtxt(r'./addition/mub370/cmucen/final/buffer/chi3.dat')
chi4mub370cen=np.loadtxt(r'./addition/mub370/cmucen/final/buffer/chi4.dat')
chi6mub370cen=np.loadtxt(r'./addition/mub370/cmucen/final/buffer/chi6.dat')
chi8mub370cen=np.loadtxt(r'./addition/mub370/cmucen/final/buffer/chi8.dat')
r32mub370cen=chi3mub370cen/chi2mub370cen
r42mub370cen=chi4mub370cen/chi2mub370cen
r62mub370cen=chi6mub370cen/chi2mub370cen
r82mub370cen=chi8mub370cen/chi2mub370cen
chi2mub370up=np.loadtxt(r'./addition/mub370/cmuup/final/buffer/chi2.dat')
chi3mub370up=np.loadtxt(r'./addition/mub370/cmuup/final/buffer/chi3.dat')
chi4mub370up=np.loadtxt(r'./addition/mub370/cmuup/final/buffer/chi4.dat')
chi6mub370up=np.loadtxt(r'./addition/mub370/cmuup/final/buffer/chi6.dat')
chi8mub370up=np.loadtxt(r'./addition/mub370/cmuup/final/buffer/chi8.dat')
r32mub370up=chi3mub370up/chi2mub370up
r42mub370up=chi4mub370up/chi2mub370up
r62mub370up=chi6mub370up/chi2mub370up
r82mub370up=chi8mub370up/chi2mub370up
chi2mub370up1=np.loadtxt(r'./addition/mub370/cmuup1/final/buffer/chi2.dat')
chi3mub370up1=np.loadtxt(r'./addition/mub370/cmuup1/final/buffer/chi3.dat')
chi4mub370up1=np.loadtxt(r'./addition/mub370/cmuup1/final/buffer/chi4.dat')
chi6mub370up1=np.loadtxt(r'./addition/mub370/cmuup1/final/buffer/chi6.dat')
chi8mub370up1=np.loadtxt(r'./addition/mub370/cmuup1/final/buffer/chi8.dat')
r32mub370up1=chi3mub370up1/chi2mub370up1
r42mub370up1=chi4mub370up1/chi2mub370up1
r62mub370up1=chi6mub370up1/chi2mub370up1
r82mub370up1=chi8mub370up1/chi2mub370up1
chi2mub370up2=np.loadtxt(r'./addition/mub370/cmuup2/final/buffer/chi2.dat')
chi3mub370up2=np.loadtxt(r'./addition/mub370/cmuup2/final/buffer/chi3.dat')
chi4mub370up2=np.loadtxt(r'./addition/mub370/cmuup2/final/buffer/chi4.dat')
chi6mub370up2=np.loadtxt(r'./addition/mub370/cmuup2/final/buffer/chi6.dat')
chi8mub370up2=np.loadtxt(r'./addition/mub370/cmuup2/final/buffer/chi8.dat')
r32mub370up2=chi3mub370up2/chi2mub370up2
r42mub370up2=chi4mub370up2/chi2mub370up2
r62mub370up2=chi6mub370up2/chi2mub370up2
r82mub370up2=chi8mub370up2/chi2mub370up2
chi2mub370up3=np.loadtxt(r'./addition/mub370/cmuup3/final/buffer/chi2.dat')
chi3mub370up3=np.loadtxt(r'./addition/mub370/cmuup3/final/buffer/chi3.dat')
chi4mub370up3=np.loadtxt(r'./addition/mub370/cmuup3/final/buffer/chi4.dat')
chi6mub370up3=np.loadtxt(r'./addition/mub370/cmuup3/final/buffer/chi6.dat')
chi8mub370up3=np.loadtxt(r'./addition/mub370/cmuup3/final/buffer/chi8.dat')
r32mub370up3=chi3mub370up3/chi2mub370up3
r42mub370up3=chi4mub370up3/chi2mub370up3
r62mub370up3=chi6mub370up3/chi2mub370up3
r82mub370up3=chi8mub370up3/chi2mub370up3
chi2mub370up4=np.loadtxt(r'./addition/mub370/cmuup4/final/buffer/chi2.dat')
chi3mub370up4=np.loadtxt(r'./addition/mub370/cmuup4/final/buffer/chi3.dat')
chi4mub370up4=np.loadtxt(r'./addition/mub370/cmuup4/final/buffer/chi4.dat')
chi6mub370up4=np.loadtxt(r'./addition/mub370/cmuup4/final/buffer/chi6.dat')
chi8mub370up4=np.loadtxt(r'./addition/mub370/cmuup4/final/buffer/chi8.dat')
r32mub370up4=chi3mub370up4/chi2mub370up4
r42mub370up4=chi4mub370up4/chi2mub370up4
r62mub370up4=chi6mub370up4/chi2mub370up4
r82mub370up4=chi8mub370up4/chi2mub370up4
chi2mub370down=np.loadtxt(r'./addition/mub370/cmudown/final/buffer/chi2.dat')
chi3mub370down=np.loadtxt(r'./addition/mub370/cmudown/final/buffer/chi3.dat')
chi4mub370down=np.loadtxt(r'./addition/mub370/cmudown/final/buffer/chi4.dat')
chi6mub370down=np.loadtxt(r'./addition/mub370/cmudown/final/buffer/chi6.dat')
chi8mub370down=np.loadtxt(r'./addition/mub370/cmudown/final/buffer/chi8.dat')
r32mub370down=chi3mub370down/chi2mub370down
r42mub370down=chi4mub370down/chi2mub370down
r62mub370down=chi6mub370down/chi2mub370down
r82mub370down=chi8mub370down/chi2mub370down
chi2mub370down1=np.loadtxt(r'./addition/mub370/cmudown1/final/buffer/chi2.dat')
chi3mub370down1=np.loadtxt(r'./addition/mub370/cmudown1/final/buffer/chi3.dat')
chi4mub370down1=np.loadtxt(r'./addition/mub370/cmudown1/final/buffer/chi4.dat')
chi6mub370down1=np.loadtxt(r'./addition/mub370/cmudown1/final/buffer/chi6.dat')
chi8mub370down1=np.loadtxt(r'./addition/mub370/cmudown1/final/buffer/chi8.dat')
r32mub370down1=chi3mub370down1/chi2mub370down1
r42mub370down1=chi4mub370down1/chi2mub370down1
r62mub370down1=chi6mub370down1/chi2mub370down1
r82mub370down1=chi8mub370down1/chi2mub370down1
chi2mub370down2=np.loadtxt(r'./addition/mub370/cmudown2/final/buffer/chi2.dat')
chi3mub370down2=np.loadtxt(r'./addition/mub370/cmudown2/final/buffer/chi3.dat')
chi4mub370down2=np.loadtxt(r'./addition/mub370/cmudown2/final/buffer/chi4.dat')
chi6mub370down2=np.loadtxt(r'./addition/mub370/cmudown2/final/buffer/chi6.dat')
chi8mub370down2=np.loadtxt(r'./addition/mub370/cmudown2/final/buffer/chi8.dat')
r32mub370down2=chi3mub370down2/chi2mub370down2
r42mub370down2=chi4mub370down2/chi2mub370down2
r62mub370down2=chi6mub370down2/chi2mub370down2
r82mub370down2=chi8mub370down2/chi2mub370down2
chi2mub370down3=np.loadtxt(r'./addition/mub370/cmudown3/final/buffer/chi2.dat')
chi3mub370down3=np.loadtxt(r'./addition/mub370/cmudown3/final/buffer/chi3.dat')
chi4mub370down3=np.loadtxt(r'./addition/mub370/cmudown3/final/buffer/chi4.dat')
chi6mub370down3=np.loadtxt(r'./addition/mub370/cmudown3/final/buffer/chi6.dat')
chi8mub370down3=np.loadtxt(r'./addition/mub370/cmudown3/final/buffer/chi8.dat')
r32mub370down3=chi3mub370down3/chi2mub370down3
r42mub370down3=chi4mub370down3/chi2mub370down3
r62mub370down3=chi6mub370down3/chi2mub370down3
r82mub370down3=chi8mub370down3/chi2mub370down3
chi2mub370down4=np.loadtxt(r'./addition/mub370/cmudown4/final/buffer/chi2.dat')
chi3mub370down4=np.loadtxt(r'./addition/mub370/cmudown4/final/buffer/chi3.dat')
chi4mub370down4=np.loadtxt(r'./addition/mub370/cmudown4/final/buffer/chi4.dat')
chi6mub370down4=np.loadtxt(r'./addition/mub370/cmudown4/final/buffer/chi6.dat')
chi8mub370down4=np.loadtxt(r'./addition/mub370/cmudown4/final/buffer/chi8.dat')
r32mub370down4=chi3mub370down4/chi2mub370down4
r42mub370down4=chi4mub370down4/chi2mub370down4
r62mub370down4=chi6mub370down4/chi2mub370down4
r82mub370down4=chi8mub370down4/chi2mub370down4
r32370=np.zeros((2991,100))
r42370=np.zeros((2991,100))
r62370=np.zeros((2991,100))
r82370=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32370[:,t]=spline(T/ct[t],r32mub370up,xsame)
    else:
       if t>=10 and t<20:
          r32370[:,t]=spline(T/ct[t-10],r32mub370up1,xsame)
       else:
          if t>=20 and t<30:
             r32370[:,t]=spline(T/ct[t-20],r32mub370up2,xsame)
          else: 
             if t>=30 and t<40:
                r32370[:,t]=spline(T/ct[t-30],r32mub370up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32370[:,t]=spline(T/ct[t-40],r32mub370up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32370[:,t]=spline(T/ct[t-50],r32mub370down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32370[:,t]=spline(T/ct[t-60],r32mub370down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32370[:,t]=spline(T/ct[t-70],r32mub370down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32370[:,t]=spline(T/ct[t-80],r32mub370down3,xsame)
                            else:
                                r32370[:,t]=spline(T/ct[t-90],r32mub370down4,xsame)

for t in range(0,100):
    if t<10:
       r42370[:,t]=spline(T/ct[t],r42mub370up,xsame)
    else:
       if t>=10 and t<20:
          r42370[:,t]=spline(T/ct[t-10],r42mub370up1,xsame)
       else:
          if t>=20 and t<30:
             r42370[:,t]=spline(T/ct[t-20],r42mub370up2,xsame)
          else: 
             if t>=30 and t<40:
                r42370[:,t]=spline(T/ct[t-30],r42mub370up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42370[:,t]=spline(T/ct[t-40],r42mub370up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42370[:,t]=spline(T/ct[t-50],r42mub370down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42370[:,t]=spline(T/ct[t-60],r42mub370down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42370[:,t]=spline(T/ct[t-70],r42mub370down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42370[:,t]=spline(T/ct[t-80],r42mub370down3,xsame)
                            else:
                                r42370[:,t]=spline(T/ct[t-90],r42mub370down4,xsame)

for t in range(0,100):
    if t<10:
       r62370[:,t]=spline(T/ct[t],r62mub370up,xsame)
    else:
       if t>=10 and t<20:
          r62370[:,t]=spline(T/ct[t-10],r62mub370up1,xsame)
       else:
          if t>=20 and t<30:
             r62370[:,t]=spline(T/ct[t-20],r62mub370up2,xsame)
          else: 
             if t>=30 and t<40:
                r62370[:,t]=spline(T/ct[t-30],r62mub370up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62370[:,t]=spline(T/ct[t-40],r62mub370up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62370[:,t]=spline(T/ct[t-50],r62mub370down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62370[:,t]=spline(T/ct[t-60],r62mub370down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62370[:,t]=spline(T/ct[t-70],r62mub370down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62370[:,t]=spline(T/ct[t-80],r62mub370down3,xsame)
                            else:
                                r62370[:,t]=spline(T/ct[t-90],r62mub370down4,xsame)

for t in range(0,100):
    if t<10:
       r82370[:,t]=spline(T/ct[t],r82mub370up,xsame)
    else:
       if t>=10 and t<20:
          r82370[:,t]=spline(T/ct[t-10],r82mub370up1,xsame)
       else:
          if t>=20 and t<30:
             r82370[:,t]=spline(T/ct[t-20],r82mub370up2,xsame)
          else: 
             if t>=30 and t<40:
                r82370[:,t]=spline(T/ct[t-30],r82mub370up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82370[:,t]=spline(T/ct[t-40],r82mub370up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82370[:,t]=spline(T/ct[t-50],r82mub370down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82370[:,t]=spline(T/ct[t-60],r82mub370down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82370[:,t]=spline(T/ct[t-70],r82mub370down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82370[:,t]=spline(T/ct[t-80],r82mub370down3,xsame)
                            else:
                                r82370[:,t]=spline(T/ct[t-90],r82mub370down4,xsame)


for num in range(1,100):
    if num==1:
       max370=np.maximum(r32370[:,num-1],r32370[:,num])
       min370=np.minimum(r32370[:,num-1],r32370[:,num])
    else:
       max370=np.maximum(max370,r32370[:,num])
       min370=np.minimum(min370,r32370[:,num])

for num in range(1,100):
    if num==1:
       max42370=np.maximum(r42370[:,num-1],r42370[:,num])
       min42370=np.minimum(r42370[:,num-1],r42370[:,num])
    else:
       max42370=np.maximum(max42370,r42370[:,num])
       min42370=np.minimum(min42370,r42370[:,num])

for num in range(1,100):
    if num==1:
       max62370=np.maximum(r62370[:,num-1],r62370[:,num])
       min62370=np.minimum(r62370[:,num-1],r62370[:,num])
    else:
       max62370=np.maximum(max62370,r62370[:,num])
       min62370=np.minimum(min62370,r62370[:,num])

for num in range(1,100):
    if num==1:
       max82370=np.maximum(r82370[:,num-1],r82370[:,num])
       min82370=np.minimum(r82370[:,num-1],r82370[:,num])
    else:
       max82370=np.maximum(max82370,r82370[:,num])
       min82370=np.minimum(min82370,r82370[:,num])

r32mub370cen=spline(T/ctcen,r32mub370cen,xsame)
r42mub370cen=spline(T/ctcen,r42mub370cen,xsame)
r62mub370cen=spline(T/ctcen,r62mub370cen,xsame)
r82mub370cen=spline(T/ctcen,r82mub370cen,xsame)

dif370cen=abs(r42mub370cen-0.140553)
dif370up=abs(max42370-0.140553)
dif370down=abs(min42370-0.140553)
min370cen_index=1409#int(round(fit7[5,2]))
min370up_index=1409#int(round(fit7[5,1]))
min370down_index=1409#int(round(fit7[5,0]))
print(min370cen_index)
r32370cen=r32mub370cen[min370cen_index]
r32370hcen=r32mub370cen[Tcen[5]]
r32=[max370[min370up_index],max370[min370down_index],min370[min370up_index],min370[min370down_index]]
r32370up=np.max(r32)
r32370down=np.min(r32)

r42370cen=r42mub370cen[min370cen_index]
r62370cen=r62mub370cen[min370cen_index]
r42=[max42370[min370up_index],max42370[min370down_index],min42370[min370up_index],min42370[min370down_index]]
r42370up=np.max(r42)
r42370down=np.min(r42)

r62=[max62370[min370up_index],max62370[min370down_index],min62370[min370up_index],min62370[min370down_index]]
r62370up=np.max(r62)
r62370down=np.min(r62)

r82370cen=r82mub370cen[min370cen_index]
r82=[max82370[min370up_index],max82370[min370down_index],min82370[min370up_index],min82370[min370down_index]]
r82370up=np.max(r82)
r82370down=np.min(r82)
####################################################################################################
chi2mub380cen=np.loadtxt(r'./addition/mub380/cmucen/final/buffer/chi2.dat')
chi3mub380cen=np.loadtxt(r'./addition/mub380/cmucen/final/buffer/chi3.dat')
chi4mub380cen=np.loadtxt(r'./addition/mub380/cmucen/final/buffer/chi4.dat')
chi6mub380cen=np.loadtxt(r'./addition/mub380/cmucen/final/buffer/chi6.dat')
chi8mub380cen=np.loadtxt(r'./addition/mub380/cmucen/final/buffer/chi8.dat')
r32mub380cen=chi3mub380cen/chi2mub380cen
r42mub380cen=chi4mub380cen/chi2mub380cen
r62mub380cen=chi6mub380cen/chi2mub380cen
r82mub380cen=chi8mub380cen/chi2mub380cen
chi2mub380up=np.loadtxt(r'./addition/mub380/cmuup/final/buffer/chi2.dat')
chi3mub380up=np.loadtxt(r'./addition/mub380/cmuup/final/buffer/chi3.dat')
chi4mub380up=np.loadtxt(r'./addition/mub380/cmuup/final/buffer/chi4.dat')
chi6mub380up=np.loadtxt(r'./addition/mub380/cmuup/final/buffer/chi6.dat')
chi8mub380up=np.loadtxt(r'./addition/mub380/cmuup/final/buffer/chi8.dat')
r32mub380up=chi3mub380up/chi2mub380up
r42mub380up=chi4mub380up/chi2mub380up
r62mub380up=chi6mub380up/chi2mub380up
r82mub380up=chi8mub380up/chi2mub380up
chi2mub380up1=np.loadtxt(r'./addition/mub380/cmuup1/final/buffer/chi2.dat')
chi3mub380up1=np.loadtxt(r'./addition/mub380/cmuup1/final/buffer/chi3.dat')
chi4mub380up1=np.loadtxt(r'./addition/mub380/cmuup1/final/buffer/chi4.dat')
chi6mub380up1=np.loadtxt(r'./addition/mub380/cmuup1/final/buffer/chi6.dat')
chi8mub380up1=np.loadtxt(r'./addition/mub380/cmuup1/final/buffer/chi8.dat')
r32mub380up1=chi3mub380up1/chi2mub380up1
r42mub380up1=chi4mub380up1/chi2mub380up1
r62mub380up1=chi6mub380up1/chi2mub380up1
r82mub380up1=chi8mub380up1/chi2mub380up1
chi2mub380up2=np.loadtxt(r'./addition/mub380/cmuup2/final/buffer/chi2.dat')
chi3mub380up2=np.loadtxt(r'./addition/mub380/cmuup2/final/buffer/chi3.dat')
chi4mub380up2=np.loadtxt(r'./addition/mub380/cmuup2/final/buffer/chi4.dat')
chi6mub380up2=np.loadtxt(r'./addition/mub380/cmuup2/final/buffer/chi6.dat')
chi8mub380up2=np.loadtxt(r'./addition/mub380/cmuup2/final/buffer/chi8.dat')
r32mub380up2=chi3mub380up2/chi2mub380up2
r42mub380up2=chi4mub380up2/chi2mub380up2
r62mub380up2=chi6mub380up2/chi2mub380up2
r82mub380up2=chi8mub380up2/chi2mub380up2
chi2mub380up3=np.loadtxt(r'./addition/mub380/cmuup3/final/buffer/chi2.dat')
chi3mub380up3=np.loadtxt(r'./addition/mub380/cmuup3/final/buffer/chi3.dat')
chi4mub380up3=np.loadtxt(r'./addition/mub380/cmuup3/final/buffer/chi4.dat')
chi6mub380up3=np.loadtxt(r'./addition/mub380/cmuup3/final/buffer/chi6.dat')
chi8mub380up3=np.loadtxt(r'./addition/mub380/cmuup3/final/buffer/chi8.dat')
r32mub380up3=chi3mub380up3/chi2mub380up3
r42mub380up3=chi4mub380up3/chi2mub380up3
r62mub380up3=chi6mub380up3/chi2mub380up3
r82mub380up3=chi8mub380up3/chi2mub380up3
chi2mub380up4=np.loadtxt(r'./addition/mub380/cmuup4/final/buffer/chi2.dat')
chi3mub380up4=np.loadtxt(r'./addition/mub380/cmuup4/final/buffer/chi3.dat')
chi4mub380up4=np.loadtxt(r'./addition/mub380/cmuup4/final/buffer/chi4.dat')
chi6mub380up4=np.loadtxt(r'./addition/mub380/cmuup4/final/buffer/chi6.dat')
chi8mub380up4=np.loadtxt(r'./addition/mub380/cmuup4/final/buffer/chi8.dat')
r32mub380up4=chi3mub380up4/chi2mub380up4
r42mub380up4=chi4mub380up4/chi2mub380up4
r62mub380up4=chi6mub380up4/chi2mub380up4
r82mub380up4=chi8mub380up4/chi2mub380up4
chi2mub380down=np.loadtxt(r'./addition/mub380/cmudown/final/buffer/chi2.dat')
chi3mub380down=np.loadtxt(r'./addition/mub380/cmudown/final/buffer/chi3.dat')
chi4mub380down=np.loadtxt(r'./addition/mub380/cmudown/final/buffer/chi4.dat')
chi6mub380down=np.loadtxt(r'./addition/mub380/cmudown/final/buffer/chi6.dat')
chi8mub380down=np.loadtxt(r'./addition/mub380/cmudown/final/buffer/chi8.dat')
r32mub380down=chi3mub380down/chi2mub380down
r42mub380down=chi4mub380down/chi2mub380down
r62mub380down=chi6mub380down/chi2mub380down
r82mub380down=chi8mub380down/chi2mub380down
chi2mub380down1=np.loadtxt(r'./addition/mub380/cmudown1/final/buffer/chi2.dat')
chi3mub380down1=np.loadtxt(r'./addition/mub380/cmudown1/final/buffer/chi3.dat')
chi4mub380down1=np.loadtxt(r'./addition/mub380/cmudown1/final/buffer/chi4.dat')
chi6mub380down1=np.loadtxt(r'./addition/mub380/cmudown1/final/buffer/chi6.dat')
chi8mub380down1=np.loadtxt(r'./addition/mub380/cmudown1/final/buffer/chi8.dat')
r32mub380down1=chi3mub380down1/chi2mub380down1
r42mub380down1=chi4mub380down1/chi2mub380down1
r62mub380down1=chi6mub380down1/chi2mub380down1
r82mub380down1=chi8mub380down1/chi2mub380down1
chi2mub380down2=np.loadtxt(r'./addition/mub380/cmudown2/final/buffer/chi2.dat')
chi3mub380down2=np.loadtxt(r'./addition/mub380/cmudown2/final/buffer/chi3.dat')
chi4mub380down2=np.loadtxt(r'./addition/mub380/cmudown2/final/buffer/chi4.dat')
chi6mub380down2=np.loadtxt(r'./addition/mub380/cmudown2/final/buffer/chi6.dat')
chi8mub380down2=np.loadtxt(r'./addition/mub380/cmudown2/final/buffer/chi8.dat')
r32mub380down2=chi3mub380down2/chi2mub380down2
r42mub380down2=chi4mub380down2/chi2mub380down2
r62mub380down2=chi6mub380down2/chi2mub380down2
r82mub380down2=chi8mub380down2/chi2mub380down2
chi2mub380down3=np.loadtxt(r'./addition/mub380/cmudown3/final/buffer/chi2.dat')
chi3mub380down3=np.loadtxt(r'./addition/mub380/cmudown3/final/buffer/chi3.dat')
chi4mub380down3=np.loadtxt(r'./addition/mub380/cmudown3/final/buffer/chi4.dat')
chi6mub380down3=np.loadtxt(r'./addition/mub380/cmudown3/final/buffer/chi6.dat')
chi8mub380down3=np.loadtxt(r'./addition/mub380/cmudown3/final/buffer/chi8.dat')
r32mub380down3=chi3mub380down3/chi2mub380down3
r42mub380down3=chi4mub380down3/chi2mub380down3
r62mub380down3=chi6mub380down3/chi2mub380down3
r82mub380down3=chi8mub380down3/chi2mub380down3
chi2mub380down4=np.loadtxt(r'./addition/mub380/cmudown4/final/buffer/chi2.dat')
chi3mub380down4=np.loadtxt(r'./addition/mub380/cmudown4/final/buffer/chi3.dat')
chi4mub380down4=np.loadtxt(r'./addition/mub380/cmudown4/final/buffer/chi4.dat')
chi6mub380down4=np.loadtxt(r'./addition/mub380/cmudown4/final/buffer/chi6.dat')
chi8mub380down4=np.loadtxt(r'./addition/mub380/cmudown4/final/buffer/chi8.dat')
r32mub380down4=chi3mub380down4/chi2mub380down4
r42mub380down4=chi4mub380down4/chi2mub380down4
r62mub380down4=chi6mub380down4/chi2mub380down4
r82mub380down4=chi8mub380down4/chi2mub380down4
r32380=np.zeros((2991,100))
r42380=np.zeros((2991,100))
r62380=np.zeros((2991,100))
r82380=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32380[:,t]=spline(T/ct[t],r32mub380up,xsame)
    else:
       if t>=10 and t<20:
          r32380[:,t]=spline(T/ct[t-10],r32mub380up1,xsame)
       else:
          if t>=20 and t<30:
             r32380[:,t]=spline(T/ct[t-20],r32mub380up2,xsame)
          else: 
             if t>=30 and t<40:
                r32380[:,t]=spline(T/ct[t-30],r32mub380up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32380[:,t]=spline(T/ct[t-40],r32mub380up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32380[:,t]=spline(T/ct[t-50],r32mub380down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32380[:,t]=spline(T/ct[t-60],r32mub380down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32380[:,t]=spline(T/ct[t-70],r32mub380down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32380[:,t]=spline(T/ct[t-80],r32mub380down3,xsame)
                            else:
                                r32380[:,t]=spline(T/ct[t-90],r32mub380down4,xsame)

for t in range(0,100):
    if t<10:
       r42380[:,t]=spline(T/ct[t],r42mub380up,xsame)
    else:
       if t>=10 and t<20:
          r42380[:,t]=spline(T/ct[t-10],r42mub380up1,xsame)
       else:
          if t>=20 and t<30:
             r42380[:,t]=spline(T/ct[t-20],r42mub380up2,xsame)
          else: 
             if t>=30 and t<40:
                r42380[:,t]=spline(T/ct[t-30],r42mub380up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42380[:,t]=spline(T/ct[t-40],r42mub380up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42380[:,t]=spline(T/ct[t-50],r42mub380down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42380[:,t]=spline(T/ct[t-60],r42mub380down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42380[:,t]=spline(T/ct[t-70],r42mub380down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42380[:,t]=spline(T/ct[t-80],r42mub380down3,xsame)
                            else:
                                r42380[:,t]=spline(T/ct[t-90],r42mub380down4,xsame)

for t in range(0,100):
    if t<10:
       r62380[:,t]=spline(T/ct[t],r62mub380up,xsame)
    else:
       if t>=10 and t<20:
          r62380[:,t]=spline(T/ct[t-10],r62mub380up1,xsame)
       else:
          if t>=20 and t<30:
             r62380[:,t]=spline(T/ct[t-20],r62mub380up2,xsame)
          else: 
             if t>=30 and t<40:
                r62380[:,t]=spline(T/ct[t-30],r62mub380up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62380[:,t]=spline(T/ct[t-40],r62mub380up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62380[:,t]=spline(T/ct[t-50],r62mub380down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62380[:,t]=spline(T/ct[t-60],r62mub380down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62380[:,t]=spline(T/ct[t-70],r62mub380down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62380[:,t]=spline(T/ct[t-80],r62mub380down3,xsame)
                            else:
                                r62380[:,t]=spline(T/ct[t-90],r62mub380down4,xsame)

for t in range(0,100):
    if t<10:
       r82380[:,t]=spline(T/ct[t],r82mub380up,xsame)
    else:
       if t>=10 and t<20:
          r82380[:,t]=spline(T/ct[t-10],r82mub380up1,xsame)
       else:
          if t>=20 and t<30:
             r82380[:,t]=spline(T/ct[t-20],r82mub380up2,xsame)
          else: 
             if t>=30 and t<40:
                r82380[:,t]=spline(T/ct[t-30],r82mub380up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82380[:,t]=spline(T/ct[t-40],r82mub380up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82380[:,t]=spline(T/ct[t-50],r82mub380down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82380[:,t]=spline(T/ct[t-60],r82mub380down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82380[:,t]=spline(T/ct[t-70],r82mub380down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82380[:,t]=spline(T/ct[t-80],r82mub380down3,xsame)
                            else:
                                r82380[:,t]=spline(T/ct[t-90],r82mub380down4,xsame)


for num in range(1,100):
    if num==1:
       max380=np.maximum(r32380[:,num-1],r32380[:,num])
       min380=np.minimum(r32380[:,num-1],r32380[:,num])
    else:
       max380=np.maximum(max380,r32380[:,num])
       min380=np.minimum(min380,r32380[:,num])

for num in range(1,100):
    if num==1:
       max42380=np.maximum(r42380[:,num-1],r42380[:,num])
       min42380=np.minimum(r42380[:,num-1],r42380[:,num])
    else:
       max42380=np.maximum(max42380,r42380[:,num])
       min42380=np.minimum(min42380,r42380[:,num])

for num in range(1,100):
    if num==1:
       max62380=np.maximum(r62380[:,num-1],r62380[:,num])
       min62380=np.minimum(r62380[:,num-1],r62380[:,num])
    else:
       max62380=np.maximum(max62380,r62380[:,num])
       min62380=np.minimum(min62380,r62380[:,num])

for num in range(1,100):
    if num==1:
       max82380=np.maximum(r82380[:,num-1],r82380[:,num])
       min82380=np.minimum(r82380[:,num-1],r82380[:,num])
    else:
       max82380=np.maximum(max82380,r82380[:,num])
       min82380=np.minimum(min82380,r82380[:,num])

r32mub380cen=spline(T/ctcen,r32mub380cen,xsame)
r42mub380cen=spline(T/ctcen,r42mub380cen,xsame)
r62mub380cen=spline(T/ctcen,r62mub380cen,xsame)
r82mub380cen=spline(T/ctcen,r82mub380cen,xsame)

dif380cen=abs(r42mub380cen-0.140553)
dif380up=abs(max42380-0.140553)
dif380down=abs(min42380-0.140553)
min380cen_index=1395#int(round(fit7[5,2]))
min380up_index=1395#int(round(fit7[5,1]))
min380down_index=1395#int(round(fit7[5,0]))
print(min380cen_index)
r32380cen=r32mub380cen[min380cen_index]
r32380hcen=r32mub380cen[Tcen[5]]
r32=[max380[min380up_index],max380[min380down_index],min380[min380up_index],min380[min380down_index]]
r32380up=np.max(r32)
r32380down=np.min(r32)

r42380cen=r42mub380cen[min380cen_index]
r62380cen=r62mub380cen[min380cen_index]
r42=[max42380[min380up_index],max42380[min380down_index],min42380[min380up_index],min42380[min380down_index]]
r42380up=np.max(r42)
r42380down=np.min(r42)

r62=[max62380[min380up_index],max62380[min380down_index],min62380[min380up_index],min62380[min380down_index]]
r62380up=np.max(r62)
r62380down=np.min(r62)

r82380cen=r82mub380cen[min380cen_index]
r82=[max82380[min380up_index],max82380[min380down_index],min82380[min380up_index],min82380[min380down_index]]
r82380up=np.max(r82)
r82380down=np.min(r82)
####################################################################################################
chi2mub390cen=np.loadtxt(r'./addition/mub390/cmucen/final/buffer/chi2.dat')
chi3mub390cen=np.loadtxt(r'./addition/mub390/cmucen/final/buffer/chi3.dat')
chi4mub390cen=np.loadtxt(r'./addition/mub390/cmucen/final/buffer/chi4.dat')
chi6mub390cen=np.loadtxt(r'./addition/mub390/cmucen/final/buffer/chi6.dat')
chi8mub390cen=np.loadtxt(r'./addition/mub390/cmucen/final/buffer/chi8.dat')
r32mub390cen=chi3mub390cen/chi2mub390cen
r42mub390cen=chi4mub390cen/chi2mub390cen
r62mub390cen=chi6mub390cen/chi2mub390cen
r82mub390cen=chi8mub390cen/chi2mub390cen
chi2mub390up=np.loadtxt(r'./addition/mub390/cmuup/final/buffer/chi2.dat')
chi3mub390up=np.loadtxt(r'./addition/mub390/cmuup/final/buffer/chi3.dat')
chi4mub390up=np.loadtxt(r'./addition/mub390/cmuup/final/buffer/chi4.dat')
chi6mub390up=np.loadtxt(r'./addition/mub390/cmuup/final/buffer/chi6.dat')
chi8mub390up=np.loadtxt(r'./addition/mub390/cmuup/final/buffer/chi8.dat')
r32mub390up=chi3mub390up/chi2mub390up
r42mub390up=chi4mub390up/chi2mub390up
r62mub390up=chi6mub390up/chi2mub390up
r82mub390up=chi8mub390up/chi2mub390up
chi2mub390up1=np.loadtxt(r'./addition/mub390/cmuup1/final/buffer/chi2.dat')
chi3mub390up1=np.loadtxt(r'./addition/mub390/cmuup1/final/buffer/chi3.dat')
chi4mub390up1=np.loadtxt(r'./addition/mub390/cmuup1/final/buffer/chi4.dat')
chi6mub390up1=np.loadtxt(r'./addition/mub390/cmuup1/final/buffer/chi6.dat')
chi8mub390up1=np.loadtxt(r'./addition/mub390/cmuup1/final/buffer/chi8.dat')
r32mub390up1=chi3mub390up1/chi2mub390up1
r42mub390up1=chi4mub390up1/chi2mub390up1
r62mub390up1=chi6mub390up1/chi2mub390up1
r82mub390up1=chi8mub390up1/chi2mub390up1
chi2mub390up2=np.loadtxt(r'./addition/mub390/cmuup2/final/buffer/chi2.dat')
chi3mub390up2=np.loadtxt(r'./addition/mub390/cmuup2/final/buffer/chi3.dat')
chi4mub390up2=np.loadtxt(r'./addition/mub390/cmuup2/final/buffer/chi4.dat')
chi6mub390up2=np.loadtxt(r'./addition/mub390/cmuup2/final/buffer/chi6.dat')
chi8mub390up2=np.loadtxt(r'./addition/mub390/cmuup2/final/buffer/chi8.dat')
r32mub390up2=chi3mub390up2/chi2mub390up2
r42mub390up2=chi4mub390up2/chi2mub390up2
r62mub390up2=chi6mub390up2/chi2mub390up2
r82mub390up2=chi8mub390up2/chi2mub390up2
chi2mub390up3=np.loadtxt(r'./addition/mub390/cmuup3/final/buffer/chi2.dat')
chi3mub390up3=np.loadtxt(r'./addition/mub390/cmuup3/final/buffer/chi3.dat')
chi4mub390up3=np.loadtxt(r'./addition/mub390/cmuup3/final/buffer/chi4.dat')
chi6mub390up3=np.loadtxt(r'./addition/mub390/cmuup3/final/buffer/chi6.dat')
chi8mub390up3=np.loadtxt(r'./addition/mub390/cmuup3/final/buffer/chi8.dat')
r32mub390up3=chi3mub390up3/chi2mub390up3
r42mub390up3=chi4mub390up3/chi2mub390up3
r62mub390up3=chi6mub390up3/chi2mub390up3
r82mub390up3=chi8mub390up3/chi2mub390up3
chi2mub390up4=np.loadtxt(r'./addition/mub390/cmuup4/final/buffer/chi2.dat')
chi3mub390up4=np.loadtxt(r'./addition/mub390/cmuup4/final/buffer/chi3.dat')
chi4mub390up4=np.loadtxt(r'./addition/mub390/cmuup4/final/buffer/chi4.dat')
chi6mub390up4=np.loadtxt(r'./addition/mub390/cmuup4/final/buffer/chi6.dat')
chi8mub390up4=np.loadtxt(r'./addition/mub390/cmuup4/final/buffer/chi8.dat')
r32mub390up4=chi3mub390up4/chi2mub390up4
r42mub390up4=chi4mub390up4/chi2mub390up4
r62mub390up4=chi6mub390up4/chi2mub390up4
r82mub390up4=chi8mub390up4/chi2mub390up4
chi2mub390down=np.loadtxt(r'./addition/mub390/cmudown/final/buffer/chi2.dat')
chi3mub390down=np.loadtxt(r'./addition/mub390/cmudown/final/buffer/chi3.dat')
chi4mub390down=np.loadtxt(r'./addition/mub390/cmudown/final/buffer/chi4.dat')
chi6mub390down=np.loadtxt(r'./addition/mub390/cmudown/final/buffer/chi6.dat')
chi8mub390down=np.loadtxt(r'./addition/mub390/cmudown/final/buffer/chi8.dat')
r32mub390down=chi3mub390down/chi2mub390down
r42mub390down=chi4mub390down/chi2mub390down
r62mub390down=chi6mub390down/chi2mub390down
r82mub390down=chi8mub390down/chi2mub390down
chi2mub390down1=np.loadtxt(r'./addition/mub390/cmudown1/final/buffer/chi2.dat')
chi3mub390down1=np.loadtxt(r'./addition/mub390/cmudown1/final/buffer/chi3.dat')
chi4mub390down1=np.loadtxt(r'./addition/mub390/cmudown1/final/buffer/chi4.dat')
chi6mub390down1=np.loadtxt(r'./addition/mub390/cmudown1/final/buffer/chi6.dat')
chi8mub390down1=np.loadtxt(r'./addition/mub390/cmudown1/final/buffer/chi8.dat')
r32mub390down1=chi3mub390down1/chi2mub390down1
r42mub390down1=chi4mub390down1/chi2mub390down1
r62mub390down1=chi6mub390down1/chi2mub390down1
r82mub390down1=chi8mub390down1/chi2mub390down1
chi2mub390down2=np.loadtxt(r'./addition/mub390/cmudown2/final/buffer/chi2.dat')
chi3mub390down2=np.loadtxt(r'./addition/mub390/cmudown2/final/buffer/chi3.dat')
chi4mub390down2=np.loadtxt(r'./addition/mub390/cmudown2/final/buffer/chi4.dat')
chi6mub390down2=np.loadtxt(r'./addition/mub390/cmudown2/final/buffer/chi6.dat')
chi8mub390down2=np.loadtxt(r'./addition/mub390/cmudown2/final/buffer/chi8.dat')
r32mub390down2=chi3mub390down2/chi2mub390down2
r42mub390down2=chi4mub390down2/chi2mub390down2
r62mub390down2=chi6mub390down2/chi2mub390down2
r82mub390down2=chi8mub390down2/chi2mub390down2
chi2mub390down3=np.loadtxt(r'./addition/mub390/cmudown3/final/buffer/chi2.dat')
chi3mub390down3=np.loadtxt(r'./addition/mub390/cmudown3/final/buffer/chi3.dat')
chi4mub390down3=np.loadtxt(r'./addition/mub390/cmudown3/final/buffer/chi4.dat')
chi6mub390down3=np.loadtxt(r'./addition/mub390/cmudown3/final/buffer/chi6.dat')
chi8mub390down3=np.loadtxt(r'./addition/mub390/cmudown3/final/buffer/chi8.dat')
r32mub390down3=chi3mub390down3/chi2mub390down3
r42mub390down3=chi4mub390down3/chi2mub390down3
r62mub390down3=chi6mub390down3/chi2mub390down3
r82mub390down3=chi8mub390down3/chi2mub390down3
chi2mub390down4=np.loadtxt(r'./addition/mub390/cmudown4/final/buffer/chi2.dat')
chi3mub390down4=np.loadtxt(r'./addition/mub390/cmudown4/final/buffer/chi3.dat')
chi4mub390down4=np.loadtxt(r'./addition/mub390/cmudown4/final/buffer/chi4.dat')
chi6mub390down4=np.loadtxt(r'./addition/mub390/cmudown4/final/buffer/chi6.dat')
chi8mub390down4=np.loadtxt(r'./addition/mub390/cmudown4/final/buffer/chi8.dat')
r32mub390down4=chi3mub390down4/chi2mub390down4
r42mub390down4=chi4mub390down4/chi2mub390down4
r62mub390down4=chi6mub390down4/chi2mub390down4
r82mub390down4=chi8mub390down4/chi2mub390down4
r32390=np.zeros((2991,100))
r42390=np.zeros((2991,100))
r62390=np.zeros((2991,100))
r82390=np.zeros((2991,100))
for t in range(0,100):
    if t<10:
       r32390[:,t]=spline(T/ct[t],r32mub390up,xsame)
    else:
       if t>=10 and t<20:
          r32390[:,t]=spline(T/ct[t-10],r32mub390up1,xsame)
       else:
          if t>=20 and t<30:
             r32390[:,t]=spline(T/ct[t-20],r32mub390up2,xsame)
          else: 
             if t>=30 and t<40:
                r32390[:,t]=spline(T/ct[t-30],r32mub390up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32390[:,t]=spline(T/ct[t-40],r32mub390up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32390[:,t]=spline(T/ct[t-50],r32mub390down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32390[:,t]=spline(T/ct[t-60],r32mub390down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32390[:,t]=spline(T/ct[t-70],r32mub390down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32390[:,t]=spline(T/ct[t-80],r32mub390down3,xsame)
                            else:
                                r32390[:,t]=spline(T/ct[t-90],r32mub390down4,xsame)

for t in range(0,100):
    if t<10:
       r42390[:,t]=spline(T/ct[t],r42mub390up,xsame)
    else:
       if t>=10 and t<20:
          r42390[:,t]=spline(T/ct[t-10],r42mub390up1,xsame)
       else:
          if t>=20 and t<30:
             r42390[:,t]=spline(T/ct[t-20],r42mub390up2,xsame)
          else: 
             if t>=30 and t<40:
                r42390[:,t]=spline(T/ct[t-30],r42mub390up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42390[:,t]=spline(T/ct[t-40],r42mub390up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42390[:,t]=spline(T/ct[t-50],r42mub390down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42390[:,t]=spline(T/ct[t-60],r42mub390down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42390[:,t]=spline(T/ct[t-70],r42mub390down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42390[:,t]=spline(T/ct[t-80],r42mub390down3,xsame)
                            else:
                                r42390[:,t]=spline(T/ct[t-90],r42mub390down4,xsame)

for t in range(0,100):
    if t<10:
       r62390[:,t]=spline(T/ct[t],r62mub390up,xsame)
    else:
       if t>=10 and t<20:
          r62390[:,t]=spline(T/ct[t-10],r62mub390up1,xsame)
       else:
          if t>=20 and t<30:
             r62390[:,t]=spline(T/ct[t-20],r62mub390up2,xsame)
          else: 
             if t>=30 and t<40:
                r62390[:,t]=spline(T/ct[t-30],r62mub390up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62390[:,t]=spline(T/ct[t-40],r62mub390up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62390[:,t]=spline(T/ct[t-50],r62mub390down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62390[:,t]=spline(T/ct[t-60],r62mub390down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62390[:,t]=spline(T/ct[t-70],r62mub390down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62390[:,t]=spline(T/ct[t-80],r62mub390down3,xsame)
                            else:
                                r62390[:,t]=spline(T/ct[t-90],r62mub390down4,xsame)

for t in range(0,100):
    if t<10:
       r82390[:,t]=spline(T/ct[t],r82mub390up,xsame)
    else:
       if t>=10 and t<20:
          r82390[:,t]=spline(T/ct[t-10],r82mub390up1,xsame)
       else:
          if t>=20 and t<30:
             r82390[:,t]=spline(T/ct[t-20],r82mub390up2,xsame)
          else: 
             if t>=30 and t<40:
                r82390[:,t]=spline(T/ct[t-30],r82mub390up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82390[:,t]=spline(T/ct[t-40],r82mub390up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82390[:,t]=spline(T/ct[t-50],r82mub390down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82390[:,t]=spline(T/ct[t-60],r82mub390down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82390[:,t]=spline(T/ct[t-70],r82mub390down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82390[:,t]=spline(T/ct[t-80],r82mub390down3,xsame)
                            else:
                                r82390[:,t]=spline(T/ct[t-90],r82mub390down4,xsame)


for num in range(1,100):
    if num==1:
       max390=np.maximum(r32390[:,num-1],r32390[:,num])
       min390=np.minimum(r32390[:,num-1],r32390[:,num])
    else:
       max390=np.maximum(max390,r32390[:,num])
       min390=np.minimum(min390,r32390[:,num])

for num in range(1,100):
    if num==1:
       max42390=np.maximum(r42390[:,num-1],r42390[:,num])
       min42390=np.minimum(r42390[:,num-1],r42390[:,num])
    else:
       max42390=np.maximum(max42390,r42390[:,num])
       min42390=np.minimum(min42390,r42390[:,num])

for num in range(1,100):
    if num==1:
       max62390=np.maximum(r62390[:,num-1],r62390[:,num])
       min62390=np.minimum(r62390[:,num-1],r62390[:,num])
    else:
       max62390=np.maximum(max62390,r62390[:,num])
       min62390=np.minimum(min62390,r62390[:,num])

for num in range(1,100):
    if num==1:
       max82390=np.maximum(r82390[:,num-1],r82390[:,num])
       min82390=np.minimum(r82390[:,num-1],r82390[:,num])
    else:
       max82390=np.maximum(max82390,r82390[:,num])
       min82390=np.minimum(min82390,r82390[:,num])

r32mub390cen=spline(T/ctcen,r32mub390cen,xsame)
r42mub390cen=spline(T/ctcen,r42mub390cen,xsame)
r62mub390cen=spline(T/ctcen,r62mub390cen,xsame)
r82mub390cen=spline(T/ctcen,r82mub390cen,xsame)

dif390cen=abs(r42mub390cen-0.140553)
dif390up=abs(max42390-0.140553)
dif390down=abs(min42390-0.140553)
min390cen_index=1381#int(round(fit7[5,2]))
min390up_index=1381#int(round(fit7[5,1]))
min390down_index=1381#int(round(fit7[5,0]))
print(min390cen_index)
r32390cen=r32mub390cen[min390cen_index]
r32390hcen=r32mub390cen[Tcen[5]]
r32=[max390[min390up_index],max390[min390down_index],min390[min390up_index],min390[min390down_index]]
r32390up=np.max(r32)
r32390down=np.min(r32)

r42390cen=r42mub390cen[min390cen_index]
r62390cen=r62mub390cen[min390cen_index]
r42=[max42390[min390up_index],max42390[min390down_index],min42390[min390up_index],min42390[min390down_index]]
r42390up=np.max(r42)
r42390down=np.min(r42)

r62=[max62390[min390up_index],max62390[min390down_index],min62390[min390up_index],min62390[min390down_index]]
r62390up=np.max(r62)
r62390down=np.min(r62)

r82390cen=r82mub390cen[min390cen_index]
r82=[max82390[min390up_index],max82390[min390down_index],min82390[min390up_index],min82390[min390down_index]]
r82390up=np.max(r82)
r82390down=np.min(r82)
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
r32406=np.zeros((2991,100))
r42406=np.zeros((2991,100))
r62406=np.zeros((2991,100))
r82406=np.zeros((2991,100))
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

for t in range(0,100):
    if t<10:
       r82406[:,t]=spline(T/ct[t],r82mub406up,xsame)
    else:
       if t>=10 and t<20:
          r82406[:,t]=spline(T/ct[t-10],r82mub406up1,xsame)
       else:
          if t>=20 and t<30:
             r82406[:,t]=spline(T/ct[t-20],r82mub406up2,xsame)
          else: 
             if t>=30 and t<40:
                r82406[:,t]=spline(T/ct[t-30],r82mub406up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82406[:,t]=spline(T/ct[t-40],r82mub406up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82406[:,t]=spline(T/ct[t-50],r82mub406down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82406[:,t]=spline(T/ct[t-60],r82mub406down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82406[:,t]=spline(T/ct[t-70],r82mub406down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82406[:,t]=spline(T/ct[t-80],r82mub406down3,xsame)
                            else:
                                r82406[:,t]=spline(T/ct[t-90],r82mub406down4,xsame)


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

for num in range(1,100):
    if num==1:
       max82406=np.maximum(r82406[:,num-1],r82406[:,num])
       min82406=np.minimum(r82406[:,num-1],r82406[:,num])
    else:
       max82406=np.maximum(max82406,r82406[:,num])
       min82406=np.minimum(min82406,r82406[:,num])

r32mub406cen=spline(T/ctcen,r32mub406cen,xsame)
r42mub406cen=spline(T/ctcen,r42mub406cen,xsame)
r62mub406cen=spline(T/ctcen,r62mub406cen,xsame)
r82mub406cen=spline(T/ctcen,r82mub406cen,xsame)

dif406cen=abs(r42mub406cen-1.766972)
dif406up=abs(max42406-1.766972)
dif406down=abs(min42406-1.766972)
min406cen_index=1355#int(round(fit7[8,2]))
min406up_index=1355#int(round(fit7[8,1]))
min406down_index=1355#int(round(fit7[8,0]))
print(min406cen_index)
#print(min406up_index)
#print(min406down_index)
r32406cen=r32mub406cen[min406cen_index]
#r32406hcen=r32mub406cen[min406cen_index+int(min406cen_index*deltat)]
r32406hcen=r32mub406cen[Tcen[8]]
r32=[max406[min406up_index],max406[min406down_index],min406[min406up_index],min406[min406down_index]]
#r32h=[max406[min406up_index+int(min406up_index*deltat)],max406[min406down_index+int(min406down_index*deltat)],min406[min406up_index+int(min406up_index*deltat)],min406[min406down_index+int(min406down_index*deltat)]]
r32h=[max406[Tcup[8]],max406[Tcdown[8]],min406[Tcup[8]],min406[Tcdown[8]]]
r32406up=np.max(r32)
r32406down=np.min(r32)
r32406uph=np.max(r32h)
r32406downh=np.min(r32h)

r42406cen=r42mub406cen[min406cen_index]
r62406cen=r62mub406cen[min406cen_index]
#r42406hcen=r42mub406cen[min406cen_index+int(min406cen_index*deltat)]
#r62406hcen=r62mub406cen[min406cen_index+int(min406cen_index*deltat)]
r42406hcen=r42mub406cen[Tcen[8]]
r62406hcen=r62mub406cen[Tcen[8]]
r42=[max42406[min406up_index],max42406[min406down_index],min42406[min406up_index],min42406[min406down_index]]
#r42h=[max42406[min406up_index+int(min406up_index*deltat)],max42406[min406down_index+int(min406down_index*deltat)],min42406[min406up_index+int(min406up_index*deltat)],min42406[min406down_index+int(min406down_index*deltat)]]
r42h=[max42406[Tcup[8]],max42406[Tcdown[8]],min42406[Tcup[8]],min42406[Tcdown[8]]]
r42406up=np.max(r42)
r42406down=np.min(r42)
r42406uph=np.max(r42h)
r42406downh=np.min(r42h)

r62=[max62406[min406up_index],max62406[min406down_index],min62406[min406up_index],min62406[min406down_index]]
#r62h=[max62406[min406up_index+int(min406up_index*deltat)],max62406[min406down_index+int(min406down_index*deltat)],min62406[min406up_index+int(min406up_index*deltat)],min62406[min406down_index+int(min406down_index*deltat)]]
r62h=[max62406[Tcup[8]],max62406[Tcdown[8]],min62406[Tcup[8]],min62406[Tcdown[8]]]
r62406up=np.max(r62)
r62406down=np.min(r62)
r62406uph=np.max(r62h)
r62406downh=np.min(r62h)

r82406cen=r82mub406cen[min406cen_index]
#r82406hcen=r82mub406cen[min406cen_index+int(min406cen_index*deltat)]
r82406hcen=r82mub406cen[Tcen[8]]
r82=[max82406[min406up_index],max82406[min406down_index],min82406[min406up_index],min82406[min406down_index]]
#r82h=[max82406[min406up_index+int(min406up_index*deltat)],max82406[min406down_index+int(min406down_index*deltat)],min82406[min406up_index+int(min406up_index*deltat)],min82406[min406down_index+int(min406down_index*deltat)]]
r82h=[max82406[Tcup[8]],max82406[Tcdown[8]],min82406[Tcup[8]],min82406[Tcdown[8]]]
r82406up=np.max(r82)
r82406down=np.min(r82)
r82406uph=np.max(r82h)
r82406downh=np.min(r82h)


#print(r62406uph)
#print(r62406downh)
####################################################################################################

r62cen=[r6222cen,r6268cen,r6278cen,r62106cen,r62120cen,r62135cen,r62148cen,r62165cen,r62180cen,r62196cen,r62215cen,r62230cen,r62252cen,r62265cen,r62280cen,r62303cen,r62310cen,r62320cen,r62330cen,r62340cen,r62350cen,r62360cen,r62370cen,r62380cen,r62390cen,r62406cen]
r62up=[r6222up,r6268up,r6278up,r62106up,r62120up,r62135up,r62148up,r62165up,r62180up,r62196up,r62215up,r62230up,r62252up,r62265up,r62280up,r62303up,r62310up,r62320up,r62330up,r62340up,r62350up,r62360up,r62370up,r62380up,r62390up,r62406up]
r62down=[r6222down,r6268down,r6278down,r62106down,r62120down,r62135down,r62148down,r62165down,r62180down,r62196down,r62215down,r62230down,r62252down,r62265down,r62280down,r62303down,r62310down,r62320down,r62330down,r62340down,r62350down,r62360down,r62370down,r62380down,r62390down,r62406down]

r42cen=np.array([r4222cen,r4268cen,r4278cen,r42106cen,r42120cen,r42135cen,r42148cen,r42165cen,r42180cen,r42196cen,r42215cen,r42230cen,r42252cen,r42265cen,r42280cen,r42303cen,r42310cen,r42320cen,r42330cen,r42340cen,r42350cen,r42360cen,r42370cen,r42380cen,r42390cen,r42406cen])
r42up=[r4222up,r4268up,r4278up,r42106up,r42120up,r42135up,r42148up,r42165up,r42180up,r42196up,r42215up,r42230up,r42252up,r42265up,r42280up,r42303up,r42310up,r42320up,r42330up,r42340up,r42350up,r42360up,r42370up,r42380up,r42390up,r42406up]
r42down=[r4222down,r4268down,r4278down,r42106down,r42120down,r42135down,r42148down,r42165down,r42180down,r42196down,r42215down,r42230down,r42252down,r42265down,r42280down,r42303down,r42310down,r42320down,r42330down,r42340down,r42350down,r42360down,r42370down,r42380down,r42390down,r42406down]

r82cen=[r8222cen,r8268cen,r8278cen,r82106cen,r82120cen,r82135cen,r82148cen,r82165cen,r82180cen,r82196cen,r82215cen,r82230cen,r82252cen,r82265cen,r82280cen,r82303cen,r82310cen,r82320cen,r82330cen,r82340cen,r82350cen,r82360cen,r82370cen,r82380cen,r82390cen,r82406cen]
r82up=[r8222up,r8268up,r8278up,r82106up,r82120up,r82135up,r82148up,r82165up,r82180up,r82196up,r82215up,r82230up,r82252up,r82265up,r82280up,r82303up,r82310up,r82320up,r82330up,r82340up,r82350up,r82360up,r82370up,r82380up,r82390up,r82406up]
r82down=[r8222down,r8268down,r8278down,r82106down,r82120down,r82135down,r82148down,r82165down,r82180down,r82196down,r82215down,r82230down,r82252down,r82265down,r82280down,r82303down,r82310down,r82320down,r82330down,r82340down,r82350down,r82360down,r82370down,r82380down,r82390down,r82406down]

r32cen=[r3222cen,r3268cen,r3278cen,r32106cen,r32120cen,r32135cen,r32148cen,r32165cen,r32180cen,r32196cen,r32215cen,r32230cen,r32252cen,r32265cen,r32280cen,r32303cen,r32310cen,r32320cen,r32330cen,r32340cen,r32350cen,r32360cen,r32370cen,r32380cen,r32390cen,r32406cen]
r32up=[r3222up,r3268up,r3278up,r32106up,r32120up,r32135up,r32148up,r32165up,r32180up,r32196up,r32215up,r32230up,r32252up,r32265up,r32280up,r32303up,r32310up,r32320up,r32330up,r32340up,r32350up,r32360up,r32370up,r32380up,r32390up,r32406up]
r32down=[r3222down,r3268down,r3278down,r32106down,r32120down,r32135down,r32148down,r32165down,r32180down,r32196down,r32215down,r32230down,r32252down,r32265down,r32280down,r32303down,r32310down,r32320down,r32330down,r32340down,r32350down,r32360down,r32370down,r32380down,r32390down,r32406down]


energynew=np.linspace(7.7,200.,300)
fr42cen=interpolate.interp1d(list(reversed(energy)),list(reversed(r42cen)),kind="slinear")
r42cen=fr42cen(energynew)
fr42up=interpolate.interp1d(list(reversed(energy)),list(reversed(r42up)),kind="slinear")
r42up=fr42up(energynew)
fr42down=interpolate.interp1d(list(reversed(energy)),list(reversed(r42down)),kind="slinear")
r42down=fr42down(energynew)
fr62cen=interpolate.interp1d(list(reversed(energy)),list(reversed(r62cen)),kind="slinear")
r62cen=fr62cen(energynew)
fr62up=interpolate.interp1d(list(reversed(energy)),list(reversed(r62up)),kind="slinear")
r62up=fr62up(energynew)
fr62down=interpolate.interp1d(list(reversed(energy)),list(reversed(r62down)),kind="slinear")
r62down=fr62down(energynew)
fr82cen=interpolate.interp1d(list(reversed(energy)),list(reversed(r82cen)),kind="slinear")
r82cen=fr82cen(energynew)
fr82up=interpolate.interp1d(list(reversed(energy)),list(reversed(r82up)),kind="slinear")
r82up=fr82up(energynew)
fr82down=interpolate.interp1d(list(reversed(energy)),list(reversed(r82down)),kind="slinear")
r82down=fr82down(energynew)


print(r42cen)
print(energynew)
for i in range(0,299):
      with open("./smooth/r42cen.dat",'a') as data:
           data.write("{}\n".format(r42cen[i]))
      with open("./smooth/r42up.dat",'a') as data:
           data.write("{}\n".format(r42up[i]))
      with open("./smooth/r42down.dat",'a') as data:
           data.write("{}\n".format(r42down[i]))
      with open("./smooth/r62cen.dat",'a') as data:
           data.write("{}\n".format(r62cen[i]))
      with open("./smooth/r62up.dat",'a') as data:
           data.write("{}\n".format(r62up[i]))
      with open("./smooth/r62down.dat",'a') as data:
           data.write("{}\n".format(r62down[i]))
      with open("./smooth/r82cen.dat",'a') as data:
           data.write("{}\n".format(r82cen[i]))
      with open("./smooth/r82up.dat",'a') as data:
           data.write("{}\n".format(r82up[i]))
      with open("./smooth/r82down.dat",'a') as data:
           data.write("{}\n".format(r82down[i])) 
          

#r42和r62的上下限与中心值
r62errup=np.zeros(26)
r62errdown=np.zeros(26)
r42errup=np.zeros(26)
r42errdown=np.zeros(26)
r82errup=np.zeros(26)
r82errdown=np.zeros(26)
r32errup=np.zeros(26)
r32errdown=np.zeros(26)


for i in range(0,26):
    r62errup[i]=r62up[i]-r62cen[i]
    r62errdown[i]=r62cen[i]-r62down[i]
    r42errup[i]=r42up[i]-r42cen[i]
    r42errdown[i]=r42cen[i]-r42down[i]
    r82errup[i]=r82up[i]-r82cen[i]
    r82errdown[i]=r82cen[i]-r82down[i]
    r32errup[i]=r32up[i]-r32cen[i]
    r32errdown[i]=r32cen[i]-r32down[i]






for num in range(0,100):
    T22up[num]=min22up_index
    T22down[num]=min22down_index
    T68up[num]=min68up_index
    T68down[num]=min68down_index
    T78up[num]=min78up_index
    T78down[num]=min78down_index
    T106up[num]=min106up_index
    T106down[num]=min106down_index
    T120up[num]=min120up_index
    T120down[num]=min120down_index
    T135up[num]=min135up_index
    T135down[num]=min135down_index
    T148up[num]=min148up_index
    T148down[num]=min148down_index
    T165up[num]=min165up_index
    T165down[num]=min165down_index
    T180up[num]=min180up_index
    T180down[num]=min180down_index
    T196up[num]=min196up_index
    T196down[num]=min196down_index
    T215up[num]=min215up_index
    T215down[num]=min215down_index
    T230up[num]=min230up_index
    T230down[num]=min230down_index
    T252up[num]=min252up_index
    T252down[num]=min252down_index
    T265up[num]=min265up_index
    T265down[num]=min265down_index
    T280up[num]=min280up_index
    T280down[num]=min280down_index
    T303up[num]=min303up_index
    T303down[num]=min303down_index
    T310up[num]=min310up_index
    T310down[num]=min310down_index
    T320up[num]=min320up_index
    T320down[num]=min320down_index
    T330up[num]=min330up_index
    T330down[num]=min330down_index
    T340up[num]=min340up_index
    T340down[num]=min340down_index
    T350up[num]=min350up_index
    T350down[num]=min350down_index
    T360up[num]=min360up_index
    T360down[num]=min360down_index
    T370up[num]=min370up_index
    T370down[num]=min370down_index
    T380up[num]=min380up_index
    T380down[num]=min380down_index
    T390up[num]=min390up_index
    T390down[num]=min390down_index
    T406up[num]=min406up_index
    T406down[num]=min406down_index

####################################################################################################
energyrhic=[200.,54.4]
value62=[-2.54509,1.20229]
erro62=[1.01682,0.480246]
# Create figure
blackline=np.linspace(0,300,100)
r42line=np.zeros(100)
r62line=np.zeros(100)
for i in range(1,100):
    r42line[i]=1

for i in range(1,100):
    r62line[i]=0

# Create figure
fig=plt.figure(figsize=(4.5, 8.))
#fig=plt.figure()
ax2=fig.add_subplot(312)
#point62cen3=ax2.errorbar(energy,r62cen,yerr=[r62errdown,r62errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,capsize=1,elinewidth=4,zorder=2)
band62cen3=ax2.fill_between(energy,r62down,r62up,color='g',alpha=0.2,facecolor='g',edgecolor='',zorder=2)
line62cen3,=ax2.plot(energy,r62cen,color='g',alpha=0.3,zorder=2)
exp=ax2.errorbar(energyrhic,value62,yerr=erro62,color='b',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
ax2.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
ax2.legend(((band62cen3,line62cen3),exp),(r'fRG-LEFT freezeout: STAR II',r'STAR preliminary'),loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
plt.axis([5.,230.,-100.,100.])
ax2.set_xscale('symlog')
ax2.set_yscale('symlog')
ax2.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
plt.yticks([-50,-40,-30,-20,-10,-1,0,1,10])
ax2.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.xaxis.set_label_position('top') 
ax2.set_ylabel(r'$R^B_{62}(R^p_{62})$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(7)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(7)


ax3=fig.add_subplot(311)
#errbartf423=ax3.errorbar(energy,r42cen,yerr=[r42errdown,r42errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,capsize=1,elinewidth=4,zorder=2)
bandtf423=ax3.fill_between(energy,r42down,r42up,color='g',alpha=0.2,facecolor='g',edgecolor='',zorder=2)
linetf423,=ax3.plot(energynew,r42cennew,color='g',alpha=0.3,zorder=2)
ax3.plot(energy2,r42cen2,color='g',alpha=0.3,zorder=2)
exp=ax3.errorbar(energyexp,kurtosis[:,0],yerr=kurtosis[:,1],color='c',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.8,zorder=3)
ax3.plot(blackline,r42line,dashes=[4,2],color='m',linewidth='1')
ax3.legend(((bandtf423,linetf423),exp),(r'fRG-LEFT freezeout: STAR II',r'STAR preliminary'),loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax3.set_xscale('symlog')
plt.axis([5,230,-0.5,2.8])
ax3.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
ax3.set_xticklabels(['406','303','252','196','148','106','78','68','22'],rotation=60,fontsize=7)
ax3.xaxis.tick_top()
ax3.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.xaxis.set_label_position('top') 
ax3.set_ylabel(r'$R^B_{42}(R^p_{42})$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(7)



ax4=fig.add_subplot(313)
#errbartf823=ax4.errorbar(energy,r82cen,yerr=[r82errdown,r82errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,capsize=1,elinewidth=4,zorder=2)
bandtf823=ax4.fill_between(energy,r82down,r82up,color='g',alpha=0.2,facecolor='g',edgecolor='',zorder=2)
linetf823,=ax4.plot(energy,r82cen,color='g',alpha=0.3,zorder=2)
ax4.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
ax4.legend([(bandtf823,linetf823)],[r'fRG-LEFT freezeout: STAR II'],loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax4.set_xscale('symlog')
plt.axis([5,230,-50,50])
ax4.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
ax4.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
ax4.set_xlabel('$\sqrt{s_{\mathrm{NN}}}\,[\mathrm{GeV}]$', fontsize=14, color='black')
ax4.set_ylabel(r'$R^B_{82}(R^p_{82})$', fontsize=14, color='black')
for label in ax4.yaxis.get_ticklabels():
    label.set_fontsize(7)


fig.subplots_adjust(top=0.93, bottom=0.08, left=0.15, right=0.9, hspace=0.,
                    wspace=0.25)

fig.savefig("Rm2-sqrtS.pdf")


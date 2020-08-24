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
y62=np.linspace(-5000,5000,100)
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
T22hup=np.zeros(100)
T22hdown=np.zeros(100)
T68hup=np.zeros(100)
T68hdown=np.zeros(100)
T78hup=np.zeros(100)
T78hdown=np.zeros(100)
T106hup=np.zeros(100)
T106hdown=np.zeros(100)
T148hup=np.zeros(100)
T148hdown=np.zeros(100)
T196hup=np.zeros(100)
T196hdown=np.zeros(100)
T252hup=np.zeros(100)
T252hdown=np.zeros(100)
T303hup=np.zeros(100)
T303hdown=np.zeros(100)
T406hup=np.zeros(100)
T406hdown=np.zeros(100)
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
print(fit7)
fit4=np.loadtxt(r'./fitSTAR/fourpointfit.dat')
energy=[200.,62.4,54.4,39.,27.,19.6,14.5,11.5,7.7]
#############################################################################################################################################
xsame=np.linspace(1.,300.,300)
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

print(xsame)
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
r3222=np.zeros((300,20))
r4222=np.zeros((300,20))
r6222=np.zeros((300,20))
r8222=np.zeros((300,20))
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


dif6222minc=np.zeros(300)
dif6222minu=np.zeros(300)
dif6222mind=np.zeros(300)
dif6222minc=abs(r62mub22cen+0.5)
dif6222minu=abs(max6222+0.5)
dif6222mind=abs(min6222+0.5)
min6222cindex=np.argmin(dif6222minc[80:300])+80
min6222uindex=np.argmin(dif6222minu[80:300])+80
min6222dindex=np.argmin(dif6222mind[80:300])+80
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
min22cen_index=int(round(fit7[0,2]))
min22up_index=int(round(fit7[0,1]))
min22down_index=int(round(fit7[0,0]))

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
r3268=np.zeros((300,20))
r4268=np.zeros((300,20))
r6268=np.zeros((300,20))
r8268=np.zeros((300,20))
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
min68cen_index=int(round(fit7[1,2]))
min68up_index=int(round(fit7[1,1]))
min68down_index=int(round(fit7[1,0]))
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
r3278=np.zeros((300,20))
r4278=np.zeros((300,20))
r6278=np.zeros((300,20))
r8278=np.zeros((300,20))
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
min78cen_index=int(round(fit7[2,2]))
min78up_index=int(round(fit7[2,1]))
min78down_index=int(round(fit7[2,0]))
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
r32106=np.zeros((300,20))
r42106=np.zeros((300,20))
r62106=np.zeros((300,20))
r82106=np.zeros((300,20))
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
min106cen_index=int(round(fit7[3,2]))
min106up_index=int(round(fit7[3,1]))
min106down_index=int(round(fit7[3,0]))
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
r82148=np.zeros((300,20))
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

r32mub148cen=spline(T/ctcen,r32mub148cen,xsame)*c
max148=max148*c
min148=min148*c
r42mub148cen=spline(T/ctcen,r42mub148cen,xsame)
r62mub148cen=spline(T/ctcen,r62mub148cen,xsame)
r82mub148cen=spline(T/ctcen,r82mub148cen,xsame)

dif148cen=abs(r42mub148cen-0.196254)
dif148up=abs(max42148-0.196254)
dif148down=abs(min42148-0.196254)
min148cen_index=int(round(fit7[4,2]))
min148up_index=int(round(fit7[4,1]))
min148down_index=int(round(fit7[4,0]))
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
r82196=np.zeros((300,100))
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

r32mub196cen=spline(T/ctcen,r32mub196cen,xsame)*c
max196=max196*c
min196=min196*c
r42mub196cen=spline(T/ctcen,r42mub196cen,xsame)
r62mub196cen=spline(T/ctcen,r62mub196cen,xsame)
r82mub196cen=spline(T/ctcen,r82mub196cen,xsame)

dif196cen=abs(r42mub196cen-0.140553)
dif196up=abs(max42196-0.140553)
dif196down=abs(min42196-0.140553)
min196cen_index=int(round(fit7[5,2]))
min196up_index=int(round(fit7[5,1]))
min196down_index=int(round(fit7[5,0]))
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
r82252=np.zeros((300,100))
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

r32mub252cen=spline(T/ctcen,r32mub252cen,xsame)*c
max252=max252*c
min252=min252*c
r42mub252cen=spline(T/ctcen,r42mub252cen,xsame)
r62mub252cen=spline(T/ctcen,r62mub252cen,xsame)
r82mub252cen=spline(T/ctcen,r82mub252cen,xsame)

dif252cen=abs(r42mub252cen-1.468760)
dif252up=abs(max42252-1.468760)
dif252down=abs(min42252-1.468760)
min252cen_index=int(round(fit7[6,2]))
min252up_index=int(round(fit7[6,1]))
min252down_index=int(round(fit7[6,0]))
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
r82303=np.zeros((300,100))
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

r32mub303cen=spline(T/ctcen,r32mub303cen,xsame)*c
max303=max303*c
min303=min303*c
r42mub303cen=spline(T/ctcen,r42mub303cen,xsame)
r62mub303cen=spline(T/ctcen,r62mub303cen,xsame)
r82mub303cen=spline(T/ctcen,r82mub303cen,xsame)

dif303cen=abs(r42mub303cen-0.695796)
dif303up=abs(max42303-0.695796)
dif303down=abs(min42303-0.695796)
min303cen_index=int(round(fit7[7,2]))
min303up_index=int(round(fit7[7,1]))
min303down_index=int(round(fit7[7,0]))
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
r82406=np.zeros((300,100))
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

r32mub406cen=spline(T/ctcen,r32mub406cen,xsame)*c
max406=max406*c
min406=min406*c
r42mub406cen=spline(T/ctcen,r42mub406cen,xsame)
r62mub406cen=spline(T/ctcen,r62mub406cen,xsame)
r82mub406cen=spline(T/ctcen,r82mub406cen,xsame)

dif406cen=abs(r42mub406cen-1.766972)
dif406up=abs(max42406-1.766972)
dif406down=abs(min42406-1.766972)
min406cen_index=int(round(fit7[8,2]))
min406up_index=int(round(fit7[8,1]))
min406down_index=int(round(fit7[8,0]))
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
#r62cen=[r6222cen,r6268cen,r6278cen,r62106cen,r62148cen,r62196cen,r62252cen,r62303cen,r62406cen]
#r62up=[r6222up,r6268up,r6278up,r62106up,r62148up,r62196up,r62252up,r62303up,r62406up]
#r62down=[r6222down,r6268down,r6278down,r62106down,r62148down,r62196down,r62252down,r62303down,r62406down]

#r42up=[r4222up,r4268up,r4278up,r42106up,r42148up,r42196up,r42252up,r42303up,r42406up]
#r42down=[r4222down,r4268down,r4278down,r42106down,r42148down,r42196down,r42252down,r42303down,r42406down]
#r42cen=[r4222cen,r4268cen,r4278cen,r42106cen,r42148cen,r42196cen,r42252cen,r42303cen,r42406cen]

r42hcen=[r4222hcen,r4268hcen,r4278hcen,r42106hcen,r42148hcen,r42196hcen,r42252hcen,r42303hcen,r42406hcen]
r62hcen=[r6222hcen,r6268hcen,r6278hcen,r62106hcen,r62148hcen,r62196hcen,r62252hcen,r62303hcen,r62406hcen]
r42hup=[r4222uph,r4268uph,r4278uph,r42106uph,r42148uph,r42196uph,r42252uph,r42303uph,r42406uph]
r42hdown=[r4222downh,r4268downh,r4278downh,r42106downh,r42148downh,r42196downh,r42252downh,r42303downh,r42406downh]
r62hup=[r6222uph,r6268uph,r6278uph,r62106uph,r62148uph,r62196uph,r62252uph,r62303uph,r62406uph]
r62hdown=[r6222downh,r6268downh,r6278downh,r62106downh,r62148downh,r62196downh,r62252downh,r62303downh,r62406downh]

#r82cen=[r8222cen,r8268cen,r8278cen,r82106cen,r82148cen,r82196cen,r82252cen,r82303cen,r82406cen]
#r82up=[r8222up,r8268up,r8278up,r82106up,r82148up,r82196up,r82252up,r82303up,r82406up]
#r82down=[r8222down,r8268down,r8278down,r82106down,r82148down,r82196down,r82252down,r82303down,r82406down]

r62cen=[r6222cen,r6268cen,r6278cen,r62106cen,r62148cen,r62196cen,r62252cen,r62303cen,r62406cen]
r62up=[r6222up,r6268up,r6278up,r62106up,r62148up,r62196up,r62252up,r62303up,r62406up]
r62down=[r6222down,r6268down,r6278down,r62106down,r62148down,r62196down,r62252down,r62303down,r62406down]

r42up=[r4222up,r4268up,r4278up,r42106up,r42148up,r42196up,r42252up,r42303up,r42406up]
r42down=[r4222down,r4268down,r4278down,r42106down,r42148down,r42196down,r42252down,r42303down,r42406down]
r42cen=[r4222cen,r4268cen,r4278cen,r42106cen,r42148cen,r42196cen,r42252cen,r42303cen,r42406cen]

r82cen=[r8222cen,r8268cen,r8278cen,r82106cen,r82148cen,r82196cen,r82252cen,r82303cen,r82406cen]
r82up=[r8222up,r8268up,r8278up,r82106up,r82148up,r82196up,r82252up,r82303up,r82406up]
r82down=[r8222down,r8268down,r8278down,r82106down,r82148down,r82196down,r82252down,r82303down,r82406down]

r82hcen=[r8222hcen,r8268hcen,r8278hcen,r82106hcen,r82148hcen,r82196hcen,r82252hcen,r82303hcen,r82406hcen]
r82hup=[r8222uph,r8268uph,r8278uph,r82106uph,r82148uph,r82196uph,r82252uph,r82303uph,r82406uph]
r82hdown=[r8222downh,r8268downh,r8278downh,r82106downh,r82148downh,r82196downh,r82252downh,r82303downh,r82406downh]

r32cen=[r3222cen,r3268cen,r3278cen,r32106cen,r32148cen,r32196cen,r32252cen,r32303cen,r32406cen]
r32up=[r3222up,r3268up,r3278up,r32106up,r32148up,r32196up,r32252up,r32303up,r32406up]
r32down=[r3222down,r3268down,r3278down,r32106down,r32148down,r32196down,r32252down,r32303down,r32406down]
r32hcen=[r3222hcen,r3268hcen,r3278hcen,r32106hcen,r32148hcen,r32196hcen,r32252hcen,r32303hcen,r32406hcen]
r32hup=[r3222uph,r3268uph,r3278uph,r32106uph,r32148uph,r32196uph,r32252uph,r32303uph,r32406uph]
r32hdown=[r3222downh,r3268downh,r3278downh,r32106downh,r32148downh,r32196downh,r32252downh,r32303downh,r32406downh]
#r42和r62的上下限与中心值
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
r82errup=np.zeros(9)
r82errdown=np.zeros(9)
r32errup=np.zeros(9)
r32errdown=np.zeros(9)
r82errhup=np.zeros(9)
r82errhdown=np.zeros(9)
r32errhup=np.zeros(9)
r32errhdown=np.zeros(9)
r82errlup=np.zeros(9)
r82errldown=np.zeros(9)
r32errlup=np.zeros(9)
r32errldown=np.zeros(9)

for i in range(0,9):
    r62errup[i]=r62up[i]-r62cen[i]
    r62errdown[i]=r62cen[i]-r62down[i]
    r42errup[i]=r42up[i]-r42cen[i]
    r42errdown[i]=r42cen[i]-r42down[i]
    r62errhup[i]=r62hup[i]-r62hcen[i]
    r62errhdown[i]=r62hcen[i]-r62hdown[i]
    r42errhup[i]=r42hup[i]-r42hcen[i]
    r42errhdown[i]=r42hcen[i]-r42hdown[i]
    r82errup[i]=r82up[i]-r82cen[i]
    r82errdown[i]=r82cen[i]-r82down[i]
    r32errup[i]=r32up[i]-r32cen[i]
    r32errdown[i]=r32cen[i]-r32down[i]
    r82errhup[i]=r82hup[i]-r82hcen[i]
    r82errhdown[i]=r82hcen[i]-r82hdown[i]
    r32errhup[i]=r32hup[i]-r32hcen[i]
    r32errhdown[i]=r32hcen[i]-r32hdown[i]





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
    T22hup[num]=Tcup[0]
    T22hdown[num]=Tcdown[0]
    T68hup[num]=Tcup[1]
    T68hdown[num]=Tcdown[1]
    T78hup[num]=Tcup[2]
    T78hdown[num]=Tcdown[2]
    T106hup[num]=Tcup[3]
    T106hdown[num]=Tcdown[3]
    T148hup[num]=Tcup[4]
    T148hdown[num]=Tcdown[4]
    T196hup[num]=Tcup[5]
    T196hdown[num]=Tcdown[5]
    T252hup[num]=Tcup[6]
    T252hdown[num]=Tcdown[6]
    T303hup[num]=Tcup[7]
    T303hdown[num]=Tcdown[7]
    T406hup[num]=Tcup[8]
    T406hdown[num]=Tcdown[8]
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
point62cen3=ax2.errorbar(energy,r62cen,yerr=[r62errdown,r62errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#point62h=ax2.errorbar(energy,r62hcen,yerr=[r62errhdown,r62errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
band62cen3=ax2.fill_between(energy,r62down,r62up,color='blue',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
line62cen3,=ax2.plot(energy,r62cen,color='r',alpha=0.3,zorder=2)
#point62h=ax2.fill_between(energy,r62hdown,r62hup,color='r',alpha=0.25,facecolor='b',edgecolor='',zorder=1)
#line62h,=ax2.plot(energy,r62hcen,color='b',alpha=0.3,zorder=1)
exp=ax2.errorbar(energyrhic,value62,yerr=erro62,color='b',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
#ax2.legend(((point62cen,band62cen,line62cen),exp),(r'fRG',r'STAR preliminary'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax2.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
plt.axis([5.,230.,-100.,100.])
ax2.set_xscale('symlog')
#plt.axis([5.,230.,-10.,20.])
ax2.set_yscale('symlog')
#plt.xticks([])
ax2.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
#ax2.set_xticklabels(['406','303','252','196','148','106','78','68','22'],rotation=60,fontsize=7)
#ax2.xaxis.tick_top()
plt.yticks([-50,-40,-30,-20,-10,-1,0,1,10,20,30,40,50])
ax2.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.xaxis.set_label_position('top') 
ax2.set_ylabel(r'$R^B_{62}(R^p_{62})$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(7)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(7)


ax3=fig.add_subplot(311)
errbartf423=ax3.errorbar(energy,r42cen,yerr=[r42errdown,r42errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#ax3.errorbar(energy,r42hcen,yerr=[r42errhdown,r42errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
bandtf423=ax3.fill_between(energy,r42down,r42up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
linetf423,=ax3.plot(energy,r42cen,color='r',alpha=0.3,zorder=2)
#ax3.fill_between(energy,r42hdown,r42hup,color='b',alpha=0.25,facecolor='b',edgecolor='',zorder=1)
#ax3.plot(energy,r42hcen,color='b',alpha=0.3,zorder=1)
exp=ax3.errorbar(energy,kurtosis[:,0],yerr=kurtosis[:,1],color='c',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
#ax3.errorbar(energy,kurtosis[:,0],color='red')
ax3.plot(blackline,r42line,dashes=[4,2],color='m',linewidth='1')
#ax3.legend(((errbartf,bandtf,linetf),exp),(r'fRG',r'STAR data'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax3.set_xscale('symlog')
plt.axis([5,230,-0.5,2.8])
ax3.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
#ax3.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
ax3.set_xticklabels(['406','303','252','196','148','106','78','68','22'],rotation=60,fontsize=7)
ax3.xaxis.tick_top()
ax3.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.xaxis.set_label_position('top') 
#ax3.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax3.set_ylabel(r'$R^B_{42}(R^p_{42})$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(7)



ax4=fig.add_subplot(313)
errbartf823=ax4.errorbar(energy,r82cen,yerr=[r82errdown,r82errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
ax4.errorbar(energy,r82cen,yerr=[r82errup,r82errdown],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#ax4.errorbar(energy,r82hcen,yerr=[r82errhdown,r82errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
bandtf823=ax4.fill_between(energy,r82down,r82up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
linetf823,=ax4.plot(energy,r82cen,color='r',alpha=0.3,zorder=2)
#ax4.fill_between(energy,r82hdown,r82hup,color='b',alpha=0.25,facecolor='b',edgecolor='',zorder=1)
#ax4.plot(energy,r82hcen,color='b',alpha=0.3,zorder=1)
ax4.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
#ax4.legend([(errbartf,bandtf,linetf)],[r'fRG'],loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax4.set_xscale('symlog')
#ax4.set_yscale('symlog')
#plt.axis([5,230,-10000.,1000.])
plt.axis([5,230,-50,50])
#plt.yticks([-10000,-9000,-8000,-7000,-6000,-5000,-4000,-3000,-2000,-1000,-900,-800,-700,-600,-500,-400,-300,-200,-100,-90,-80,-70,-60,-50,-40,-30,-20,-10,-1,0,1,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
ax4.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
ax4.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
ax4.set_xlabel('$\sqrt{s_{\mathrm{NN}}}\,[\mathrm{GeV}]$', fontsize=14, color='black')
ax4.set_ylabel(r'$R^B_{82}(R^p_{82})$', fontsize=14, color='black')
for label in ax4.yaxis.get_ticklabels():
    label.set_fontsize(7)
print(r62down)
print(r62up)

fig.subplots_adjust(top=0.93, bottom=0.08, left=0.15, right=0.9, hspace=0.,
                    wspace=0.25)


#############################################################################################################################################
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
T22hup=np.zeros(100)
T22hdown=np.zeros(100)
T68hup=np.zeros(100)
T68hdown=np.zeros(100)
T78hup=np.zeros(100)
T78hdown=np.zeros(100)
T106hup=np.zeros(100)
T106hdown=np.zeros(100)
T148hup=np.zeros(100)
T148hdown=np.zeros(100)
T196hup=np.zeros(100)
T196hdown=np.zeros(100)
T252hup=np.zeros(100)
T252hdown=np.zeros(100)
T303hup=np.zeros(100)
T303hdown=np.zeros(100)
T406hup=np.zeros(100)
T406hdown=np.zeros(100)
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


fit7=fit4

xsame=np.linspace(1.,300.,300)
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

print(xsame)
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
r3222=np.zeros((300,20))
r4222=np.zeros((300,20))
r6222=np.zeros((300,20))
r8222=np.zeros((300,20))
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


dif6222minc=np.zeros(300)
dif6222minu=np.zeros(300)
dif6222mind=np.zeros(300)
dif6222minc=abs(r62mub22cen+0.5)
dif6222minu=abs(max6222+0.5)
dif6222mind=abs(min6222+0.5)
min6222cindex=np.argmin(dif6222minc[80:300])+80
min6222uindex=np.argmin(dif6222minu[80:300])+80
min6222dindex=np.argmin(dif6222mind[80:300])+80
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
min22cen_index=int(round(fit7[0,2]))
min22up_index=int(round(fit7[0,1]))
min22down_index=int(round(fit7[0,0]))

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
r3268=np.zeros((300,20))
r4268=np.zeros((300,20))
r6268=np.zeros((300,20))
r8268=np.zeros((300,20))
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
min68cen_index=int(round(fit7[1,2]))
min68up_index=int(round(fit7[1,1]))
min68down_index=int(round(fit7[1,0]))
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
r3278=np.zeros((300,20))
r4278=np.zeros((300,20))
r6278=np.zeros((300,20))
r8278=np.zeros((300,20))
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
min78cen_index=int(round(fit7[2,2]))
min78up_index=int(round(fit7[2,1]))
min78down_index=int(round(fit7[2,0]))
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
r32106=np.zeros((300,20))
r42106=np.zeros((300,20))
r62106=np.zeros((300,20))
r82106=np.zeros((300,20))
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
min106cen_index=int(round(fit7[3,2]))
min106up_index=int(round(fit7[3,1]))
min106down_index=int(round(fit7[3,0]))
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
r82148=np.zeros((300,20))
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

r32mub148cen=spline(T/ctcen,r32mub148cen,xsame)*c
max148=max148*c
min148=min148*c
r42mub148cen=spline(T/ctcen,r42mub148cen,xsame)
r62mub148cen=spline(T/ctcen,r62mub148cen,xsame)
r82mub148cen=spline(T/ctcen,r82mub148cen,xsame)

dif148cen=abs(r42mub148cen-0.196254)
dif148up=abs(max42148-0.196254)
dif148down=abs(min42148-0.196254)
min148cen_index=int(round(fit7[4,2]))
min148up_index=int(round(fit7[4,1]))
min148down_index=int(round(fit7[4,0]))
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
r82196=np.zeros((300,100))
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

r32mub196cen=spline(T/ctcen,r32mub196cen,xsame)*c
max196=max196*c
min196=min196*c
r42mub196cen=spline(T/ctcen,r42mub196cen,xsame)
r62mub196cen=spline(T/ctcen,r62mub196cen,xsame)
r82mub196cen=spline(T/ctcen,r82mub196cen,xsame)

dif196cen=abs(r42mub196cen-0.140553)
dif196up=abs(max42196-0.140553)
dif196down=abs(min42196-0.140553)
min196cen_index=int(round(fit7[5,2]))
min196up_index=int(round(fit7[5,1]))
min196down_index=int(round(fit7[5,0]))
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
r82252=np.zeros((300,100))
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

r32mub252cen=spline(T/ctcen,r32mub252cen,xsame)*c
max252=max252*c
min252=min252*c
r42mub252cen=spline(T/ctcen,r42mub252cen,xsame)
r62mub252cen=spline(T/ctcen,r62mub252cen,xsame)
r82mub252cen=spline(T/ctcen,r82mub252cen,xsame)

dif252cen=abs(r42mub252cen-1.468760)
dif252up=abs(max42252-1.468760)
dif252down=abs(min42252-1.468760)
min252cen_index=int(round(fit7[6,2]))
min252up_index=int(round(fit7[6,1]))
min252down_index=int(round(fit7[6,0]))
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
r82303=np.zeros((300,100))
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

r32mub303cen=spline(T/ctcen,r32mub303cen,xsame)*c
max303=max303*c
min303=min303*c
r42mub303cen=spline(T/ctcen,r42mub303cen,xsame)
r62mub303cen=spline(T/ctcen,r62mub303cen,xsame)
r82mub303cen=spline(T/ctcen,r82mub303cen,xsame)

dif303cen=abs(r42mub303cen-0.695796)
dif303up=abs(max42303-0.695796)
dif303down=abs(min42303-0.695796)
min303cen_index=int(round(fit7[7,2]))
min303up_index=int(round(fit7[7,1]))
min303down_index=int(round(fit7[7,0]))
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
r82406=np.zeros((300,100))
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

r32mub406cen=spline(T/ctcen,r32mub406cen,xsame)*c
max406=max406*c
min406=min406*c
r42mub406cen=spline(T/ctcen,r42mub406cen,xsame)
r62mub406cen=spline(T/ctcen,r62mub406cen,xsame)
r82mub406cen=spline(T/ctcen,r82mub406cen,xsame)

dif406cen=abs(r42mub406cen-1.766972)
dif406up=abs(max42406-1.766972)
dif406down=abs(min42406-1.766972)
min406cen_index=int(round(fit7[8,2]))
min406up_index=int(round(fit7[8,1]))
min406down_index=int(round(fit7[8,0]))
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
#r62cen=[r6222cen,r6268cen,r6278cen,r62106cen,r62148cen,r62196cen,r62252cen,r62303cen,r62406cen]
#r62up=[r6222up,r6268up,r6278up,r62106up,r62148up,r62196up,r62252up,r62303up,r62406up]
#r62down=[r6222down,r6268down,r6278down,r62106down,r62148down,r62196down,r62252down,r62303down,r62406down]

#r42up=[r4222up,r4268up,r4278up,r42106up,r42148up,r42196up,r42252up,r42303up,r42406up]
#r42down=[r4222down,r4268down,r4278down,r42106down,r42148down,r42196down,r42252down,r42303down,r42406down]
#r42cen=[r4222cen,r4268cen,r4278cen,r42106cen,r42148cen,r42196cen,r42252cen,r42303cen,r42406cen]

r42hcen=[r4222hcen,r4268hcen,r4278hcen,r42106hcen,r42148hcen,r42196hcen,r42252hcen,r42303hcen,r42406hcen]
r62hcen=[r6222hcen,r6268hcen,r6278hcen,r62106hcen,r62148hcen,r62196hcen,r62252hcen,r62303hcen,r62406hcen]
r42hup=[r4222uph,r4268uph,r4278uph,r42106uph,r42148uph,r42196uph,r42252uph,r42303uph,r42406uph]
r42hdown=[r4222downh,r4268downh,r4278downh,r42106downh,r42148downh,r42196downh,r42252downh,r42303downh,r42406downh]
r62hup=[r6222uph,r6268uph,r6278uph,r62106uph,r62148uph,r62196uph,r62252uph,r62303uph,r62406uph]
r62hdown=[r6222downh,r6268downh,r6278downh,r62106downh,r62148downh,r62196downh,r62252downh,r62303downh,r62406downh]

#r82cen=[r8222cen,r8268cen,r8278cen,r82106cen,r82148cen,r82196cen,r82252cen,r82303cen,r82406cen]
#r82up=[r8222up,r8268up,r8278up,r82106up,r82148up,r82196up,r82252up,r82303up,r82406up]
#r82down=[r8222down,r8268down,r8278down,r82106down,r82148down,r82196down,r82252down,r82303down,r82406down]

r62cen=[r6222cen,r6268cen,r6278cen,r62106cen,r62148cen,r62196cen,r62252cen,r62303cen,r62406cen]
r62up=[r6222up,r6268up,r6278up,r62106up,r62148up,r62196up,r62252up,r62303up,r62406up]
r62down=[r6222down,r6268down,r6278down,r62106down,r62148down,r62196down,r62252down,r62303down,r62406down]

r42up=[r4222up,r4268up,r4278up,r42106up,r42148up,r42196up,r42252up,r42303up,r42406up]
r42down=[r4222down,r4268down,r4278down,r42106down,r42148down,r42196down,r42252down,r42303down,r42406down]
r42cen=[r4222cen,r4268cen,r4278cen,r42106cen,r42148cen,r42196cen,r42252cen,r42303cen,r42406cen]

r82cen=[r8222cen,r8268cen,r8278cen,r82106cen,r82148cen,r82196cen,r82252cen,r82303cen,r82406cen]
r82up=[r8222up,r8268up,r8278up,r82106up,r82148up,r82196up,r82252up,r82303up,r82406up]
r82down=[r8222down,r8268down,r8278down,r82106down,r82148down,r82196down,r82252down,r82303down,r82406down]

r82hcen=[r8222hcen,r8268hcen,r8278hcen,r82106hcen,r82148hcen,r82196hcen,r82252hcen,r82303hcen,r82406hcen]
r82hup=[r8222uph,r8268uph,r8278uph,r82106uph,r82148uph,r82196uph,r82252uph,r82303uph,r82406uph]
r82hdown=[r8222downh,r8268downh,r8278downh,r82106downh,r82148downh,r82196downh,r82252downh,r82303downh,r82406downh]

r32cen=[r3222cen,r3268cen,r3278cen,r32106cen,r32148cen,r32196cen,r32252cen,r32303cen,r32406cen]
r32up=[r3222up,r3268up,r3278up,r32106up,r32148up,r32196up,r32252up,r32303up,r32406up]
r32down=[r3222down,r3268down,r3278down,r32106down,r32148down,r32196down,r32252down,r32303down,r32406down]
r32hcen=[r3222hcen,r3268hcen,r3278hcen,r32106hcen,r32148hcen,r32196hcen,r32252hcen,r32303hcen,r32406hcen]
r32hup=[r3222uph,r3268uph,r3278uph,r32106uph,r32148uph,r32196uph,r32252uph,r32303uph,r32406uph]
r32hdown=[r3222downh,r3268downh,r3278downh,r32106downh,r32148downh,r32196downh,r32252downh,r32303downh,r32406downh]
#r42和r62的上下限与中心值
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
r82errup=np.zeros(9)
r82errdown=np.zeros(9)
r32errup=np.zeros(9)
r32errdown=np.zeros(9)
r82errhup=np.zeros(9)
r82errhdown=np.zeros(9)
r32errhup=np.zeros(9)
r32errhdown=np.zeros(9)
r82errlup=np.zeros(9)
r82errldown=np.zeros(9)
r32errlup=np.zeros(9)
r32errldown=np.zeros(9)

for i in range(0,9):
    r62errup[i]=r62up[i]-r62cen[i]
    r62errdown[i]=r62cen[i]-r62down[i]
    r42errup[i]=r42up[i]-r42cen[i]
    r42errdown[i]=r42cen[i]-r42down[i]
    r62errhup[i]=r62hup[i]-r62hcen[i]
    r62errhdown[i]=r62hcen[i]-r62hdown[i]
    r42errhup[i]=r42hup[i]-r42hcen[i]
    r42errhdown[i]=r42hcen[i]-r42hdown[i]
    r82errup[i]=r82up[i]-r82cen[i]
    r82errdown[i]=r82cen[i]-r82down[i]
    r32errup[i]=r32up[i]-r32cen[i]
    r32errdown[i]=r32cen[i]-r32down[i]
    r82errhup[i]=r82hup[i]-r82hcen[i]
    r82errhdown[i]=r82hcen[i]-r82hdown[i]
    r32errhup[i]=r32hup[i]-r32hcen[i]
    r32errhdown[i]=r32hcen[i]-r32hdown[i]





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
    T22hup[num]=Tcup[0]
    T22hdown[num]=Tcdown[0]
    T68hup[num]=Tcup[1]
    T68hdown[num]=Tcdown[1]
    T78hup[num]=Tcup[2]
    T78hdown[num]=Tcdown[2]
    T106hup[num]=Tcup[3]
    T106hdown[num]=Tcdown[3]
    T148hup[num]=Tcup[4]
    T148hdown[num]=Tcdown[4]
    T196hup[num]=Tcup[5]
    T196hdown[num]=Tcdown[5]
    T252hup[num]=Tcup[6]
    T252hdown[num]=Tcdown[6]
    T303hup[num]=Tcup[7]
    T303hdown[num]=Tcdown[7]
    T406hup[num]=Tcup[8]
    T406hdown[num]=Tcdown[8]
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
#fig=plt.figure(figsize=(4.5, 8.))
#fig=plt.figure()
ax2=fig.add_subplot(312)
point62cen1=ax2.errorbar(energy,r62cen,yerr=[r62errdown,r62errup],color='b',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#point62h=ax2.errorbar(energy,r62hcen,yerr=[r62errhdown,r62errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
band62cen1=ax2.fill_between(energy,r62down,r62up,color='blue',alpha=0.25,facecolor='b',edgecolor='',zorder=2)
line62cen1,=ax2.plot(energy,r62cen,color='b',alpha=0.3,zorder=2)
#point62h=ax2.fill_between(energy,r62hdown,r62hup,color='r',alpha=0.25,facecolor='b',edgecolor='',zorder=1)
#line62h,=ax2.plot(energy,r62hcen,color='b',alpha=0.3,zorder=1)
exp=ax2.errorbar(energyrhic,value62,yerr=erro62,color='b',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
#ax2.legend(((point62cen,band62cen,line62cen),exp),(r'fRG',r'STAR preliminary'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax2.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
plt.axis([5.,230.,-100.,100.])
ax2.set_xscale('symlog')
#plt.axis([5.,230.,-10.,20.])
ax2.set_yscale('symlog')
#plt.xticks([])
ax2.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
#ax2.set_xticklabels(['406','303','252','196','148','106','78','68','22'],rotation=60,fontsize=7)
#ax2.xaxis.tick_top()
plt.yticks([-50,-40,-30,-20,-10,-1,0,1,10,20,30,40,50])
ax2.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.xaxis.set_label_position('top') 
ax2.set_ylabel(r'$R^B_{62}(R^p_{62})$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(7)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(7)


ax3=fig.add_subplot(311)
errbartf421=ax3.errorbar(energy,r42cen,yerr=[r42errdown,r42errup],color='b',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#ax3.errorbar(energy,r42hcen,yerr=[r42errhdown,r42errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
bandtf421=ax3.fill_between(energy,r42down,r42up,color='b',alpha=0.25,facecolor='b',edgecolor='',zorder=2)
linetf421,=ax3.plot(energy,r42cen,color='b',alpha=0.3,zorder=2)
#ax3.fill_between(energy,r42hdown,r42hup,color='b',alpha=0.25,facecolor='b',edgecolor='',zorder=1)
#ax3.plot(energy,r42hcen,color='b',alpha=0.3,zorder=1)
exp=ax3.errorbar(energy,kurtosis[:,0],yerr=kurtosis[:,1],color='c',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
#ax3.errorbar(energy,kurtosis[:,0],color='red')
ax3.plot(blackline,r42line,dashes=[4,2],color='m',linewidth='1')
#ax3.legend(((errbartf,bandtf,linetf),exp),(r'fRG',r'STAR data'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax3.set_xscale('symlog')
plt.axis([5,230,-0.5,2.8])
ax3.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
#ax3.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
ax3.set_xticklabels(['406','303','252','196','148','106','78','68','22'],rotation=60,fontsize=7)
ax3.xaxis.tick_top()
ax3.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.xaxis.set_label_position('top') 
#ax3.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax3.set_ylabel(r'$R^B_{42}(R^p_{42})$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(7)



ax4=fig.add_subplot(313)
errbartf821=ax4.errorbar(energy,r82cen,yerr=[r82errdown,r82errup],color='b',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
ax4.errorbar(energy,r82cen,yerr=[r82errup,r82errdown],color='b',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#ax4.errorbar(energy,r82hcen,yerr=[r82errhdown,r82errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
bandtf821=ax4.fill_between(energy,r82down,r82up,color='b',alpha=0.25,facecolor='b',edgecolor='',zorder=2)
linetf821,=ax4.plot(energy,r82cen,color='b',alpha=0.3,zorder=2)
#ax4.fill_between(energy,r82hdown,r82hup,color='b',alpha=0.25,facecolor='b',edgecolor='',zorder=1)
#ax4.plot(energy,r82hcen,color='b',alpha=0.3,zorder=1)
ax4.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
#ax4.legend([(errbartf,bandtf,linetf)],[r'fRG'],loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax4.set_xscale('symlog')
#ax4.set_yscale('symlog')
#plt.axis([5,230,-10000.,1000.])
plt.axis([5,230,-50,50])
#plt.yticks([-10000,-9000,-8000,-7000,-6000,-5000,-4000,-3000,-2000,-1000,-900,-800,-700,-600,-500,-400,-300,-200,-100,-90,-80,-70,-60,-50,-40,-30,-20,-10,-1,0,1,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
ax4.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
ax4.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
ax4.set_xlabel('$\sqrt{s_{\mathrm{NN}}}\,[\mathrm{GeV}]$', fontsize=14, color='black')
ax4.set_ylabel(r'$R^B_{82}(R^p_{82})$', fontsize=14, color='black')
for label in ax4.yaxis.get_ticklabels():
    label.set_fontsize(7)
print(r62down)
print(r62up)

fig.subplots_adjust(top=0.93, bottom=0.08, left=0.15, right=0.9, hspace=0.,
                    wspace=0.25)




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
T22hup=np.zeros(100)
T22hdown=np.zeros(100)
T68hup=np.zeros(100)
T68hdown=np.zeros(100)
T78hup=np.zeros(100)
T78hdown=np.zeros(100)
T106hup=np.zeros(100)
T106hdown=np.zeros(100)
T148hup=np.zeros(100)
T148hdown=np.zeros(100)
T196hup=np.zeros(100)
T196hdown=np.zeros(100)
T252hup=np.zeros(100)
T252hdown=np.zeros(100)
T303hup=np.zeros(100)
T303hdown=np.zeros(100)
T406hup=np.zeros(100)
T406hdown=np.zeros(100)
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
    Tf22[num]=162.
    Tf68[num]=163.
    Tf78[num]=163.
    Tf106[num]=161.
    Tf148[num]=159.
    Tf196[num]=156.
    Tf252[num]=151.
    Tf303[num]=145.
    Tf406[num]=134.



energy=[200.,62.4,54.4,39.,27.,19.6,14.5,11.5,7.7]
#############################################################################################################################################
xsame=np.linspace(0.,299.,300)
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

print(xsame)
print(Tcup)
print(T)

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
r8222=np.zeros((300,20))
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


dif6222minc=np.zeros(300)
dif6222minu=np.zeros(300)
dif6222mind=np.zeros(300)
dif6222minc=abs(r62mub22cen+0.5)
dif6222minu=abs(max6222+0.5)
dif6222mind=abs(min6222+0.5)
min6222cindex=np.argmin(dif6222minc[80:300])+80
min6222uindex=np.argmin(dif6222minu[80:300])+80
min6222dindex=np.argmin(dif6222mind[80:300])+80
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
min22cen_index=162
min22up_index=162
min22down_index=162

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
r3268=np.zeros((300,20))
r4268=np.zeros((300,20))
r6268=np.zeros((300,20))
r8268=np.zeros((300,20))
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
min68cen_index=163
min68up_index=163
min68down_index=163
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
r3278=np.zeros((300,20))
r4278=np.zeros((300,20))
r6278=np.zeros((300,20))
r8278=np.zeros((300,20))
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
min78cen_index=163
min78up_index=163
min78down_index=163
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
r32106=np.zeros((300,20))
r42106=np.zeros((300,20))
r62106=np.zeros((300,20))
r82106=np.zeros((300,20))
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
min106cen_index=161
min106up_index=161
min106down_index=161
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
r82148=np.zeros((300,20))
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

r32mub148cen=spline(T/ctcen,r32mub148cen,xsame)*c
max148=max148*c
min148=min148*c
r42mub148cen=spline(T/ctcen,r42mub148cen,xsame)
r62mub148cen=spline(T/ctcen,r62mub148cen,xsame)
r82mub148cen=spline(T/ctcen,r82mub148cen,xsame)

dif148cen=abs(r42mub148cen-0.196254)
dif148up=abs(max42148-0.196254)
dif148down=abs(min42148-0.196254)
min148cen_index=159
min148up_index=159
min148down_index=159
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
r82196=np.zeros((300,100))
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

r32mub196cen=spline(T/ctcen,r32mub196cen,xsame)*c
max196=max196*c
min196=min196*c
r42mub196cen=spline(T/ctcen,r42mub196cen,xsame)
r62mub196cen=spline(T/ctcen,r62mub196cen,xsame)
r82mub196cen=spline(T/ctcen,r82mub196cen,xsame)

dif196cen=abs(r42mub196cen-0.140553)
dif196up=abs(max42196-0.140553)
dif196down=abs(min42196-0.140553)
min196cen_index=156
min196up_index=156
min196down_index=156
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
r82252=np.zeros((300,100))
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

r32mub252cen=spline(T/ctcen,r32mub252cen,xsame)*c
max252=max252*c
min252=min252*c
r42mub252cen=spline(T/ctcen,r42mub252cen,xsame)
r62mub252cen=spline(T/ctcen,r62mub252cen,xsame)
r82mub252cen=spline(T/ctcen,r82mub252cen,xsame)

dif252cen=abs(r42mub252cen-1.468760)
dif252up=abs(max42252-1.468760)
dif252down=abs(min42252-1.468760)
min252cen_index=151
min252up_index=151
min252down_index=151
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
print(r42252cen)
print(r42252up)
print(r42252down)
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
r82303=np.zeros((300,100))
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

r32mub303cen=spline(T/ctcen,r32mub303cen,xsame)*c
max303=max303*c
min303=min303*c
r42mub303cen=spline(T/ctcen,r42mub303cen,xsame)
r62mub303cen=spline(T/ctcen,r62mub303cen,xsame)
r82mub303cen=spline(T/ctcen,r82mub303cen,xsame)

dif303cen=abs(r42mub303cen-0.695796)
dif303up=abs(max42303-0.695796)
dif303down=abs(min42303-0.695796)
min303cen_index=145
min303up_index=145
min303down_index=145
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
r82406=np.zeros((300,100))
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

r32mub406cen=spline(T/ctcen,r32mub406cen,xsame)*c
max406=max406*c
min406=min406*c
r42mub406cen=spline(T/ctcen,r42mub406cen,xsame)
r62mub406cen=spline(T/ctcen,r62mub406cen,xsame)
r82mub406cen=spline(T/ctcen,r82mub406cen,xsame)

dif406cen=abs(r42mub406cen-1.766972)
dif406up=abs(max42406-1.766972)
dif406down=abs(min42406-1.766972)
min406cen_index=134
min406up_index=134
min406down_index=134
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


r42hcen=[r4222hcen,r4268hcen,r4278hcen,r42106hcen,r42148hcen,r42196hcen,r42252hcen,r42303hcen,r42406hcen]
r62hcen=[r6222hcen,r6268hcen,r6278hcen,r62106hcen,r62148hcen,r62196hcen,r62252hcen,r62303hcen,r62406hcen]
r42hup=[r4222uph,r4268uph,r4278uph,r42106uph,r42148uph,r42196uph,r42252uph,r42303uph,r42406uph]
r42hdown=[r4222downh,r4268downh,r4278downh,r42106downh,r42148downh,r42196downh,r42252downh,r42303downh,r42406downh]
r62hup=[r6222uph,r6268uph,r6278uph,r62106uph,r62148uph,r62196uph,r62252uph,r62303uph,r62406uph]
r62hdown=[r6222downh,r6268downh,r6278downh,r62106downh,r62148downh,r62196downh,r62252downh,r62303downh,r62406downh]


r62cen=[r6222cen,r6268cen,r6278cen,r62106cen,r62148cen,r62196cen,r62252cen,r62303cen,r62406cen]
r62up=[r6222up,r6268up,r6278up,r62106up,r62148up,r62196up,r62252up,r62303up,r62406up]
r62down=[r6222down,r6268down,r6278down,r62106down,r62148down,r62196down,r62252down,r62303down,r62406down]

r42up=[r4222up,r4268up,r4278up,r42106up,r42148up,r42196up,r42252up,r42303up,r42406up]
r42down=[r4222down,r4268down,r4278down,r42106down,r42148down,r42196down,r42252down,r42303down,r42406down]
r42cen=[r4222cen,r4268cen,r4278cen,r42106cen,r42148cen,r42196cen,r42252cen,r42303cen,r42406cen]

r82cen=[r8222cen,r8268cen,r8278cen,r82106cen,r82148cen,r82196cen,r82252cen,r82303cen,r82406cen]
r82up=[r8222up,r8268up,r8278up,r82106up,r82148up,r82196up,r82252up,r82303up,r82406up]
r82down=[r8222down,r8268down,r8278down,r82106down,r82148down,r82196down,r82252down,r82303down,r82406down]

r82hcen=[r8222hcen,r8268hcen,r8278hcen,r82106hcen,r82148hcen,r82196hcen,r82252hcen,r82303hcen,r82406hcen]
r82hup=[r8222uph,r8268uph,r8278uph,r82106uph,r82148uph,r82196uph,r82252uph,r82303uph,r82406uph]
r82hdown=[r8222downh,r8268downh,r8278downh,r82106downh,r82148downh,r82196downh,r82252downh,r82303downh,r82406downh]

r32cen=[r3222cen,r3268cen,r3278cen,r32106cen,r32148cen,r32196cen,r32252cen,r32303cen,r32406cen]
r32up=[r3222up,r3268up,r3278up,r32106up,r32148up,r32196up,r32252up,r32303up,r32406up]
r32down=[r3222down,r3268down,r3278down,r32106down,r32148down,r32196down,r32252down,r32303down,r32406down]
r32hcen=[r3222hcen,r3268hcen,r3278hcen,r32106hcen,r32148hcen,r32196hcen,r32252hcen,r32303hcen,r32406hcen]
r32hup=[r3222uph,r3268uph,r3278uph,r32106uph,r32148uph,r32196uph,r32252uph,r32303uph,r32406uph]
r32hdown=[r3222downh,r3268downh,r3278downh,r32106downh,r32148downh,r32196downh,r32252downh,r32303downh,r32406downh]
#r42和r62的上下限与中心值
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
r82errup=np.zeros(9)
r82errdown=np.zeros(9)
r32errup=np.zeros(9)
r32errdown=np.zeros(9)
r82errhup=np.zeros(9)
r82errhdown=np.zeros(9)
r32errhup=np.zeros(9)
r32errhdown=np.zeros(9)
r82errlup=np.zeros(9)
r82errldown=np.zeros(9)
r32errlup=np.zeros(9)
r32errldown=np.zeros(9)

for i in range(0,9):
    r62errup[i]=r62up[i]-r62cen[i]
    r62errdown[i]=r62cen[i]-r62down[i]
    r42errup[i]=r42up[i]-r42cen[i]
    r42errdown[i]=r42cen[i]-r42down[i]
    r62errhup[i]=r62hup[i]-r62hcen[i]
    r62errhdown[i]=r62hcen[i]-r62hdown[i]
    r42errhup[i]=r42hup[i]-r42hcen[i]
    r42errhdown[i]=r42hcen[i]-r42hdown[i]
    r82errup[i]=r82up[i]-r82cen[i]
    r82errdown[i]=r82cen[i]-r82down[i]
    r32errup[i]=r32up[i]-r32cen[i]
    r32errdown[i]=r32cen[i]-r32down[i]
    r82errhup[i]=r82hup[i]-r82hcen[i]
    r82errhdown[i]=r82hcen[i]-r82hdown[i]
    r32errhup[i]=r32hup[i]-r32hcen[i]
    r32errhdown[i]=r32hcen[i]-r32hdown[i]





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
    T22hup[num]=Tcup[0]
    T22hdown[num]=Tcdown[0]
    T68hup[num]=Tcup[1]
    T68hdown[num]=Tcdown[1]
    T78hup[num]=Tcup[2]
    T78hdown[num]=Tcdown[2]
    T106hup[num]=Tcup[3]
    T106hdown[num]=Tcdown[3]
    T148hup[num]=Tcup[4]
    T148hdown[num]=Tcdown[4]
    T196hup[num]=Tcup[5]
    T196hdown[num]=Tcdown[5]
    T252hup[num]=Tcup[6]
    T252hdown[num]=Tcdown[6]
    T303hup[num]=Tcup[7]
    T303hdown[num]=Tcdown[7]
    T406hup[num]=Tcup[8]
    T406hdown[num]=Tcdown[8]
####################################################################################################
####################################################################################################
ax2=fig.add_subplot(312)
#point62cen1=ax2.errorbar(STARenergy,STARr62cen,yerr=[STARr62errdown,STARr62errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
#band62cen1=ax2.fill_between(STARenergy,STARr62down,STARr62up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=1)
#line62cen1,=ax2.plot(STARenergy,STARr62cen,color='r',alpha=0.3,zorder=1)
point62cen2=ax2.errorbar(energy,r62cen,yerr=[r62errdown,r62errup],color='k',marker='s',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.4,zorder=2)
band62cen2=ax2.fill_between(energy,r62down,r62up,color='k',alpha=0.2,facecolor='k',edgecolor='',zorder=2)
line62cen2,=ax2.plot(energy,r62cen,color='grey',alpha=0.3,zorder=2)
exp=ax2.errorbar(energyrhic,value62,yerr=erro62,color='b',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
#ax2.legend(((point62cen1,band62cen1,line62cen1),(point62cen2,band62cen2,line62cen2),exp),(r'fRG-LEFT freezeout: STAR',r'fRG-LEFT freezeout: Andronic et al.',r'STAR preliminary'),loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax2.legend(((point62cen2,band62cen2,line62cen2),(point62cen3,band62cen3,line62cen3),(point62cen1,band62cen1,line62cen1),exp),(r'fRG-LEFT freezeout: Andronic et al.',r'fRG-LEFT 7 points fit',r'fRG-LEFT 4 points fit',r'STAR preliminary'),loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

ax2.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
plt.axis([5.,230.,-100.,100.])
ax2.set_xscale('symlog')
ax2.set_yscale('symlog')
ax2.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
plt.yticks([-50,-40,-30,-20,-10,-1,0,1,10,20,30,40,50])
ax2.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.xaxis.set_label_position('top') 
ax2.set_ylabel(r'$R^B_{62}(R^p_{62})$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(7)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(7)


ax3=fig.add_subplot(311)
#errbartf421=ax3.errorbar(STARenergy,STARr42cen,yerr=[STARr42errdown,STARr42errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
#bandtf421=ax3.fill_between(STARenergy,STARr42down,STARr42up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=1)
#linetf421,=ax3.plot(STARenergy,STARr42cen,color='r',alpha=0.3,zorder=1)
errbartf422=ax3.errorbar(energy,r42cen,yerr=[r42errdown,r42errup],color='k',marker='s',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.4,zorder=2)
bandtf422=ax3.fill_between(energy,r42down,r42up,color='k',alpha=0.2,facecolor='k',edgecolor='',zorder=2)
linetf422,=ax3.plot(energy,r42cen,color='grey',alpha=0.3,zorder=2)

exp=ax3.errorbar(energy,kurtosis[:,0],yerr=kurtosis[:,1],color='c',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
#ax3.errorbar(energy,kurtosis[:,0],color='red')
ax3.plot(blackline,r42line,dashes=[4,2],color='m',linewidth='1')
ax3.legend([(errbartf422,bandtf422,linetf422),(errbartf423,bandtf423,linetf423),(errbartf421,bandtf421,linetf421),exp],[r'fRG-LEFT freezeout: Andronic et al.',r'fRG-LEFT 7 points fit',r'fRG-LEFT 4 points fit',r'STAR data'],loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
#ax3.legend((exp),(r'STAR data'),loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax3.set_xscale('symlog')
plt.axis([5,230,-0.5,2.8])
ax3.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
#ax3.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
ax3.set_xticklabels(['406','303','252','196','148','106','78','68','22'],rotation=60,fontsize=7)
ax3.xaxis.tick_top()
ax3.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.xaxis.set_label_position('top') 
#ax3.set_xlabel('$\sqrt{S_{NN}}$', fontsize=14, color='black')
ax3.set_ylabel(r'$R^B_{42}(R^p_{42})$', fontsize=14, color='black')
#for label in ax1.xaxis.get_ticklabels():
#    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(7)



ax4=fig.add_subplot(313)
#errbartf821=ax4.errorbar(STARenergy,STARr82cen,yerr=[STARr82errdown,STARr82errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
#bandtf821=ax4.fill_between(STARenergy,STARr82down,STARr82up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=1)
#linetf821,=ax4.plot(STARenergy,STARr82cen,color='r',alpha=0.3,zorder=1)

errbartf822=ax4.errorbar(energy,r82cen,yerr=[r82errdown,r82errup],color='k',marker='s',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.4,zorder=2)
bandtf822=ax4.fill_between(energy,r82down,r82up,color='k',alpha=0.2,facecolor='k',edgecolor='',zorder=2)
linetf822,=ax4.plot(energy,r82cen,color='grey',alpha=0.3,zorder=2)

ax4.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
ax4.legend([(errbartf822,bandtf822,linetf822),(errbartf823,bandtf823,linetf823),(errbartf821,bandtf821,linetf821)],[r'fRG-LEFT freezeout: Andronic et al.',r'fRG-LEFT 7 points fit',r'fRG-LEFT 4 points fit'],loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax4.set_xscale('symlog')
ax4.set_yscale('symlog')
#plt.axis([5,230,-10000.,1000.])
plt.axis([5,230,-2000,2000])
#plt.yticks([-10000,-9000,-8000,-7000,-6000,-5000,-4000,-3000,-2000,-1000,-900,-800,-700,-600,-500,-400,-300,-200,-100,-90,-80,-70,-60,-50,-40,-30,-20,-10,-1,0,1,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
ax4.set_xticks([7.7,11.5,14.5,19.6,27,39,54.4,62.4,200])
ax4.set_xticklabels(['7.7','11.5','14.5','19.6','27','39','54.4','62.4','200'],rotation=60,fontsize=7)
ax4.set_xlabel('$\sqrt{s_{\mathrm{NN}}}\,[\mathrm{GeV}]$', fontsize=14, color='black')
ax4.set_ylabel(r'$R^B_{82}(R^p_{82})$', fontsize=14, color='black')
for label in ax4.yaxis.get_ticklabels():
    label.set_fontsize(7)
print(r62down)
print(r62up)

fig.subplots_adjust(top=0.93, bottom=0.08, left=0.15, right=0.9, hspace=0.,
                    wspace=0.25)


fig.savefig("Rm2-sqrtS.pdf")


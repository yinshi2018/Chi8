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
min22cen_index=158
min22up_index=158
min22down_index=158

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
min68cen_index=158
min68up_index=158
min68down_index=158
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
min78cen_index=158
min78up_index=158
min78down_index=158
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
min106cen_index=158
min106up_index=158
min106down_index=158
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
min148cen_index=157
min148up_index=157
min148down_index=157
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
min252cen_index=153
min252up_index=153
min252down_index=153
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
min303cen_index=150
min303up_index=150
min303down_index=150
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
min406cen_index=138
min406up_index=138
min406down_index=138
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
#point62cen1=ax2.errorbar(energy,r62cen,yerr=[r62errdown,r62errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#point62h=ax2.errorbar(energy,r62hcen,yerr=[r62errhdown,r62errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
#band62cen1=ax2.fill_between(energy,r62down,r62up,color='blue',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
#line62cen1,=ax2.plot(energy,r62cen,color='r',alpha=0.3,zorder=2)
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
#errbartf421=ax3.errorbar(energy,r42cen,yerr=[r42errdown,r42errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#ax3.errorbar(energy,r42hcen,yerr=[r42errhdown,r42errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
#bandtf421=ax3.fill_between(energy,r42down,r42up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
#linetf421,=ax3.plot(energy,r42cen,color='r',alpha=0.3,zorder=2)
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
#errbartf821=ax4.errorbar(energy,r82cen,yerr=[r82errdown,r82errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#ax4.errorbar(energy,r82cen,yerr=[r82errup,r82errdown],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
#ax4.errorbar(energy,r82hcen,yerr=[r82errhdown,r82errhup],color='b',marker='^',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=1)
#bandtf821=ax4.fill_between(energy,r82down,r82up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
#linetf821,=ax4.plot(energy,r82cen,color='r',alpha=0.3,zorder=2)
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
#STAR
T27up=np.zeros(100)
T27down=np.zeros(100)
T69up=np.zeros(100)
T69down=np.zeros(100)
T104up=np.zeros(100)
T104down=np.zeros(100)
T151up=np.zeros(100)
T151down=np.zeros(100)
T195up=np.zeros(100)
T195down=np.zeros(100)
T292up=np.zeros(100)
T292down=np.zeros(100)
T399up=np.zeros(100)
T399down=np.zeros(100)
####################################################################################################
#STAR200
chi2mub27cen=np.loadtxt(r'./STAR/mub27/cmucen/final/buffer/chi2.dat')
chi3mub27cen=np.loadtxt(r'./STAR/mub27/cmucen/final/buffer/chi3.dat')
chi4mub27cen=np.loadtxt(r'./STAR/mub27/cmucen/final/buffer/chi4.dat')
chi6mub27cen=np.loadtxt(r'./STAR/mub27/cmucen/final/buffer/chi6.dat')
chi8mub27cen=np.loadtxt(r'./STAR/mub27/cmucen/final/buffer/chi8.dat')
r32mub27cen=chi3mub27cen/chi2mub27cen
r42mub27cen=chi4mub27cen/chi2mub27cen
r62mub27cen=chi6mub27cen/chi2mub27cen
r82mub27cen=chi8mub27cen/chi2mub27cen
chi2mub27up=np.loadtxt(r'./STAR/mub27/cmuup/final/buffer/chi2.dat')
chi3mub27up=np.loadtxt(r'./STAR/mub27/cmuup/final/buffer/chi3.dat')
chi4mub27up=np.loadtxt(r'./STAR/mub27/cmuup/final/buffer/chi4.dat')
chi6mub27up=np.loadtxt(r'./STAR/mub27/cmuup/final/buffer/chi6.dat')
chi8mub27up=np.loadtxt(r'./STAR/mub27/cmuup/final/buffer/chi8.dat')
r32mub27up=chi3mub27up/chi2mub27up
r42mub27up=chi4mub27up/chi2mub27up
r62mub27up=chi6mub27up/chi2mub27up
r82mub27up=chi8mub27up/chi2mub27up
chi2mub27down=np.loadtxt(r'./STAR/mub27/cmudown/final/buffer/chi2.dat')
chi3mub27down=np.loadtxt(r'./STAR/mub27/cmudown/final/buffer/chi3.dat')
chi4mub27down=np.loadtxt(r'./STAR/mub27/cmudown/final/buffer/chi4.dat')
chi6mub27down=np.loadtxt(r'./STAR/mub27/cmudown/final/buffer/chi6.dat')
chi8mub27down=np.loadtxt(r'./STAR/mub27/cmudown/final/buffer/chi8.dat')
r32mub27down=chi3mub27down/chi2mub27down
r42mub27down=chi4mub27down/chi2mub27down
r62mub27down=chi6mub27down/chi2mub27down
r82mub27down=chi8mub27down/chi2mub27down
r3227=np.zeros((300,20))
r4227=np.zeros((300,20))
r6227=np.zeros((300,20))
r8227=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r3227[:,t]=spline(T/ct[t],r32mub27up,xsame)
    else:
       r3227[:,t]=spline(T/ct[t-10],r32mub27down,xsame)


for num in range(1,20):
    if num==1:
       max27=np.maximum(r3227[:,num-1],r3227[:,num])
       min27=np.minimum(r3227[:,num-1],r3227[:,num])
    else:
       max27=np.maximum(max27,r3227[:,num])
       min27=np.minimum(min27,r3227[:,num])

for t in range(0,20):
    if t<10:
       r4227[:,t]=spline(T/ct[t],r42mub27up,xsame)
    else:
       r4227[:,t]=spline(T/ct[t-10],r42mub27down,xsame)

for t in range(0,20):
    if t<10:
       r4227[:,t]=spline(T/ct[t],r42mub27up,xsame)
    else:
       r4227[:,t]=spline(T/ct[t-10],r42mub27down,xsame)


for num in range(1,20):
    if num==1:
       max4227=np.maximum(r4227[:,num-1],r4227[:,num])
       min4227=np.minimum(r4227[:,num-1],r4227[:,num])
    else:
       max4227=np.maximum(max4227,r4227[:,num])
       min4227=np.minimum(min4227,r4227[:,num])

for t in range(0,20):
    if t<10:
       r6227[:,t]=spline(T/ct[t],r62mub27up,xsame)
    else:
       r6227[:,t]=spline(T/ct[t-10],r62mub27down,xsame)


for num in range(1,20):
    if num==1:
       max6227=np.maximum(r6227[:,num-1],r6227[:,num])
       min6227=np.minimum(r6227[:,num-1],r6227[:,num])
    else:
       max6227=np.maximum(max6227,r6227[:,num])
       min6227=np.minimum(min6227,r6227[:,num])

for t in range(0,20):
    if t<10:
       r8227[:,t]=spline(T/ct[t],r82mub27up,xsame)
    else:
       r8227[:,t]=spline(T/ct[t-10],r82mub27down,xsame)

for num in range(1,20):
    if num==1:
       max8227=np.maximum(r8227[:,num-1],r8227[:,num])
       min8227=np.minimum(r8227[:,num-1],r8227[:,num])
    else:
       max8227=np.maximum(max8227,r8227[:,num])
       min8227=np.minimum(min8227,r8227[:,num])

r32mub27cen=spline(T/ctcen,r32mub27cen,xsame)*c
max27=max27*c
min27=min27*c
r42mub27cen=spline(T/ctcen,r42mub27cen,xsame)
r62mub27cen=spline(T/ctcen,r62mub27cen,xsame)
r82mub27cen=spline(T/ctcen,r82mub27cen,xsame)


dif6227minc=np.zeros(300)
dif6227minu=np.zeros(300)
dif6227mind=np.zeros(300)
dif6227minc=abs(r62mub27cen+0.5)
dif6227minu=abs(max6227+0.5)
dif6227mind=abs(min6227+0.5)
min6227cindex=np.argmin(dif6227minc[80:300])+80
min6227uindex=np.argmin(dif6227minu[80:300])+80
min6227dindex=np.argmin(dif6227mind[80:300])+80
r62minc=r62mub27cen[min6227cindex]
r62minu=max6227[min6227uindex]
r62mind=min6227[min6227dindex]
erru=r62minu-r62minc
errd=r62minc-r62mind
print(r62minc)
print(erru)
print(errd)



dif27cen=abs(r42mub27cen-0.900669)
dif27up=abs(max4222-0.900669)
dif27down=abs(min4222-0.900669)
min27cen_index=168
min27up_index=168
min27down_index=168

print(min27cen_index)
#print(min22up_index)
#print(min22down_index)
r3227cen=r32mub27cen[min27cen_index]
r4227cen=r42mub27cen[min27cen_index]
r6227cen=r62mub27cen[min27cen_index]
r8227cen=r82mub27cen[min27cen_index]
#r3227hcen=r32mub27cen[min22cen_index+int(min22cen_index*deltat)]
#r4227hcen=r42mub27cen[min22cen_index+int(min22cen_index*deltat)]
#r6227hcen=r62mub27cen[min22cen_index+int(min22cen_index*deltat)]
#r8227hcen=r82mub27cen[min22cen_index+int(min22cen_index*deltat)]
r3227hcen=r32mub27cen[Tcen[0]]
r4227hcen=r42mub27cen[Tcen[0]]
r6227hcen=r62mub27cen[Tcen[0]]
r8227hcen=r82mub27cen[Tcen[0]]


r32=[max27[min27up_index],max27[min27down_index],min27[min27up_index],min27[min27down_index]]
#r32h=[max22[min22up_index+int(min22up_index*deltat)],max22[min22down_index+int(min22down_index*deltat)],min22[min22up_index+int(min22up_index*deltat)],min22[min22down_index+int(min22down_index*deltat)]]
r32h=[max27[Tcup[0]],max27[Tcdown[0]],min27[Tcup[0]],min27[Tcdown[0]]]
r3227up=np.max(r32)
r3227down=np.min(r32)
r3227uph=np.max(r32h)
r3227downh=np.min(r32h)

r42=[max4227[min27up_index],max4227[min27down_index],min4227[min27up_index],min4227[min27down_index]]
#r42h=[max4222[min22up_index+int(min22up_index*deltat)],max4222[min22down_index+int(min22down_index*deltat)],min4222[min22up_index+int(min22up_index*deltat)],min4222[min22down_index+int(min22down_index*deltat)]]
r42h=[max4227[Tcup[0]],max4227[Tcdown[0]],min4227[Tcup[0]],min4227[Tcdown[0]]]
r4227up=np.max(r42)
r4227down=np.min(r42)
r4227uph=np.max(r42h)
r4227downh=np.min(r42h)


r62=[max6227[min27up_index],max6227[min27down_index],min6227[min27up_index],min6227[min27down_index]]
#r62h=[max6222[min22up_index+int(min22up_index*deltat)],max6222[min22down_index+int(min22down_index*deltat)],min6222[min22up_index+int(min22up_index*deltat)],min6222[min22down_index+int(min22down_index*deltat)]]
r62h=[max6227[Tcup[0]],max6227[Tcdown[0]],min6227[Tcup[0]],min6227[Tcdown[0]]]
r6227up=np.max(r62)
r6227down=np.min(r62)
r6227uph=np.max(r62h)
r6227downh=np.min(r62h)


r82=[max8227[min27up_index],max8227[min27down_index],min8227[min27up_index],min8227[min22down_index]]
#r82h=[max8222[min22up_index+int(min22up_index*deltat)],max8222[min22down_index+int(min22down_index*deltat)],min8222[min22up_index+int(min22up_index*deltat)],min8222[min22down_index+int(min22down_index*deltat)]]
r82h=[max8227[Tcup[0]],max8227[Tcdown[0]],min8227[Tcup[0]],min8227[Tcdown[0]]]
r8227up=np.max(r82)
r8227down=np.min(r82)
r8227uph=np.max(r82h)
r8227downh=np.min(r82h)
####################################################################################################
#STAR62
chi2mub69cen=np.loadtxt(r'./STAR/mub69/cmucen/final/buffer/chi2.dat')
chi3mub69cen=np.loadtxt(r'./STAR/mub69/cmucen/final/buffer/chi3.dat')
chi4mub69cen=np.loadtxt(r'./STAR/mub69/cmucen/final/buffer/chi4.dat')
chi6mub69cen=np.loadtxt(r'./STAR/mub69/cmucen/final/buffer/chi6.dat')
chi8mub69cen=np.loadtxt(r'./STAR/mub69/cmucen/final/buffer/chi8.dat')
r32mub69cen=chi3mub69cen/chi2mub69cen
r42mub69cen=chi4mub69cen/chi2mub69cen
r62mub69cen=chi6mub69cen/chi2mub69cen
r82mub69cen=chi8mub69cen/chi2mub69cen
chi2mub69up=np.loadtxt(r'./STAR/mub69/cmuup/final/buffer/chi2.dat')
chi3mub69up=np.loadtxt(r'./STAR/mub69/cmuup/final/buffer/chi3.dat')
chi4mub69up=np.loadtxt(r'./STAR/mub69/cmuup/final/buffer/chi4.dat')
chi6mub69up=np.loadtxt(r'./STAR/mub69/cmuup/final/buffer/chi6.dat')
chi8mub69up=np.loadtxt(r'./STAR/mub69/cmuup/final/buffer/chi8.dat')
r32mub69up=chi3mub69up/chi2mub69up
r42mub69up=chi4mub69up/chi2mub69up
r62mub69up=chi6mub69up/chi2mub69up
r82mub69up=chi8mub69up/chi2mub69up
chi2mub69down=np.loadtxt(r'./STAR/mub69/cmudown/final/buffer/chi2.dat')
chi3mub69down=np.loadtxt(r'./STAR/mub69/cmudown/final/buffer/chi3.dat')
chi4mub69down=np.loadtxt(r'./STAR/mub69/cmudown/final/buffer/chi4.dat')
chi6mub69down=np.loadtxt(r'./STAR/mub69/cmudown/final/buffer/chi6.dat')
chi8mub69down=np.loadtxt(r'./STAR/mub69/cmudown/final/buffer/chi8.dat')
r32mub69down=chi3mub69down/chi2mub69down
r42mub69down=chi4mub69down/chi2mub69down
r62mub69down=chi6mub69down/chi2mub69down
r82mub69down=chi8mub69down/chi2mub69down
r3269=np.zeros((300,20))
r4269=np.zeros((300,20))
r6269=np.zeros((300,20))
r8269=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r3269[:,t]=spline(T/ct[t],r32mub69up,xsame)
    else:
       r3269[:,t]=spline(T/ct[t-10],r32mub69down,xsame)


for num in range(1,20):
    if num==1:
       max69=np.maximum(r3269[:,num-1],r3269[:,num])
       min69=np.minimum(r3269[:,num-1],r3269[:,num])
    else:
       max69=np.maximum(max69,r3269[:,num])
       min69=np.minimum(min69,r3269[:,num])

for t in range(0,20):
    if t<10:
       r4269[:,t]=spline(T/ct[t],r42mub69up,xsame)
    else:
       r4269[:,t]=spline(T/ct[t-10],r42mub69down,xsame)


for num in range(1,20):
    if num==1:
       max4269=np.maximum(r4269[:,num-1],r4269[:,num])
       min4269=np.minimum(r4269[:,num-1],r4269[:,num])
    else:
       max4269=np.maximum(max4269,r4269[:,num])
       min4269=np.minimum(min4269,r4269[:,num])

for t in range(0,20):
    if t<10:
       r6269[:,t]=spline(T/ct[t],r62mub69up,xsame)
    else:
       r6269[:,t]=spline(T/ct[t-10],r62mub69down,xsame)


for num in range(1,20):
    if num==1:
       max6269=np.maximum(r6269[:,num-1],r6269[:,num])
       min6269=np.minimum(r6269[:,num-1],r6269[:,num])
    else:
       max6269=np.maximum(max6269,r6269[:,num])
       min6269=np.minimum(min6269,r6269[:,num])

for t in range(0,20):
    if t<10:
       r8269[:,t]=spline(T/ct[t],r82mub69up,xsame)
    else:
       r8269[:,t]=spline(T/ct[t-10],r82mub69down,xsame)


for num in range(1,20):
    if num==1:
       max8269=np.maximum(r8269[:,num-1],r8269[:,num])
       min8269=np.minimum(r8269[:,num-1],r8269[:,num])
    else:
       max8269=np.maximum(max8269,r8269[:,num])
       min8269=np.minimum(min8269,r8269[:,num])

r32mub69cen=spline(T/ctcen,r32mub69cen,xsame)*c
max69=max69*c
min69=min69*c
r42mub69cen=spline(T/ctcen,r42mub69cen,xsame)
r62mub69cen=spline(T/ctcen,r62mub69cen,xsame)
r82mub69cen=spline(T/ctcen,r82mub69cen,xsame)

dif69cen=abs(r42mub69cen-0.792955)
dif69up=abs(max4269-0.792955)
dif69down=abs(min4269-0.792955)
min69cen_index=164
min69up_index=164
min69down_index=164
print(min69cen_index)
#print(min69up_index)
#print(min69down_index)
r3269cen=r32mub69cen[min69cen_index]
#r3269hcen=r32mub69cen[min69cen_index+int(min69cen_index*deltat)]
r3269hcen=r32mub69cen[Tcen[1]]
r32=[max69[min69up_index],max69[min69down_index],min69[min69up_index],min69[min69down_index]]
#r32h=[max69[min69up_index+int(min69up_index*deltat)],max69[min69down_index+int(min69down_index*deltat)],min69[min69up_index+int(min69up_index*deltat)],min69[min69down_index+int(min69down_index*deltat)]]
r32h=[max69[Tcup[1]],max69[Tcdown[1]],min69[Tcup[1]],min69[Tcdown[1]]]
r3269up=np.max(r32)
r3269down=np.min(r32)
r3269uph=np.max(r32h)
r3269downh=np.min(r32h)

r4269cen=r42mub69cen[min69cen_index]
r6269cen=r62mub69cen[min69cen_index]
#r4269hcen=r42mub69cen[min69cen_index+int(min69cen_index*deltat)]
#r6269hcen=r62mub69cen[min69cen_index+int(min69cen_index*deltat)]
r4269hcen=r42mub69cen[Tcen[1]]
r6269hcen=r62mub69cen[Tcen[1]]
r42=[max4269[min69up_index],max4269[min69down_index],min4269[min69up_index],min4269[min69down_index]]
#r42h=[max4269[min69up_index+int(min69up_index*deltat)],max4269[min69down_index+int(min69down_index*deltat)],min4269[min69up_index+int(min69up_index*deltat)],min4269[min69down_index+int(min69down_index*deltat)]]
r42h=[max4269[Tcup[1]],max4269[Tcdown[1]],min4269[Tcup[1]],min4269[Tcdown[1]]]
r4269up=np.max(r42)
r4269down=np.min(r42)
r4269uph=np.max(r42h)
r4269downh=np.min(r42h)

r62=[max6269[min69up_index],max6269[min69down_index],min6269[min69up_index],min6269[min69down_index]]
#r62h=[max6269[min69up_index+int(min69up_index*deltat)],max6269[min69down_index+int(min69down_index*deltat)],min6269[min69up_index+int(min69up_index*deltat)],min6269[min69down_index+int(min69down_index*deltat)]]
r62h=[max6269[Tcup[1]],max6269[Tcdown[1]],min6269[Tcup[1]],min6269[Tcdown[1]]]
r6269up=np.max(r62)
r6269down=np.min(r62)
r6269uph=np.max(r62h)
r6269downh=np.min(r62h)

r8269cen=r82mub69cen[min69cen_index]
#r8269hcen=r82mub69cen[min69cen_index+int(min69cen_index*deltat)]
r8269hcen=r82mub69cen[Tcen[1]]
r82=[max8269[min69up_index],max8269[min69down_index],min8269[min69up_index],min8269[min69down_index]]
#r82h=[max8269[min69up_index+int(min69up_index*deltat)],max8269[min69down_index+int(min69down_index*deltat)],min8269[min69up_index+int(min69up_index*deltat)],min8269[min69down_index+int(min69down_index*deltat)]]
r82h=[max8269[Tcup[1]],max8269[Tcdown[1]],min8269[Tcup[1]],min8269[Tcdown[1]]]
r8269up=np.max(r82)
r8269down=np.min(r82)
r8269uph=np.max(r82h)
r8269downh=np.min(r82h)
####################################################################################################
#STAR39
chi2mub104cen=np.loadtxt(r'./STAR/mub104/cmucen/final/buffer/chi2.dat')
chi3mub104cen=np.loadtxt(r'./STAR/mub104/cmucen/final/buffer/chi3.dat')
chi4mub104cen=np.loadtxt(r'./STAR/mub104/cmucen/final/buffer/chi4.dat')
chi6mub104cen=np.loadtxt(r'./STAR/mub104/cmucen/final/buffer/chi6.dat')
chi8mub104cen=np.loadtxt(r'./STAR/mub104/cmucen/final/buffer/chi8.dat')
r32mub104cen=chi3mub104cen/chi2mub104cen
r42mub104cen=chi4mub104cen/chi2mub104cen
r62mub104cen=chi6mub104cen/chi2mub104cen
r82mub104cen=chi8mub104cen/chi2mub104cen
chi2mub104up=np.loadtxt(r'./STAR/mub104/cmuup/final/buffer/chi2.dat')
chi3mub104up=np.loadtxt(r'./STAR/mub104/cmuup/final/buffer/chi3.dat')
chi4mub104up=np.loadtxt(r'./STAR/mub104/cmuup/final/buffer/chi4.dat')
chi6mub104up=np.loadtxt(r'./STAR/mub104/cmuup/final/buffer/chi6.dat')
chi8mub104up=np.loadtxt(r'./STAR/mub104/cmuup/final/buffer/chi8.dat')
r32mub104up=chi3mub104up/chi2mub104up
r42mub104up=chi4mub104up/chi2mub104up
r62mub104up=chi6mub104up/chi2mub104up
r82mub104up=chi8mub104up/chi2mub104up
chi2mub104down=np.loadtxt(r'./STAR/mub104/cmudown/final/buffer/chi2.dat')
chi3mub104down=np.loadtxt(r'./STAR/mub104/cmudown/final/buffer/chi3.dat')
chi4mub104down=np.loadtxt(r'./STAR/mub104/cmudown/final/buffer/chi4.dat')
chi6mub104down=np.loadtxt(r'./STAR/mub104/cmudown/final/buffer/chi6.dat')
chi8mub104down=np.loadtxt(r'./STAR/mub104/cmudown/final/buffer/chi8.dat')
r32mub104down=chi3mub104down/chi2mub104down
r42mub104down=chi4mub104down/chi2mub104down
r62mub104down=chi6mub104down/chi2mub104down
r82mub104down=chi8mub104down/chi2mub104down
r32104=np.zeros((300,20))
r42104=np.zeros((300,20))
r62104=np.zeros((300,20))
r82104=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r32104[:,t]=spline(T/ct[t],r32mub104up,xsame)
    else:
       r32104[:,t]=spline(T/ct[t-10],r32mub104down,xsame)


for num in range(1,20):
    if num==1:
       max104=np.maximum(r32104[:,num-1],r32104[:,num])
       min104=np.minimum(r32104[:,num-1],r32104[:,num])
    else:
       max104=np.maximum(max104,r32104[:,num])
       min104=np.minimum(min104,r32104[:,num])

for t in range(0,20):
    if t<10:
       r42104[:,t]=spline(T/ct[t],r42mub104up,xsame)
    else:
       r42104[:,t]=spline(T/ct[t-10],r42mub104down,xsame)


for num in range(1,20):
    if num==1:
       max42104=np.maximum(r42104[:,num-1],r42104[:,num])
       min42104=np.minimum(r42104[:,num-1],r42104[:,num])
    else:
       max42104=np.maximum(max42104,r42104[:,num])
       min42104=np.minimum(min42104,r42104[:,num])

for t in range(0,20):
    if t<10:
       r62104[:,t]=spline(T/ct[t],r62mub104up,xsame)
    else:
       r62104[:,t]=spline(T/ct[t-10],r62mub104down,xsame)


for num in range(1,20):
    if num==1:
       max62104=np.maximum(r62104[:,num-1],r62104[:,num])
       min62104=np.minimum(r62104[:,num-1],r62104[:,num])
    else:
       max62104=np.maximum(max62104,r62104[:,num])
       min62104=np.minimum(min62104,r62104[:,num])

for t in range(0,20):
    if t<10:
       r82104[:,t]=spline(T/ct[t],r82mub104up,xsame)
    else:
       r82104[:,t]=spline(T/ct[t-10],r82mub104down,xsame)


for num in range(1,20):
    if num==1:
       max82104=np.maximum(r82104[:,num-1],r82104[:,num])
       min82104=np.minimum(r82104[:,num-1],r82104[:,num])
    else:
       max82104=np.maximum(max82104,r82104[:,num])
       min82104=np.minimum(min82104,r82104[:,num])

r32mub104cen=spline(T/ctcen,r32mub104cen,xsame)*c
max104=max104*c
min104=min104*c
r42mub104cen=spline(T/ctcen,r42mub104cen,xsame)
r62mub104cen=spline(T/ctcen,r62mub104cen,xsame)
r82mub104cen=spline(T/ctcen,r82mub104cen,xsame)

dif104cen=abs(r42mub104cen-0.739693)
dif104up=abs(max42104-0.739693)
dif104down=abs(min42104-0.739693)
min104cen_index=160
min104up_index=160
min104down_index=160
print(min104cen_index)
#print(min104up_index)
#print(min104down_index)
r32104cen=r32mub104cen[min104cen_index]
#r32104hcen=r32mub104cen[min104cen_index+int(min104cen_index*deltat)]
r32104hcen=r32mub104cen[Tcen[3]]
r32=[max104[min104up_index],max104[min104down_index],min104[min104up_index],min104[min104down_index]]
#r32h=[max104[min104up_index+int(min104up_index*deltat)],max104[min104down_index+int(min104down_index*deltat)],min104[min104up_index+int(min104up_index*deltat)],min104[min104down_index+int(min104down_index*deltat)]]
r32h=[max104[Tcup[3]],max104[Tcdown[3]],min104[Tcup[3]],min104[Tcdown[3]]]
r32104up=np.max(r32)
r32104down=np.min(r32)
r32104uph=np.max(r32h)
r32104downh=np.min(r32h)

r42104cen=r42mub104cen[min104cen_index]
r62104cen=r62mub104cen[min104cen_index]
#r42104hcen=r42mub104cen[min104cen_index+int(min104cen_index*deltat)]
#r62104hcen=r62mub104cen[min104cen_index+int(min104cen_index*deltat)]
r42104hcen=r42mub104cen[Tcen[3]]
r62104hcen=r62mub104cen[Tcen[3]]
r42=[max42104[min104up_index],max42104[min104down_index],min42104[min104up_index],min42104[min104down_index]]
#r42h=[max42104[min104up_index+int(min104up_index*deltat)],max42104[min104down_index+int(min104down_index*deltat)],min42104[min104up_index+int(min104up_index*deltat)],min42104[min104down_index+int(min104down_index*deltat)]]
r42h=[max42104[Tcup[3]],max42104[Tcdown[3]],min42104[Tcup[3]],min42104[Tcdown[3]]]
r42104up=np.max(r42)
r42104down=np.min(r42)
r42104uph=np.max(r42h)
r42104downh=np.min(r42h)

r62=[max62104[min104up_index],max62104[min104down_index],min62104[min104up_index],min62104[min104down_index]]
#r62h=[max62104[min104up_index+int(min104up_index*deltat)],max62104[min104down_index+int(min104down_index*deltat)],min62104[min104up_index+int(min104up_index*deltat)],min62104[min104down_index+int(min104down_index*deltat)]]
r62h=[max62104[Tcup[3]],max62104[Tcdown[3]],min62104[Tcup[3]],min62104[Tcdown[3]]]
r62104up=np.max(r62)
r62104down=np.min(r62)
r62104uph=np.max(r62h)
r62104downh=np.min(r62h)

r82104cen=r82mub104cen[min104cen_index]
#r82104hcen=r82mub104cen[min104cen_index+int(min104cen_index*deltat)]
r82104hcen=r82mub104cen[Tcen[3]]
r82=[max82104[min104up_index],max82104[min104down_index],min82104[min104up_index],min82104[min104down_index]]
#r82h=[max82104[min104up_index+int(min104up_index*deltat)],max82104[min104down_index+int(min104down_index*deltat)],min82104[min104up_index+int(min104up_index*deltat)],min82104[min104down_index+int(min104down_index*deltat)]]
r82h=[max82104[Tcup[3]],max82104[Tcdown[3]],min82104[Tcup[3]],min82104[Tcdown[3]]]
r82104up=np.max(r82)
r82104down=np.min(r82)
r82104uph=np.max(r82h)
r82104downh=np.min(r82h)
####################################################################################################
#STAR27
chi2mub151cen=np.loadtxt(r'./STAR/mub151/cmucen/final/buffer/chi2.dat')
chi3mub151cen=np.loadtxt(r'./STAR/mub151/cmucen/final/buffer/chi3.dat')
chi4mub151cen=np.loadtxt(r'./STAR/mub151/cmucen/final/buffer/chi4.dat')
chi6mub151cen=np.loadtxt(r'./STAR/mub151/cmucen/final/buffer/chi6.dat')
chi8mub151cen=np.loadtxt(r'./STAR/mub151/cmucen/final/buffer/chi8.dat')
r32mub151cen=chi3mub151cen/chi2mub151cen
r42mub151cen=chi4mub151cen/chi2mub151cen
r62mub151cen=chi6mub151cen/chi2mub151cen
r82mub151cen=chi8mub151cen/chi2mub151cen
chi2mub151up=np.loadtxt(r'./STAR/mub151/cmuup/final/buffer/chi2.dat')
chi3mub151up=np.loadtxt(r'./STAR/mub151/cmuup/final/buffer/chi3.dat')
chi4mub151up=np.loadtxt(r'./STAR/mub151/cmuup/final/buffer/chi4.dat')
chi6mub151up=np.loadtxt(r'./STAR/mub151/cmuup/final/buffer/chi6.dat')
chi8mub151up=np.loadtxt(r'./STAR/mub151/cmuup/final/buffer/chi8.dat')
r32mub151up=chi3mub151up/chi2mub151up
r42mub151up=chi4mub151up/chi2mub151up
r62mub151up=chi6mub151up/chi2mub151up
r82mub151up=chi8mub151up/chi2mub151up
chi2mub151down=np.loadtxt(r'./STAR/mub151/cmudown/final/buffer/chi2.dat')
chi3mub151down=np.loadtxt(r'./STAR/mub151/cmudown/final/buffer/chi3.dat')
chi4mub151down=np.loadtxt(r'./STAR/mub151/cmudown/final/buffer/chi4.dat')
chi6mub151down=np.loadtxt(r'./STAR/mub151/cmudown/final/buffer/chi6.dat')
chi8mub151down=np.loadtxt(r'./STAR/mub151/cmudown/final/buffer/chi8.dat')
r32mub151down=chi3mub151down/chi2mub151down
r42mub151down=chi4mub151down/chi2mub151down
r62mub151down=chi6mub151down/chi2mub151down
r82mub151down=chi8mub151down/chi2mub151down
r32151=np.zeros((300,20))
r42151=np.zeros((300,20))
r62151=np.zeros((300,20))
r82151=np.zeros((300,20))
for t in range(0,20):
    if t<10:
       r32151[:,t]=spline(T/ct[t],r32mub151up,xsame)
    else:
       r32151[:,t]=spline(T/ct[t-10],r32mub151down,xsame)


for num in range(1,20):
    if num==1:
       max151=np.maximum(r32151[:,num-1],r32151[:,num])
       min151=np.minimum(r32151[:,num-1],r32151[:,num])
    else:
       max151=np.maximum(max151,r32151[:,num])
       min151=np.minimum(min151,r32151[:,num])

for t in range(0,20):
    if t<10:
       r42151[:,t]=spline(T/ct[t],r42mub151up,xsame)
    else:
       r42151[:,t]=spline(T/ct[t-10],r42mub151down,xsame)


for num in range(1,20):
    if num==1:
       max42151=np.maximum(r42151[:,num-1],r42151[:,num])
       min42151=np.minimum(r42151[:,num-1],r42151[:,num])
    else:
       max42151=np.maximum(max42151,r42151[:,num])
       min42151=np.minimum(min42151,r42151[:,num])

for t in range(0,20):
    if t<10:
       r62151[:,t]=spline(T/ct[t],r62mub151up,xsame)
    else:
       r62151[:,t]=spline(T/ct[t-10],r62mub151down,xsame)


for num in range(1,20):
    if num==1:
       max62151=np.maximum(r62151[:,num-1],r62151[:,num])
       min62151=np.minimum(r62151[:,num-1],r62151[:,num])
    else:
       max62151=np.maximum(max62151,r62151[:,num])
       min62151=np.minimum(min62151,r62151[:,num])

for t in range(0,20):
    if t<10:
       r82151[:,t]=spline(T/ct[t],r82mub151up,xsame)
    else:
       r82151[:,t]=spline(T/ct[t-10],r82mub151down,xsame)


for num in range(1,20):
    if num==1:
       max82151=np.maximum(r82151[:,num-1],r82151[:,num])
       min82151=np.minimum(r82151[:,num-1],r82151[:,num])
    else:
       max82151=np.maximum(max82151,r82151[:,num])
       min82151=np.minimum(min82151,r82151[:,num])

r32mub151cen=spline(T/ctcen,r32mub151cen,xsame)*c
max151=max151*c
min151=min151*c
r42mub151cen=spline(T/ctcen,r42mub151cen,xsame)
r62mub151cen=spline(T/ctcen,r62mub151cen,xsame)
r82mub151cen=spline(T/ctcen,r82mub151cen,xsame)

dif151cen=abs(r42mub151cen-0.196254)
dif151up=abs(max42151-0.196254)
dif151down=abs(min42151-0.196254)
min151cen_index=160
min151up_index=160
min151down_index=160
print(min151cen_index)
#print(min151up_index)
#print(min151down_index)
r32151cen=r32mub151cen[min151cen_index]
#r32151hcen=r32mub151cen[min151cen_index+int(min151cen_index*deltat)]
r32151hcen=r32mub151cen[Tcen[4]]
r32=[max151[min151up_index],max151[min151down_index],min151[min151up_index],min151[min151down_index]]
#r32h=[max151[min151up_index+int(min151up_index*deltat)],max151[min151down_index+int(min151down_index*deltat)],min151[min151up_index+int(min151up_index*deltat)],min151[min151down_index+int(min151down_index*deltat)]]
r32h=[max151[Tcup[4]],max151[Tcdown[4]],min151[Tcup[4]],min151[Tcdown[4]]]
r32151up=np.max(r32)
r32151down=np.min(r32)
r32151uph=np.max(r32h)
r32151downh=np.min(r32h)

r42151cen=r42mub151cen[min151cen_index]
r62151cen=r62mub151cen[min151cen_index]
#r42151hcen=r42mub151cen[min151cen_index+int(min151cen_index*deltat)]
#r62151hcen=r62mub151cen[min151cen_index+int(min151cen_index*deltat)]
r42151hcen=r42mub151cen[Tcen[4]]
r62151hcen=r62mub151cen[Tcen[4]]
r42=[max42151[min151up_index],max42151[min151down_index],min42151[min151up_index],min42151[min151down_index]]
#r42h=[max42151[min151up_index+int(min151up_index*deltat)],max42151[min151down_index+int(min151down_index*deltat)],min42151[min151up_index+int(min151up_index*deltat)],min42151[min151down_index+int(min151down_index*deltat)]]
r42h=[max42151[Tcup[4]],max42151[Tcdown[4]],min42151[Tcup[4]],min42151[Tcdown[4]]]
r42151up=np.max(r42)
r42151down=np.min(r42)
r42151uph=np.max(r42h)
r42151downh=np.min(r42h)

r62=[max62151[min151up_index],max62151[min151down_index],min62151[min151up_index],min62151[min151down_index]]
#r62h=[max62151[min151up_index+int(min151up_index*deltat)],max62151[min151down_index+int(min151down_index*deltat)],min62151[min151up_index+int(min151up_index*deltat)],min62151[min151down_index+int(min151down_index*deltat)]]
r62h=[max62151[Tcup[4]],max62151[Tcdown[4]],min62151[Tcup[4]],min62151[Tcdown[4]]]
r62151up=np.max(r62)
r62151down=np.min(r62)
r62151uph=np.max(r62h)
r62151downh=np.min(r62h)

r82151cen=r82mub151cen[min151cen_index]
#r82151hcen=r82mub151cen[min151cen_index+int(min151cen_index*deltat)]
r82151hcen=r82mub151cen[Tcen[4]]
r82=[max82151[min151up_index],max82151[min151down_index],min82151[min151up_index],min82151[min151down_index]]
#r82h=[max82151[min151up_index+int(min151up_index*deltat)],max82151[min151down_index+int(min151down_index*deltat)],min82151[min151up_index+int(min151up_index*deltat)],min82151[min151down_index+int(min151down_index*deltat)]]
r82h=[max82151[Tcup[4]],max82151[Tcdown[4]],min82151[Tcup[4]],min82151[Tcdown[4]]]
r82151up=np.max(r82)
r82151down=np.min(r82)
r82151uph=np.max(r82h)
r82151downh=np.min(r82h)
####################################################################################################
#STAR19.6
chi2mub195cen=np.loadtxt(r'./STAR/mub195/cmucen/final/buffer/chi2.dat')
chi3mub195cen=np.loadtxt(r'./STAR/mub195/cmucen/final/buffer/chi3.dat')
chi4mub195cen=np.loadtxt(r'./STAR/mub195/cmucen/final/buffer/chi4.dat')
chi6mub195cen=np.loadtxt(r'./STAR/mub195/cmucen/final/buffer/chi6.dat')
chi8mub195cen=np.loadtxt(r'./STAR/mub195/cmucen/final/buffer/chi8.dat')
r32mub195cen=chi3mub195cen/chi2mub195cen
r42mub195cen=chi4mub195cen/chi2mub195cen
r62mub195cen=chi6mub195cen/chi2mub195cen
r82mub195cen=chi8mub195cen/chi2mub195cen
chi2mub195up=np.loadtxt(r'./STAR/mub195/cmuup/final/buffer/chi2.dat')
chi3mub195up=np.loadtxt(r'./STAR/mub195/cmuup/final/buffer/chi3.dat')
chi4mub195up=np.loadtxt(r'./STAR/mub195/cmuup/final/buffer/chi4.dat')
chi6mub195up=np.loadtxt(r'./STAR/mub195/cmuup/final/buffer/chi6.dat')
chi8mub195up=np.loadtxt(r'./STAR/mub195/cmuup/final/buffer/chi8.dat')
r32mub195up=chi3mub195up/chi2mub195up
r42mub195up=chi4mub195up/chi2mub195up
r62mub195up=chi6mub195up/chi2mub195up
r82mub195up=chi8mub195up/chi2mub195up
chi2mub195up1=np.loadtxt(r'./STAR/mub195/cmuup1/final/buffer/chi2.dat')
chi3mub195up1=np.loadtxt(r'./STAR/mub195/cmuup1/final/buffer/chi3.dat')
chi4mub195up1=np.loadtxt(r'./STAR/mub195/cmuup1/final/buffer/chi4.dat')
chi6mub195up1=np.loadtxt(r'./STAR/mub195/cmuup1/final/buffer/chi6.dat')
chi8mub195up1=np.loadtxt(r'./STAR/mub195/cmuup1/final/buffer/chi8.dat')
r32mub195up1=chi3mub195up1/chi2mub195up1
r42mub195up1=chi4mub195up1/chi2mub195up1
r62mub195up1=chi6mub195up1/chi2mub195up1
r82mub195up1=chi8mub195up1/chi2mub195up1
chi2mub195up2=np.loadtxt(r'./STAR/mub195/cmuup2/final/buffer/chi2.dat')
chi3mub195up2=np.loadtxt(r'./STAR/mub195/cmuup2/final/buffer/chi3.dat')
chi4mub195up2=np.loadtxt(r'./STAR/mub195/cmuup2/final/buffer/chi4.dat')
chi6mub195up2=np.loadtxt(r'./STAR/mub195/cmuup2/final/buffer/chi6.dat')
chi8mub195up2=np.loadtxt(r'./STAR/mub195/cmuup2/final/buffer/chi8.dat')
r32mub195up2=chi3mub195up2/chi2mub195up2
r42mub195up2=chi4mub195up2/chi2mub195up2
r62mub195up2=chi6mub195up2/chi2mub195up2
r82mub195up2=chi8mub195up2/chi2mub195up2
chi2mub195up3=np.loadtxt(r'./STAR/mub195/cmuup3/final/buffer/chi2.dat')
chi3mub195up3=np.loadtxt(r'./STAR/mub195/cmuup3/final/buffer/chi3.dat')
chi4mub195up3=np.loadtxt(r'./STAR/mub195/cmuup3/final/buffer/chi4.dat')
chi6mub195up3=np.loadtxt(r'./STAR/mub195/cmuup3/final/buffer/chi6.dat')
chi8mub195up3=np.loadtxt(r'./STAR/mub195/cmuup3/final/buffer/chi8.dat')
r32mub195up3=chi3mub195up3/chi2mub195up3
r42mub195up3=chi4mub195up3/chi2mub195up3
r62mub195up3=chi6mub195up3/chi2mub195up3
r82mub195up3=chi8mub195up3/chi2mub195up3
chi2mub195up4=np.loadtxt(r'./STAR/mub195/cmuup4/final/buffer/chi2.dat')
chi3mub195up4=np.loadtxt(r'./STAR/mub195/cmuup4/final/buffer/chi3.dat')
chi4mub195up4=np.loadtxt(r'./STAR/mub195/cmuup4/final/buffer/chi4.dat')
chi6mub195up4=np.loadtxt(r'./STAR/mub195/cmuup4/final/buffer/chi6.dat')
chi8mub195up4=np.loadtxt(r'./STAR/mub195/cmuup4/final/buffer/chi8.dat')
r32mub195up4=chi3mub195up4/chi2mub195up4
r42mub195up4=chi4mub195up4/chi2mub195up4
r62mub195up4=chi6mub195up4/chi2mub195up4
r82mub195up4=chi8mub195up4/chi2mub195up4
chi2mub195down=np.loadtxt(r'./STAR/mub195/cmudown/final/buffer/chi2.dat')
chi3mub195down=np.loadtxt(r'./STAR/mub195/cmudown/final/buffer/chi3.dat')
chi4mub195down=np.loadtxt(r'./STAR/mub195/cmudown/final/buffer/chi4.dat')
chi6mub195down=np.loadtxt(r'./STAR/mub195/cmudown/final/buffer/chi6.dat')
chi8mub195down=np.loadtxt(r'./STAR/mub195/cmudown/final/buffer/chi8.dat')
r32mub195down=chi3mub195down/chi2mub195down
r42mub195down=chi4mub195down/chi2mub195down
r62mub195down=chi6mub195down/chi2mub195down
r82mub195down=chi8mub195down/chi2mub195down
chi2mub195down1=np.loadtxt(r'./STAR/mub195/cmudown1/final/buffer/chi2.dat')
chi3mub195down1=np.loadtxt(r'./STAR/mub195/cmudown1/final/buffer/chi3.dat')
chi4mub195down1=np.loadtxt(r'./STAR/mub195/cmudown1/final/buffer/chi4.dat')
chi6mub195down1=np.loadtxt(r'./STAR/mub195/cmudown1/final/buffer/chi6.dat')
chi8mub195down1=np.loadtxt(r'./STAR/mub195/cmudown1/final/buffer/chi8.dat')
r32mub195down1=chi3mub195down1/chi2mub195down1
r42mub195down1=chi4mub195down1/chi2mub195down1
r62mub195down1=chi6mub195down1/chi2mub195down1
r82mub195down1=chi8mub195down1/chi2mub195down1
chi2mub195down2=np.loadtxt(r'./STAR/mub195/cmudown2/final/buffer/chi2.dat')
chi3mub195down2=np.loadtxt(r'./STAR/mub195/cmudown2/final/buffer/chi3.dat')
chi4mub195down2=np.loadtxt(r'./STAR/mub195/cmudown2/final/buffer/chi4.dat')
chi6mub195down2=np.loadtxt(r'./STAR/mub195/cmudown2/final/buffer/chi6.dat')
chi8mub195down2=np.loadtxt(r'./STAR/mub195/cmudown2/final/buffer/chi8.dat')
r32mub195down2=chi3mub195down2/chi2mub195down2
r42mub195down2=chi4mub195down2/chi2mub195down2
r62mub195down2=chi6mub195down2/chi2mub195down2
r82mub195down2=chi8mub195down2/chi2mub195down2
chi2mub195down3=np.loadtxt(r'./STAR/mub195/cmudown3/final/buffer/chi2.dat')
chi3mub195down3=np.loadtxt(r'./STAR/mub195/cmudown3/final/buffer/chi3.dat')
chi4mub195down3=np.loadtxt(r'./STAR/mub195/cmudown3/final/buffer/chi4.dat')
chi6mub195down3=np.loadtxt(r'./STAR/mub195/cmudown3/final/buffer/chi6.dat')
chi8mub195down3=np.loadtxt(r'./STAR/mub195/cmudown3/final/buffer/chi8.dat')
r32mub195down3=chi3mub195down3/chi2mub195down3
r42mub195down3=chi4mub195down3/chi2mub195down3
r62mub195down3=chi6mub195down3/chi2mub195down3
r82mub195down3=chi8mub195down3/chi2mub195down3
chi2mub195down4=np.loadtxt(r'./STAR/mub195/cmudown4/final/buffer/chi2.dat')
chi3mub195down4=np.loadtxt(r'./STAR/mub195/cmudown4/final/buffer/chi3.dat')
chi4mub195down4=np.loadtxt(r'./STAR/mub195/cmudown4/final/buffer/chi4.dat')
chi6mub195down4=np.loadtxt(r'./STAR/mub195/cmudown4/final/buffer/chi6.dat')
chi8mub195down4=np.loadtxt(r'./STAR/mub195/cmudown4/final/buffer/chi8.dat')
r32mub195down4=chi3mub195down4/chi2mub195down4
r42mub195down4=chi4mub195down4/chi2mub195down4
r62mub195down4=chi6mub195down4/chi2mub195down4
r82mub195down4=chi8mub195down4/chi2mub195down4
r32195=np.zeros((300,100))
r42195=np.zeros((300,100))
r62195=np.zeros((300,100))
r82195=np.zeros((300,100))
for t in range(0,100):
    if t<10:
       r32195[:,t]=spline(T/ct[t],r32mub195up,xsame)
    else:
       if t>=10 and t<20:
          r32195[:,t]=spline(T/ct[t-10],r32mub195up1,xsame)
       else:
          if t>=20 and t<30:
             r32195[:,t]=spline(T/ct[t-20],r32mub195up2,xsame)
          else: 
             if t>=30 and t<40:
                r32195[:,t]=spline(T/ct[t-30],r32mub195up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32195[:,t]=spline(T/ct[t-40],r32mub195up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32195[:,t]=spline(T/ct[t-50],r32mub195down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32195[:,t]=spline(T/ct[t-60],r32mub195down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32195[:,t]=spline(T/ct[t-70],r32mub195down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32195[:,t]=spline(T/ct[t-80],r32mub195down3,xsame)
                            else:
                                r32195[:,t]=spline(T/ct[t-90],r32mub195down4,xsame)

for t in range(0,100):
    if t<10:
       r42195[:,t]=spline(T/ct[t],r42mub195up,xsame)
    else:
       if t>=10 and t<20:
          r42195[:,t]=spline(T/ct[t-10],r42mub195up1,xsame)
       else:
          if t>=20 and t<30:
             r42195[:,t]=spline(T/ct[t-20],r42mub195up2,xsame)
          else: 
             if t>=30 and t<40:
                r42195[:,t]=spline(T/ct[t-30],r42mub195up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42195[:,t]=spline(T/ct[t-40],r42mub195up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42195[:,t]=spline(T/ct[t-50],r42mub195down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42195[:,t]=spline(T/ct[t-60],r42mub195down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42195[:,t]=spline(T/ct[t-70],r42mub195down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42195[:,t]=spline(T/ct[t-80],r42mub195down3,xsame)
                            else:
                                r42195[:,t]=spline(T/ct[t-90],r42mub195down4,xsame)

for t in range(0,100):
    if t<10:
       r62195[:,t]=spline(T/ct[t],r62mub195up,xsame)
    else:
       if t>=10 and t<20:
          r62195[:,t]=spline(T/ct[t-10],r62mub195up1,xsame)
       else:
          if t>=20 and t<30:
             r62195[:,t]=spline(T/ct[t-20],r62mub195up2,xsame)
          else: 
             if t>=30 and t<40:
                r62195[:,t]=spline(T/ct[t-30],r62mub195up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62195[:,t]=spline(T/ct[t-40],r62mub195up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62195[:,t]=spline(T/ct[t-50],r62mub195down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62195[:,t]=spline(T/ct[t-60],r62mub195down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62195[:,t]=spline(T/ct[t-70],r62mub195down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62195[:,t]=spline(T/ct[t-80],r62mub195down3,xsame)
                            else:
                                r62195[:,t]=spline(T/ct[t-90],r62mub195down4,xsame)

for t in range(0,100):
    if t<10:
       r82195[:,t]=spline(T/ct[t],r82mub195up,xsame)
    else:
       if t>=10 and t<20:
          r82195[:,t]=spline(T/ct[t-10],r82mub195up1,xsame)
       else:
          if t>=20 and t<30:
             r82195[:,t]=spline(T/ct[t-20],r82mub195up2,xsame)
          else: 
             if t>=30 and t<40:
                r82195[:,t]=spline(T/ct[t-30],r82mub195up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82195[:,t]=spline(T/ct[t-40],r82mub195up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82195[:,t]=spline(T/ct[t-50],r82mub195down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82195[:,t]=spline(T/ct[t-60],r82mub195down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82195[:,t]=spline(T/ct[t-70],r82mub195down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82195[:,t]=spline(T/ct[t-80],r82mub195down3,xsame)
                            else:
                                r82195[:,t]=spline(T/ct[t-90],r82mub195down4,xsame)


for num in range(1,100):
    if num==1:
       max195=np.maximum(r32195[:,num-1],r32195[:,num])
       min195=np.minimum(r32195[:,num-1],r32195[:,num])
    else:
       max195=np.maximum(max195,r32195[:,num])
       min195=np.minimum(min195,r32195[:,num])

for num in range(1,100):
    if num==1:
       max42195=np.maximum(r42195[:,num-1],r42195[:,num])
       min42195=np.minimum(r42195[:,num-1],r42195[:,num])
    else:
       max42195=np.maximum(max42195,r42195[:,num])
       min42195=np.minimum(min42195,r42195[:,num])

for num in range(1,100):
    if num==1:
       max62195=np.maximum(r62195[:,num-1],r62195[:,num])
       min62195=np.minimum(r62195[:,num-1],r62195[:,num])
    else:
       max62195=np.maximum(max62195,r62195[:,num])
       min62195=np.minimum(min62195,r62195[:,num])

for num in range(1,100):
    if num==1:
       max82195=np.maximum(r82195[:,num-1],r82195[:,num])
       min82195=np.minimum(r82195[:,num-1],r82195[:,num])
    else:
       max82195=np.maximum(max82195,r82195[:,num])
       min82195=np.minimum(min82195,r82195[:,num])

r32mub195cen=spline(T/ctcen,r32mub195cen,xsame)*c
max195=max195*c
min195=min195*c
r42mub195cen=spline(T/ctcen,r42mub195cen,xsame)
r62mub195cen=spline(T/ctcen,r62mub195cen,xsame)
r82mub195cen=spline(T/ctcen,r82mub195cen,xsame)

dif195cen=abs(r42mub195cen-0.140553)
dif195up=abs(max42195-0.140553)
dif195down=abs(min42195-0.140553)
min195cen_index=158
min195up_index=158
min195down_index=158
print(min195cen_index)
#print(min195up_index)
#print(min195down_index)
r32195cen=r32mub195cen[min195cen_index]
#r32195hcen=r32mub195cen[min195cen_index+int(min195cen_index*deltat)]
r32195hcen=r32mub195cen[Tcen[5]]
r32=[max195[min195up_index],max195[min195down_index],min195[min195up_index],min195[min195down_index]]
#r32h=[max195[min195up_index+int(min195up_index*deltat)],max195[min195down_index+int(min195down_index*deltat)],min195[min195up_index+int(min195up_index*deltat)],min195[min195down_index+int(min195down_index*deltat)]]
r32h=[max195[Tcup[5]],max195[Tcdown[5]],min195[Tcup[5]],min195[Tcdown[5]]]
r32195up=np.max(r32)
r32195down=np.min(r32)
r32195uph=np.max(r32h)
r32195downh=np.min(r32h)

r42195cen=r42mub195cen[min195cen_index]
r62195cen=r62mub195cen[min195cen_index]
#r42195hcen=r42mub195cen[min195cen_index+int(min195cen_index*deltat)]
#r62195hcen=r62mub195cen[min195cen_index+int(min195cen_index*deltat)]
r42195hcen=r42mub195cen[Tcen[5]]
r62195hcen=r62mub195cen[Tcen[5]]
r42=[max42195[min195up_index],max42195[min195down_index],min42195[min195up_index],min42195[min195down_index]]
#r42h=[max42195[min195up_index+int(min195up_index*deltat)],max42195[min195down_index+int(min195down_index*deltat)],min42195[min195up_index+int(min195up_index*deltat)],min42195[min195down_index+int(min195down_index*deltat)]]
r42h=[max42195[Tcup[5]],max42195[Tcdown[5]],min42195[Tcup[5]],min42195[Tcdown[5]]]
r42195up=np.max(r42)
r42195down=np.min(r42)
r42195uph=np.max(r42h)
r42195downh=np.min(r42h)

r62=[max62195[min195up_index],max62195[min195down_index],min62195[min195up_index],min62195[min195down_index]]
#r62h=[max62195[min195up_index+int(min195up_index*deltat)],max62195[min195down_index+int(min195down_index*deltat)],min62195[min195up_index+int(min195up_index*deltat)],min62195[min195down_index+int(min195down_index*deltat)]]
r62h=[max62195[Tcup[5]],max62195[Tcdown[5]],min62195[Tcup[5]],min62195[Tcdown[5]]]
r62195up=np.max(r62)
r62195down=np.min(r62)
r62195uph=np.max(r62h)
r62195downh=np.min(r62h)

r82195cen=r82mub195cen[min195cen_index]
#r82195hcen=r82mub195cen[min195cen_index+int(min195cen_index*deltat)]
r82195hcen=r82mub195cen[Tcen[5]]
r82=[max82195[min195up_index],max82195[min195down_index],min82195[min195up_index],min82195[min195down_index]]
#r82h=[max82195[min195up_index+int(min195up_index*deltat)],max82195[min195down_index+int(min195down_index*deltat)],min82195[min195up_index+int(min195up_index*deltat)],min82195[min195down_index+int(min195down_index*deltat)]]
r82h=[max82195[Tcup[5]],max82195[Tcdown[5]],min82195[Tcup[5]],min82195[Tcdown[5]]]
r82195up=np.max(r82)
r82195down=np.min(r82)
r82195uph=np.max(r82h)
r82195downh=np.min(r82h)
####################################################################################################
#STAR11.5
chi2mub292cen=np.loadtxt(r'./STAR/mub292/cmucen/final/buffer/chi2.dat')
chi3mub292cen=np.loadtxt(r'./STAR/mub292/cmucen/final/buffer/chi3.dat')
chi4mub292cen=np.loadtxt(r'./STAR/mub292/cmucen/final/buffer/chi4.dat')
chi6mub292cen=np.loadtxt(r'./STAR/mub292/cmucen/final/buffer/chi6.dat')
chi8mub292cen=np.loadtxt(r'./STAR/mub292/cmucen/final/buffer/chi8.dat')
r32mub292cen=chi3mub292cen/chi2mub292cen
r42mub292cen=chi4mub292cen/chi2mub292cen
r62mub292cen=chi6mub292cen/chi2mub292cen
r82mub292cen=chi8mub292cen/chi2mub292cen
chi2mub292up=np.loadtxt(r'./STAR/mub292/cmuup/final/buffer/chi2.dat')
chi3mub292up=np.loadtxt(r'./STAR/mub292/cmuup/final/buffer/chi3.dat')
chi4mub292up=np.loadtxt(r'./STAR/mub292/cmuup/final/buffer/chi4.dat')
chi6mub292up=np.loadtxt(r'./STAR/mub292/cmuup/final/buffer/chi6.dat')
chi8mub292up=np.loadtxt(r'./STAR/mub292/cmuup/final/buffer/chi8.dat')
r32mub292up=chi3mub292up/chi2mub292up
r42mub292up=chi4mub292up/chi2mub292up
r62mub292up=chi6mub292up/chi2mub292up
r82mub292up=chi8mub292up/chi2mub292up
chi2mub292up1=np.loadtxt(r'./STAR/mub292/cmuup1/final/buffer/chi2.dat')
chi3mub292up1=np.loadtxt(r'./STAR/mub292/cmuup1/final/buffer/chi3.dat')
chi4mub292up1=np.loadtxt(r'./STAR/mub292/cmuup1/final/buffer/chi4.dat')
chi6mub292up1=np.loadtxt(r'./STAR/mub292/cmuup1/final/buffer/chi6.dat')
chi8mub292up1=np.loadtxt(r'./STAR/mub292/cmuup1/final/buffer/chi8.dat')
r32mub292up1=chi3mub292up1/chi2mub292up1
r42mub292up1=chi4mub292up1/chi2mub292up1
r62mub292up1=chi6mub292up1/chi2mub292up1
r82mub292up1=chi8mub292up1/chi2mub292up1
chi2mub292up2=np.loadtxt(r'./STAR/mub292/cmuup2/final/buffer/chi2.dat')
chi3mub292up2=np.loadtxt(r'./STAR/mub292/cmuup2/final/buffer/chi3.dat')
chi4mub292up2=np.loadtxt(r'./STAR/mub292/cmuup2/final/buffer/chi4.dat')
chi6mub292up2=np.loadtxt(r'./STAR/mub292/cmuup2/final/buffer/chi6.dat')
chi8mub292up2=np.loadtxt(r'./STAR/mub292/cmuup2/final/buffer/chi8.dat')
r32mub292up2=chi3mub292up2/chi2mub292up2
r42mub292up2=chi4mub292up2/chi2mub292up2
r62mub292up2=chi6mub292up2/chi2mub292up2
r82mub292up2=chi8mub292up2/chi2mub292up2
chi2mub292up3=np.loadtxt(r'./STAR/mub292/cmuup3/final/buffer/chi2.dat')
chi3mub292up3=np.loadtxt(r'./STAR/mub292/cmuup3/final/buffer/chi3.dat')
chi4mub292up3=np.loadtxt(r'./STAR/mub292/cmuup3/final/buffer/chi4.dat')
chi6mub292up3=np.loadtxt(r'./STAR/mub292/cmuup3/final/buffer/chi6.dat')
chi8mub292up3=np.loadtxt(r'./STAR/mub292/cmuup3/final/buffer/chi8.dat')
r32mub292up3=chi3mub292up3/chi2mub292up3
r42mub292up3=chi4mub292up3/chi2mub292up3
r62mub292up3=chi6mub292up3/chi2mub292up3
r82mub292up3=chi8mub292up3/chi2mub292up3
chi2mub292up4=np.loadtxt(r'./STAR/mub292/cmuup4/final/buffer/chi2.dat')
chi3mub292up4=np.loadtxt(r'./STAR/mub292/cmuup4/final/buffer/chi3.dat')
chi4mub292up4=np.loadtxt(r'./STAR/mub292/cmuup4/final/buffer/chi4.dat')
chi6mub292up4=np.loadtxt(r'./STAR/mub292/cmuup4/final/buffer/chi6.dat')
chi8mub292up4=np.loadtxt(r'./STAR/mub292/cmuup4/final/buffer/chi8.dat')
r32mub292up4=chi3mub292up4/chi2mub292up4
r42mub292up4=chi4mub292up4/chi2mub292up4
r62mub292up4=chi6mub292up4/chi2mub292up4
r82mub292up4=chi8mub292up4/chi2mub292up4
chi2mub292down=np.loadtxt(r'./STAR/mub292/cmudown/final/buffer/chi2.dat')
chi3mub292down=np.loadtxt(r'./STAR/mub292/cmudown/final/buffer/chi3.dat')
chi4mub292down=np.loadtxt(r'./STAR/mub292/cmudown/final/buffer/chi4.dat')
chi6mub292down=np.loadtxt(r'./STAR/mub292/cmudown/final/buffer/chi6.dat')
chi8mub292down=np.loadtxt(r'./STAR/mub292/cmudown/final/buffer/chi8.dat')
r32mub292down=chi3mub292down/chi2mub292down
r42mub292down=chi4mub292down/chi2mub292down
r62mub292down=chi6mub292down/chi2mub292down
r82mub292down=chi8mub292down/chi2mub292down
chi2mub292down1=np.loadtxt(r'./STAR/mub292/cmudown1/final/buffer/chi2.dat')
chi3mub292down1=np.loadtxt(r'./STAR/mub292/cmudown1/final/buffer/chi3.dat')
chi4mub292down1=np.loadtxt(r'./STAR/mub292/cmudown1/final/buffer/chi4.dat')
chi6mub292down1=np.loadtxt(r'./STAR/mub292/cmudown1/final/buffer/chi6.dat')
chi8mub292down1=np.loadtxt(r'./STAR/mub292/cmudown1/final/buffer/chi8.dat')
r32mub292down1=chi3mub292down1/chi2mub292down1
r42mub292down1=chi4mub292down1/chi2mub292down1
r62mub292down1=chi6mub292down1/chi2mub292down1
r82mub292down1=chi8mub292down1/chi2mub292down1
chi2mub292down2=np.loadtxt(r'./STAR/mub292/cmudown2/final/buffer/chi2.dat')
chi3mub292down2=np.loadtxt(r'./STAR/mub292/cmudown2/final/buffer/chi3.dat')
chi4mub292down2=np.loadtxt(r'./STAR/mub292/cmudown2/final/buffer/chi4.dat')
chi6mub292down2=np.loadtxt(r'./STAR/mub292/cmudown2/final/buffer/chi6.dat')
chi8mub292down2=np.loadtxt(r'./STAR/mub292/cmudown2/final/buffer/chi8.dat')
r32mub292down2=chi3mub292down2/chi2mub292down2
r42mub292down2=chi4mub292down2/chi2mub292down2
r62mub292down2=chi6mub292down2/chi2mub292down2
r82mub292down2=chi8mub292down2/chi2mub292down2
chi2mub292down3=np.loadtxt(r'./STAR/mub292/cmudown3/final/buffer/chi2.dat')
chi3mub292down3=np.loadtxt(r'./STAR/mub292/cmudown3/final/buffer/chi3.dat')
chi4mub292down3=np.loadtxt(r'./STAR/mub292/cmudown3/final/buffer/chi4.dat')
chi6mub292down3=np.loadtxt(r'./STAR/mub292/cmudown3/final/buffer/chi6.dat')
chi8mub292down3=np.loadtxt(r'./STAR/mub292/cmudown3/final/buffer/chi8.dat')
r32mub292down3=chi3mub292down3/chi2mub292down3
r42mub292down3=chi4mub292down3/chi2mub292down3
r62mub292down3=chi6mub292down3/chi2mub292down3
r82mub292down3=chi8mub292down3/chi2mub292down3
chi2mub292down4=np.loadtxt(r'./STAR/mub292/cmudown4/final/buffer/chi2.dat')
chi3mub292down4=np.loadtxt(r'./STAR/mub292/cmudown4/final/buffer/chi3.dat')
chi4mub292down4=np.loadtxt(r'./STAR/mub292/cmudown4/final/buffer/chi4.dat')
chi6mub292down4=np.loadtxt(r'./STAR/mub292/cmudown4/final/buffer/chi6.dat')
chi8mub292down4=np.loadtxt(r'./STAR/mub292/cmudown4/final/buffer/chi8.dat')
r32mub292down4=chi3mub292down4/chi2mub292down4
r42mub292down4=chi4mub292down4/chi2mub292down4
r62mub292down4=chi6mub292down4/chi2mub292down4
r82mub292down4=chi8mub292down4/chi2mub292down4
r32292=np.zeros((300,100))
r42292=np.zeros((300,100))
r62292=np.zeros((300,100))
r82292=np.zeros((300,100))
for t in range(0,100):
    if t<10:
       r32292[:,t]=spline(T/ct[t],r32mub292up,xsame)
    else:
       if t>=10 and t<20:
          r32292[:,t]=spline(T/ct[t-10],r32mub292up1,xsame)
       else:
          if t>=20 and t<30:
             r32292[:,t]=spline(T/ct[t-20],r32mub292up2,xsame)
          else: 
             if t>=30 and t<40:
                r32292[:,t]=spline(T/ct[t-30],r32mub292up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32292[:,t]=spline(T/ct[t-40],r32mub292up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32292[:,t]=spline(T/ct[t-50],r32mub292down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32292[:,t]=spline(T/ct[t-60],r32mub292down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32292[:,t]=spline(T/ct[t-70],r32mub292down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32292[:,t]=spline(T/ct[t-80],r32mub292down3,xsame)
                            else:
                                r32292[:,t]=spline(T/ct[t-90],r32mub292down4,xsame)

for t in range(0,100):
    if t<10:
       r42292[:,t]=spline(T/ct[t],r42mub292up,xsame)
    else:
       if t>=10 and t<20:
          r42292[:,t]=spline(T/ct[t-10],r42mub292up1,xsame)
       else:
          if t>=20 and t<30:
             r42292[:,t]=spline(T/ct[t-20],r42mub292up2,xsame)
          else: 
             if t>=30 and t<40:
                r42292[:,t]=spline(T/ct[t-30],r42mub292up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42292[:,t]=spline(T/ct[t-40],r42mub292up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42292[:,t]=spline(T/ct[t-50],r42mub292down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42292[:,t]=spline(T/ct[t-60],r42mub292down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42292[:,t]=spline(T/ct[t-70],r42mub292down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42292[:,t]=spline(T/ct[t-80],r42mub292down3,xsame)
                            else:
                                r42292[:,t]=spline(T/ct[t-90],r42mub292down4,xsame)

for t in range(0,100):
    if t<10:
       r62292[:,t]=spline(T/ct[t],r62mub292up,xsame)
    else:
       if t>=10 and t<20:
          r62292[:,t]=spline(T/ct[t-10],r62mub292up1,xsame)
       else:
          if t>=20 and t<30:
             r62292[:,t]=spline(T/ct[t-20],r62mub292up2,xsame)
          else: 
             if t>=30 and t<40:
                r62292[:,t]=spline(T/ct[t-30],r62mub292up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62292[:,t]=spline(T/ct[t-40],r62mub292up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62292[:,t]=spline(T/ct[t-50],r62mub292down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62292[:,t]=spline(T/ct[t-60],r62mub292down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62292[:,t]=spline(T/ct[t-70],r62mub292down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62292[:,t]=spline(T/ct[t-80],r62mub292down3,xsame)
                            else:
                                r62292[:,t]=spline(T/ct[t-90],r62mub292down4,xsame)

for t in range(0,100):
    if t<10:
       r82292[:,t]=spline(T/ct[t],r82mub292up,xsame)
    else:
       if t>=10 and t<20:
          r82292[:,t]=spline(T/ct[t-10],r82mub292up1,xsame)
       else:
          if t>=20 and t<30:
             r82292[:,t]=spline(T/ct[t-20],r82mub292up2,xsame)
          else: 
             if t>=30 and t<40:
                r82292[:,t]=spline(T/ct[t-30],r82mub292up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82292[:,t]=spline(T/ct[t-40],r82mub292up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82292[:,t]=spline(T/ct[t-50],r82mub292down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82292[:,t]=spline(T/ct[t-60],r82mub292down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82292[:,t]=spline(T/ct[t-70],r82mub292down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82292[:,t]=spline(T/ct[t-80],r82mub292down3,xsame)
                            else:
                                r82292[:,t]=spline(T/ct[t-90],r82mub292down4,xsame)


for num in range(1,100):
    if num==1:
       max292=np.maximum(r32292[:,num-1],r32292[:,num])
       min292=np.minimum(r32292[:,num-1],r32292[:,num])
    else:
       max292=np.maximum(max292,r32292[:,num])
       min292=np.minimum(min292,r32292[:,num])

for num in range(1,100):
    if num==1:
       max42292=np.maximum(r42292[:,num-1],r42292[:,num])
       min42292=np.minimum(r42292[:,num-1],r42292[:,num])
    else:
       max42292=np.maximum(max42292,r42292[:,num])
       min42292=np.minimum(min42292,r42292[:,num])

for num in range(1,100):
    if num==1:
       max62292=np.maximum(r62292[:,num-1],r62292[:,num])
       min62292=np.minimum(r62292[:,num-1],r62292[:,num])
    else:
       max62292=np.maximum(max62292,r62292[:,num])
       min62292=np.minimum(min62292,r62292[:,num])

for num in range(1,100):
    if num==1:
       max82292=np.maximum(r82292[:,num-1],r82292[:,num])
       min82292=np.minimum(r82292[:,num-1],r82292[:,num])
    else:
       max82292=np.maximum(max82292,r82292[:,num])
       min82292=np.minimum(min82292,r82292[:,num])

r32mub292cen=spline(T/ctcen,r32mub292cen,xsame)*c
max292=max292*c
min292=min292*c
r42mub292cen=spline(T/ctcen,r42mub292cen,xsame)
r62mub292cen=spline(T/ctcen,r62mub292cen,xsame)
r82mub292cen=spline(T/ctcen,r82mub292cen,xsame)

dif292cen=abs(r42mub292cen-0.695796)
dif292up=abs(max42292-0.695796)
dif292down=abs(min42292-0.695796)
min292cen_index=151
min292up_index=151
min292down_index=151
print(min292cen_index)
#print(min292up_index)
#print(min292down_index)
r32292cen=r32mub292cen[min292cen_index]
#r32292hcen=r32mub292cen[min292cen_index+int(min292cen_index*deltat)]
r32292hcen=r32mub292cen[Tcen[7]]
r32=[max292[min292up_index],max292[min292down_index],min292[min292up_index],min292[min292down_index]]
#r32h=[max292[min292up_index+int(min292up_index*deltat)],max292[min292down_index+int(min292down_index*deltat)],min292[min292up_index+int(min292up_index*deltat)],min292[min292down_index+int(min292down_index*deltat)]]
r32h=[max292[Tcup[7]],max292[Tcdown[7]],min292[Tcup[7]],min292[Tcdown[7]]]
r32292up=np.max(r32)
r32292down=np.min(r32)
r32292uph=np.max(r32h)
r32292downh=np.min(r32h)

r42292cen=r42mub292cen[min292cen_index]
r62292cen=r62mub292cen[min292cen_index]
#r42292hcen=r42mub292cen[min292cen_index+int(min292cen_index*deltat)]
#r62292hcen=r62mub292cen[min292cen_index+int(min292cen_index*deltat)]
r42292hcen=r42mub292cen[Tcen[7]]
r62292hcen=r62mub292cen[Tcen[7]]
r42=[max42292[min292up_index],max42292[min292down_index],min42292[min292up_index],min42292[min292down_index]]
#r42h=[max42292[min292up_index+int(min292up_index*deltat)],max42292[min292down_index+int(min292down_index*deltat)],min42292[min292up_index+int(min292up_index*deltat)],min42292[min292down_index+int(min292down_index*deltat)]]
r42h=[max42292[Tcup[7]],max42292[Tcdown[7]],min42292[Tcup[7]],min42292[Tcdown[7]]]
r42292up=np.max(r42)
r42292down=np.min(r42)
r42292uph=np.max(r42h)
r42292downh=np.min(r42h)

r62=[max62292[min292up_index],max62292[min292down_index],min62292[min292up_index],min62292[min292down_index]]
#r62h=[max62292[min292up_index+int(min292up_index*deltat)],max62292[min292down_index+int(min292down_index*deltat)],min62292[min292up_index+int(min292up_index*deltat)],min62292[min292down_index+int(min292down_index*deltat)]]
r62h=[max62292[Tcup[7]],max62292[Tcdown[7]],min62292[Tcup[7]],min62292[Tcdown[7]]]
r62292up=np.max(r62)
r62292down=np.min(r62)
r62292uph=np.max(r62h)
r62292downh=np.min(r62h)

r82292cen=r82mub292cen[min292cen_index]
#r82292hcen=r82mub292cen[min292cen_index+int(min292cen_index*deltat)]
r82292hcen=r82mub292cen[Tcen[7]]
r82=[max82292[min292up_index],max82292[min292down_index],min82292[min292up_index],min82292[min292down_index]]
#r82h=[max82292[min292up_index+int(min292up_index*deltat)],max82292[min292down_index+int(min292down_index*deltat)],min82292[min292up_index+int(min292up_index*deltat)],min82292[min292down_index+int(min292down_index*deltat)]]
r82h=[max82292[Tcup[7]],max82292[Tcdown[7]],min82292[Tcup[7]],min82292[Tcdown[7]]]
r82292up=np.max(r82)
r82292down=np.min(r82)
r82292uph=np.max(r82h)
r82292downh=np.min(r82h)
####################################################################################################
#STAR7.7
chi2mub399cen=np.loadtxt(r'./STAR/mub399/cmucen/final/buffer/chi2.dat')
chi3mub399cen=np.loadtxt(r'./STAR/mub399/cmucen/final/buffer/chi3.dat')
chi4mub399cen=np.loadtxt(r'./STAR/mub399/cmucen/final/buffer/chi4.dat')
chi6mub399cen=np.loadtxt(r'./STAR/mub399/cmucen/final/buffer/chi6.dat')
chi8mub399cen=np.loadtxt(r'./STAR/mub399/cmucen/final/buffer/chi8.dat')
r32mub399cen=chi3mub399cen/chi2mub399cen
r42mub399cen=chi4mub399cen/chi2mub399cen
r62mub399cen=chi6mub399cen/chi2mub399cen
r82mub399cen=chi8mub399cen/chi2mub399cen
chi2mub399up=np.loadtxt(r'./STAR/mub399/cmuup/final/buffer/chi2.dat')
chi3mub399up=np.loadtxt(r'./STAR/mub399/cmuup/final/buffer/chi3.dat')
chi4mub399up=np.loadtxt(r'./STAR/mub399/cmuup/final/buffer/chi4.dat')
chi6mub399up=np.loadtxt(r'./STAR/mub399/cmuup/final/buffer/chi6.dat')
chi8mub399up=np.loadtxt(r'./STAR/mub399/cmuup/final/buffer/chi8.dat')
r32mub399up=chi3mub399up/chi2mub399up
r42mub399up=chi4mub399up/chi2mub399up
r62mub399up=chi6mub399up/chi2mub399up
r82mub399up=chi8mub399up/chi2mub399up
chi2mub399up1=np.loadtxt(r'./STAR/mub399/cmuup1/final/buffer/chi2.dat')
chi3mub399up1=np.loadtxt(r'./STAR/mub399/cmuup1/final/buffer/chi3.dat')
chi4mub399up1=np.loadtxt(r'./STAR/mub399/cmuup1/final/buffer/chi4.dat')
chi6mub399up1=np.loadtxt(r'./STAR/mub399/cmuup1/final/buffer/chi6.dat')
chi8mub399up1=np.loadtxt(r'./STAR/mub399/cmuup1/final/buffer/chi8.dat')
r32mub399up1=chi3mub399up1/chi2mub399up1
r42mub399up1=chi4mub399up1/chi2mub399up1
r62mub399up1=chi6mub399up1/chi2mub399up1
r82mub399up1=chi8mub399up1/chi2mub399up1
chi2mub399up2=np.loadtxt(r'./STAR/mub399/cmuup2/final/buffer/chi2.dat')
chi3mub399up2=np.loadtxt(r'./STAR/mub399/cmuup2/final/buffer/chi3.dat')
chi4mub399up2=np.loadtxt(r'./STAR/mub399/cmuup2/final/buffer/chi4.dat')
chi6mub399up2=np.loadtxt(r'./STAR/mub399/cmuup2/final/buffer/chi6.dat')
chi8mub399up2=np.loadtxt(r'./STAR/mub399/cmuup2/final/buffer/chi8.dat')
r32mub399up2=chi3mub399up2/chi2mub399up2
r42mub399up2=chi4mub399up2/chi2mub399up2
r62mub399up2=chi6mub399up2/chi2mub399up2
r82mub399up2=chi8mub399up2/chi2mub399up2
chi2mub399up3=np.loadtxt(r'./STAR/mub399/cmuup3/final/buffer/chi2.dat')
chi3mub399up3=np.loadtxt(r'./STAR/mub399/cmuup3/final/buffer/chi3.dat')
chi4mub399up3=np.loadtxt(r'./STAR/mub399/cmuup3/final/buffer/chi4.dat')
chi6mub399up3=np.loadtxt(r'./STAR/mub399/cmuup3/final/buffer/chi6.dat')
chi8mub399up3=np.loadtxt(r'./STAR/mub399/cmuup3/final/buffer/chi8.dat')
r32mub399up3=chi3mub399up3/chi2mub399up3
r42mub399up3=chi4mub399up3/chi2mub399up3
r62mub399up3=chi6mub399up3/chi2mub399up3
r82mub399up3=chi8mub399up3/chi2mub399up3
chi2mub399up4=np.loadtxt(r'./STAR/mub399/cmuup4/final/buffer/chi2.dat')
chi3mub399up4=np.loadtxt(r'./STAR/mub399/cmuup4/final/buffer/chi3.dat')
chi4mub399up4=np.loadtxt(r'./STAR/mub399/cmuup4/final/buffer/chi4.dat')
chi6mub399up4=np.loadtxt(r'./STAR/mub399/cmuup4/final/buffer/chi6.dat')
chi8mub399up4=np.loadtxt(r'./STAR/mub399/cmuup4/final/buffer/chi8.dat')
r32mub399up4=chi3mub399up4/chi2mub399up4
r42mub399up4=chi4mub399up4/chi2mub399up4
r62mub399up4=chi6mub399up4/chi2mub399up4
r82mub399up4=chi8mub399up4/chi2mub399up4
chi2mub399down=np.loadtxt(r'./STAR/mub399/cmudown/final/buffer/chi2.dat')
chi3mub399down=np.loadtxt(r'./STAR/mub399/cmudown/final/buffer/chi3.dat')
chi4mub399down=np.loadtxt(r'./STAR/mub399/cmudown/final/buffer/chi4.dat')
chi6mub399down=np.loadtxt(r'./STAR/mub399/cmudown/final/buffer/chi6.dat')
chi8mub399down=np.loadtxt(r'./STAR/mub399/cmudown/final/buffer/chi8.dat')
r32mub399down=chi3mub399down/chi2mub399down
r42mub399down=chi4mub399down/chi2mub399down
r62mub399down=chi6mub399down/chi2mub399down
r82mub399down=chi8mub399down/chi2mub399down
chi2mub399down1=np.loadtxt(r'./STAR/mub399/cmudown1/final/buffer/chi2.dat')
chi3mub399down1=np.loadtxt(r'./STAR/mub399/cmudown1/final/buffer/chi3.dat')
chi4mub399down1=np.loadtxt(r'./STAR/mub399/cmudown1/final/buffer/chi4.dat')
chi6mub399down1=np.loadtxt(r'./STAR/mub399/cmudown1/final/buffer/chi6.dat')
chi8mub399down1=np.loadtxt(r'./STAR/mub399/cmudown1/final/buffer/chi8.dat')
r32mub399down1=chi3mub399down1/chi2mub399down1
r42mub399down1=chi4mub399down1/chi2mub399down1
r62mub399down1=chi6mub399down1/chi2mub399down1
r82mub399down1=chi8mub399down1/chi2mub399down1
chi2mub399down2=np.loadtxt(r'./STAR/mub399/cmudown2/final/buffer/chi2.dat')
chi3mub399down2=np.loadtxt(r'./STAR/mub399/cmudown2/final/buffer/chi3.dat')
chi4mub399down2=np.loadtxt(r'./STAR/mub399/cmudown2/final/buffer/chi4.dat')
chi6mub399down2=np.loadtxt(r'./STAR/mub399/cmudown2/final/buffer/chi6.dat')
chi8mub399down2=np.loadtxt(r'./STAR/mub399/cmudown2/final/buffer/chi8.dat')
r32mub399down2=chi3mub399down2/chi2mub399down2
r42mub399down2=chi4mub399down2/chi2mub399down2
r62mub399down2=chi6mub399down2/chi2mub399down2
r82mub399down2=chi8mub399down2/chi2mub399down2
chi2mub399down3=np.loadtxt(r'./STAR/mub399/cmudown3/final/buffer/chi2.dat')
chi3mub399down3=np.loadtxt(r'./STAR/mub399/cmudown3/final/buffer/chi3.dat')
chi4mub399down3=np.loadtxt(r'./STAR/mub399/cmudown3/final/buffer/chi4.dat')
chi6mub399down3=np.loadtxt(r'./STAR/mub399/cmudown3/final/buffer/chi6.dat')
chi8mub399down3=np.loadtxt(r'./STAR/mub399/cmudown3/final/buffer/chi8.dat')
r32mub399down3=chi3mub399down3/chi2mub399down3
r42mub399down3=chi4mub399down3/chi2mub399down3
r62mub399down3=chi6mub399down3/chi2mub399down3
r82mub399down3=chi8mub399down3/chi2mub399down3
chi2mub399down4=np.loadtxt(r'./STAR/mub399/cmudown4/final/buffer/chi2.dat')
chi3mub399down4=np.loadtxt(r'./STAR/mub399/cmudown4/final/buffer/chi3.dat')
chi4mub399down4=np.loadtxt(r'./STAR/mub399/cmudown4/final/buffer/chi4.dat')
chi6mub399down4=np.loadtxt(r'./STAR/mub399/cmudown4/final/buffer/chi6.dat')
chi8mub399down4=np.loadtxt(r'./STAR/mub399/cmudown4/final/buffer/chi8.dat')
r32mub399down4=chi3mub399down4/chi2mub399down4
r42mub399down4=chi4mub399down4/chi2mub399down4
r62mub399down4=chi6mub399down4/chi2mub399down4
r82mub399down4=chi8mub399down4/chi2mub399down4
r32399=np.zeros((300,100))
r42399=np.zeros((300,100))
r62399=np.zeros((300,100))
r82399=np.zeros((300,100))
for t in range(0,100):
    if t<10:
       r32399[:,t]=spline(T/ct[t],r32mub399up,xsame)
    else:
       if t>=10 and t<20:
          r32399[:,t]=spline(T/ct[t-10],r32mub399up1,xsame)
       else:
          if t>=20 and t<30:
             r32399[:,t]=spline(T/ct[t-20],r32mub399up2,xsame)
          else: 
             if t>=30 and t<40:
                r32399[:,t]=spline(T/ct[t-30],r32mub399up3,xsame)
             else: 
                if t>=40 and t<50:
                   r32399[:,t]=spline(T/ct[t-40],r32mub399up4,xsame)
                else:
                   if t>=50 and t<60:
                      r32399[:,t]=spline(T/ct[t-50],r32mub399down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r32399[:,t]=spline(T/ct[t-60],r32mub399down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r32399[:,t]=spline(T/ct[t-70],r32mub399down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r32399[:,t]=spline(T/ct[t-80],r32mub399down3,xsame)
                            else:
                                r32399[:,t]=spline(T/ct[t-90],r32mub399down4,xsame)

for t in range(0,100):
    if t<10:
       r42399[:,t]=spline(T/ct[t],r42mub399up,xsame)
    else:
       if t>=10 and t<20:
          r42399[:,t]=spline(T/ct[t-10],r42mub399up1,xsame)
       else:
          if t>=20 and t<30:
             r42399[:,t]=spline(T/ct[t-20],r42mub399up2,xsame)
          else: 
             if t>=30 and t<40:
                r42399[:,t]=spline(T/ct[t-30],r42mub399up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42399[:,t]=spline(T/ct[t-40],r42mub399up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42399[:,t]=spline(T/ct[t-50],r42mub399down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42399[:,t]=spline(T/ct[t-60],r42mub399down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42399[:,t]=spline(T/ct[t-70],r42mub399down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42399[:,t]=spline(T/ct[t-80],r42mub399down3,xsame)
                            else:
                                r42399[:,t]=spline(T/ct[t-90],r42mub399down4,xsame)

for t in range(0,100):
    if t<10:
       r62399[:,t]=spline(T/ct[t],r62mub399up,xsame)
    else:
       if t>=10 and t<20:
          r62399[:,t]=spline(T/ct[t-10],r62mub399up1,xsame)
       else:
          if t>=20 and t<30:
             r62399[:,t]=spline(T/ct[t-20],r62mub399up2,xsame)
          else: 
             if t>=30 and t<40:
                r62399[:,t]=spline(T/ct[t-30],r62mub399up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62399[:,t]=spline(T/ct[t-40],r62mub399up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62399[:,t]=spline(T/ct[t-50],r62mub399down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62399[:,t]=spline(T/ct[t-60],r62mub399down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62399[:,t]=spline(T/ct[t-70],r62mub399down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62399[:,t]=spline(T/ct[t-80],r62mub399down3,xsame)
                            else:
                                r62399[:,t]=spline(T/ct[t-90],r62mub399down4,xsame)

for t in range(0,100):
    if t<10:
       r82399[:,t]=spline(T/ct[t],r82mub399up,xsame)
    else:
       if t>=10 and t<20:
          r82399[:,t]=spline(T/ct[t-10],r82mub399up1,xsame)
       else:
          if t>=20 and t<30:
             r82399[:,t]=spline(T/ct[t-20],r82mub399up2,xsame)
          else: 
             if t>=30 and t<40:
                r82399[:,t]=spline(T/ct[t-30],r82mub399up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82399[:,t]=spline(T/ct[t-40],r82mub399up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82399[:,t]=spline(T/ct[t-50],r82mub399down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82399[:,t]=spline(T/ct[t-60],r82mub399down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82399[:,t]=spline(T/ct[t-70],r82mub399down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82399[:,t]=spline(T/ct[t-80],r82mub399down3,xsame)
                            else:
                                r82399[:,t]=spline(T/ct[t-90],r82mub399down4,xsame)


for num in range(1,100):
    if num==1:
       max399=np.maximum(r32399[:,num-1],r32399[:,num])
       min399=np.minimum(r32399[:,num-1],r32399[:,num])
    else:
       max399=np.maximum(max399,r32399[:,num])
       min399=np.minimum(min399,r32399[:,num])

for num in range(1,100):
    if num==1:
       max42399=np.maximum(r42399[:,num-1],r42399[:,num])
       min42399=np.minimum(r42399[:,num-1],r42399[:,num])
    else:
       max42399=np.maximum(max42399,r42399[:,num])
       min42399=np.minimum(min42399,r42399[:,num])

for num in range(1,100):
    if num==1:
       max62399=np.maximum(r62399[:,num-1],r62399[:,num])
       min62399=np.minimum(r62399[:,num-1],r62399[:,num])
    else:
       max62399=np.maximum(max62399,r62399[:,num])
       min62399=np.minimum(min62399,r62399[:,num])

for num in range(1,100):
    if num==1:
       max82399=np.maximum(r82399[:,num-1],r82399[:,num])
       min82399=np.minimum(r82399[:,num-1],r82399[:,num])
    else:
       max82399=np.maximum(max82399,r82399[:,num])
       min82399=np.minimum(min82399,r82399[:,num])

r32mub399cen=spline(T/ctcen,r32mub399cen,xsame)*c
max399=max399*c
min399=min399*c
r42mub399cen=spline(T/ctcen,r42mub399cen,xsame)
r62mub399cen=spline(T/ctcen,r62mub399cen,xsame)
r82mub399cen=spline(T/ctcen,r82mub399cen,xsame)

dif399cen=abs(r42mub399cen-1.766972)
dif399up=abs(max42399-1.766972)
dif399down=abs(min42399-1.766972)
min399cen_index=135
min399up_index=135
min399down_index=135
print(min399cen_index)
#print(min399up_index)
#print(min399down_index)
r32399cen=r32mub399cen[min399cen_index]
#r32399hcen=r32mub399cen[min399cen_index+int(min399cen_index*deltat)]
r32399hcen=r32mub399cen[Tcen[8]]
r32=[max399[min399up_index],max399[min399down_index],min399[min399up_index],min399[min399down_index]]
#r32h=[max399[min399up_index+int(min399up_index*deltat)],max399[min399down_index+int(min399down_index*deltat)],min399[min399up_index+int(min399up_index*deltat)],min399[min399down_index+int(min399down_index*deltat)]]
r32h=[max399[Tcup[8]],max399[Tcdown[8]],min399[Tcup[8]],min399[Tcdown[8]]]
r32399up=np.max(r32)
r32399down=np.min(r32)
r32399uph=np.max(r32h)
r32399downh=np.min(r32h)

r42399cen=r42mub399cen[min399cen_index]
r62399cen=r62mub399cen[min399cen_index]
#r42399hcen=r42mub399cen[min399cen_index+int(min399cen_index*deltat)]
#r62399hcen=r62mub399cen[min399cen_index+int(min399cen_index*deltat)]
r42399hcen=r42mub399cen[Tcen[8]]
r62399hcen=r62mub399cen[Tcen[8]]
r42=[max42399[min399up_index],max42399[min399down_index],min42399[min399up_index],min42399[min399down_index]]
#r42h=[max42399[min399up_index+int(min399up_index*deltat)],max42399[min399down_index+int(min399down_index*deltat)],min42399[min399up_index+int(min399up_index*deltat)],min42399[min399down_index+int(min399down_index*deltat)]]
r42h=[max42399[Tcup[8]],max42399[Tcdown[8]],min42399[Tcup[8]],min42399[Tcdown[8]]]
r42399up=np.max(r42)
r42399down=np.min(r42)
r42399uph=np.max(r42h)
r42399downh=np.min(r42h)

r62=[max62399[min399up_index],max62399[min399down_index],min62399[min399up_index],min62399[min399down_index]]
#r62h=[max62399[min399up_index+int(min399up_index*deltat)],max62399[min399down_index+int(min399down_index*deltat)],min62399[min399up_index+int(min399up_index*deltat)],min62399[min399down_index+int(min399down_index*deltat)]]
r62h=[max62399[Tcup[8]],max62399[Tcdown[8]],min62399[Tcup[8]],min62399[Tcdown[8]]]
r62399up=np.max(r62)
r62399down=np.min(r62)
r62399uph=np.max(r62h)
r62399downh=np.min(r62h)

r82399cen=r82mub399cen[min399cen_index]
#r82399hcen=r82mub399cen[min399cen_index+int(min399cen_index*deltat)]
r82399hcen=r82mub399cen[Tcen[8]]
r82=[max82399[min399up_index],max82399[min399down_index],min82399[min399up_index],min82399[min399down_index]]
#r82h=[max82399[min399up_index+int(min399up_index*deltat)],max82399[min399down_index+int(min399down_index*deltat)],min82399[min399up_index+int(min399up_index*deltat)],min82399[min399down_index+int(min399down_index*deltat)]]
r82h=[max82399[Tcup[8]],max82399[Tcdown[8]],min82399[Tcup[8]],min82399[Tcdown[8]]]
r82399up=np.max(r82)
r82399down=np.min(r82)
r82399uph=np.max(r82h)
r82399downh=np.min(r82h)
####################################################################################################
STARr62cen=[r6227cen,r6269cen,r62104cen,r62151cen,r62195cen,r62292cen,r62399cen]
STARr62up=[r6227up,r6269up,r62104up,r62151up,r62195up,r62292up,r62399up]
STARr62down=[r6227down,r6269down,r62104down,r62151down,r62195down,r62292down,r62399down]

STARr42up=[r4227up,r4269up,r42104up,r42151up,r42195up,r42292up,r42399up]
STARr42down=[r4227down,r4269down,r42104down,r42151down,r42195down,r42292down,r42399down]
STARr42cen=[r4227cen,r4269cen,r42104cen,r42151cen,r42195cen,r42292cen,r42399cen]

STARr82cen=[r8227cen,r8269cen,r82104cen,r82151cen,r82195cen,r82292cen,r82399cen]
STARr82up=[r8227up,r8269up,r82104up,r82151up,r82195up,r82292up,r82399up]
STARr82down=[r8227down,r8269down,r82104down,r82151down,r82195down,r82292down,r82399down]

STARr32cen=[r3227cen,r3269cen,r32104cen,r32151cen,r32195cen,r32292cen,r32399cen]
STARr32up=[r3227up,r3269up,r32104up,r32151up,r32195up,r32292up,r32399up]
STARr32down=[r3227down,r3269down,r32104down,r32151down,r32195down,r32292down,r32399down]

#r42和r62的上下限与中心值
STARr62errup=np.zeros(7)
STARr62errdown=np.zeros(7)
STARr42errup=np.zeros(7)
STARr42errdown=np.zeros(7)
STARr62errhup=np.zeros(7)
STARr62errhdown=np.zeros(7)
STARr42errhup=np.zeros(7)
STARr42errhdown=np.zeros(7)
STARr62errlup=np.zeros(7)
STARr62errldown=np.zeros(7)
STARr42errlup=np.zeros(7)
STARr42errldown=np.zeros(7)
STARr82errup=np.zeros(7)
STARr82errdown=np.zeros(7)
STARr32errup=np.zeros(7)
STARr32errdown=np.zeros(7)
STARr82errhup=np.zeros(7)
STARr82errhdown=np.zeros(7)
STARr32errhup=np.zeros(7)
STARr32errhdown=np.zeros(7)
STARr82errlup=np.zeros(7)
STARr82errldown=np.zeros(7)
STARr32errlup=np.zeros(7)
STARr32errldown=np.zeros(7)

for i in range(0,7):
    STARr62errup[i]=STARr62up[i]-STARr62cen[i]
    STARr62errdown[i]=STARr62cen[i]-STARr62down[i]
    STARr42errup[i]=STARr42up[i]-STARr42cen[i]
    STARr42errdown[i]=STARr42cen[i]-STARr42down[i]
    STARr82errup[i]=STARr82up[i]-STARr82cen[i]
    STARr82errdown[i]=STARr82cen[i]-STARr82down[i]
    STARr32errup[i]=STARr32up[i]-STARr32cen[i]
    STARr32errdown[i]=STARr32cen[i]-STARr32down[i]






for num in range(0,100):
    T27up[num]=min27up_index
    T27down[num]=min27down_index
    T69up[num]=min69up_index
    T69down[num]=min69down_index
    T104up[num]=min104up_index
    T104down[num]=min104down_index
    T151up[num]=min151up_index
    T151down[num]=min151down_index
    T195up[num]=min195up_index
    T195down[num]=min195down_index
    T292up[num]=min292up_index
    T292down[num]=min292down_index
    T399up[num]=min399up_index
    T399down[num]=min399down_index
STARenergy=[200.,62.4,39.,27.,19.6,11.5,7.7]
####################################################################################################
ax2=fig.add_subplot(312)
point62cen1=ax2.errorbar(STARenergy,STARr62cen,yerr=[STARr62errdown,STARr62errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
band62cen1=ax2.fill_between(STARenergy,STARr62down,STARr62up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
line62cen1,=ax2.plot(STARenergy,STARr62cen,color='r',alpha=0.3,zorder=2)
point62cen2=ax2.errorbar(energy,r62cen,yerr=[r62errdown,r62errup],color='grey',marker='s',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
band62cen2=ax2.fill_between(energy,r62down,r62up,color='grey',alpha=0.25,facecolor='grey',edgecolor='',zorder=2)
line62cen2,=ax2.plot(energy,r62cen,color='grey',alpha=0.3,zorder=2)
exp=ax2.errorbar(energyrhic,value62,yerr=erro62,color='b',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
ax2.legend(((point62cen1,band62cen1,line62cen1),(point62cen2,band62cen2,line62cen2),exp),(r'fRG-LEFT freezeout: I',r'fRG-LEFT freezeout: II',r'STAR preliminary'),loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

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
errbartf421=ax3.errorbar(STARenergy,STARr42cen,yerr=[STARr42errdown,STARr42errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
bandtf421=ax3.fill_between(STARenergy,STARr42down,STARr42up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
linetf421,=ax3.plot(STARenergy,STARr42cen,color='r',alpha=0.3,zorder=2)
errbartf422=ax3.errorbar(energy,r42cen,yerr=[r42errdown,r42errup],color='grey',marker='s',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
bandtf422=ax3.fill_between(energy,r42down,r42up,color='grey',alpha=0.25,facecolor='grey',edgecolor='',zorder=2)
linetf422,=ax3.plot(energy,r42cen,color='grey',alpha=0.3,zorder=2)

exp=ax3.errorbar(energy,kurtosis[:,0],yerr=kurtosis[:,1],color='c',marker='*',linestyle='',linewidth=1,markersize=10,fillstyle='full',alpha=0.5,zorder=3)
#ax3.errorbar(energy,kurtosis[:,0],color='red')
ax3.plot(blackline,r42line,dashes=[4,2],color='m',linewidth='1')
ax3.legend([(errbartf421,bandtf421,linetf421),(errbartf422,bandtf422,linetf422),exp],[r'fRG-LEFT freezeout: I',r'fRG-LEFT freezeout: II',r'STAR data'],loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
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
errbartf821=ax4.errorbar(STARenergy,STARr82cen,yerr=[STARr82errdown,STARr82errup],color='r',marker='o',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
bandtf821=ax4.fill_between(STARenergy,STARr82down,STARr82up,color='r',alpha=0.25,facecolor='r',edgecolor='',zorder=2)
linetf821,=ax4.plot(STARenergy,STARr82cen,color='r',alpha=0.3,zorder=2)

errbartf822=ax4.errorbar(energy,r82cen,yerr=[r82errdown,r82errup],color='grey',marker='s',linestyle='',linewidth=1,markersize=5,fillstyle='full',alpha=0.5,zorder=2)
bandtf822=ax4.fill_between(energy,r82down,r82up,color='grey',alpha=0.25,facecolor='grey',edgecolor='',zorder=2)
linetf822,=ax4.plot(energy,r82cen,color='grey',alpha=0.3,zorder=2)

ax4.plot(blackline,r62line,dashes=[4,2],color='m',linewidth='1')
ax4.legend([(errbartf821,bandtf821,linetf821),(errbartf822,bandtf822,linetf822)],[r'fRG-LEFT freezeout: I',r'fRG-LEFT freezeout: II'],loc=0,fontsize=7,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)
ax4.set_xscale('symlog')
ax4.set_yscale('symlog')
#plt.axis([5,230,-10000.,1000.])
plt.axis([5,230,-2000,1000])
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


fig.savefig("STAR.pdf")


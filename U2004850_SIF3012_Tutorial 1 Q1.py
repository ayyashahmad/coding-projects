# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:22:43 2022

@author: Home
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')

t0=0
tf=0.5
h=0.1
x0=1

def F1(t, x, v):
    return v
def F2(t,x,v):
    return 6*x**2

def RK4(v0):
    t=np.arange(t0,tf+h,h)
    x=[x0]
    v=[v0]


    for i in range(len(t)-1):
        K1x = F1(t[i],x[i],v[i])
        K1v = F2(t[i],x[i],v[i])
        K2x = F1(t[i]+(h/2.0), x[i]+(h/2.0)*K1x, v[i]+h*K1v/2)
        K2v = F2(t[i]+(h/2.0), x[i]+(h/2.0)*K1x, v[i]+h*K1v/2)
        K3x = F1(t[i]+(h/2), x[i]+(h/2.0)*K2x,v[i]+h*K2v/2)
        K3v = F2(t[i]+(h/2), x[i]+(h/2.0)*K2x,v[i]+h*K2v/2)
        K4x = F1(t[i]+h, x[i]+h*K3x,v[i]+h*K3v/2)
        K4v = F2(t[i]+h, x[i]+h*K3x,v[i]+h*K3v/2)
        x.append(x[i]+h/6*(K1x+2*K2x+2*K3x+K4x))
        v.append(v[i]+h/6*(K1v+2*K2v+2*K3v+K4v))

    return x[-1]-4/9


z0=np.linspace(-2.5,-1.8,50)
y=[]
for i in z0:
    y.append(RK4(i))
print(RK4(-1.8))
print(RK4(-1.9))

plt.plot(z0,y)
plt.axhline(y=0,color='r')
plt.xlabel('x')
plt.ylabel('y')
# plt.show()

#secant method once
root=(-1.9)-RK4(-1.9)*((-1.9)-(-1.8))/(RK4(-1.9)-RK4(-1.8))
print("Root=",root)

true_root=-2*(1+0)**(-3)
print("True root=",true_root)

root_error=(root-true_root)/true_root
print("Root_error",root_error)


# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:22:29 2022

@author: Home
"""

import numpy as np
import matplotlib.pyplot as plt

l_length=50
t_length=10
dt=3
t_fin=10
dx=0.01
T_left=100
T_right=25
T_int=20
L=0.05
D=54/(7800*490)

t=np.arange(0,t_fin+1,dt)

x=np.arange(0,L+dx,dx)


grid=np.zeros((len(t),len(x)))
grid[0]=20
grid[:,0]=T_left
grid[:,-1]=T_right


for i in range(len(t)):
    for j in range(len(x)):
        if 0<i and 0<j<len(x)-1:
            grid[i][j]=grid[i-1][j]+D*(dt/(dx**2))*(grid[i-1][j-1]-2*grid[i-1][j]+grid[i-1][j+1])
            
gridplot=np.flip(grid,0)

fig, ax = plt.subplots()
im=ax.imshow(gridplot, cmap='RdBu_r', vmin = np.abs(gridplot).min(),vmax = np.abs(gridplot).max())

ax.set_xlabel('Length (m)')
ax.set_ylabel('Time (s)')

ax.set_xticks(range(len(x)))
ax.set_xticklabels(x)
ax.set_yticks(range(len(t)))
ax.set_yticklabels(np.flip(t))
ax.set_title('Diffusion evolution')
fig.colorbar(im, orientation='vertical',label="Temperature (°C)")


from numba import jit    

@jit
def TDMA(a,b,c,d):
    n = len(d)
    w= np.zeros(n-1,float)
    g= np.zeros(n, float)
    p = np.zeros(n,float)
    
    w[0] = c[0]/b[0]
    g[0] = d[0]/b[0]

    for i in range(1,n-1):
        w[i] = c[i]/(b[i] - a[i-1]*w[i-1])
    for i in range(1,n):
        g[i] = (d[i] - a[i-1]*g[i-1])/(b[i] - a[i-1]*w[i-1])
    p[n-1] = g[n-1]
    for i in range(n-1,0,-1):
        p[i-1] = g[i-1] - w[i-1]*p[i]
    return p
print(grid)
plt.show()
        
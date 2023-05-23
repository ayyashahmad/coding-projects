# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:24:41 2022

@author: Home
"""

import numpy as np
import scienceplots

plt.style.use(['science','no-latex'])
l_length=50
t_length=10
dt=3
t_fin=10
dx=0.01
T_left=100
T_right=25
T_int=20
L=0.05
D=54/(7800*490)*dt/(dx**2)

t=np.arange(0,t_fin+1,dt)

x=np.arange(0,L+dx,dx)

grid=np.zeros((len(x),len(t)))
grid[:,0]=T_int
grid[0,:]=T_left
grid[-1,:]=T_right


A=np.diag([2+2*D]*(len(x)-2),0)+np.diag([-D]*(len(x)-3),-1)+np.diag([-D]*(len(x)-3),1)
B=np.diag([2-2*D]*(len(x)-2),0)+np.diag([D]*(len(x)-3),-1)+np.diag([D]*(len(x)-3),1)

for j in range(0,len(t)-1):
    b=grid[1:-1,j].copy()
    b=np.dot(B,b)
    b[0]=b[0]+D*(grid[0,j]+grid[0,j+1])
    b[-1]=b[-1]+D*(grid[-1,j]+grid[-1,j+1])
    sol=np.linalg.solve(A,b)
    grid[1:-1,j+1]=sol


print(grid)
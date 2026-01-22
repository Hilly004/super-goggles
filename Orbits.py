import numpy as np
import matplotlib.pyplot as plt
import Positions as pos
import Data_Extraction as datex
import Planetary_Data as pdat
import RK4_Method as rk
import YR4_Orbit as ast
from mpl_toolkits import mplot3d


fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'

######

plt.figure(num=1,dpi=150)

s = (-5e9,5e9)
ax = plt.axes(projection='3d')
plt.subplot().set_aspect('equal')
ax.set_xlim3d(s)
ax.set_ylim3d(s)
ax.set_zlim3d(s)
ax.set_xlabel('x (km)')
ax.set_ylabel('y (km)')
ax.set_zlabel('z (km)')
for n in range(len(pdat.names)):
    p = pos.positions[n,:,1:4]
    ax.plot(p[:,0],p[:,1],p[:,2],linewidth=pdat.linewidths[n],color=pdat.colours[n])
ax.plot(ast.posAst[:,0],ast.posAst[:,1],ast.posAst[:,2])

#######

plt.figure(num=2)

s1=(-1e9,1e9)
ax1 = plt.axes(projection='3d')
plt.subplot().set_aspect('equal')
ax1.set_xlim3d(s1)
ax1.set_ylim3d(s1)
ax1.set_zlim3d(s1)
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.set_zlabel('z (m)')
for n in range(len(pdat.names)-3):
    posit = pos.positions[[0,1,2,3,4,5,9,10]]
    p = posit[n,:,1:4]
    ax1.plot(p[:,0],p[:,1],p[:,2],linewidth=pdat.linewidths[n],color=pdat.colours[n])
ax1.plot(ast.posAst[:,0],ast.posAst[:,1],ast.posAst[:,2])

######

plt.figure(num=3)

s2=(-1e9,1e9)
ax2 = plt.axes(projection='3d')
plt.subplot().set_aspect('equal')
ax2.set_xlim3d(s2)
ax2.set_ylim3d(s2)
ax2.set_zlim3d(s2)
ax2.set_xlabel('x (m)')
ax2.set_ylabel('y (m)')
ax2.set_zlabel('z (m)')
for n in range(len(pdat.names)-3):
    position = pos.positions2[[0,1,2,3,4,5,9,10]]
    p = position[n,:,1:4]
    ax2.plot(p[:,0],p[:,1],p[:,2],linewidth=pdat.linewidths[n],color=pdat.colours[n])
ax2.plot(ast.posAst2[:,0],ast.posAst2[:,1],ast.posAst2[:,2])
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import Positions as pos
import Data_Extraction as datex
import Planetary_Data as pdat
import RK4_Method as rk
import YR4_Orbit as ast
from mpl_toolkits import mplot3d


fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'

s = (-1e9,1e9)
plt.figure(dpi=150)
ax = plt.axes(projection='3d')

plt.subplot().set_aspect('equal')
ax.set_xlim3d(s)
ax.set_ylim3d(s)
ax.set_zlim3d(s)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
#ax.set_xticklabels((-1,-0.5,0,0.5,1))
#ax.set_yticklabels((-1,-0.5,0,0.5,1))
#ax.set_zticklabels((-1,-0.5,0,0.5,1))


for n in range(len(pdat.names)):
    p = pos.positions[n,:,1:4]
    ax.plot(p[:,0],p[:,1],p[:,2])

plt.plot(ast.posAst[:,0],ast.posAst[:,1],ast.posAst[:,2])

plt.show()


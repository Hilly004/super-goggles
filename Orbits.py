import numpy as np
import matplotlib.pyplot as plt
import Positions as pos
import Data_Extraction as datex
import Planetary_Data as pdat
import RK4_Method as rk
from mpl_toolkits import mplot3d

fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'
times = np.arange(0,4385,1)
dt = 2
posAst = np.zeros((len(times),3))
#print(pos.pos('2024YR4',0))
r = np.array(pos.vec('2024YR4',0)[1:6])

#for i,t in enumerate(times):
    #posAst[i] = r[:3]
    #rk.rk4(r,t,dt)

ax = plt.axes(projection='3d')
plt.subplot().set_aspect('equal')
ax.set_xlim3d(-1e9,1e9)
ax.set_ylim3d(-1e9,1e9)
ax.set_zlim3d(-1e9,1e9)
#ax.set_xticklabels((-1,-0.5,0,0.5,1))
#ax.set_yticklabels((-1,-0.5,0,0.5,1))
#ax.set_zticklabels((-1,-0.5,0,0.5,1))
for name in pdat.names:
    ax.plot(datex.out(fol+name+'.txt')[1],datex.out(fol+name+'.txt')[2],datex.out(fol+name+'.txt')[3], label = name)
    ax.plot(datex.out(fol+name+'.txt')[1][-1],datex.out(fol+name+'.txt')[2][-1],datex.out(fol+name+'.txt')[3][-1],marker = 'x')
    #plt.legend()
#plt.plot(posAst[:,0],posAst[:,1],posAst[:,2])

plt.show()
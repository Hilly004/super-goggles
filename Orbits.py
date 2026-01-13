import numpy as np
import matplotlib.pyplot as plt
import Positions as pos
import Data_Extraction as datex
import Planetary_Data as pdat
import RK4_Method as rk

fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'
times = np.arange(0,4385,1)
dt = 2
posAst = np.zeros((len(times),3))
#print(pos.pos('2024YR4',0))
r = np.array(pos.vec('2024YR4',0)[1:6])

for i,t in enumerate(times):
    posAst[i] = r[:3]
    rk.rk4(r,t,dt)

plt.figure().add_subplot(111,projection = '3d')
plt.subplot().set_aspect('equal')
plt.xlim((-1e9,1e9))
plt.ylim((-1e9,1e9))
for name in pdat.names:
    plt.plot(datex.out(fol+name+'.txt')[1],datex.out(fol+name+'.txt')[2],datex.out(fol+name+'.txt')[3], label = name)
    #plt.legend()
plt.plot(posAst[:,0],posAst[:,1],posAst[:,2])
plt.show()
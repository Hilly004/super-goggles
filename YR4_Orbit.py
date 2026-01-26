import RK4_Method as rk
import numpy as np
import Positions as pos

times = np.arange(0,2000,1)
dt = 2

posAst = np.zeros((len(times),3))

r0 = pos.positions[10,0,1:7] #initial position and velocity of 2024YR4

r = np.array(r0)

for t in range(len(times)):
    posAst[t] = r[:3]
    r = rk.rk4(r,t,dt)
    

######


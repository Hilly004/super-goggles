import numpy as np
import Planetary_Data as pdat
import Positions as pos

G = 6.6726e-11

def accel(p,t):
    a = [0,0,0]
    for j in range(len(pdat.names)-1): # -1 so the acceleration of the asteroid on itself isn't counted
        vec = np.array(pos.positions[j,int(t),1:4]) - np.array(p)
        d = np.sqrt(vec[0]**2+vec[1]**2+vec[2]**2)
        a = a + G*pdat.masses[j]*vec/d**3
    return(a)

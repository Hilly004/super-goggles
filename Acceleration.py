import numpy as np
import Planetary_Data as pdat
import Positions as pos

G = 6.6726*10**(-11)

def accel(p,t):
    a = [0,0,0]
    for j in range(len(pdat.names)):
        vec = np.array(pos.pos(pdat.names[j],t)) - np.array(p)
        d = 0
        for i in range(len(vec)):
            d = d + vec[i]**2
        l = np.sqrt(d)
        a = a+G*pdat.masses[j]*vec/l**3
    return(a)

#print(accel([1e8,1e8,1e8],1))
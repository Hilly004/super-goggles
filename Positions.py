import Planetary_Data as pdat
import Data_Extraction as datex
import numpy as np

fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'

loc = [f'{fol}Mercury.txt',
       f'{fol}Venus.txt',
       f'{fol}Earth.txt',
       f'{fol}Mars.txt']

for name in pdat.names:
    d0=[name]
    for i in range(0,7):
        d0.append(datex.out(fol+name+'.txt')[i,1]) #d0 = name, time, x,y,z, vx,vy,vz
    
def pos(t):
    l = []
    for name in pdat.names:
        d0=[name]
        for i in range(0,7):
            d0.append(datex.out(fol+name+'.txt')[i,t]) #d0 = name, time, x,y,z, vx,vy,vz
        l.append(d0)
    return(l) #l = [ [name1, time, x,y,z, vx,vy,vz ], [name2, time, x,y,z, vx,vy,vz ], ... ]

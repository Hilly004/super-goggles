import Planetary_Data as pdat
import Data_Extraction as datex
import numpy as np

fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'

def pos(name,t):
    d0=[]
    for i in range(1,4):
        d0.append(datex.out(fol+name+'.txt')[i,t]) #d0 = x,y,z
    return(d0) 

def vec(name,t):
    d0=[]
    for i in range(1,7):
        d0.append(datex.out(fol+name+'.txt')[i,t]) #d0 = x,y,z, vx,vy,vz
    return(d0) 

def all(name,t):
    d0=[]
    for i in range(0,7):
        d0.append(datex.out(fol+name+'.txt')[i,t]) #d0 = name, time, x,y,z, vx,vy,vz
    return(d0) 

for n in range(0,4385):
    if all('Earth',n)[0] == 2462980.5:
        print(n)
    else:
        continue

#print(np.size(datex.out(fol+'Earth.txt'))/13)

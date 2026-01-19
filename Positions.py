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
        d0.append(datex.out(fol+name+'.txt')[i,t]) #d0 = time,x,y,z, vx,vy,vz
    return(d0) 

def all(name,t):
    d0=[]
    for i in range(0,7):
        d0.append(datex.out(fol+name+'.txt')[i,t]) #d0 = name, time, x,y,z, vx,vy,vz
    return(d0) 

######

times = np.arange(0,4385)
positions = np.empty((len(pdat.names),len(times),13))

for n,name in enumerate(pdat.names):
    data = pdat.object_data[name]
    positions[n,:,:] = data[0:13,times].T
    
#######

col_times = np.arange(0,145)
col_positions = np.empty((len(pdat.col_names),len(col_times),13))

for n,name in enumerate(pdat.col_names):
    data = pdat.col_data[name]
    col_positions[n,:,:] = data[0:13,col_times].T

#print(positions[7,0,1:7])
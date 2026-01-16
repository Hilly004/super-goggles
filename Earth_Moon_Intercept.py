import numpy as np
import matplotlib.pyplot as plt
import Positions as pos
import Data_Extraction as datex
import Planetary_Data as pdat
import RK4_Method as rk

fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'
s = (-1.75e8,1.75e8)
plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim3d(s)
ax.set_ylim3d(s)
ax.set_zlim3d(s)
plt.plot(datex.out(fol+'Moon.txt')[1],datex.out(fol+'Moon.txt')[2],datex.out(fol+'Moon.txt')[3])
plt.plot(datex.out(fol+'Earth.txt')[1],datex.out(fol+'Earth.txt')[2],datex.out(fol+'Earth.txt')[3])
plt.show()
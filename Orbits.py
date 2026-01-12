import numpy as np
import matplotlib.pyplot as plt
import Positions as pos
import Data_Extraction as datex

plt.figure().add_subplot(projection = '3d')

for t in range(len(datex.out('/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/Mercury.txt')[0])-4380):
    print(pos.pos(t)[0][2],pos.pos(t)[0][3])#,pos.pos(t)[0][4])



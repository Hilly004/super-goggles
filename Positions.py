import Planetary_Data as pdat
import Data_Extraction as datex
import numpy as np

fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/dt=1day/'

######

times = np.arange(0,len(pdat.object_data['2024YR4'][0]),1)
positions = np.empty((len(pdat.names),len(times),13))

for n,name in enumerate(pdat.names):
    data = pdat.object_data[name]
    positions[n,:,:] = data[0:13,times].T
    positions[n,:,4:7]*=1000
    
#######


    



import numpy as np
import matplotlib.pyplot as plt
import Positions as pos
import Data_Extraction as datex
import Planetary_Data as pdat
import RK4_Method as rk

fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'
s = (-1.5e7,1.5e7)

####### timestep = 1 day #######

plt.figure(num = 1)

ax = plt.axes(projection='3d')
ax.set_xlim3d(s)
#ax.set_ylim3d(s)
#ax.set_zlim3d(s)
t = np.arange(2578,2585,1)
p_m = pos.positions[9,t,:]
p_e = pos.positions[3,t,:]
p_a = pos.positions[10,t,:]
ax.plot(p_m[:,1],p_m[:,2],p_m[:,3])
ax.plot(p_e[:,1],p_e[:,2],p_e[:,3])
ax.plot(p_a[:,1],p_a[:,2],p_a[:,3])

####### timestep = 1 hour #######

# 00:00 18-12-2032 _ 00:00 24-12-2032 #

plt.figure(num=2)

t1 = np.arange(0,145)
p_e_col = pos.col_positions[0,t1,:]
p_m_col = pos.col_positions[1,t1,:]
p_a_col = pos.col_positions[2,t1,:]

ax1 = plt.axes(projection='3d')

ax1.plot(p_m_col[:,1],p_m_col[:,2],p_m_col[:,3])
ax1.plot(p_e_col[:,1],p_e_col[:,2],p_e_col[:,3])
ax1.plot(p_a_col[:,1],p_a_col[:,2],p_a_col[:,3])

#######

t1 = np.arange(0,145)
p_e_col = pos.col_positions[0,t1,:]
p_m_col = pos.col_positions[1,t1,:]
p_a_col = pos.col_positions[2,t1,:]

####### timestep = 1 hour #######

# 00:00 18-12-2032 _ 00:00 24-12-2032 #

plt.figure(num=3)

ax1 = plt.axes(projection='3d')
ax1.set_xlim3d((0,-0.6e7))
ax1.set_ylim3d((1.46e8,1.48e8))

ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')


ax1.plot(p_m_col[:,1],p_m_col[:,2],p_m_col[:,3])
ax1.plot(p_e_col[:,1],p_e_col[:,2],p_e_col[:,3])
ax1.plot(p_a_col[:,1],p_a_col[:,2],p_a_col[:,3])

#ax1.plot(p_a_col[:,1]-p_a_col[:,7],p_a_col[:,2]-p_a_col[:,8],p_a_col[:,3]-p_a_col[:,9])
#ax1.plot(p_a_col[:,1]+p_a_col[:,7],p_a_col[:,2]+p_a_col[:,8],p_a_col[:,3]+p_a_col[:,9])

#######

plt.figure(num=4)

dr=np.sqrt((p_m_col[:,0]-p_e_col[:,0])**2+(p_m_col[:,1]-p_e_col[:,1])**2+(p_m_col[:,2]-p_e_col[:,2])**2)
plt.plot(dr)

#######

plt.figure(num=5)
plt.axes().set_aspect('equal')

plt.xlim((-0.6e7,0e7))
plt.ylim((14.55e7,14.85e7))

plt.plot(p_m_col[:,1],p_m_col[:,2])
plt.plot(p_e_col[:,1],p_e_col[:,2])
plt.plot(p_a_col[:,1],p_a_col[:,2])
plt.quiver(p_a_col[:,1],p_a_col[:,2],0,-p_a_col[:,3],scale_units = 'inches',width = 0.003, scale=0.7e6, headwidth = 0, headaxislength = 0, headlength = 0)
plt.quiver(p_m_col[:,1],p_m_col[:,2],0,-p_m_col[:,3],scale_units = 'inches',width = 0.003, scale=0.7e6, headwidth = 0, headaxislength = 0, headlength = 0)
plt.quiver(p_e_col[:,1],p_e_col[:,2],0,-p_e_col[:,3],scale_units = 'inches',width = 0.003, scale=0.7e6, headwidth = 0, headaxislength = 0, headlength = 0)


plt.show()
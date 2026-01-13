import numpy as np
import Acceleration as acc

def rk4(r,t,dt): #r = x,y,z,vx,vy,vz
    def deriv(r_,t_):
        pos = r_[:3]
        #print(pos)
        vel = r_[3:]
        #print(vel)
        a = acc.accel(pos,t_)
        return np.concatenate((vel,a))
    k1 = deriv(r,t)
    #print('k1',k1)
    k2 = deriv(r+0.5*dt*k1,int(t+0.5*dt))
    #print('k2',k2)
    k3 = deriv(r+0.5*dt*k2,int(t+0.5*dt))
    #print('k3',k3)
    k4 = deriv(r+dt*k3,int(t+dt))
    #print('k4',k4)
    return(r + (dt/6)*(k1+2*k2+2*k3+k4))

#print(rk4([1e8,1e8,1e8,0,0,0],0,2))
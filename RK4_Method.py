import numpy as np
import Acceleration as acc

def rk4(r,t,dt): #r = x,y,z,vx,vy,vz

    def deriv(r_,t_):

        pos = r_[:3]
        vel = r_[3:]
        a = acc.accel(pos,t_)
        return np.concatenate((vel,a))
    
    k1 = deriv(r,t)
    k2 = deriv(r+0.5*dt*k1,int(t+0.5*dt))
    k3 = deriv(r+0.5*dt*k2,int(t+0.5*dt))
    k4 = deriv(r+dt*k3,int(t+dt))

    return(r + (dt/6)*(k1+2*k2+2*k3+k4))

def rk42(r,t,dt): #r = x,y,z,vx,vy,vz

    def deriv(r_,t_):

        pos = r_[:3]
        vel = r_[3:]
        a = acc.accel2(pos,t_)
        return np.concatenate((vel,a))
    
    k1 = deriv(r,t)
    k2 = deriv(r+0.5*dt*k1,int(t+0.5*dt))
    k3 = deriv(r+0.5*dt*k2,int(t+0.5*dt))
    k4 = deriv(r+dt*k3,int(t+dt))

    return(r + (dt/6)*(k1+2*k2+2*k3+k4))
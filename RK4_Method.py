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

#print(rk4([-4.867967918197486E+08,-1.630370799414298E+08,-2.916253791783430E+07,-3.928545265704444E+00,-1.219488990091812E+01,-2.521671367514120E-01],1,2))
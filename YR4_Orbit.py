import RK4_Method as rk
import numpy as np

times = np.arange(0,2000,1)
dt = 2

posAst = np.zeros((len(times),3))

r0 = [-4.867967918197486E+08,-1.630370799414298E+08,-2.916253791783430E+07,-3.928545265704444E+00*10e3,-1.219488990091812E+01*10e3,-2.521671367514120E-01*10e3s]

r = np.array(r0)

for t in range(len(times)):
    posAst[t] = r[:3]
    r = rk.rk4(r,t,dt)

print(posAst)
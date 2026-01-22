import RK4_Method as rk
import numpy as np
import Positions as pos

times = pos.times
dt = 2

posAst = np.zeros((len(times),3))

r0 = [-4.86796792e+08, -1.63037080e+08, -2.91625379e+07, -3.92854527e+03,
 -1.21948899e+04, -2.52167137e+02]#pos.positions[10,0,1:7]

r = np.array(r0)

for t in range(len(times)-5):
    posAst[t] = r[:3]
    r = rk.rk4(r,t,dt)
######

times2 = pos.times2
dt = 2

posAst2 = np.zeros((len(times2),3))

r02 = pos.positions2[10,0,1:7]

r = np.array(r02)
for t in range(len(times2)-5):
    posAst2[t] = r[:3]
    r = rk.rk42(r,t,dt)

print(pos.positions[10,0,1:7])
import numpy as np

list = np.array([[[0,1,1,1],
        [1,2,2,2],
        [2,3,3,3]],
        [[0,1,1,1],
        [1,2,2,2],
        [2,3,3,3]]
        ])

def ac(t):
    a =[0,0]
    for j in range(len(list)):
        a = a+np.array(list[j,t,1:3])
    return(a)

for i in range(3):
    print(ac(i))
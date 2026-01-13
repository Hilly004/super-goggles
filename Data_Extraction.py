import numpy as np
import matplotlib.pyplot as plt

def out(name):
    lines = []
    new_list=[]
    my_list=[]
    n=0
    with open(name, 'rt') as f:
        for line in f:
            lines.append(line)
    for i in range(0,len(lines)):
        if lines[i].find('$$SOE')==-1:
            n=n+1
        else:
            for k in range(n+1,len(lines)):
                if lines[k].find('$$EOE')==-1:
                        my_list.append(lines[k])
                else:
                    break        
    for i in range(len(my_list)):
        if my_list[i].find('TDB')!=-1:
            new_list.append(float((my_list[i].split())[0]))
        elif my_list[i].find('XYZ')!=-1:
            x = my_list[i].split()
            for i in range(2,8):
                new_list.append(float(x[i]))
        elif my_list[i].find('sigmas')!=-1:
            y = my_list[i].split()
            for i in range(1,7):
                if y[i]=='n.a.':
                    new_list.append(0)
                else:
                    new_list.append(float(y[i]))
        else:
            n=+1
    list1=np.zeros((13,int(len(new_list)/13)))      
    for r in range(13):
        x = np.arange(r,len(new_list),13)
        for j in range(len(x)):
            list1[r,j]=new_list[x[j]]

    return(list1)

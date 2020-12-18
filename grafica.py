import sys
import numpy as np
import matplotlib.pyplot as plt
plt.ioff()

Prob_video = np.load(
    "Probabilidad Spin Down.npy",
    allow_pickle=True).item()

def grafica(x_M, dic, name, y_M=1):
    ejeX = np.arange(-x_M, x_M + 1)  
    y = [dic[i] if i in dic.keys() else 0 for i in ejeX]
    ejeY = np.array(y)
    fig, vax = plt.subplots(1, 1, figsize=(12, 6))
    plt.ylim((0, y_M))
    vax.vlines(ejeX, [0], ejeY,colors='b', lw=2)
    plt.xticks(np.arange(-x_M, x_M + 1 , 0.2*x_M) )
    
    if name in range (57,60): 
         plt.title("Probabilidad en t:" + str(name))
    else: 
        plt.title("Probabilidad en t:" + str(name))
    return plt.savefig(str(name), dpi=100)

def video(n):
    Prob = Prob_video
    xmax, ymax = 25, 1.1
    zoom = np.array([max(Prob[i].values()) for i in range(n+1)])
    for i in range(0,n+1):
        if (ymax > 4*zoom[i:]).all():
            ymax = ymax/2    
        if i>0 and i%25 == 0:
            xmax += 25
        grafica(xmax, Prob[i], i, ymax)
    return print("Done :-)")

video(200) 

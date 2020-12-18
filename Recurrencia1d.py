# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:37:50 2019

@author: feder
"""

import sys
import numpy as np
from functools import lru_cache
from frozendict import frozendict

sys.setrecursionlimit(int(1e5))

#Estados iniciales
SpinUp = frozendict({(0,0) : 1, (-1,-1): 0.5})   #spin up
SpinDown = frozendict({(0,0): 0, (1,1) : 1, (-1,1): 0.5})  #spin down


#Funcion de Recurrencia para n>-1
@lru_cache(maxsize=10000)            #decorador
def a(n, i, init):
    # Condición inicial 
    if (n,i) in init.keys():
        return init[(n,i)]
    # Recurrencia
    elif abs(i) > n:
        return 0
    else:
        return a(n - 1, i - 1,init) + 2 * a(n - 2, i,init) - a(n - 1, i + 1,init)
        



#Funcion de Probabilidad
def probabilidad(n,init):
    """ Input:  n: números de pasos.
        Output: diccionario con la probabilidad en cada punto"""
    A = lambda i: abs(a(n, i,init))**2
    B = lambda i: abs(a(n + 1, i + 1,init) - a(n, i,init))**2
    norm = 2**(-n/2)
    dic = {i: norm * np.sqrt(float(A(i) + B(i))) for i in range(-n, n + 1)}
    return dic


# Prob_video = {i:probabilidad(i,SpinDown) for i in range(1001)}
# np.save("Probabilidad Spin Down", Prob_video)


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:47:44 2020

@author: feder
"""

from math import factorial as fac
import Recurrencia1d as R1d
import FuncionGeneratriz as FG

def HiperGeometric(n,l):
  j_0 = min(n-l,l) 
  A = lambda n,l,j: ((-1)**(n-l+j))*2**(j)
  B = lambda n,l,j: A(n,l,j) * fac(n-j)/( fac(j)*fac(l-j)*fac(n-l-j))
  sumatoria = [B(n,l,j) for j in range(0,j_0+1)]
  return sum(sumatoria)

def g_minus_coef(n,l):
    if l%2 != 0: return 0
    else: return HiperGeometric(n-1, l//2 -1)
        
# =============================================================================
# bool_list = []
# for n in range(45,46):
#     for i in range(-n,n+1):
#         bool_list.append(g_minus_coef(n,i+n) == R1d.a(n,i, R1d.SpinDown))
#         if bool_list[-1] == False: 
#             print("paso",n,"lugar",i)
#             print(g_minus_coef(n,i+n) , R1d.a(n,i, R1d.SpinDown))
# =============================================================================

def pruebaA(n,j):
    return sum([ fac(m)/(fac(n-2*m)*fac(m-j)*fac(2*m+1)) for m in range(j,int(n/2)+1)])

def pruebaB(n,j):
    return (2**(n-2*j))*fac(n-j)/(fac(n+1)*fac(n-2*j))

lista = [ [pruebaA(n,j) , pruebaB(n,j) ]for n in range(5) for j in range(int(n/2)+1)]

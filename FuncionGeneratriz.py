# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:17:21 2020
En este archivo quiero testear si los coeficiente que se deducen del desarrollo
en serie de McLaurin de las funciones generatrices g_plus y g_minus
coinciden con los hallados en Recurrencia1d.py
@author: feder
"""
from sympy import *
import Recurrencia1d as R1d

x, y = symbols('x,y')  
g_plus = (1+y)/(-x**2*y - 2*(x**2)*y**2 + y + 1)
g_minus = (y*x**2)/(-x**2*y - 2*(x**2)*y**2 + y + 1)

def McLaurin(expr,n):
    """Retorna todos los términos de la serie de la forma (x**i)*(y**j),
    con i<=j<= n"""  
    a = expr.series(y, 0, n).removeO().series(x, 0, 2*n).removeO()
    return Poly(a,x,y)    

def Coef(expr, n,i):
    """ Retorna el coeficiente del monomio x**(i+n)*y**n) """
    return int(expr.coeff_monomial(x**(i+n)*y**n))



def testfunction(expr,n):
    """
    Test de n pasos para verificar si g_plus y g_minus calculan 
    los coefs a(n,i) con -n<i<n.
    Retorna True solo si todos los valores coinciden.
    """
    
    if expr == g_plus: init, expr = R1d.SpinUp, g_plus
    elif expr == g_minus: init, expr = R1d.SpinDown, g_minus
    else:  return "error"
    
    a = McLaurin(expr, n)  
    
    bool_list = []
    for n in range(5):
        for i in range(-n,n+1):
              bool_list.append(Coef(a,n,i) == R1d.a(n,i, init))
              if bool_list[-1] == False:
                  print("Step: ", n, " pos: ", i)
    return all(bool_list)


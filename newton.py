from math import *
from sympy import *
x = symbols('x')
n=0
ind= int(input('Defina o indice: '))
a = float(input('Insira a : '))
b = float(input('Insira b : '))
var = (a+b)/2
f = cos(x) + (x**2)
derivada =  diff(f)



while n<= ind:
    var = var - (f.subs(x , var)/derivada.subs(x, var))
    n = n+1
    print(var)




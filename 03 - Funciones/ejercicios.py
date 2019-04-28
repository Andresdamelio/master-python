""" 
======================================================================
    Ejercicions
======================================================================
"""

# 1) Realiza una funcion llamada area_rectangulo() que devuelva el area del cuadrado a paratir de una base y una altura. Calcula el area de un rectangulo de 15 de base y 10 de altura

def area_rectangulo(base, altura):
    return base*altura

area = area_rectangulo(15,10)
print(area)

# 2) Realiza una funcion llamada area_circulo() que devuelva el area de un circulo a partir de un radio. Calcula el area de un circulo de radio 5

import math

def area_circulo(radio):
    return (math.pi)*(radio)**2

area_circulo = area_circulo(5)
print(area_circulo)

# 3) Realiza una funcion llamada relacion() que a partir de dos numero cumpla lo siguiente
    # - Si el primer numero es mayor que el segundo, debe devolver 1
    # - Si el primer numero es menor que el segudno, debe devolver -1
    # - Si ambos numero son iguales, debe devolver 0
# Comprueba la relacion entre los numeros " 6 y 10", "10 y 5" y "5 y 5"

def relacion(num1, num2):       
    if ( num1 - num2 > 0):
      return 1
    elif ( num1 - num2 < 0):
      return -1
    else:
        return 0

n = relacion(5,5)
print(n) 

# 4) Raaliza una funcion llamada intermedio() que a partir de dos numeros, devuelva su punto intermedio (compruebe el punto intermedio entre -12 y 24)

def intermedio(num1, num2):
    return (num1+num2)/2
    
punto_medio = intermedio(-12,24)
print(punto_medio)   

# 5) Realiza una funcion llamada recortar() que reciba tres parametros. El primero es el numero a recortar, el segundo es el limite inferior, y el tercero el limite superio. La funcion tendra que cumplir lo siguiente

    # - Devolver el limite inferior si el numero es menor que este.
    # - Devolver el limite superior si el numero es mayor que este.
    # - Devolver el numero sin cambios si no se supera ningun limite.
    
def recortar(num, limi, lims):
    if (num < limi):
      return limi
    elif (num > lims):
      return lims
    else:
        return num
    
result = recortar(15,0,10)
print(result)

# 6) Realiza una funcion llamada separar() que tome una lista de numeros enteros y devuelva dos listas ordenadas. La primera con los numeros pares, y la segunda con los numero impares

def separar(numeros):
    numeros.sort()
    pares = []
    impares = []
    
    for x in numeros:
        if( x % 2 == 0):
            pares.append(x)
        else:
            impares.append(x)
    return pares, impares

list = [-12, 84, 13, 20, -33, 101, 9]
pares, impares = separar(list)
print(pares)
print(impares)    
            
        
        
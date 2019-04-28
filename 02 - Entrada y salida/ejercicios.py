""" 
======================================================================
    Ejercicio 1
======================================================================
"""

# 1) Formatea los siguientes valores para mostrar el resultado indicado

# - "Hola Mundo" - Alineado a la derecha en 20 caracteres
print("{:>20}".format("Hola Mundo"))

# - "Hola Mundo" - truncamiento en el cuarto caracter (Indice 3)    
print("{:.3}".format("Hola Mundo"))

# - "Hola Mundo" - Alineamiento al centro en 20 caracteres con truncamiento en el segundo caracter (Indice 1)
print("{:^20.1}".format("Hola Mundo"))

# 150 - formateo a 5 numeros enteros rellenados con espacios
print("{:05d}".format(150))

# 7887 - formateo a 7 numeros enteros rellenados con espacios
print("{:7d}".format(7887))

# 7887 - formateo a 7 numeros enteros rellenados con ceros    
print("{:07d}".format(7887))

# 20.02 - Formateo a 3 numeros enteros y 3 decinmales    
print("{:07.3f}".format(20.02))  

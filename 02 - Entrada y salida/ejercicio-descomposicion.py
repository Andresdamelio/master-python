""" 
======================================================================
    Ejercicio 3
======================================================================
"""

# Crear un script que realice las siguientes tareas
    # 1) Debe tomar un argumeto que sera un numero entero positivo.
    # 2) En caso de no recibir un argumento, debe mostrar informacion acerca de como usar el script
    
# El objetivo del script es descomponer el numero en unidades, decenas, centenas y miles... tal que por ejemplo si se introduce el numero 3647 el programa debera devolver una descomposicion linea a linea como la siguiente, utilizando tecnicas de formateo

""" 
    0007
    0040
    0600
    3000
"""

import sys

if ( len(sys.argv) == 2 ):
    if (sys.argv[1].isdigit()):
        num = int(sys.argv[1])
        cadena = str(num)
        digitos = len(cadena)
        
        for x in range(digitos):
            print("{:0{digitos}d}".format(int(cadena[ digitos - 1 - x])*10**x, digitos=digitos))
    else:
        print("Debe ingresar un numero entero positivo")
else:
    print(" Debe introducir un numero, ej: python script.py numero")

""" 
======================================================================
    Ejercicio 2
======================================================================
"""

# Crear un script que realice las siguientes tareas:
    
    # 1) Debe tomar 2 argumentos, ambos numeros positivos del 1 al 9 sino mostrara un error
    
    # 2) El primer argumento hará referencia a las filas de una tabla, el segundo las columnas
    
    # 3) En caso de no recibir uno  o ambos argumentos, debe mostrar informacion acerca de como mostrar el script
    
    # 4) El script contendra un bucle for que itere el numero de veces del primer argumento
    
    # 5) Dentro del for añade un segundo for que itere el numero de veces del segundo argumento.
    
    # 6) Dentro del segundo for ejecuta una instruccion print("+", end=") (end=" evita el salto de linea)
    
    # 7) Ejecuta el codigo y ibserva el resultado
    
import sys
    
if len(sys.argv) == 3:
    if (sys.argv[1].isdigit() and sys.argv[2].isdigit()):
        filas = int(sys.argv[1])
        columnas = int(sys.argv[2])
        if( filas in range(1,10) and columnas in range(1,10) ):
            for i in range(filas):
                for j in range(columnas):
                    print(" * ", end="")
                print("")
        else:
            print("Los argumentos deben ser un numero entre el 1 y el 9")  
    else:
        print("Los argumentos deben ser numericos")
else:
    print("Por favor, debe introducir dos numeros, ejemplo: python ejercicio-tabla.py numero1 numero2")



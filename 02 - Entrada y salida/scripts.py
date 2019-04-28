
""" 
======================================================================
    Que es un script
======================================================================
"""

import sys

# Guiones con instrucciones en codigo fuente que se ejecutan de arriba a abajo, guardados en un fichero con un nombre unico y ejecutados desde el interprete

# Puede tomas datos (argumentos) en el momento de la ejecucion

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])

    for x in range(repeticiones):
        print(texto)
else:
    print("Por favor, ingrese todos los argumentos")
    print("Ejemplo: python scripts.py palabra nro_repeticion")
    
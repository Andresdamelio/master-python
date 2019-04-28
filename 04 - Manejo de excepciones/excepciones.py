""" 
======================================================================
    Excepciones
======================================================================
"""

# Para manejar las excepciones se utiliza el try - except, en el try va el codigo que pudiese generar algun error, y en el except mostrar si ocurre algun error, tambien este manejo de excepciones se compone por un else, y un finally, el else, forma parte del try, es decir, si no ocurre un error, inmediatamente se ejecuta lo que esta en el bloque else, y el finally se ejecuta al final de cada llamada

while(True):
    # El try (intentar) ejecutara las instrucciones, en caso se ocurrir un error 
    try:
        numero = float( input('Introduce un numero real: ') )
        numero2 = 4
        print("{}/{} = {}".format(numero, numero2, numero/numero2))

    # En caso de que ocurra un error, se ejecutara el codigo dentro del except, y se ira directamente al finally
    except:
        print("Por favor, introduce un numero correcto")
    
    # Aqui despues de que se ejecute las instrucciones dentro del try, se ejecutaran las instrucciones dentro del else, es decir, si no ocurren errores, se ejecutara lo que este dentro del bloque else
    else:
        print("La operacion se ha efectuado con exito")
        # Se ejecuta un break para romper el ciclo
        break
        
    # Lo que se encuentra dentro de este bloque se ejecutara, independientemente del resultado, es decir, se ejecutara si da error y si no da error
    finally:
        print("termino el proceso")
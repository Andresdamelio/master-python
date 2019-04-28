# COMPRESION DE LISTAS
    # Es una forma de optimizar las lineas de codigo al crear una lista de elementos
''' 
======================================================================================================
                        CREANDO UNA LISTA CON LAS LETRAS DE UNA PALABRA
======================================================================================================
 '''

# METODO TRADICIONAL

lista = []
for letra in "palabra":
    lista.append(letra)
print(lista)

# COMPRESION DE LISTAS
    # Es una forma muy optima de crear una linea, ademas es sencillo, aqui estamos indicando que letra sera el elemento que se ira agregando, y despues se realiza el for iterando letra, implicitamente realiza los mismos pasos que el ejemplo tradicional

lista = [letra for letra in "palabra"]
print(lista)

''' 
======================================================================================================
                    CREANDO UNA LISTA CON LOS NUMEROS DEL 1 AL 10 ELEVADOS A 2
======================================================================================================
 '''

# METODO TRADICIONAL
numeros = []
for numero in range(0,11):
    numeros.append(numero**2)
print(numeros)

# COMPRESION DE LISTAS
numeros = [numero**2 for numero in range(0,11)]
print(numeros)


''' 
======================================================================================================
                        CREANDO UNA LISTA CON LOS NUMEROS PARES DEL 1 AL 10
======================================================================================================
 '''
 
# METODO TRADICIONAL
numeros = []
for numero in range(0,11):
    if( numero % 2 == 0):
        numeros.append(numero)
print(numeros)

# COMPRESION DE LISTAS
numeros = [numero for numero in range(0,11) if numero%2==0]
print(numeros)

''' 
======================================================================================================
            CREANDO UNA LISTA CON LOS NUMEROS PARES DEL 1 AL 10 CON POTENCIA 2 SACADOS 
                                        DE OTRA LISTA
======================================================================================================
 '''
 
# METODO TRADICIONAL

# Creadndo una lista con los numeros del 1 al 10 elevados a 2
numeros = []
for numero in range(0,11):
    numeros.append(numero**2)
print(numeros)

# Creando una lista con numeros pares a partir de la creada
pares = []
for numero in numeros:
    if(numero % 2 == 0):
        pares.append(numero)
        
print(pares)

# COMPRESION DE LISTAS

pares = [ numero for numero in [potencia**2 for potencia in range(0,11)] if numero%2 == 0 ]
print(pares)
"""
===============================================================================================================
                                                EJERCICIO
===============================================================================================================
"""

# Ejercicio 1

cadena = "Un dia el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"


nuevo = cadena.split("#")

for item, cadena in enumerate(nuevo):
    l = list(cadena)
    if( item == 0):
        l.append("...")
    else:
        l.insert(0,"- ")   
        l.append(".")
        l[1] = cadena[0].upper()
    
    cadena = "".join(l)    
    print(cadena)
    

# Ejercicio 2

# Crea una funcion llamada modificar() que a partir de una lista de numeros realice las siguientes tareas sin modificar la original:
    # borrar todos los elementos duplicados
    # ordenar la lista de mayor a menor
    # eliminar todos los numeros impares
    # realizar una suma de todos los numeros que quedan
    # añadir como primer elemento de la lista la suma realizada
    # devolver la lista modificada
    # finalmente despues de ejecutar la funcion, comprueba que la suma de todos los numeros a partir del segundo, concuerda con el primer numero de la lista tal que asi
    
        # nueva_lista = modificar(lista)
        # print( nueva_lista[0] == sum(nueva_lista[1:]))
        
    # Nota: La funcion sum(lista) devuelve una suma de los elementos de una lista 
    

def modificar(lista):
    
    # Creando copia de la lista
    copia_lista = lista[:]
    
    # Eliminando repetidos de la lista, llevandola a un conjunto
    copia_lista = list(set(copia_lista))
    print("Lista sin numeros repetidos:",copia_lista)
    
    # lista ordenada
    copia_lista.sort(reverse=True)
    print("Lista ordenada de mayor a menor", copia_lista)
    
    # Eliminando numero impares
    nueva = []
    for v in copia_lista:
        if( v % 2 == 0):
            nueva.append(v)
            
    copia_lista = nueva            
    print("Lista sin numeros impares:", copia_lista)
    # Suma de todos los valores de los elementos restantes de la lista
    suma = sum(copia_lista[0:])
    print("Suma de valores restantes:", suma)
    
    #Insertando el valor de la suma a la primera posicion de la lista
    copia_lista.insert(0, suma)
    print("nueva lista con primer valor", copia_lista)
    
    return copia_lista 

lista = [29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]

resultado = modificar(lista)

print( resultado[0] == sum(resultado[1:]))
print(resultado)
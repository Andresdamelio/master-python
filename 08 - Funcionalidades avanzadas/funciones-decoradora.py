
""" 
==============================================================================================
                        FUNCIÓN LOCALS Y GLOBALS
==============================================================================================
 """
 
# En python existen dos funciones donde se pueden encontrar los elementos globles y locales en un programa python, estos elementos pueden ser clases funciones, variables, se pueden usar llamando globals() o locals(), estas funciones devuelven un diccionario
 
#print(locals())
#print(globals())

""" 
==============================================================================================
                            FUNCIONES DECORADORAS
==============================================================================================
 """
 
 # Es una función que envuelve la ejecución de otra función, y permite extender su comportamiento, estan pensadas para reutilizarlas gracias a una sintaxis de ejecución mucho mas simple
 
 # ejemplo de como usar una funcion decoradora en cualquier funcion, el ejemplo es de operaciones basicas de matematica, sencillas sin validaciones, suponiendo que los argumentos a recibir son validos


# Como crear una función decoradora
def operaciones_decorador( funcion ):
    def decorar( a,b ):
        print("Se ejecutará la {} de {} y {}".format(funcion.__name__, a, b))
        funcion(a,b)
        print("El resultado de la {} de {} y {} es {}".format(funcion.__name__, a, b, a+b))
    return decorar

# En este caso se esta creando una función principal, que tiene una función interna que sera la encargada de ejecutar la función recibida como argumento y monitorizar la ejecución de esta misma, para agregar la función decoradora a una función solo basta con agregar @nombre_funcion_decoradora

def suma(a,b):
    print( a + b )
def resta(a,b):
    print( a - b )
def multiplicacion(a,b):
    print( a * b )
def division(a,b):
    print( a / b )
# Como crear una funcion decoradora


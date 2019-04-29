""" 
==============================================================================================
                        FUNCION LOCALS Y GLOBALS
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
 
 # Es una funcion que envuelve la ejecucion de otra funcion, y permite extender su comportamiento, estan pensadas para reutilizarlas gracias a una sintaxis de ejecucion mucho mas simple
 
 # ejemplo de como usar una funcion decoradora en cualquier funcion, el ejemplo es de operaciones basicas de matematica, sencillas sin validaciones, suponiendo que los argumentos a recibir son validos


 
# Como crear una funcion decoradora
def operaciones_decorador( funcion ):
    def decorar( a,b ):
        print("Se ejecutara la {} de {} y {}".format(funcion.__name__, a, b))
        funcion(a,b)
        print("El resultado de la {} de {} y {} es {}".format(funcion.__name__, a, b, a+b))
    return decorar

# En este caso se esta creando una funcion principal, que tiene una funcion interna que sera la encargada de ejecutar la funcion recibida como argumento y monitorizar la ejecucion de esta misma, para agregar la funcion decoradora a una funcion solo basta con agregar @nombre_funcion_decoradora

@operaciones_decorador
def suma(a,b):
    print( "{} + {}".format(a,b) )

@operaciones_decorador
def resta(a,b):
    print( "{} - {}".format(a,b) )

@operaciones_decorador
def multiplicacion(a,b):
    print( "{} * {}".format(a,b) )

@operaciones_decorador
def division(a,b):
    print( "{} / {}".format(a,b) )

suma(3,2)
resta(10,5)
multiplicacion(3,10)
division(4,3)


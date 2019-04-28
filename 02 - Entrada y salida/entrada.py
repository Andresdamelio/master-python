""" 
======================================================================
    Entrada de datos
======================================================================
"""

# Para pedir datos al usuario se utiliza la funcion input(), donde dentro de dicha funcion indicamos el mensaje que sera mostrado en pantalla

# Como hacer una asignación de un dato solicitado por pantalla

    decimal = float( input("Introduce un numero decimal con punto: "))
    
# Introducir varios valores por consola
valores = []
    
print("Introduce 3 valores")
valores = []
for x in range(3):
    valores.append( input("Introduce valor "+ str(x+1)+ ": ") )

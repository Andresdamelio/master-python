# Operadores encadenados

# Para hacer una comparacion encadenada se puede hacer de la siguiente manera, donde se comprueba si uno es menor que dos, y si 2 es menor que 3, el resultado de esta comparacion es un booleano, True si es verdadero, es decir, si se cumple lo expuesto, o false en caso contrario

print(1 < 2 and 2 < 3)

# Lo anterio se puede reducir un poco mas, de la siguiente manera

print( 1<2<3 )

# Estas operaciones se pueden agrupar, para hacer diversas comparaciones, mediante parentesis

print( (3 > 2 ) and (2 > 1) )

numero = 35

# Ejemplo de una compracion con condicionales, veremos otra forma de realizarlo, cambiando la logica

if(numero >= 0 and numero <= 100):
    print("El numero {} esta entre 0 y 100".format(numero))
else:
    print("El numero {} no se encuentra entre 0 y 100".format(numero))
    
# Otra forma de realizarlo, es usando operadores encadenados con limites, es decir, se hace una comparacion contra dos numeros, un limite inferior y un limite superio

if(0 <= numero <= 100):
    print("El numero {} esta entre 0 y 100".format(numero))
else:
    print("El numero {} no se encuentra entre 0 y 100".format(numero))



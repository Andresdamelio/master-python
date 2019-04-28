"""
===============================================================================================================
                            METODOS DISPONIBLES PARA LAS CADENAS DE TEXTO
===============================================================================================================
"""

cadena = "hola mundo mundo"
cadena_s = "ciclico"
cadena_n = "100"
cadena_a = "El dia de hoy se hiciero 3 llamadas de 20 minutos"
cadena_st = "      cadena de texto con espacios en los laterales         "
cadena_st1 = "------cadena de texto con espacios en los laterales----"
cadena_l = "Hola mundo mundo mundo mundo"

# el metodo upper() permite convertir una cadena de texto a mayusculas completamente

print(cadena.upper())

# el metodo lower() permite convertir una cadena de texto a minusculass completamente

print(cadena.lower())

# El metodo capitalize() permite poner en mayuscula la primera letra de cada palabra

print(cadena.capitalize())

# El metodo title() tambien permite colocar la primera letra de cada palabra en mayuscula

print(cadena.title())

# contar el numero de veces que aparece una letra en una palabra, esto se realiza con el metodo count()

print(cadena.count("mundo"))

# como buscar los indices de aparicion de una letra o una subcadena de una cadena, esto se realiza con el metodo find()

print(cadena.find("mundo"))

# Tambien se puede buscar el indice de la ultima posicion donde aparece la pabara, es decir, si una palabra o una letra se reptie mas de una vez en una cadena, el metodo rfind() nos dara la posicion de la ultima aparicion de la letra o palabra, estos es una busqueda al reves


print(cadena.rfind("mundo"))

# Como verificar si una cadena es de digitos (metodo isdigit(), esto verificara si todos los elementos de la cadena son numeros enteros

print(cadena_n.isdigit())

# Para verificar si una cadena es alfanumerica( contiene letras desde la A-Z y numeros desde el 0-9), isalnum() solo arrojará True si contiene letras y numeros unicamente

print(cadena_a.isalnum())

# Comprobar si una cadena tiene unicamente letra, es decir, caracteres alfabeticos (Es de notar que el espacio se considera un caracter, pero este no pertenece al alfabeto)

print(cadena_s.isalpha())


# tambien se puede comprobar si todos los caracteres de una cadena esta en mayuscula o minuscula, o verificar si las primeras letras de las palabras estan en mayuscula

# Mayuscula
print(cadena.isupper())

# Minuscula
print(cadena.islower())

#primera en mayuscula
print(cadena.istitle())

# Comprobar si una cadena contiene espacios

print(cadena.isspace())

#Comprobar si una cadena empieza con una letra o con una palabra, tambien se termina con una letra o una palabra

# comienzo

print(cadena.startswith("h"))
print(cadena.startswith("hola"))

# fibal
print(cadena.endswith("h"))
print(cadena.endswith("mundo"))


# Como separa, unir y reemplazar cadena

# split() nos permite separar cadenas, y las devuelve en una lista, se puede separar palabras con una ",", ".", " "

print(cadena.split())

# join() sirve para unir cadenas, nos permite unir una palabra con algun caracter

print("-".join(cadena))

# Si tenemos una cadena con varios espacios extras, caracteres, se pueden borrar con el metodo strip()

print(cadena_st.strip())
print(cadena_st1.strip("-"))


# el replace(), sirve para reemplazar una letra o una subcadena de una cadena, este metodo recibe dos argumentos, el inicial es la letra o palabra a cambiar y el segundo sera la letra o palabra que ocupara a la reemplazada

print(cadena.replace("o", "0"))

# Este metodo tambien puede recibir un tercer argumento, y es la cantida de reemplazos que hara
print(cadena_l.replace("mundo", ".", 3))



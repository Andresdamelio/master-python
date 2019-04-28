""" 
======================================================================
    Multiples excepciones
======================================================================
"""

try:
  n = float(input("Introduce un numero: "))
  print(5/n)
except TypeError:
    print("No se puede dividir el numero por una cadena")
except ValueError:
    print("Debes introducir un numero")
except ZeroDivisionError:
    print("Introuce un numero distinto de cero, no se puede dividir por cero")
except Exception as e:
  print(type(e).__name__)
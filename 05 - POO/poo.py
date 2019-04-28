""" 
======================================================================
    Como definir clases
======================================================================
"""
# Una clase es como un molde para crear objetos

class Galleta:
  chocolate = False
  #Es un metodo especial que se ejecuta al crear un objeto, permite el envio de argumento al momento de la instanciacion, es un metodo especial, por eso lleva en el nombre los __, el parametro self hace referencia al propio objeto para diferenciar entre el ambito de clase y un metodo
  def __init__(self, sabor = None, forma = None):
      self.sabor = sabor
      self.forma = forma
      print("Se acaba de crear una galleta {} {}".format(sabor, forma))

  def chocolatear(self):
      self.chocolate = True
  def tiene_chocolate(self):
      if(self.chocolate):
          print("Soy una galleta chocolateada")
      else:
          print("soy una galleta sin chocolate")

# Creando objetos de la clase galleta, un objeto es una instancia de una clase

g = Galleta("dulce", "cuadrada")
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()


# Como ver el tipo de un objeto

#print(type(una_galleta))
# <class '__main__.Galleta'>

""" 
======================================================================
    Programacion orientada a objetos
======================================================================
"""





# La encapsulacon es una funcionalidad para impedir acceso externo a atributos y metodos de una clase, python no posee esta funcionalidad, pero se puede simular

class Ejemplo():
    __atributo_privado = "Soy un atributo inancalzable desde fuera"
    
    def __metodo_privado(self):
        print("Soy un metodo inancalzable desde fuera")
    
    def atributo_publico(self):
        return self.__atributo_privado
    
    def metodo_publico(self):
        return self.__metodo_privado()
        
e = Ejemplo()
print(e.atributo_publico())
print(e.metodo_publico())
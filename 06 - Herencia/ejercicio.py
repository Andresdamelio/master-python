""" 
======================================================================
    Ejercicio
======================================================================
"""

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", {} k/h, {} cc".format(self.velocidad,self.cilindrada)
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", tipo {}".format(self.tipo)
    
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
        
    def __str__(self):
        return super().__str__() + ", carga {}".format(self.carga)
        
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", velocidad {}, {} cc".format(self.velocidad, self.cilindrada)

coche = Coche("Azul", 4, 150, 1200)
camioneta = Camioneta("Rojo", 4, 300, 1500, 1000)
bicicleta = Bicicleta("Blanco", 2, "Urbano")
motoclicleta = Motocicleta("Verde", 2, "Deportivo", 180, 700)

vehiculos = [
    coche,
    camioneta,
    bicicleta,
    motoclicleta
]

def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print("clase",type(vehiculo).__name__, vehiculo)

def catalogar(vehiculos, ruedas):
    if( ruedas != None):
        ct = 0
        for vehiculo in vehiculos:
            if( vehiculo.ruedas == ruedas):
                ct +=1
        
        if( ct > 0):
            print("Hay {} vehiculos con {} ruedas ".format(ct,ruedas))
            print("================================")
        else:
            print("No hay vehiculos con {} ruedas ".format(ruedas))
            print("================================")
    
    for vehiculo in vehiculos:
        if( vehiculo.ruedas == ruedas):
            print("clase",type(vehiculo).__name__, vehiculo)
        elif( vehiculo.ruedas == None):
            print("clase",type(vehiculo).__name__, vehiculo)
            
catalogar(vehiculos,2)


    
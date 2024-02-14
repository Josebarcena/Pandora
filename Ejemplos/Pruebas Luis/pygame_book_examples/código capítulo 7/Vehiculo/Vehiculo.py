# Definición de la clase Vehiculo
class Vehiculo:

    # Constructor de la clase Vehiculo
    def __init__(self, matricula, color, numeroPuertas):
        self.MATRICULA = matricula
        self.COLOR = color
        self.NUMERO = numeroPuertas
        self.AVANZA = False
        print("Constucción de un vehículo : " + self.MATRICULA)

    # Metodo Avanzar
    def Avanzar(self):
        self.AVANZA = True
        print(self.MATRICULA + " avanza.")

    # Metodo Detenerse
    def Detenerse(self):
        self.AVANZA = False
        print(self.MATRICULA + " se detiene.")

# Construcción de una primera instancia
vehiculo1 = Vehiculo("AR123", "rojo", 3)


# Construcción de una segunda instancia
vehiculo2 = Vehiculo("FR456", "verde", 5)

# El primer vehículo avanza
vehiculo1.Avanzar()

# El primer vehículo se detiene
vehiculo1.Detenerse()

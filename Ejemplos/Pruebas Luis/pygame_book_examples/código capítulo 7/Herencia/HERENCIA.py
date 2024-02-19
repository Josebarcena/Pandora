class Personaje:

    def __init__(self):

        self.NOMBRE = "nombre por defecto"

        self.TIPO = "tipo por defecto"

    def Cantar(self):
        print("El personaje llamado " + self.NOMBRE + " canta.")

class Druida(Personaje):

    def __init__(self, nombre, nivel):

        self.NOMBRE = nombre
        self.TIPO = "DRUIDA"
        self.NIVEL_DRUIDA = nivel

    def InventarPocion(self):
        print("El druida llamado " + self.NOMBRE + " inventa una poción.")


pygamix = Druida("Pygamix", 5)

pygamix.Cantar()

pygamix.InventarPocion()
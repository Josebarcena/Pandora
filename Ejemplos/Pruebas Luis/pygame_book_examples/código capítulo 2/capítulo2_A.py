class Pais:

    def __init__(self, nombre, capital):
        self.nombre = nombre
        self.capital = capital

    def __str__(self):
        return self.nombre + " (" + self.capital + ")"

    def phrase(self):
        return "La capital de : " + self.nombre + "  es : " + self.capital + "."


listaPais = []

francia = Pais("Francia", "París")
listaPais.append(francia)

espania = Pais("España", "Madrid")
listaPais.append(espania)

portugal = Pais("Portugal", "Lisboa")
listaPais.append(portugal)

print(listaPais[0])

for p in listaPais:
    print(p.phrase())
class Persona:

    def __init__(self, nombre, apellido, anio):
        self.nombre = nombre
        self.apellido = apellido
        self.anio = anio

    def __str__(self):
        return self.nombre + " - " + self.apellido + " - " + str(self.anio)


class Prof(Persona):

    def __init__(self, nombre, apellido, anio, materias):
        super().__init__(nombre, apellido, anio)

        self.materias = materias

    def __str__(self):
        return super().__str__() + " - " + ", ".join(self.materias)


materias = ["matemáticas", "física", "tecnología"]
prof1 = Prof("Marcel", "Dupont", 1960, materias)

materias = ["historia", "geografía"]
prof2 = Prof("Marcelle", "Dupond", 1955, materias)

print(prof1)
print(prof2)

import xml.etree.ElementTree as ET
import pygame, sys, os
from pygame.locals import *
from pytmx.util_pygame import load_pygame
from Recursos.config import *

# -------------------------------------------------
# Clase GestorRecursos

# En este caso se implementa como una clase vacía, solo con métodos de clase
class GestorRecursos(object):
    resources = {}
    
    @classmethod
    def LoadImage(cls, path, name, transparent=None):
        # Si el nombre de archivo está entre los recursos ya cargados
        if name in cls.resources:
            # Se devuelve ese recurso
            return cls.resources[name]
        # Si no ha sido cargado anteriormente
        else:
            if (name == "sprites"):
                resource = cls.LoadSpritesPandora()
            # Se carga la imagen indicando la carpeta en la que está
            fullname = os.path.join("Recursos", path, name)
            if(path == "Imagenes"):
                try:
                    resource = pygame.image.load(fullname)
                except pygame.error as message:
                    print('Cannot load image:', fullname)
                    raise SystemExit(message)
                resource = resource.convert_alpha()

            elif(path == "Fases"):
                try:
                    resource = load_pygame(fullname)
                except pygame.error as message:
                    print('Cannot load Fase:', fullname)
                    raise SystemExit(message)
                
            if transparent is not None and path == "Imagenes":
                if transparent == -1:
                    transparent = resource.get_at((0,0))
                resource.set_colorkey(transparent, RLEACCEL)
            # Se almacena
            cls.resources[name] = resource
            # Se devuelve
            return resource

    @classmethod
    def LoadSpritesPandora(cls):
        # Cargar la imagen desde el archivo
        imagen = pygame.image.load('Warrior_Sheet-Effect.png').convert_alpha()

        # Inicializar el vector bidimensional como una lista vacía
        vectorBidimensional = []

        # Verificar si la carga de la imagen fue exitosa
        if imagen is not None:
            # Definir las dimensiones de corte
            corte_ancho = 64
            corte_alto = 44
            distancia_entre_imagenes = 5

            # Iterar sobre las secciones de la imagen
            for j in range(imagen.get_height() // corte_alto):
                # Crear una nueva fila en el vector bidimensional
                vectorBidimensional.append([])
                for i in range(imagen.get_width() // (corte_ancho + distancia_entre_imagenes)):
                    # Calcular las coordenadas de inicio y fin para el recorte
                    x1 = (corte_ancho + distancia_entre_imagenes) * i
                    x2 = x1 + corte_ancho
                    y1 = j * corte_alto
                    y2 = y1 + corte_alto

                    # Recortar la sección de la imagen
                    imagen_recortada = imagen.subsurface((x1, y1, corte_ancho, corte_alto))

                    # Almacenar la imagen recortada en el vector bidimensional
                    vectorBidimensional[j].append(imagen_recortada)

        return vectorBidimensional

    @classmethod
    def almacenar_animacion_fila(cls, num_imagenes, inicio_x, inicio_y,
                                 inicio_fila2_x = None, inicio_fila2_y = None, inicio_fila3_x = None, inicio_fila3_y = None):
        ancho_imagen = 69
        altura_imagen = 44
        imagen = pygame.image.load('Warrior_SheetAlex.png').convert_alpha()
        animaciones = []
        j = 0  # Inicializamos j en 0 para rastrear la posición en la fila
        limite = 414
        cambioFila = 0
        for i in range(num_imagenes):

            if i == 0:
                x = inicio_x * ancho_imagen
                y = inicio_y * altura_imagen
                j += 1  # Incrementamos j para rastrear la posición en la fila
            else:
                x = ancho_imagen * (j - 1) + (inicio_x * ancho_imagen)
                j += 1  # Incrementamos j para rastrear la posición en la fila

            # Comprobacion para saber si cambiamos de fila
            if (x + ancho_imagen) > limite:
                cambioFila += 1
                j = 0  # Reiniciamos j cuando cambiamos de fila

            if cambioFila == 1 and inicio_fila2_x != None:
                if j == 0:
                    x = inicio_fila2_x * ancho_imagen
                    y = inicio_fila2_y * altura_imagen
                    j += 1  # Incrementamos j para rastrear la posición en la fila
                else:
                    x = inicio_fila2_x * ancho_imagen + ((ancho_imagen) * (j - 1))
                    j += 1  # Incrementamos j para rastrear la posición en la fila

            if cambioFila == 2 and inicio_fila3_x != None:
                
                if j == 0:
                    x = inicio_fila3_x * ancho_imagen
                    y = inicio_fila3_y * altura_imagen
                    j += 1  # Incrementamos j para rastrear la posición en la fila
                else:
                    x = inicio_fila3_x * ancho_imagen + ((ancho_imagen) * (j - 1))
                    j += 1  # Incrementamos j para rastrear la posición en la fila

            imagen_recortada = imagen.subsurface((x, y, ancho_imagen, altura_imagen))
            animaciones.append(imagen_recortada)
        return animaciones

    @classmethod
    def loadSpritesEnemies(cls, direccion, imagenes, inicio_x, inicio_y, separacion_x, width, height):
        imagen = pygame.image.load(direccion).convert_alpha()
        animaciones = []

        x = inicio_x
        y = inicio_y
        for i in range(imagenes):

            if i != 0:
                x = x + width + separacion_x

            imagen_recortada = imagen.subsurface((x, y, width, height))
            animaciones.append(imagen_recortada)

        return animaciones
    
    def create_xml(data):
        # Crea el elemento raíz del XML
        root = ET.Element("Data")

        # Crea un elemento llamado 'score' y lo agrega como hijo del elemento raíz
        for tag, value in data:
            element = ET.SubElement(root, tag)
            element.text = str(value)

        # Crea un objeto ElementTree con la raíz y luego escribe el XML en un archivo
        tree = ET.ElementTree(root)
        with open(join("recursos", "data.xml"), "wb") as file:
            tree.write(file)

    def change_xml(data):
        # Parsea el archivo XML
        tree = ET.parse(join("recursos", "data.xml"))
        root = tree.getroot()

        # Busca el elemento a modificar por su nombre y actualiza su valor
        for tag, value in data:
            for element in root.iter(tag):
                element.text = str(value)

        # Guarda los cambios en el archivo XML
        tree.write(join("recursos", "data.xml"))

    def read_xml(field):
        # Parsea el archivo XML
        tree = ET.parse(join("recursos", "data.xml"))
        root = tree.getroot()

        # Busca el elemento por su nombre y devuelve su valor
        for element in root.iter(field):
            return element.text

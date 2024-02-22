import pygame, sys, os
from pygame.locals import *
from pytmx.util_pygame import load_pygame

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
            # Se carga la imagen indicando la carpeta en la que está
            fullname = os.path.join(path, name)
            if(path == "Imagenes"):
                try:
                    resource = pygame.image.load(fullname)
                except pygame.error as message:
                    print('Cannot load image:', fullname)
                    raise SystemExit(message)
                resource = resource.convert()
            elif(path == "Fases"):
                resource = load_pygame(fullname)
            if transparent is not None and path == "Imagenes":
                if transparent == -1:
                    transparent = resource.get_at((0,0))
                resource.set_colorkey(transparent, RLEACCEL)
           
            # Se almacena
            cls.resources[name] = resource
            # Se devuelve
            return resource

    @classmethod
    def CargarArchivoCoordenadas(cls, ruta, nombre):
        # Si el nombre de archivo está entre los recursos ya cargados
        if nombre in cls.recursos:
            # Se devuelve ese recurso
            return cls.recursos[nombre]
        # Si no ha sido cargado anteriormente
        else:
            # Se carga el recurso indicando el nombre de su carpeta
            fullname = os.path.join(ruta, nombre)
            pfile=open(fullname,'r')
            datos=pfile.read()
            pfile.close()
            # Se almacena
            cls.recursos[nombre] = datos
            # Se devuelve
            return datos

# -*- coding: utf-8 -*-

# Importar las librerías
import pygame, sys
from pygame.locals import *

# Inicializar la librería de pygame
pygame.init()

BLANCO = (255,255,255)

# Creamos la pantalla
pantalla = pygame.display.set_mode((800,600))

# Bucle infinito
while True:

        # Para cada evento posible
        for evento in pygame.event.get():

                # Si el evento es la pulsación de la tecla Escape
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                        # Se sale del programa
                        pygame.quit()
                        sys.exit()


        # Rellenamos la pantalla de color negro
        pantalla.fill((0,0,0))

        # Dibujamos un círculo de color blanco en esa posición en el buffer
        pygame.draw.circle(pantalla, BLANCO, (50,50),4,0)

        # Actualizamos la pantalla
        pygame.display.update()


# -*- coding: utf-8 -*-

# Importar las librerías
import pygame, sys
from pygame.locals import *

# Inicializar la librería de pygame
pygame.init()

BLANCO = (255,255,255)

# Frames por segundo
fps = 60

# Posicion de la pelota
pelotaX = 50
pelotaY = 50

# Creamos la pantalla
pantalla = pygame.display.set_mode((800,600))

# Creamos el objeto reloj para sincronizar el juego
reloj = pygame.time.Clock()

# Bucle infinito
while True:

        # Hacemos que el reloj espere a un determinado fps
        reloj.tick(60)

        # Para cada evento posible
        for evento in pygame.event.get():

                # Si el evento es la pulsación de la tecla Escape
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                        # Se sale del programa
                        pygame.quit()
                        sys.exit()

        # Actualizamos la posición de la pelota
        pelotaX += 2
        pelotaY += 2

        # Rellenamos la pantalla de color negro
        pantalla.fill((0,0,0))

        # Dibujamos un círculo de color blanco en esa posición en el buffer
        pygame.draw.circle(pantalla, BLANCO, (pelotaX,pelotaY),4,0)

        # Actualizamos la pantalla
        pygame.display.update()


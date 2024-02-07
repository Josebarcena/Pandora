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

# Tamano de la pelota
RadioPelota = 4

# Velocidad de movimiento de la pelota en cada eje
VelocidadPelotaX = 2
VelocidadPelotaY = 2

# Resolución de la pantalla
MaxX = 800
MaxY = 600

# Creamos la pantalla
pantalla = pygame.display.set_mode((MaxX,MaxY))

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

        # Miramos a ver si la pelota está en el límite en el eje X
        if pelotaX <= RadioPelota or pelotaX >= MaxX - RadioPelota:
                # Invertimos la velocidad en el eje X
                VelocidadPelotaX = -VelocidadPelotaX
                
        # Miramos a ver si la pelota está en el límite en el eje Y
        if pelotaY < RadioPelota or pelotaY > MaxY - RadioPelota:
                # Invertimos la velocidad en el eje Y
                VelocidadPelotaY = -VelocidadPelotaY
        
        # Actualizamos la posición de la pelota
        pelotaX += VelocidadPelotaX
        pelotaY += VelocidadPelotaY

        # Rellenamos la pantalla de color negro
        pantalla.fill((0,0,0))

        # Dibujamos un círculo de color blanco en esa posición en el buffer
        pygame.draw.circle(pantalla, BLANCO, (pelotaX,pelotaY),RadioPelota,0)

        # Actualizamos la pantalla
        pygame.display.update()


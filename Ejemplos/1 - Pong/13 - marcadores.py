# -*- coding: utf-8 -*-

# Importar las librerías
import pygame, sys, time
from pygame.locals import *

# Inicializar la librería de pygame
pygame.init()

BLANCO = (255,255,255)

# Frames por segundo
fps = 60

# Posicion de la pelota
pelotaX = 100
pelotaY = 100

# Tamano de la pelota
RadioPelota = 4

# Velocidad de movimiento de la pelota en cada eje
VelocidadPelotaX = 2
VelocidadPelotaY = 2

# Resolución de la pantalla
MaxX = 800
MaxY = 600

# Puntuacion del jugador 1 y jugador 2
puntos1 = 0
puntos2 = 0

# Posición de la raqueta del jugador 1 y jugador 2
raqueta1X = 50
raqueta1Y = MaxY/2
raqueta2X = MaxX-50
raqueta2Y = MaxY/2

# Tamano de cada raqueta
tamanoRaquetaX = 10
tamanoRaquetaY = 50

# Movimiento de la raqueta
velocidadRaquetaY = 5

# Creamos la pantalla
pantalla = pygame.display.set_mode((MaxX,MaxY))

# Las letras para el marcador
tipoLetra = pygame.font.SysFont('arial', 96)

# Creamos el objeto reloj para sincronizar el juego
reloj = pygame.time.Clock()

# Permitimos que la tecla este pulsada
pygame.key.set_repeat(1, 25)

# Eliminamos el raton
pygame.mouse.set_visible(False)

# Bucle infinito
while True:

        # Hacemos que el reloj espere a un determinado fps
        reloj.tick(60)

        # Para cada evento posible
        for evento in pygame.event.get():

                # Si el evento es la pulsación de una tecla
                if evento.type == KEYDOWN:

                        # Si la tecla es Escape
                        if evento.key == K_ESCAPE:
                                # Se sale del programa
                                pygame.quit()
                                sys.exit()

                        # si no, si es la tecla 'q'
                        elif evento.key == K_q:
                                # Se mueve la raqueta del jugador 1 arriba
                                raqueta1Y -= velocidadRaquetaY
                                # Si se sale por arriba
                                if raqueta1Y < 0:
                                        raqueta1Y = 0

                        # si no, si es la tecla 'a'
                        elif evento.key == K_a:
                                # Se mueve la raqueta del jugador 1 abajo
                                raqueta1Y += velocidadRaquetaY
                                # Si se sale por abajo
                                if raqueta1Y > MaxY - tamanoRaquetaY:
                                        raqueta1Y = MaxY - tamanoRaquetaY

                        # si no, si es la tecla 'o'
                        elif evento.key == K_o:
                                # Se mueve la raqueta del jugador 2 arriba
                                raqueta2Y -= velocidadRaquetaY
                                # Si se sale por arriba
                                if raqueta2Y < 0:
                                        raqueta2Y = 0

                        # si no, si es la tecla 'l'
                        elif evento.key == K_l:
                                # Se mueve la raqueta del jugador 2 abajo
                                raqueta2Y += velocidadRaquetaY
                                # Si se sale por abajo
                                if raqueta2Y > MaxY - tamanoRaquetaY:
                                        raqueta2Y = MaxY - tamanoRaquetaY


        # Miramos a ver si hay colision con la raqueta del jugador 1
        if pelotaX - RadioPelota < raqueta1X + tamanoRaquetaX and pelotaX + RadioPelota > raqueta1X and pelotaY - RadioPelota < raqueta1Y + tamanoRaquetaY and pelotaY + RadioPelota > raqueta1Y:
                # Invertimos la velocidad en el eje X
                VelocidadPelotaX = -VelocidadPelotaX

        # Miramos a ver si hay colision con la raqueta del jugador 2
        if pelotaX - RadioPelota < raqueta2X + tamanoRaquetaX and pelotaX + RadioPelota > raqueta2X and pelotaY - RadioPelota < raqueta2Y + tamanoRaquetaY and pelotaY + RadioPelota > raqueta2Y:
                # Invertimos la velocidad en el eje X
                VelocidadPelotaX = -VelocidadPelotaX

        
        # Miramos a ver si la pelota está en el límite en el eje X
        if pelotaX <= RadioPelota or pelotaX >= MaxX - RadioPelota:
                # Sumamos los puntos al jugador correspondiente
                if pelotaX <= RadioPelota:
                        puntos2 += 1
                else:
                        puntos1 += 1
                               
                # Realizamos una pausa
                time.sleep(1)
                # Ponemos la pelota en el centro
                pelotaX = MaxX / 2;
                pelotaY = MaxY / 2;
                # Invertimos la velocidad en el eje X (para que vaya contra el otro jugador)
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

        # Dibujamos como un rectángulo cada raqueta
        pygame.draw.rect(pantalla, BLANCO, (raqueta1X, raqueta1Y, tamanoRaquetaX, tamanoRaquetaY))
        pygame.draw.rect(pantalla, BLANCO, (raqueta2X, raqueta2Y, tamanoRaquetaX, tamanoRaquetaY))

        # Creamos los marcadores
        marcador1 = tipoLetra.render(str(puntos1), True, BLANCO)
        marcador2 = tipoLetra.render(str(puntos2), True, BLANCO)
        #  y los mostramos
        pantalla.blit(marcador1, (MaxX/4,   MaxY/8, 50, 50))
        pantalla.blit(marcador2, (MaxX*3/4, MaxY/8, 50, 50))
        
        # Actualizamos la pantalla
        pygame.display.update()


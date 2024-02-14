import pygame, sys
import math
PI = math.pi

pygame.init()

# VENTANA DE 400 POR 400 CON FONDO NEGRO
PANTALLA = pygame.display.set_mode((400,400))
pygame.display.set_caption("Capítulo 5")
COLOR_NEGRO = pygame.Color(0, 0, 0)
PANTALLA.fill(COLOR_NEGRO)


# DIAGONALES EN ROJO
COLOR_ROJO = pygame.Color(255, 0, 0)
pygame.draw.line(PANTALLA, COLOR_ROJO, (0,0), (400, 400))
pygame.draw.line(PANTALLA, COLOR_ROJO, (0, 400), (400, 0))


# LÍNEAS DISCONTINUAS
COLOR_AZUL = pygame.Color(0, 0, 255)
COLOR_VERDE = pygame.Color(0, 255, 0)

puntos = [(0, 0), (50, 100), (100, 150), (250, 200), (400, 400)]
pygame.draw.lines(PANTALLA, COLOR_AZUL, False, puntos)
puntos2 = [(0, 0), (100, 50), (150, 100), (200, 250)]
pygame.draw.lines(PANTALLA, COLOR_VERDE, True, puntos2)


# RECTÁNGULO
COLOR_ROSA = pygame.Color(255,192,203)
pygame.draw.rect(PANTALLA, COLOR_ROSA, ((50, 75), (150, 200)), 1)


# POLÍGONO
puntos3 = [(200, 200), (250, 300), (300, 325), (400, 350)]
COLOR_AMARILLO = pygame.Color(255,255,0)
pygame.draw.polygon(PANTALLA, COLOR_AMARILLO, puntos3, 1)

# CÍRCULO
COLOR_BLANCO = (255, 255, 255)
pygame.draw.circle(PANTALLA, COLOR_BLANCO, (200, 200), 100, 1)

# ELIPSE
COLOR_NARANJA = (255, 165, 0)
xx_izquierda = 100
yy_arriba = 150
pequenio_eje = 100
grande_eje = 200
pygame.draw.ellipse(PANTALLA, COLOR_NARANJA, (xx_izquierda, yy_arriba, grande_eje, pequenio_eje), 1)


# ARCO DE CÍRCULO
COLOR_CIAN = (0, 255, 255)
xx_izquierda2 = 300
yy_arriba2 = 25
pequenio_eje2= 150
grande_eje2 = 180
pygame.draw.arc(PANTALLA, COLOR_CIAN, (xx_izquierda2, yy_arriba2, grande_eje2, pequenio_eje2), PI/2, PI, 1)

# BUCLE DE JUEGO
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.flip()

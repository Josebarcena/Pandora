import pygame, sys
import math
PI = math.pi

pygame.init()

# VENTANA DE 400 POR 400 CON UN FONDO NEGRO
PANTALLA = pygame.display.set_mode((400,400))
pygame.display.set_caption("Capítulo  - transformaciones")
COLOR_NEGRO = pygame.Color(0, 0, 0)
PANTALLA.fill(COLOR_NEGRO)

#Image
logo = pygame.image.load("logo_ENI.png").convert()
PANTALLA.blit(logo, (50, 50))

color = pygame.transform.average_color(logo)
print(color)

# BUCLE DE JUEGO
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.flip()
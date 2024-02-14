import pygame, sys

pygame.init()

PANTALLA = pygame.display.set_mode((400,400))
pygame.display.set_caption("Capítulo 5")
COLOR_NEGRO = pygame.Color(0, 0, 0)
PANTALLA.fill(COLOR_NEGRO)

COLOR_CIAN = (0, 255, 255)
pygame.draw.line(PANTALLA, COLOR_CIAN, (0, 200), (200, 0), 1)
pygame.draw.aaline(PANTALLA, COLOR_CIAN, (0, 400), (400, 0), 1)

# BUCLE DE JUEGO
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.flip()

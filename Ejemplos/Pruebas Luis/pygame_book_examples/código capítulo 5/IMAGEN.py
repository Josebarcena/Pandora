import pygame, sys

pygame.init()

PANTALLA = pygame.display.set_mode((400,400))
pygame.display.set_caption("Capítulo 5")
COLOR_NEGRO = pygame.Color(0, 0, 0)
PANTALLA.fill(COLOR_NEGRO)

selfie = pygame.image.load("Selfie.jpg").convert()
PANTALLA.blit(selfie, (50, 50))

# BUCLE DE JUEGO
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.flip()

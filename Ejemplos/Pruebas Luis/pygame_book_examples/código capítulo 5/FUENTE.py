import pygame, sys

pygame.init()

# VENTANA DE 400 POR 400
PANTALLA = pygame.display.set_mode((400,400))
pygame.display.set_caption("Capítulo 5")
COLOR_NEGRO = pygame.Color(0, 0, 0)
PANTALLA.fill(COLOR_NEGRO)

# FUENTE
COLOR_BLANCO = (255, 255, 255)
FUENTE_ARIAL = pygame.font.SysFont("Arial", 35, 1, 1)
TEXTO = FUENTE_ARIAL.render("Es Arial.", 1, COLOR_BLANCO)
PANTALLA.blit(TEXTO, (50, 50))

# BUCLE DE JUEGO
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.flip()
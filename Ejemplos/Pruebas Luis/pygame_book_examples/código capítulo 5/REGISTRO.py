import pygame, sys

pygame.init()

# VENTANA DE 400 POR 400
PANTALLA = pygame.display.set_mode((400,400))
pygame.display.set_caption("Capítulo 5")

COLOR_ROJO = pygame.Color(255, 0, 0)
IMAGE = pygame.Surface((300, 300))
IMAGE.fill(COLOR_ROJO)

# CÍRCULO
COLOR_BLANCO = (255, 255, 255)
pygame.draw.circle(IMAGE, COLOR_BLANCO, (150, 150), 100, 5)

PANTALLA.blit(IMAGE, (50, 50))

pygame.image.save(IMAGE, "Circulo.png")

# BUCLE DE JUEGO
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.flip()
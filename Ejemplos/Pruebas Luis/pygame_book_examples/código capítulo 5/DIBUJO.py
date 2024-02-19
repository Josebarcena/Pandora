import pygame, sys

pygame.init()

# COLORES
COLOR_BLANCO = pygame.Color(255, 255, 255)
COLOR_NEGRO = pygame.Color(0, 0, 0)
COLOR_ROJO = pygame.Color(255, 0, 0)
COLOR_VERDE = pygame.Color(0, 255, 0)
COLOR_AZUL = pygame.Color(0, 0, 255)

# VENTANA DE 400 POR 400
PANTALLA = pygame.display.set_mode((400,400))
PANTALLA.fill(COLOR_BLANCO)
pygame.display.set_caption("Capítulo 5")

CONTINUAR = True
inicio_linea = 0, 0
COLOR = COLOR_NEGRO
GROSOR = 1

# BUCLE DE JUEGO
while CONTINUAR:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      CONTINUAR = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        CONTINUAR = False
      elif event.key == pygame.K_r:
        COLOR = COLOR_ROJO
      elif event.key == pygame.K_v:
        COLOR = COLOR_VERDE
      elif event.key == pygame.K_b:
        COLOR = COLOR_AZUL
      elif event.key == pygame.K_n:
        COLOR = COLOR_NEGRO
      elif event.key == pygame.K_p:
        GROSOR = GROSOR +1
      elif event.key == pygame.K_m:
        GROSOR = GROSOR - 1
        if GROSOR < 1:
          GROSOR = 1
      elif event.key == pygame.K_s:
        pygame.image.save(PANTALLA, "MiDiseño.png")
    elif event.type == pygame.MOUSEMOTION:
       fin_linea = pygame.mouse.get_pos()
       if pygame.mouse.get_pressed() == (1, 0, 0):
         pygame.draw.line(PANTALLA, COLOR, inicio_linea, fin_linea, GROSOR)
       inicio_linea = fin_linea

  pygame.display.flip()
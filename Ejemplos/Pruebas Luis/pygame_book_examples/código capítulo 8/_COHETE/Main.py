import pygame
from CLASES import *
pygame.init()

def VER_MARCADOR():
  texto = FUENTE.render(str(_MARCADOR) + " puntos", 1, (255, 0, 0))
  textpos = texto.get_rect(centerx=ALTURA_VENTANA / 2, centery=50)
  PANTALLA.blit(texto, textpos)

PANTALLA = pygame.display.set_mode((ALTURA_VENTANA, ANCHURA_VENTANA))
pygame.display.set_caption("COHETE PLANETAS - CH 7")
FUENTE = pygame.font.Font(None, 24)
_MARCADOR = 0

cohete = COHETE()
LISTA_GLOBAL_SPRITES.add(cohete)

planeta_izquierdo = PLANETA(XX_PLANETA, YY_PLANETA)
LISTA_PLANETAS.add(planeta_izquierdo)
LISTA_GLOBAL_SPRITES.add(planeta_izquierdo)

planeta_derecho = PLANETA(XX_PLANETA + XX_ENTRE_PLANETAS,
                         YY_PLANETA + YY_ENTRE_PLANETA)
LISTA_PLANETAS.add(planeta_derecho)
LISTA_GLOBAL_SPRITES.add(planeta_derecho)

reloj = pygame.time.Clock()
print("Empezamos...")

while not PARAR_JUEGO:

  LISTA_CONFLICTO = pygame.sprite.spritecollide(cohete, LISTA_PLANETAS, False)
  if len(LISTA_CONFLICTO) > 0:
    PARAR_JUEGO = True
    print("Ha perdido")
    pygame.time.wait(5000)

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      PARAR_JUEGO = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          cohete.DIRECCION = 'D'
    elif event.type == pygame.KEYUP:
      cohete.DIRECCION = 'I'

  if len(LISTA_PLANETAS) == 0:

     XX_PLANETA = randint(30, 130)
     planeta_izquierdo = PLANETA(XX_PLANETA, YY_PLANETA)
     LISTA_PLANETAS.add(planeta_izquierdo)
     LISTA_GLOBAL_SPRITES.add(planeta_izquierdo)

     planeta_derecho = PLANETA(XX_PLANETA + XX_ENTRE_PLANETAS, YY_PLANETA + YY_ENTRE_PLANETA)
     LISTA_PLANETAS.add(planeta_derecho)
     LISTA_GLOBAL_SPRITES.add(planeta_derecho)

     _MARCADOR = _MARCADOR + 1

  LISTA_GLOBAL_SPRITES.update()
  PANTALLA.fill(COLOR_FONDO)
  LISTA_GLOBAL_SPRITES.draw(PANTALLA)
  print(_MARCADOR)
  VER_MARCADOR()
  pygame.display.flip()


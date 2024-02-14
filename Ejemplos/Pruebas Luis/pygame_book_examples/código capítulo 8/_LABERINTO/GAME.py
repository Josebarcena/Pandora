import pygame, random, sys
from CLASES import *
from CONSTANTES import *

def VER_MARCADOR():
  font = pygame.font.SysFont('Arial', BALDOSA_TAMANIO - 5)
  background = pygame.Surface((ALTURA, MARCADOR_ANCHURA))
  background = background.convert()
  background.fill(BLANCO)
  text = font.render(_personaje.reloj.Timer.strftime("%H:%M:%S"), 1, NEGRO)
  textpos = text.get_rect(centerx=ALTURA / 2, centery=MARCADOR_ANCHURA / 2)
  background.blit(text, textpos)
  screen.blit(background, (0, 0))

pygame.init()

screen = pygame.display.set_mode([ALTURA, ANCHURA])
pygame.display.set_caption('El juego del laberinto')

XX = 0
YY = 0
with open("Laberinto.txt", "r") as archivo:
  for linea in archivo:
    for sprite in linea:
      if sprite == 'M':
        _pared = PARED(XX, YY)
        LISTA_PAREDES.add(_pared)
        LISTA_GLOBAL_SPRITES.add(_pared)
      XX = XX + 1
    XX = 0
    YY = YY + 1

_personaje = None
BUSCAR_PERSONAJE = True
while BUSCAR_PERSONAJE:
    _personaje = PERSONAJE()
    LISTA_CONFLICTO = pygame.sprite.spritecollide(_personaje, LISTA_PAREDES, False)
    if len(LISTA_CONFLICTO) == 0:
        LISTA_GLOBAL_SPRITES.add(_personaje)
        BUSCAR_PERSONAJE = False

while len(LISTA_OBJETOS) < 10:
    _objeto = OBJETO()
    LISTA_CONFLICTO = pygame.sprite.spritecollide(_objeto, LISTA_GLOBAL_SPRITES, False)
    if len(LISTA_CONFLICTO) == 0:
        LISTA_GLOBAL_SPRITES.add(_objeto)
        LISTA_OBJETOS.add(_objeto)

reloj = pygame.time.Clock()

print("Empezamos...")

TERMINA = False

while not TERMINA:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      TERMINA = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        _personaje.DIRECCION = 'I'
        break
      elif event.key == pygame.K_RIGHT:
        _personaje.DIRECCION = 'D'
        break
      elif event.key == pygame.K_UP:
        _personaje.DIRECCION = 'A'
        break
      elif event.key == pygame.K_DOWN:
        _personaje.DIRECCION = 'B'
        break

  LISTA_GLOBAL_SPRITES.update()
  screen.fill(BLANCO)

  LISTA_GLOBAL_SPRITES.draw(screen)
  VER_MARCADOR()

  if _personaje.TERMINA:
    pygame.time.wait(5000)
    TERMINA = True

  pygame.display.flip()
  dt = reloj.tick(60)
  _personaje.reloj.update(dt)

print("Número de objetos recogidos: %d" % _personaje.PUNTOS)
pygame.quit()

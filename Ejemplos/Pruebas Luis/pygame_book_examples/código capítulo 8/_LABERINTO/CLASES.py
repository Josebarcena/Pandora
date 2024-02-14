import pygame, random, sys
from CONSTANTES import *
from datetime import timedelta, datetime, date, time

LISTA_OBJETOS = pygame.sprite.Group()
LISTA_PAREDES = pygame.sprite.Group()
LISTA_GLOBAL_SPRITES = pygame.sprite.Group()

class PARED(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("PARED.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = BALDOSA_TAMANIO * y + MARCADOR_ANCHURA
    self.rect.x = BALDOSA_TAMANIO * x

class OBJETO(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("OBJETO.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = random.randint(0, BALDOSA_NUMERO - 1) * BALDOSA_TAMANIO + MARCADOR_ANCHURA
    self.rect.x = random.randint(0, BALDOSA_NUMERO - 1) * BALDOSA_TAMANIO

class PERSONAJE(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("PERSONAJE.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.y = random.randint(0, BALDOSA_NUMERO - 1) * BALDOSA_TAMANIO + MARCADOR_ANCHURA
    self.rect.x = random.randint(0, BALDOSA_NUMERO - 1) * BALDOSA_TAMANIO
    self.PUNTOS = 0
    self.TERMINA = False
    self.DIRECCION = '-'
    self.reloj = Reloj()

  def update(self):
    X_ACTUAL = self.rect.x
    Y_ACTUAL = self.rect.y
    if self.DIRECCION == 'I':
      self.rect.x -= BALDOSA_TAMANIO
      self.DIRECCION = '-'
    elif self.DIRECCION == 'D':
      self.rect.x += BALDOSA_TAMANIO
      self.DIRECCION = '-'
    elif self.DIRECCION == 'A':
      self.rect.y -= BALDOSA_TAMANIO
      self.DIRECCION = '-'
    elif self.DIRECCION == 'B':
      self.rect.y += BALDOSA_TAMANIO
      self.DIRECCION = '-'

    LISTA_COLISION_PARED = pygame.sprite.spritecollide(self, LISTA_PAREDES, False)
    if len(LISTA_COLISION_PARED) > 0:
        self.rect.x = X_ACTUAL
        self.rect.y = Y_ACTUAL

    LISTA_COLISION_OBJETO = pygame.sprite.spritecollide(self, LISTA_OBJETOS, False)
    for objeto in LISTA_COLISION_OBJETO:
      objeto.kill()
      self.PUNTOS += PUNTO_UNIDAD
      if self.PUNTOS == 10:
          self.reloj.stop()

class Reloj:
  def __init__(self):
   self.Timer = datetime.combine(date.today(), time(0, 0))
   self.STOP = False

  def stop(self):
      self.STOP = True

  def update(self, dt):
      if self.STOP == False:
        self.Timer += timedelta(milliseconds=dt)

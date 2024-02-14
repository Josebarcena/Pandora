import pygame, random, sys
from CONSTANTES import *
from datetime import timedelta, datetime, date, time

LISTA_PLANETAS = pygame.sprite.Group()
LISTA_GLOBAL_SPRITES = pygame.sprite.Group()

class PLANETA(pygame.sprite.Sprite):

  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("img/PLANETA.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def update(self):

    self.rect.y = self.rect.y + VELOCIDAD_PLANETAS

    if self.rect.y > ANCHURA_VENTANA:
      LISTA_GLOBAL_SPRITES.remove(self)
      LISTA_PLANETAS.remove(self)
      self.kill()

class COHETE(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("img/COHETE.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = 210
    self.rect.y = 300
    self.DIRECCION = 'I'

  def update(self):

    print(self.DIRECCION)
    if self.DIRECCION == 'I':
      self.rect.x -= 4
    elif self.DIRECCION == 'D':
      self.rect.x += 4

    if self.rect.x < 0:
      self.rect.x = 0
    elif self.rect.x > ALTURA_VENTANA - ALTURA_COHETE:
      self.rect.x = ALTURA_VENTANA - ALTURA_COHETE


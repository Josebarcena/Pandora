import pygame
from pygame.math import Vector2 as vector
from Ajustes import *

""" class Pandora(pygame.sprite.sprite):
    def __init__(self):

    def update(self):

    def draw(self):

    def colisiones(self, objetos):

    def estado(self): #si esta saltando...

    def mover(self):
 """
    

class Jugador(pygame.sprite.Sprite):
    def __init__(self, posicion, groups, colision_completa, colision_superior):
        super().__init__(groups)
        self.image = pygame.Surface((16, 32))
        self.image.fill('green')

        self.rect = self.image.get_rect(topleft = posicion)
        self.rect_anterior = self.rect.copy()

        self.direccion = vector(0,0)
        self.velocidad = PANDORA_SPEED
        self.jumping = False
        self.on_ground = True
        self.fall_count = 0
        self.velocidad_y = JUMP_HEIGHT

        self.colision_completa = colision_completa
        self.colision_superior = colision_superior
        #print(self.colision_completa)

    def input(self):
        teclas = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if teclas[pygame.K_RIGHT]:
            input_vector.x += 1
        if teclas[pygame.K_LEFT]:
            input_vector.x -= 1
        if teclas[pygame.K_UP]:
            input_vector.y -= 1
            if self.on_ground: 
                self.jumping = True
                self.on_ground = False 
        if teclas[pygame.K_DOWN]:
            input_vector.y += 1

        self.direccion = input_vector.normalize() if input_vector else input_vector

    def landed(self):
        self.fall_count = 0
        self.jumping = False
        self.on_ground = True

    def movimiento(self, dt):
        self.rect.x += self.direccion.x * self.velocidad
        if self.jumping :
            self.rect.y -= self.velocidad_y
            self.velocidad_y -= GRAVITY
            self.fall_count += 1
            if self.velocidad_y < -JUMP_HEIGHT:
                self.jumping = False
                self.velocidad_y = JUMP_HEIGHT
        else:
            self.rect.y +=  min(3, (self.fall_count / dt) * GRAVITY)
        self.fall_count += 1

    def colisiones(self, eje):
        objetos_chocados=[] #Añadimos los objetos con los que hay contacto en caso de gestionar unos pinchos u otra superficie.

        for sprite in self.colision_completa:
            if sprite.rect.colliderect(self.rect):
                if eje == 'horizontal':
                    #izquierda
                    if self.rect.left <= sprite.rect.right and self.rect_anterior.left >= sprite.rect_anterior.right :
                        self.rect.left = sprite.rect.right
                    #derecha
                    if self.rect.right >= sprite.rect.left and self.rect_anterior.right <= sprite.rect_anterior.left :
                        self.rect.right = sprite.rect.left
                else:
                    #arriba
                    if self.rect.top <= sprite.rect.bottom and self.rect_anterior.bottom >= sprite.rect_anterior.top :
                        self.rect.top = sprite.rect.bottom
                    #abajo
                    if self.rect.bottom >= sprite.rect.top and self.rect_anterior.bottom <= sprite.rect_anterior.top :
                        self.rect.bottom = sprite.rect.top
                        self.landed()

            objetos_chocados.append(sprite)

        for sprite in self.colision_superior:
            if sprite.rect.colliderect(self.rect):
                if eje == 'horizontal':
                    pass
                else:
                    #abajo
                    if self.rect.bottom >= sprite.rect.top and self.rect_anterior.bottom <= sprite.rect_anterior.top :
                        self.rect.bottom = sprite.rect.top

            objetos_chocados.append(sprite)
        
        return objetos_chocados

    def update(self, dt):
        self.rect_anterior = self.rect.copy()
        self.input()
        self.movimiento(dt)
        self.colisiones('horizontal')
        self.colisiones('vertical')

class Sprite(pygame.sprite.Sprite):
        def __init__(self, posicion, superficie, groups):
            super().__init__(groups)
            self.image = superficie
            self.rect = self.image.get_rect(topleft = posicion)
            self.group = groups
            self.rect_anterior = self.rect.copy()


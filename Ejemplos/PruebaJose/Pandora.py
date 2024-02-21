import pygame
from pygame.math import Vector2 as vector
from Ajustes import *
from control_pandora import Control

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
        self.image = pygame.Surface((16*ESCALA_BASE, 32*ESCALA_BASE))
        
        self.image.fill('green')

        self.rect = self.image.get_rect(topleft = posicion)
        self.rect_anterior = self.rect.copy()

        self.control = Control()
        self.cualquier_sprite = groups
        self.direccion = vector(0,0)
        self.velocidad = PANDORA_SPEED * ESCALA_BASE
        self.jumping = False
        self.on_ground = True
        self.fall_count = 0
        self.velocidad_y = JUMP_HEIGHT * ESCALA_BASE

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

        self.direccion = input_vector
        

    def landed(self):
        self.fall_count = 0
        self.jumping = False
        self.on_ground = True

    def movimiento(self, dt):
        self.rect.x += round(self.direccion.x * self.velocidad / dt)
        if self.jumping :
            self.rect.y -= round(self.velocidad_y / dt)
            self.velocidad_y -= GRAVITY * ESCALA_BASE
            self.fall_count += 1
            if self.velocidad_y < -JUMP_HEIGHT * ESCALA_BASE:
                self.jumping = False
                self.velocidad_y = JUMP_HEIGHT * ESCALA_BASE
        else:
            self.rect.y +=  round(min(3 * ESCALA_BASE, (self.fall_count / dt) * GRAVITY / ESCALA_BASE))
        self.fall_count += 1

    def collisions(self, eje):
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
                        self.control.change_state('ground')
                    else:
                        self.control.change_state('air')

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
    
    def screen_check(self, dt):
        if self.rect.x <= SCROLL_LIMIT_X:
            self.rect.x = SCROLL_LIMIT_X
            for sprite in self.cualquier_sprite:
                sprite.rect.x += PANDORA_SPEED
        elif self.rect.x >= ANCHO_VENTANA - SCROLL_LIMIT_X:
            self.rect.x = ANCHO_VENTANA - SCROLL_LIMIT_X
            for sprite in self.cualquier_sprite:
                sprite.rect.x -= PANDORA_SPEED 
        if self.rect.y <= SCROLL_LIMIT_Y:
            self.rect.y = SCROLL_LIMIT_Y
            for sprite in self.cualquier_sprite:
                sprite.rect.y += PANDORA_SPEED
        elif self.rect.y >= ALTO_VENTANA - SCROLL_LIMIT_Y:
            self.rect.y = ALTO_VENTANA - SCROLL_LIMIT_Y
            for sprite in self.cualquier_sprite:
                sprite.rect.y -= PANDORA_SPEED

    def update(self, dt):
        self.x_change, self.y_change = self.control.movement()

        self.x_change, self.y_change = self.control.update_character(self.x_change, self.y_change)
        self.rect.x += (self.x_change * ESCALA_BASE) / dt
        self.collisions('horizontal')

        self.rect.y += (self.y_change * ESCALA_BASE) / dt
        self.collisions('vertical')

        self.screen_check(dt)

        self.x_change = 0
        self.y_change = 0
        

class Sprite(pygame.sprite.Sprite):
        def __init__(self, posicion, superficie, groups):
            super().__init__(groups)
            self.image = superficie
            self.image = pygame.transform.scale(self.image, (16*ESCALA_BASE, 16*ESCALA_BASE))
            self.rect = self.image.get_rect(topleft = posicion)
            self.group = groups
            self.rect_anterior = self.rect.copy()


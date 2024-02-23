import pygame
from config import *
from control_pandora import *
import math
import random

# Definimos la clase Player en la que está implementada la mayoría de funcionalidad del código, debería de encapsularse y quitarle "responsabilidades"
class Player(pygame.sprite.Sprite):
    # Método con el que iniciamos el objeto, partimos de las coordenadas iniciales del juego y el propio juego
    def __init__(self, game, x, y):
        # Iniciamos las variables del jugador para poder acceder a ellas más adelante
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Posiciones iniciales del cubo y tamaño
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.heigh = TILESIZE * 2

        # Variables auxiliares que nos ayudarán a actualizar la posición del personaje
        self.x_change = 0
        self.y_change = 0

        # Para las animaciones, sin implementar
        self.facing = 'lef'

        # Control del personaje
        self.control = Control()

        # Inicializamos el rect del Sprite, ya que es un objeto importado de la libreria debemos de inicializar el rect
        # para poder usar estas librerias correctamente, véase en las colisiones
        self.image = pygame.Surface([self.width, self.heigh])
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.previous_rect = self.rect

    # Método en el que se actualiza el cubo
    def update(self):
        self.x_change, self.y_change = self.control.movement()

        self.x_change, self.y_change = self.control.update_character(self.x_change, self.y_change)
        self.rect.x += self.x_change
        self.collide_blocks('x')

        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.screen_check()
        self.previous_rect = self.rect
        self.x_change = 0
        self.y_change = 0

    # Comprobamos la posición del jugador al final de la actualización de pantalla, si se sale de los márgenes
    # establecidos, moveremos la lista de sprites que conforman el nivel en dirección contraria a la que va el jugador
    # y a la velocidad del jugador
    def screen_check(self):
        if self.rect.x <= SCROLL_LIMIT_X:
            self.rect.x = SCROLL_LIMIT_X
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
        elif self.rect.x >= WIN_WIDTH - SCROLL_LIMIT_X:
            self.rect.x = WIN_WIDTH - SCROLL_LIMIT_X
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
        if self.rect.y <= SCROLL_LIMIT_Y:
            self.rect.y = SCROLL_LIMIT_Y
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
        elif self.rect.y >= WIN_HEIGHT - SCROLL_LIMIT_Y:
            self.rect.y = WIN_HEIGHT - SCROLL_LIMIT_Y
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED

    # Se estudian las colisiones del jugador con los sprites almacenados en game.blocks, que son los distintos bloques
    # con los que se crea el nivel
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.full_collision, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits_full = pygame.sprite.spritecollide(self, self.game.full_collision, False)
            if hits_full:
                if self.y_change > 0:
                    self.rect.y = hits_full[0].rect.top - self.rect.height
                    self.control.change_state('ground')
                if self.y_change < 0:
                    self.rect.y = hits_full[0].rect.bottom
            else:
                self.control.change_state('air')
            
            #(Jose) segui el ejemplo de full colision para bloques de daño
            hits_damage = pygame.sprite.spritecollide(self, self.game.damage_collision, False)
            
            if hits_damage:
                print("DAMAGE")
                if self.y_change > 0:
                    self.rect.y = hits_damage[0].rect.top - self.rect.height
                    self.control.change_state('ground')
                if self.y_change < 0:
                    self.rect.y = hits_damage[0].rect.bottom
            else:
                self.control.change_state('air')
            
            hits_upper = pygame.sprite.spritecollide(self, self.game.upper_collision, False)
            if hits_upper:
                if self.y_change > 0 and self.previous_rect.y < hits_upper[0].rect.top:
                    self.rect.y = hits_upper[0].rect.top - self.rect.height
                    self.control.change_state('ground')
            # En caso de que no se haya colisiones verticalmente y bool_air era falso en el anterior frame significa que
            # debemos de aplicar la gravedad, el jugador se cayó de la plataforma
            if (hits_upper == 0) and (hits_full == 0): 
                self.control.change_state('air')
            
            

            print(hits_full, hits_upper, self.control.state)
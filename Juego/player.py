import pygame
from config import *
from control_pandora import *
import math
import random

# Definimos la clase Player en la que está implementada la mayoría de funcionalidad del código, debería de encapsularse y quitarle "responsabilidades"
class Player(pygame.sprite.Sprite):
    # Método con el que iniciamos el objeto, partimos de las coordenadas iniciales del juego y el propio juego
    def __init__(self, game, x, y,group):
        # Iniciamos las variables del jugador para poder acceder a ellas más adelante
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = (self.game.all_sprites,self.game.visible_sprites,group)
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Posiciones iniciales del cubo y tamaño
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE * SCALE
        self.heigh = TILESIZE * 2 * SCALE

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
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.previous_rect = self.rect

    # Método en el que se actualiza el cubo
    def update(self):
        self.x_change, self.y_change = self.control.movement()

        self.x_change, self.y_change = self.control.update_character(self.x_change, self.y_change)
        self.rect.x += self.x_change
        self.collide_blocks(self.game.collide_Fase(self),"x")

        self.rect.y += self.y_change
        self.collide_blocks(self.game.collide_Fase(self),"y")

        self.previous_rect = self.rect
        self.x_change = 0
        self.y_change = 0
        

    # Comprobamos la posición del jugador al final de la actualización de pantalla, si se sale de los márgenes
    # establecidos, moveremos la lista de sprites que conforman el nivel en dirección contraria a la que va el jugador
    # y a la velocidad del jugador
    

    # Se estudian las colisiones del jugador con los sprites almacenados en game.blocks, que son los distintos bloques
    # con los que se crea el nivel
    def collide_blocks(self, collision, direction):
        
        #Comprobamos con que choca
        if collision[0] == "Solid":
            self.solid_Collision(collision[1],direction)

        elif collision[0] == "Platform":
            self.platform_Collision(collision[1], direction)

        elif collision[0] == "Damage":
            print("DAMAGE")
            self.solid_Collision(collision[1], direction)
        
        elif collision[0] == "Stairs":
            self.stairs_Collision(collision[1], direction)

        else:
            self.control.change_state('air')
            
    def solid_Collision(self,blocks, direction):
        if  direction == "x":
            if self.x_change > 0:
                self.rect.x = blocks[0].rect.left - self.rect.width
            if self.x_change < 0:
                self.rect.x = blocks[0].rect.right
        if  direction == "y":
            if self.y_change > 0:
                self.rect.y = blocks[0].rect.top - self.rect.height
                self.control.change_state('ground')
            if self.y_change < 0:
                self.rect.y = blocks[0].rect.bottom


    def platform_Collision(self, platforms, direction):
        if direction == "y":
                player_necessary_y = self.rect.bottom
                platform_necessary_y = platforms[0].rect.top + 0.75 * platforms[0].rect.height
            
                # Verificar si el jugador está por encima del 75% de la plataforma
                if player_necessary_y < (platform_necessary_y):
                    if self.y_change > 0 and self.previous_rect.y < platforms[0].rect.top:
                        self.rect.y = platforms[0].rect.top - self.rect.height
                        self.control.change_state('ground')



    def stairs_Collision(self, ramps, direction):
                for ramp in ramps:
                    # Si el jugador está sobre la rampa y su centro vertical está por encima del borde superior de la rampa
                    if self.rect.colliderect(ramp.rect) and self.rect.centery < ramp.rect.centery:
                        # Calcular la nueva posición vertical del jugador para subir la rampa
                        new_y = ramp.rect.top - self.rect.height + (self.rect.centerx - ramp.rect.left) * 0.5  # Pendiente del 45%

                        # Mover al jugador a la nueva posición
                        self.rect.y = new_y
                    self.control.change_state('ground')

    def draw(self, surface):
        pygame.Surface.blit(surface, self.image, self.rect)
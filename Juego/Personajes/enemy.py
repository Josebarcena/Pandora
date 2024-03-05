import pygame
from Recursos.config import *
from Personajes.Viewers import *
import numpy as np
from Recursos.Gestor_recursos import GestorRecursos

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, group):
        self.game = game
        self.groups = (self.game.all_sprites, group)
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE 
        self.y = y * TILESIZE
        self.width = TILESIZE * SCALE
        self.heigh = TILESIZE * 2 * SCALE

        self.x_change = 0
        self.y_change = 0
        self.frames_jump = 0
        self.jump = 0
        

        self.facing = 'left'
        self.state = 'normal'
        self.animaciones_idle = GestorRecursos.loadSpritesEnemies('Enemies_Sheet-Effect.png', 8, 25, 27, 51, 13, 22)
        self.animaciones_idle_angry = GestorRecursos.loadSpritesEnemies('EnemiesAngry_Sheet-Effect.png', 8, 25, 27, 51, 13, 22)
        self.animacion_actual = self.animaciones_idle
        self.frame_index_idle = 0  # Índice del fotograma actual para la animación de estar quieto
        self.frame_index_run = 0  # Índice del fotograma actual para la animación de correr
        self.update_time = 0  # Tiempo de última actualización de la animación de estar quieto

        # Cargar la imagen del personaje
        self.update_image(self.animacion_actual)

        self.rect = self.image.get_rect(bottomleft = (x,y))
        self.previous_rect = self.rect

    def update_image(self, animation_array):
        tiempo_actual = pygame.time.get_ticks()

        cooldown_animacion = 180
        frame_index = self.frame_index_idle

        if tiempo_actual - self.update_time >= cooldown_animacion:
            frame_index += 1
            self.update_time = tiempo_actual
            if frame_index >= len(animation_array):
                frame_index = 0

        self.frame_index_idle = frame_index
        self.animation_image = animation_array[frame_index]

        if self.facing == 'left':
            self.image = pygame.transform.flip(self.animation_image, True, False)
        else:
            self.image = self.animation_image


        self.image = pygame.transform.scale(self.image, (TILESIZE * SCALE, TILESIZE * 2 * SCALE))

    def draw(self, screen):
        screen.blit(screen, self.image, self.rect)

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.collide_blocks(self.game.collide_Fase(self),"x")

        self.rect.y += self.y_change
        self.collide_blocks(self.game.collide_Fase(self),"y")

        self.x_change = 0
        self.y_change = 0

    def in_screen(self):
        if self.rect.x + self.width < 0 or self.rect.x > WIN_WIDTH:
            return False
        elif self.rect.y + self.heigh < 0 or self.rect.y > WIN_HEIGHT:
            return False
        else:
            return True

    def checkPlayer(self):
        dx = np.sqrt((self.game.player.rect.x - self.rect.x)**2) < PIXELS_ENEMIES_AGRO_X
        dy = np.sqrt((self.game.player.rect.y - self.rect.y)**2) < PIXELS_ENEMIES_AGRO_Y
        if dx and dy:
            if self.game.player.rect.x > self.rect.x:
                self.facing = 'right'
            else:
                self.facing = 'left'
        return dx and dy

    def movement(self):
        if self.frames_jump == ENEMIES_JUMP_FRAMES:
            self.jump = False
        if self.frames_jump <= 0:
            self.y_change += GRAVITY
        else:
            self.y_change -= ENEMIES_JUMP_SPEED
            self.frames_jump -= 1
        if self.in_screen():
            if self.facing == 'left':
                if self.checkPlayer():
                    self.animacion_actual = self.animaciones_idle_angry
                    self.update_image(self.animacion_actual)
                    self.state = 'agro'
                    self.x_change -= ENEMIES_SPEED_AGRO
                else:
                    self.animacion_actual = self.animaciones_idle
                    self.state = 'normal'
                    self.update_image(self.animacion_actual)
                    self.x_change -= ENEMY_SPEED
            if self.facing == 'right':
                if self.checkPlayer():
                    self.animacion_actual = self.animaciones_idle_angry
                    self.state = 'agro'
                    self.update_image(self.animacion_actual)
                    self.x_change += ENEMIES_SPEED_AGRO
                else:
                    self.animacion_actual = self.animaciones_idle
                    self.state = 'normal'
                    self.update_image(self.animacion_actual)
                    self.x_change += ENEMY_SPEED

    def collide_blocks(self, collision, direction):
         #Comprobamos con que choca
        if collision[0] == "Solid":
            self.solid_Collision(collision[1],direction)
        elif collision[0] == "Limit":
            self.solid_Collision(collision[1],direction)
    def solid_Collision(self, blocks, direction):
        if  direction == "x":
            if self.x_change > 0:
                self.rect.x = blocks[0].rect.left - self.rect.width
                if self.state == 'normal':
                    self.facing = 'left'
            if self.x_change < 0:
                self.rect.x = blocks[0].rect.right
                if self.state == 'normal':
                    self.facing = 'right'
        if  direction == "y":
            if self.y_change > 0:
                self.rect.y = blocks[0].rect.top - self.rect.height
            if self.y_change < 0:
                self.rect.y = blocks[0].rect.bottom




import pygame
from Recursos.config import *
from Personajes.Viewers import *
import numpy as np

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, group):
        self.game = game
        self._layer = ENEMY_LAYER
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
        self.image = pygame.Surface([self.width, self.heigh])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.previous_rect = self.rect

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.collide_blocks('x')

        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0
    def in_screen(self):
        if self.rect.x < -TILESIZE or self.rect.x > WIN_WIDTH:
            return False
        elif self.rect.y < - TILESIZE or self.rect.y > WIN_HEIGHT:
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
                    self.image.fill(RED)
                    self.state = 'agro'
                    self.x_change -= ENEMIES_SPEED_AGRO
                else:
                    self.state = 'normal'
                    self.image.fill(BLACK)
                    self.x_change -= ENEMY_SPEED
            if self.facing == 'right':
                if self.checkPlayer():
                    self.state = 'agro'
                    self.image.fill(RED)
                    self.x_change += ENEMIES_SPEED_AGRO
                else:
                    self.state = 'normal'
                    self.image.fill(BLACK)
                    self.x_change += ENEMY_SPEED
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.full_collision, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.facing = 'left'
                    if self.state == 'agro' and self.frames_jump <= 0 and self.jump:
                        self.frames_jump = ENEMIES_JUMP_FRAMES
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    self.facing = 'right'
                    if self.state == 'agro' and self.frames_jump <= 0 and self.jump:
                        self.frames_jump = ENEMIES_JUMP_FRAMES

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.full_collision, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.jump = True
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
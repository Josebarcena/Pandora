import pygame
from Personajes.player import *
from Recursos.config import *
class Attack(pygame.sprite.Sprite):
    def __init__(self, x, y, game, player):
        self.game = game
        self.groups = game.all_sprites
        self.player = player
        self._layer = 4
        self.groups = self.game.all_sprites, self.game.visible_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = ATTACK_WIDTH * SCALE
        self.height = ATTACK_HEIGHT * SCALE

        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill(RED)

        # Almacena si se está realizando el dash o no
        self.run = False
        self.face = None

    def run_att(self, run1, dir):
        self.run = run1
        self.facing = dir
    def update(self):
        if self.run:
            self.image.fill(BLACK)
            self.rect.y = self.player.rect.y - (self.height - self.player.heigh)
            if self.facing == 'right':
                self.rect.x = self.player.rect.x
            elif self.facing == 'left':
                self.rect.x = self.player.rect.x - (self.width - self.player.width)
        else:
            self.rect.y = -300

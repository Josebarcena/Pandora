import pygame
from Personajes.player import *
from Recursos.config import *
class Attack(pygame.sprite.Sprite):
    def __init__(self, x, y, game, player):
        self.game = game
        self.groups = game.all_sprites
        self.player = player
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Tamaño del sprite de ataque
        self.width = ATTACK_WIDTH * SCALE
        self.height = ATTACK_HEIGHT * SCALE

        # Creación del sprite de ataque, nótese de que realmente no se está pintando nada
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft=(x, y))

        # Almacena si se está realizando el ataque o no, y en que dirección
        self.attacking = False
        self.facing = None

    # Actualización del ataque cada vez que el personaje está atacando
    def update_state(self, attacking1, dir):
        self.attacking = attacking1
        self.facing = dir

    # Se reposiciona la posicion del sprite según la posición del personaje asociado y la direccion del ataque
    def update(self):
        if self.attacking:
            self.rect.y = self.player.hitbox.rect.y - (self.height - self.player.height)
            if self.facing == 'right':
                self.rect.x = self.player.hitbox.rect.x
            elif self.facing == 'left':
                self.rect.x = self.player.hitbox.rect.x - (self.width - self.player.width)
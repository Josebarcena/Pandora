from config import *
import pygame

# Defino los diferentes bloques que formarán parte del nivel
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, color):
        self.game = game
        self._layer = BLOCK_LAYER
        # Se añade el bloque a las distintas listas del juego
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Colocamos el bloque según las posición que se nos indica y le damos el size oportuno
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # Añadimos color y superficio al bloque
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)

        # Inicializamos el rect del Sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
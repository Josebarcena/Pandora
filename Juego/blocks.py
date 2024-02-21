from config import *
import pygame

# Defino los diferentes bloques que formarán parte del nivel
class Sprite(pygame.sprite.Sprite):
    def __init__(self, game, x, y, surface, groups):
        
        # Se añade el bloque a las distintas listas del juego
        super().__init__(groups)
        # Añadimos textura al bloque
        self.image = surface
        self.rect = self.image.get_rect(topleft = (x,y))
        self.group = groups
        self.rect_anterior = self.rect.copy()

        self.game = game
        self._layer = BLOCK_LAYER

from pygame.sprite import AbstractGroup
from ajustes import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, posicion, superficie, groups):
        super().__init__(groups)
        self.image = superficie
        self.rect = self.image.get_rect(topleft = posicion)
        self.group = groups
        self.rect_anterior = self.rect.copy()

        
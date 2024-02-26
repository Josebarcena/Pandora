from config import *
import pygame

# Defino los diferentes bloques que formarán parte del nivel
class Sprite(pygame.sprite.Sprite):
    def __init__(self, game, x, y, surface, groups):
        
        # Se añade el bloque a las distintas listas del juego
        super().__init__(groups)
        # Añadimos textura al bloque
   
        self.image = surface
        self.image = pygame.transform.scale(self.image, (16*SCALE, 16*SCALE))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.group = groups
        self.rect_anterior = self.rect.copy()

        self.game = game
        self._layer = BLOCK_LAYER


        for group in self.group:
            if group == game.full_collision:
                self.image.fill(RED)
            if group == game.upper_collision:
                self.image.fill(YELLOW)
            if group == game.damage_collision:
                self.image.fill(BLUE)
            if group == game.stairs_collision:
                self.image.fill(GREEN)


    def draw(self, surface):        
        pass




class Stage(pygame.sprite.Sprite):
    def __init__(self, game, x, y, surface, groups):
        
        # Se añade el bloque a las distintas listas del juego
        super().__init__(groups)
        # Añadimos textura al bloque
        self.image = surface
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*SCALE, self.image.get_height()*SCALE))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.group = groups
        self.rect_anterior = self.rect.copy()

        self.game = game
        self._layer = BLOCK_LAYER


    def draw(self, surface, debug):
        pygame.Surface.blit(surface, self.image, self.rect)
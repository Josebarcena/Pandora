from Niveles.Fase import *
from Recursos.Gestor_recursos import *
from Niveles.blocks import *
from Niveles.Menus import *
from Personajes.player import *
from Personajes.enemy import *
import math

class Item(pygame.sprite.Sprite):
    def __init__(self):
        self.image = None

    
    def update(self):
        pass

    def utility(self):
        pass


class small_Potion(Item):
    def __init__(self, game, x, y, group):
        super(small_Potion,self).__init__()

        self.game = game
        self.groups = (self.game.all_sprites, group)
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.width = TILESIZE * SCALE
        self.height = TILESIZE * SCALE
        self.image = GestorRecursos.LoadImage("Imagenes","small_potion.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.change_y = 0
        # Ajusta la posición inicial
        self.starting_y = y - 30
        self.amplitude = 1  # Amplitud del movimiento sinusoidal
        self.frequency = 0.008  # Frecuencia del movimiento sinusoidal

    def update(self):
        # Obtiene el tiempo transcurrido en milisegundos desde que se inició el juego
        current_time = pygame.time.get_ticks()

        # Calcula la nueva posición y basada en el movimiento sinusoidal
        self.change_y = self.amplitude * math.sin(self.frequency * current_time)
        self.rect.y += self.change_y 

    def utility(self):
        return 1
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)





class Hope(Item):
    def __init__(self, game, x, y, group):
        super(Hope, self).__init__()

        self.game = game
        self.groups = (self.game.all_sprites,group)
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.width = TILESIZE * SCALE
        self.height = TILESIZE * SCALE
        self.image = GestorRecursos.LoadImage("Imagenes","hope.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #self.rect = self.image.get_rect(topleft=(x, y))
        self.rect = self.image.get_rect(bottomleft = (x,y))

    def utility(self):
        return 2
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

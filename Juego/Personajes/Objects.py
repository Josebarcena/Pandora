from Niveles.Fase import *
from Recursos.Gestor_recursos import *
from Niveles.blocks import *
from Niveles.Menus import *
from Personajes.player import *
from Personajes.enemy import *

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
        self.groups = (self.game.all_sprites,group)
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE * SCALE
        self.height = TILESIZE * SCALE
        self.image = GestorRecursos.LoadImage("Imagenes","small_potion.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #self.rect = self.image.get_rect(topleft=(x, y))
        self.rect = self.image.get_rect(bottomleft = (x,y))

    def utility(self):
        return 1
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

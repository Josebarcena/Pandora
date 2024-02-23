import config
from Main_menu import *
from player import *
from config import *
from blocks import *

class Fase1(Base_state):
    def __init__(self):
        super(Fase1,self).__init__()
        self.sound = ("fase1.mp3")
        self.all_sprites = pygame.sprite.Group()
        self.upper_collision = pygame.sprite.Group()
        self.full_collision = pygame.sprite.Group()
        self.damage_collision = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.attacks = pygame.sprite.Group()
        
        self.level1 = GestorRecursos.LoadImage("Fases","fase12.tmx")
        self.createTilemap(self.level1)

    def createTilemap(self, tmx_map):
        for x, y, surface in tmx_map.get_layer_by_name('Fondo').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites))

        for x, y, surface in tmx_map.get_layer_by_name('Solido').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites, self.full_collision))

        for x, y, surface in tmx_map.get_layer_by_name('Semi').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites, self.upper_collision))

        for x, y, surface in tmx_map.get_layer_by_name('Pincho').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites, self.damage_collision))
        
        for x, y, surface in tmx_map.get_layer_by_name('Escalera').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites, self.full_collision))

        for x, y, surface in tmx_map.get_layer_by_name('Falso').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites, self.full_collision))
        
        for objeto in tmx_map.get_layer_by_name('Jugador'):
            Player(self, objeto.x, objeto.y)

    def collide_Fase(self, player): # Crear 
        if ((hits := pygame.sprite.spritecollide(player, self.full_collision, False))):
            return ("Solid", hits)
        elif((hits := pygame.sprite.spritecollide(player, self.upper_collision, False))):
            return ("Platform", hits)
        elif((hits := pygame.sprite.spritecollide(player, self.damage_collision, False))):
            return ("Damage", hits)
        else:
            return (None,None)


    def get_event(self, event):
            if event.type == pygame.QUIT:
                self.quit = True

    def update(self, tick):
        self.all_sprites.update()

    def draw(self, surface):
        self.all_sprites.draw(surface)
        pygame.display.update()
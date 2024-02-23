import config
from Main_menu import *
from player import *
from config import *
from blocks import *


class Fase(Base_state):
    def __init__(self, mapa, sonido, next_state = None):
        super(Fase,self).__init__()
        self.all_sprites = pygame.sprite.Group()
        self.upper_collision = pygame.sprite.Group()
        self.full_collision = pygame.sprite.Group()
        self.damage_collision = pygame.sprite.Group()

        self.player_layer = pygame.sprite.Group()
        self.player = None
        self.enemies = pygame.sprite.Group()
        self.attacks = pygame.sprite.Group()
        

        self.next_state = next_state

        self.sound = (sonido)
        self.level = GestorRecursos.LoadImage("Fases",mapa)
        
        self.chunk_size = 10  # Tamaño de cada chunk en tiles

        # Variables para rastrear los límites del área cargada
        self.min_chunk_x = 0
        self.max_chunk_x = self.chunk_size
        self.total_chunks = math.ceil(self.level.width / self.chunk_size)

        self.createTilemap(self.level)


    def createTilemap(self, tmx_map): #crea el mapa desde tiled
        
        for x, y, surface in tmx_map.get_layer_by_name('Montanas').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites))

        for x, y, surface in tmx_map.get_layer_by_name('Fondo').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites))

        for x, y, surface in tmx_map.get_layer_by_name('Decoracion').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites))

        for x, y, surface in tmx_map.get_layer_by_name('Solido').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites, self.full_collision))

        for x, y, surface in tmx_map.get_layer_by_name('Semi').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites, self.upper_collision))

        for x, y, surface in tmx_map.get_layer_by_name('Pincho').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites, self.damage_collision))
        
        for x, y, surface in tmx_map.get_layer_by_name('Escalera').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites, self.full_collision))

        for x, y, surface in tmx_map.get_layer_by_name('Falso').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites, self.full_collision))
        
        for x, y, surface in tmx_map.get_layer_by_name('Rompible').tiles():
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites))

        for objeto in tmx_map.get_layer_by_name('Meta'):
            Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites))
        
        for objeto in tmx_map.get_layer_by_name('Jugador'):
            Player(self, objeto.x *SCALE, objeto.y*SCALE,self.player_layer)
            self.player = self.player_layer.sprites()[0]

    def get_event(self, event):
            if event.type == pygame.QUIT:
                self.quit = True

    def update(self, tick): #hace update acorde a los fps
        self.screen_check()
        self.all_sprites.update()


    def screen_check(self):
        if self.player.rect.x <= SCROLL_LIMIT_X:
            self.player.rect.x = SCROLL_LIMIT_X
            for sprite in self.all_sprites:
                sprite.rect.x += PLAYER_SPEED
        elif self.player.rect.x >= WIN_WIDTH - SCROLL_LIMIT_X:
            self.player.rect.x = WIN_WIDTH - SCROLL_LIMIT_X
            for sprite in self.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
        if self.player.rect.y <= SCROLL_LIMIT_Y:
            self.player.rect.y = SCROLL_LIMIT_Y
            for sprite in self.all_sprites:
                sprite.rect.y += PLAYER_SPEED
        elif self.player.rect.y >= WIN_HEIGHT - SCROLL_LIMIT_Y:
            self.player.rect.y = WIN_HEIGHT - SCROLL_LIMIT_Y
            for sprite in self.all_sprites:
                sprite.rect.y -= PLAYER_SPEED


    def draw(self, surface): #pintar la fase
        surface.fill((123,211,247))
        self.all_sprites.draw(surface)
        pygame.display.update()


    def collide_Fase(self, player): # chequea las colisiones con los bloques de las fases
        if ((hits := pygame.sprite.spritecollide(player, self.full_collision, False))):
            return ("Solid", hits)
        elif((hits := pygame.sprite.spritecollide(player, self.upper_collision, False))):
            return ("Platform", hits)
        elif((hits := pygame.sprite.spritecollide(player, self.damage_collision, False))):
            return ("Damage", hits)
        else:
            return (None,None)


class Chunk(pygame.sprite.Sprite):
    def __init__(self, fase, x, y, surface):
        super().__init__(fase.all_sprites)
        self.fase = fase
        self.image = surface
        self.rect = self.image.get_rect(topleft=(x, y))
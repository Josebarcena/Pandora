from player import *
from config import *
from blocks import *
from pytmx.util_pygame import load_pygame
from os.path import join
# Objeto que simila el juego, en este se realiza la lógica principal de nuestro juego
class Game(object):
    # Iniciamos el juego, creando la pantalla, variables que se usarán y el reloj
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 32)
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.upper_collision = pygame.sprite.Group()
        self.full_collision = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.attacks = pygame.sprite.Group()
        self.level1 = load_pygame(join(".","Fases","fase11.tmx"))
        self.createTilemap(self.level1)
    # Mediante la matriz titlemap, definida en config.py, que representa el nivel, creamos los diferentes objetos de
    # bloques y el jugador.
    def createTilemap(self, tmx_map):
        for x, y, surface in tmx_map.get_layer_by_name('Fondo').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites))

        for x, y, surface in tmx_map.get_layer_by_name('Solido').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites, self.full_collision))

        for x, y, surface in tmx_map.get_layer_by_name('Semi').tiles():
            Sprite(self, x*TILESIZE, y*TILESIZE, surface, (self.all_sprites, self.upper_collision))
        
        for objeto in tmx_map.get_layer_by_name('Jugador'):
            Player(self, objeto.x, objeto.y)

        
    # Método en el que se gestionan los eventos del juego a un alto nivel, se me ocurren eventos como darle al menú
    # de pausa, cambiar de nivel o el gameover.
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    # Llamamos al método update de los diferentes sprites de nuestro juego
    def update(self):
        self.all_sprites.update()
    # Dibujamos los diferentes sprites
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    # Bucle principal de nuestro juego
    def main(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        self.running = False
    # Por implementar
    def game_over(self):
        pass

    # Por implementar
    def intro_screen(self):
        pass
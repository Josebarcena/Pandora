from player import *
from config import *
from blocks import *

# Objeto que simila el juego, en este se realiza la lógica principal de nuestro juego
class Game(object):
    # Iniciamos el juego, creando la pantalla, variables que se usarán y el reloj
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 32)
        self.running = True
    # Mediante la matriz titlemap, definida en config.py, que representa el nivel, creamos los diferentes objetos de
    # bloques y el jugador.
    def createTilemap(self):
        for i, row in enumerate(titlemap):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i, BLUE)
                if column == "P":
                    Player(self, j, i)
    def new(self):
        self.playing = True
        # Variables en las que almacenaremos los distintos srpites del juego, como podemos ver podemos darles capas
        # a estos layers
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.createTilemap()
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
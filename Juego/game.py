from pygame import mixer
from player import *
from config import *
from blocks import *
from Gestor_recursos import *
from Main_menu import *
from Fase1 import *

# Objeto super de la clase state (fases o niveles del juego)




#Clase director que mira los states por los que pasa el juego
class Game(object):
    def __init__(self,screen, states, start_state):
        self.screen = screen
        self.done = False
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

        mixer.init()
        mixer.music.load(self.state.sound)
        mixer.music.set_volume(0.2)
        mixer.music.play()


    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self):
        mixer.music.stop()
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)
        self.screen.fill((0, 0, 0))
        mixer.music.load(self.state.sound)
        mixer.music.set_volume(0.2)
        mixer.music.play()

    def update(self, tick):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(tick)
    
    def draw(self):
        self.state.draw(self.screen)
    
    def run(self):
        while not self.done:
            tick = self.clock.tick(self.fps)
            self.event_loop()
            self.update(tick)
            self.draw()
            pygame.display.update()


'''
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
        
        self.level1 = GestorRecursos.LoadImage("Fases","fase11.tmx")
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
    '''
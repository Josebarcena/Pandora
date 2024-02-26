
from player import *
from config import *
from blocks import *
from Gestor_recursos import *
from Main_menu import *
from Fase1 import *

# Objeto super de la clase state (fases o niveles del juego)




#Clase director que mira los states por los que pasa el juego, administra los states
class Game(object):
    def __init__(self,screen, states, start_state):
        self.screen = screen
        self.done = False
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

        mixer.init()
        mixer.music.load("Sonidos\\"+ self.state.sound)
        mixer.music.set_volume(0.2)
        mixer.music.play()


    def event_loop(self): #el state es el que recibe los eventos y actua acorde a ellos
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self): #Cambiar de estado
        mixer.music.stop()
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)
        self.screen.fill((0, 0, 0)) #pintar negro al principio del state
        mixer.music.load("Sonidos\\"+ self.state.sound)
        mixer.music.set_volume(0.2)
        mixer.music.play()

    def update(self, tick): #actualiza el state de acuerdo a su funcion mirando si se dio la condicion de salir
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(tick)
    
    def draw(self): # se pinta el state con su funcion
        self.state.draw(self.screen)
    
    def run(self): # el bucle clasico de pygame con los fps
        while not self.done:
            tick = self.clock.tick(self.fps)
            self.event_loop()
            self.update(tick)
            self.draw()
            pygame.display.update()

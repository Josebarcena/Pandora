from blocks import *
from config import *
from control_pandora import *
from Fase import *
from Fase1 import *
from Gestor_recursos import *
from Menus import *
from player import *


#Clase director que mira los states por los que pasa el juego, administra los states
class Game(object):
    def __init__(self,screen, states, start_state):
        self.screen = screen
        self.done = False #condicion para el siguiente nivel del juego
        self.clock = pygame.time.Clock() #reloj 
        self.fps = FPS #los fps para el reloj
        self.states = states #los estados que existen en los juegos
        self.state_name = start_state #primer nivel
        self.state = self.states[self.state_name] #se selecciona ese nivel de los estados que se pasaron

        mixer.init()
        mixer.music.load("Sonidos\\"+ self.state.sound)
        mixer.music.set_volume(0.2)
        mixer.music.play()


    def event_loop(self): #el state es el que recibe los eventos y actua acorde a ellos
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self): #Cambiar de estado
        mixer.music.stop() #se para la musica
        next_state = self.state.next_state #se marca el siguiente estado a usar despues del cambio
        self.state.done = False #se resetea la condicion
        self.state_name = next_state #el estado al que vamos
        persistent = self.state.persist
        self.state = self.states[self.state_name] #igual que arriba
        self.state.startup()
        self.screen.fill((0, 0, 0)) #pintar negro al principio del state
        mixer.music.load("Sonidos\\"+ self.state.sound) #se carga el nuevo sonido
        mixer.music.set_volume(0.2) #el volumen
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

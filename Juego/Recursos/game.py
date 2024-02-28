from Niveles.blocks import *
from Recursos.config import *
from Personajes.control_pandora import *
from Niveles.Fase import *
from Niveles.Fase1 import *
from Recursos.Gestor_recursos import *
from Niveles.Menus import *
from Personajes.player import *


#Clase director que mira los states por los que pasa el juego, administra los states
class Game(object):
    def __init__(self,screen, start_state):
        self.screen = screen
        self.done = False #condicion para el siguiente nivel del juego
        self.clock = pygame.time.Clock() #reloj 
        self.fps = FPS #los fps para el reloj
        self.state = start_state #se selecciona ese nivel de los estados que se pasaron

        mixer.init()
        mixer.music.load("Recursos\\Sonidos\\"+ self.state.sound)
        mixer.music.set_volume(0.2)
        mixer.music.play()


    def event_loop(self): #el state es el que recibe los eventos y actua acorde a ellos
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self): #Cambiar de estado
        mixer.music.stop() #se para la musica
        self.state.done = False #se resetea la condicion
        self.state = self.state.next_state


        #Preparamos el siguiente nivel
        self.screen.fill((0, 0, 0)) #pintar negro al principio del state
        mixer.music.load("Recursos\\Sonidos\\"+ self.state.sound) #se carga el nuevo sonido
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

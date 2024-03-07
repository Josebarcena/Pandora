from Niveles.blocks import *
from Recursos.config import *
from Personajes.control_pandora import *
from Niveles.Fase import *
from Niveles.Fase1 import *
from Recursos.Gestor_recursos import *
from Niveles.Menus import *
from Personajes.player import *
from Recursos.Factory import *


#Clase director que mira los states por los que pasa el juego, administra los states
class Game(object):
    def __init__(self,screen, start_state):
        self.screen = screen
        self.clock = pygame.time.Clock() #reloj 
        self.fps = FPS #los fps para el reloj

        self.states = []
        self.state = Factory.create_state(start_state,self) #se selecciona ese nivel de los estados que se pasaron
        self.states.insert(0,self.state)
        mixer.init()
        mixer.music.load("Recursos\\Sonidos\\"+ self.state.sound)
        mixer.music.set_volume(0.2)
        mixer.music.play()


    def add_state(self, state, prio = False):
        if prio:
            self.states.insert(0,Factory.create_state(state,self))
        else:
            self.states.append(Factory.create_state(state,self))
        print(self.states)



    def unstack_state(self):
        print("ANTES UN: ",self.states)
        mixer.music.stop() #se para la musica
        self.state.done = False #se resetea la condicion
        self.states.pop(0)
        self.state = self.states[0]
        print("DESPUES UN: ",self.states)
        #Preparamos el siguiente nivel
        self.screen.fill((0, 0, 0)) #pintar negro al principio del state
        mixer.music.load("Recursos\\Sonidos\\"+ self.state.sound) #se carga el nuevo sonido
        mixer.music.set_volume(0.2) #el volumen
        mixer.music.play(-1)

    def flip_state(self): #Cambiar de estado
        print("ANTES FLIP: ",self.states)
        mixer.music.stop() #se para la musica
        self.state.done = False #se resetea la condicion
        print("DESPUES FLIP: ",self.states)
        self.state = self.states[0]

        #Preparamos el siguiente nivel
        mixer.music.load("Recursos\\Sonidos\\"+ self.state.sound) #se carga el nuevo sonido
        mixer.music.set_volume(0.2) #el volumen
        mixer.music.play(-1)

    def draw(self): # se pinta el state con su funcion
        self.state.draw(self.screen)
    
    def run(self): # el bucle clasico de pygame con los fps
        while not self.state.quit:
            tick = self.clock.tick(self.fps)
            events =  pygame.event.get()
            self.state.update(tick,events)
            self.draw()
            pygame.display.update()

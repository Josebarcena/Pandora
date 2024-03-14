import pygame.time
from Recursos.config import *
from Recursos.Gestor_recursos import *
from Niveles.Fase import *

class Splash(Base_state): #Clase splash para el principio del juego
    def __init__(self, director):
        super(Splash,self).__init__()
        self.font = pygame.font.Font(join(".", "Recursos", "Fuente", "FetteClassicUNZFraktur.ttf"), 72)
        self.title  = self.font.render("Pandora's Game", True, pygame.Color(160, 192, 222)) #Titulo y color del titulo
        self.title_rect = self.title.get_rect(center = self.screen_rect.center) #Posicion del titulo
        self.director = director
        self.time = 0 #Timer para finalizar el splash
        self.background = GestorRecursos.LoadImage("Imagenes","splash.jpg") #fondo del Splash
        self.sound = "splash.mp3" # Sonido de nintendo de fondo

    def update(self, tick, events): #se actualiza el timer con el tick
        for event in events:
            self.get_event(event)
        if self.done:
            self.director.add_state("MAIN_MENU")
            self.director.unstack_state()
        else:
            self.time += tick
            if self.time  >= 2500:
                self.done = True

    def draw(self, surface): # se dibuja el splash por pantalla
        surface.blit(self.background, (0,0))
        title_background_rect = pygame.Rect(self.title_rect.left - 10, self.title_rect.top - 10, self.title_rect.width + 20, self.title_rect.height + 20)
        pygame.draw.rect(surface, pygame.Color(25, 51, 77), title_background_rect)
        surface.blit(self.title,self.title_rect)

class Main_menu(Base_state):# Menu principal del juego
    def __init__(self, director):
        super(Main_menu, self).__init__()
        self.index = 0 #indice para la opcion marcada
        self.options = ["START", "QUIT"] #opciones
        self.director = director
        self.background = GestorRecursos.LoadImage("Imagenes","bg.png")
        self.font = pygame.font.SysFont("arialblack", 42) #fuente del sistema que se usara
        self.sound = "main_menu.mp3" 
        self.alpha = 250 # alpha para el efecto parpadeo
        GestorRecursos.create_xml([("score",0)])

    def render_text(self, index): # efecto parpadeo y marcado
        if index == self.index:
            color = pygame.Color("white")
            text = self.font.render(self.options[index], True, color)
            text.set_alpha(self.alpha)
        else:
            color = pygame.Color(115, 115, 115)
            text = self.font.render(self.options[index], True, color)
        return text
    
    def get_text_position(self, text, index): # se coloca la posicion del texto
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * (WIN_HEIGHT/10)))
        return text.get_rect(center = center)

    def handle_action(self): # dependiendo de la opcion elegida
        if self.index == 0:
            self.done = True
        elif self.index == 1:
            self.quit = True

    def update(self, tick, events): # se cambia el alpha con los frames
        for event in events:
            self.get_event(event)
        if self.done:
            self.director.add_state("FASE1")
            self.director.unstack_state()
        else:
            if self.alpha <= 120:
                self.alpha = 255
            else:
                self.alpha -= (tick * 0.1)

    def get_event(self, event): #dependiendo del evento de salir o si se pulso alguna tecla, se actualiza la fase
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if self.index == 0:
                    self.index = 1
                else:
                    self.index = 0
            if event.key == pygame.K_DOWN:
                if self.index == 0:
                    self.index = 1
                else:
                    self.index = 0
            elif event.key == pygame.K_RETURN: #si se pulsa enter se toma la opcion marcada
                self.handle_action()

    def draw(self, surface): #pintar el menu por pantalla cada frame
        surface.blit(self.background, (0,0))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))


class Game_over(Base_state): #COPIA Y PEGA DE LA CLASE MAIN MENU 
    def __init__(self, director):
            super(Game_over, self).__init__()
            self.index = 0
            self.options = ["Menu", "Quit"]
            self.director = director
            self.score = "SCORE: " + GestorRecursos.read_xml("score")
            self.background = GestorRecursos.LoadImage("Imagenes","game_over.jpg")
            self.font = pygame.font.SysFont("trajan", 42)
            self.sound = "game_over.mp3"
            self.alpha = 250
            self.time = 0

    def render_text(self, index):
        if index == self.index:
            color = pygame.Color("red")
            text = self.font.render(self.options[index], True, color)
            text.set_alpha(self.alpha)
        else:
            color = pygame.Color(115, 115, 115)
            text = self.font.render(self.options[index], True, color)
        return text
    
    def get_text_position(self, text, index): #SE CAMBIA AQUI PARA QUE ESTE LADEADO NO ENCIMA Y DEBAJO
        center = (self.screen_rect.center[0]- 100 + (index * (WIN_WIDTH/10)), self.screen_rect.center[1])
        return text.get_rect(center = center)

    def handle_action(self):
        if self.index == 0:
            self.done = True
        elif self.index == 1:
            self.quit = True

    def update(self, tick, events): #Se pone un timer por si no se pulsa nada en un rato largo
        for event in events:
            self.get_event(event)
        
        if self.done:
            self.director.add_state("MAIN_MENU")
            self.director.unstack_state()
        else:
            self.time += tick
            if self.time  >= 50500:
                self.done = True
            elif self.alpha <= 120:
                self.alpha = 255
            else:
                self.alpha -= (tick * 0.1)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if self.index == 0:
                    self.index = 1
                    self.index = 1
                else:
                    self.index = 0
            if event.key == pygame.K_RIGHT:
                if self.index == 0:
                    self.index = 1
                else:
                    self.index = 0
            elif event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        surface.blit(self.background, (0,0))
        text = self.font.render(self.score, True, pygame.Color("orange"))
        #RECUADRO PARA VER BIEN EL SCORE
        text_rect = text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT - 300))
        pygame.draw.rect(surface, pygame.Color(25, 51, 77), (text_rect.left - 50, text_rect.bottom - 20, text_rect.width*1.5, text_rect.height*1.2))
        surface.blit(text, (WIN_WIDTH/2 - 100 ,WIN_HEIGHT - 300))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))

class Pause_menu(Base_state):# Menu principal del juego
    def __init__(self, director):
        super(Pause_menu, self).__init__()
        self.index = 0 #indice para la opcion marcada
        self.options = ["RESUME", "QUIT"] #opciones
        self.director = director
        #self.background = GestorRecursos.LoadImage("Imagenes","pause.png")
        self.font = pygame.font.SysFont("arialblack", 42) #fuente del sistema que se usara
        self.sound = "pause.mp3" 
        self.alpha = 250 # alpha para el efecto parpadeo

    def render_text(self, index): # efecto parpadeo y marcado
        if index == self.index:
            color = pygame.Color("white")
            text = self.font.render(self.options[index], True, color)
            text.set_alpha(self.alpha)
        else:
            color = pygame.Color(115, 115, 115)
            text = self.font.render(self.options[index], True, color)
        return text
    
    def get_text_position(self, text, index): # se coloca la posicion del texto
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * (WIN_HEIGHT/10)))
        return text.get_rect(center = center)

    def handle_action(self): # dependiendo de la opcion elegida
        if self.index == 0:
            self.done = True
        elif self.index == 1:
            self.quit = True

    def update(self, tick, events): # se cambia el alpha con los frames
        for event in events:
            self.get_event(event)
        if self.done:
            self.director.unstack_state()
        else:
            if self.alpha <= 120:
                self.alpha = 255
            else:
                self.alpha -= (tick * 0.1)

    def get_event(self, event): #dependiendo del evento de salir o si se pulso alguna tecla, se actualiza la fase
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if self.index == 0:
                    self.index = 1
                else:
                    self.index = 0
            if event.key == pygame.K_DOWN:
                if self.index == 0:
                    self.index = 1
                else:
                    self.index = 0
            elif event.key == pygame.K_RETURN: #si se pulsa enter se toma la opcion marcada
                self.handle_action()

    def draw(self, surface): #pintar el menu por pantalla cada frame
        #surface.blit(self.background, (0,0))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))

class Win_menu(Base_state): #COPIA Y PEGA DE LA CLASE MAIN MENU 
    def __init__(self, director):
            super(Win_menu, self).__init__()
            self.index = 0
            self.options = ["Menu", "Quit"]
            self.director = director
            self.score = "SCORE: " + GestorRecursos.read_xml("score")
            self.background = GestorRecursos.LoadImage("Imagenes","win.png")
            self.font = pygame.font.SysFont("trajan", 42)
            self.sound = "win.mp3"
            self.alpha = 250
            self.time = 0

    def render_text(self, index):
        if index == self.index:
            color = pygame.Color("white")
            text = self.font.render(self.options[index], True, color)
            text.set_alpha(self.alpha)
        else:
            color = pygame.Color(115, 115, 115)
            text = self.font.render(self.options[index], True, color)
        return text
    
    def get_text_position(self, text, index): #SE CAMBIA AQUI PARA QUE ESTE LADEADO NO ENCIMA Y DEBAJO
        center = (self.screen_rect.center[0]- 100 + (index * (WIN_WIDTH/10)), self.screen_rect.center[1])
        return text.get_rect(center = center)

    def handle_action(self):
        if self.index == 0:
            self.done = True
        elif self.index == 1:
            self.quit = True

    def update(self, tick, events): #Se pone un timer por si no se pulsa nada en un rato largo
        for event in events:
            self.get_event(event)
        
        if self.done:
            self.director.add_state("MAIN_MENU")
            self.director.unstack_state()
        else:
            self.time += tick
            if self.time  >= 50500:
                self.done = True
            elif self.alpha <= 120:
                self.alpha = 255
            else:
                self.alpha -= (tick * 0.1)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if self.index == 0:
                    self.index = 1
                    self.index = 1
                else:
                    self.index = 0
            if event.key == pygame.K_RIGHT:
                if self.index == 0:
                    self.index = 1
                else:
                    self.index = 0
            elif event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        surface.blit(self.background, (0,0))
        text = self.font.render(self.score, True, pygame.Color("orange"))
        #RECUADRO PARA QUE SE VEA BIEN SCORE
        text_rect = text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT - 300))
        pygame.draw.rect(surface, pygame.Color(25, 51, 77), (text_rect.left - 50, text_rect.bottom - 20, text_rect.width*1.5, text_rect.height*1.2))
        
        surface.blit(text, (WIN_WIDTH/2 - 100 ,WIN_HEIGHT - 300))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
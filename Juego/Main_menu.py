from config import *
from Gestor_recursos import *
from pygame import mixer

class Base_state(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.SysFont(FONT, 72)
        self.background = GestorRecursos.LoadImage("Imagenes","splash.jpg")
    
    def startup(self,persistent):
        self.persist = persistent
    
    def get_event(self,event):
        pass
    
    def update(self, tick):
        pass

    def draw(self, surface):
        pass

class Splash(Base_state):
    def __init__(self):
        super(Splash,self).__init__()
        self.title  = self.font.render("Pandora's Game", True, pygame.Color("orange"))
        self.title_rect = self.title.get_rect(center = self.screen_rect.center)
        self.next_state = "MENU"
        self.time = 0
        self.sound = "Sonidos\\splash.mp3"

    def update(self, tick):
        self.time += tick
        if self.time  >= 5000:
            self.done = True
            mixer.music.stop()

    def draw(self, surface):
        surface.blit(self.background, (0,0))
        surface.blit(self.title,self.title_rect)

class Main_menu(Base_state):
    def __init__(self):
        super(Main_menu, self).__init__()
        self.index = 0
        self.options = ["START", "QUIT"]
        self.next_state = "FASE1"
        self.background = GestorRecursos.LoadImage("Imagenes","bg.png")
        self.font = pygame.font.SysFont("arial", 42)
        self.sound = "Sonidos\\main_menu.mp3"

    def render_text(self, index):
        if index == self.index:
            color = pygame.Color("lightgray") 
        else:
            color = pygame.Color("White")
        return self.font.render(self.options[index], True, color)
    
    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * (WIN_HEIGHT/10)))
        return text.get_rect(center = center)

    def handle_action(self):
        if self.index == 0:
            print("HOLA")
            self.done = True
            mixer.music.stop()
        elif self.index == 1:
            self.quit = True

    def get_event(self, event):
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
            elif event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        surface.blit(self.background, (0,0))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
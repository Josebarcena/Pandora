from config import *
from Gestor_recursos import *

class Base_state(object):
    def __init__(self):
        self.done = False # Condicion final
        self.quit = False # Condicion cierre juego
        self.next_state = None #Siguiente fase

        self.screen_rect = pygame.display.get_surface().get_rect() #Tamaño ventana
        self.persist = {}
        self.font = pygame.font.Font("Fuente\\FetteClassicUNZFraktur.ttf", 72)
        
    
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
        self.title  = self.font.render("Pandora's Game", True, pygame.Color(160, 192, 222))
        self.title_rect = self.title.get_rect(center = self.screen_rect.center)
        self.next_state = "MENU"
        self.time = 0
        self.background = GestorRecursos.LoadImage("Imagenes","splash.jpg")
        self.sound = "splash.mp3"

    def update(self, tick):
        self.time += tick
        if self.time  >= 2500:
            self.done = True

    def draw(self, surface):
        surface.blit(self.background, (0,0))
        title_background_rect = pygame.Rect(self.title_rect.left - 10, self.title_rect.top - 10, self.title_rect.width + 20, self.title_rect.height + 20)
        pygame.draw.rect(surface, pygame.Color(25, 51, 77), title_background_rect)
        surface.blit(self.title,self.title_rect)

class Main_menu(Base_state):
    def __init__(self):
        super(Main_menu, self).__init__()
        self.index = 0
        self.options = ["START", "QUIT"]
        self.next_state = "FASE1"
        self.background = GestorRecursos.LoadImage("Imagenes","bg.png")
        self.font = pygame.font.SysFont("arialblack", 42)
        self.sound = "main_menu.mp3"
        self.alpha = 250

    def render_text(self, index):
        if index == self.index:
            color = pygame.Color("white")
            text = self.font.render(self.options[index], True, color)
            text.set_alpha(self.alpha)
        else:
            color = pygame.Color(115, 115, 115)
            text = self.font.render(self.options[index], True, color)
        return text
    
    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * (WIN_HEIGHT/10)))
        return text.get_rect(center = center)

    def handle_action(self):
        if self.index == 0:
            self.done = True
        elif self.index == 1:
            self.quit = True

    def update(self, tick):
        if self.alpha <= 120:
            self.alpha = 255
        else:
            self.alpha -= (tick * 0.1)

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


class Game_Over(Base_state):
    def __init__(self):
            super(Game_Over, self).__init__()
            self.index = 0
            self.options = ["Menu", "Quit"]
            self.next_state = "MENU"
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
    
    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0]- 100 + (index * (WIN_WIDTH/10)), self.screen_rect.center[1])
        return text.get_rect(center = center)

    def handle_action(self):
        if self.index == 0:
            self.done = True
        elif self.index == 1:
            self.quit = True

    def update(self, tick):
        self.time += tick
        if self.time  >= 12500:
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
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
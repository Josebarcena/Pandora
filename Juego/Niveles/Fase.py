from Recursos.config import *

class Base_state(object): # Objeto super de la clase state ( TODAS LAS fases o niveles del juego)

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
    
    def update(self, tick): # lo que se tiene que actualizar acorde a los ticks del juego
        pass

    def draw(self, surface):
        pass


class Fase(Base_state):
    def __init__(self): # Definimos la superclase de las fases jugables
        super(Fase,self).__init__()

        self.stage_image = None
        
        self.next_state = None

        self.sound = None
        self.level = None
    

    def createTilemap(self, tmx_map):
       pass

    def get_event(self, event):
        pass    

    def screen_check(self, sprites): #Movimiento de camara que mueve todos los pixeles con el jugador, se define aqui porque es comun a todos los niveles
        if self.player.rect.x <= SCROLL_LIMIT_X:
            self.player.rect.x = SCROLL_LIMIT_X
            for sprite in sprites:
                sprite.rect.x += PLAYER_SPEED
        elif self.player.rect.x >= WIN_WIDTH - SCROLL_LIMIT_X:
            self.player.rect.x = WIN_WIDTH - SCROLL_LIMIT_X
            for sprite in sprites:
                sprite.rect.x -= PLAYER_SPEED
        if self.player.rect.y <= SCROLL_LIMIT_Y:
            self.player.rect.y = SCROLL_LIMIT_Y
            for sprite in sprites:
                sprite.rect.y += PLAYER_SPEED
        elif self.player.rect.y >= WIN_HEIGHT - SCROLL_LIMIT_Y:
            self.player.rect.y = WIN_HEIGHT - SCROLL_LIMIT_Y
            for sprite in sprites:
                sprite.rect.y -= PLAYER_SPEED


    def draw(self, surface): #pintar la fase
        pass

    def collide_Fase(self, player): # chequea las colisiones con los bloques de las fases
       pass

    def gameover(self): # se le llama para indicar game_over en el nivel (QUEDA VER COMO RESETEAR EL NIVEL)
        pass
    
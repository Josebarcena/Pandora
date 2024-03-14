from Recursos.config import *
from Recursos.Gestor_recursos import *
class Base_state(object): # Objeto super de la clase state ( TODAS LAS fases o niveles del juego)

    def __init__(self):
        self.done = False # Condicion final
        self.quit = False # Condicion cierre juego
        self.next_state = None #Siguiente fase
        self.sound = None
        self.screen_rect = pygame.display.get_surface().get_rect() #Tamaño ventana
        
    
    def get_event(self,event):
        pass
    
    def update(self, tick, events): # lo que se tiene que actualizar acorde a los ticks del juego
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

    # Actualización del scoll de pantalla, antes se movían todos los sprites del mapa a la velocidad del jugador, ahora
    # se mueve a la velocidad a la que vaya el personaje
    def screen_check(self, sprites, player, stage):
        dx = 0
        dy = 0
        if player.rect.x > SCROLL_LIMIT_X_RIGHT and stage.rect.right > WIN_WIDTH:
            dx = player.rect.x - SCROLL_LIMIT_X_RIGHT
        elif player.rect.x < SCROLL_LIMIT_X_LEFT and stage.rect.left < 0:
            dx = player.rect.x - SCROLL_LIMIT_X_LEFT
        if player.rect.y > SCROLL_LIMIT_Y_BOTTOM and stage.rect.bottom > WIN_HEIGHT:
            dy = player.rect.y - SCROLL_LIMIT_Y_BOTTOM
        elif player.rect.y < SCROLL_LIMIT_Y_TOP and stage.rect.top < 0:
            dy = player.rect.y - SCROLL_LIMIT_Y_TOP

        # Aplicar el desplazamiento a todos los sprites
            
        if dx < stage.rect.left:
            dx = stage.rect.left
        elif dx > stage.rect.right - WIN_WIDTH:
            dx = stage.rect.right - WIN_WIDTH
        if dy < stage.rect.top:
            dy = stage.rect.top
        elif dy > stage.rect.bottom - WIN_HEIGHT:
            dy = stage.rect.bottom - WIN_HEIGHT

        for sprite in sprites:
            sprite.rect.x -= dx
            sprite.rect.y -= dy


    def draw(self, surface): #pintar la fase
        pass

    def collide_Fase(self, player): # chequea las colisiones con los bloques de las fases
       pass

    def gameover(self): # se le llama para indicar game_over en el nivel (QUEDA VER COMO RESETEAR EL NIVEL)
        GestorRecursos.change_xml([("score",self.player.score)])
        self.director.add_state("GAME_OVER")
        self.done = True
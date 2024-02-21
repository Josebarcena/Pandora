import pygame
from Ajustes import *
from Pandora import *

class Fase:
    def __init__(self, tmx_mapa):
        self.superficie_ventana = pygame.display.get_surface()
        self.cualquier_sprite = pygame.sprite.Group()
        self.colision_completa = pygame.sprite.Group() 
        self.colision_superior = pygame.sprite.Group()
        self.dibujar(tmx_mapa)

    def dibujar(self, tmx_mapa):
        for x, y, superficie in tmx_mapa.get_layer_by_name('Fondo').tiles():
            Sprite((x*TAMAÑO_TILE*ESCALA_BASE, y*TAMAÑO_TILE*ESCALA_BASE), superficie, (self.cualquier_sprite))

        for x, y, superficie in tmx_mapa.get_layer_by_name('Solido').tiles():
            Sprite((x*TAMAÑO_TILE*ESCALA_BASE, y*TAMAÑO_TILE*ESCALA_BASE), superficie, (self.cualquier_sprite, self.colision_completa))

        for x, y, superficie in tmx_mapa.get_layer_by_name('Semi').tiles():
            Sprite((x*TAMAÑO_TILE*ESCALA_BASE, y*TAMAÑO_TILE*ESCALA_BASE), superficie, (self.cualquier_sprite, self.colision_superior))
        
        for objeto in tmx_mapa.get_layer_by_name('Jugador'):
            Jugador((objeto.x*ESCALA_BASE, objeto.y*ESCALA_BASE), self.cualquier_sprite, self.colision_completa, self.colision_superior)

    def run(self, dt):
        self.cualquier_sprite.update(dt)
        #self.superficie_ventana.fill('grey')
        self.cualquier_sprite.draw(self.superficie_ventana)

    def eventos(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclasPulsadas = pygame.key.get_pressed()
        if teclasPulsadas[pygame.K_ESCAPE]:
            return True 



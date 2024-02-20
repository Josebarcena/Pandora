import pygame
from Ajustes import *


class Jugador(pygame.sprite.Sprite):
    def __init__(self, posicion, groups, colision_completa, colision_superior):
        super().__init__(groups)
        self.image = pygame.Surface((16, 16))
        self.image.fill('green')

        
        self.rect = self.image.get_rect(topleft = posicion)
        self.rect_anterior = self.rect.copy()

        self.direccion = vector(0,0)
        self.velocidad = 100

        self.colision_completa = colision_completa
        self.colision_superior = colision_superior
        print(self.colision_completa)
        

    def input(self):
        teclas = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if teclas[pygame.K_RIGHT]:
            input_vector.x += 1
        if teclas[pygame.K_LEFT]:
            input_vector.x -= 1
        if teclas[pygame.K_UP]:
            input_vector.y -= 1
        if teclas[pygame.K_DOWN]:
            input_vector.y += 1

        self.direccion = input_vector.normalize() if input_vector else input_vector
            

    def movimiento(self, dt):
        self.rect.x += self.direccion.x * self.velocidad * dt
        self.colisiones('horizontal')
        self.rect.y += self.direccion.y * self.velocidad * dt
        self.colisiones('vertical')

    def colisiones(self, eje):
        for sprite in self.colision_completa:
            if sprite.rect.colliderect(self.rect):
                if eje == 'horizontal':
                    #izquierda
                    if self.rect.left <= sprite.rect.right and self.rect_anterior.left >= sprite.rect_anterior.right :
                        self.rect.left = sprite.rect.right
                    #derecha
                    if self.rect.right >= sprite.rect.left and self.rect_anterior.right <= sprite.rect_anterior.left :
                        self.rect.right = sprite.rect.left
                else:
                    #arriba
                    if self.rect.top <= sprite.rect.bottom and self.rect_anterior.bottom >= sprite.rect_anterior.top :
                        self.rect.top = sprite.rect.bottom
                    #abajo
                    if self.rect.bottom >= sprite.rect.top and self.rect_anterior.bottom <= sprite.rect_anterior.top :
                        self.rect.bottom = sprite.rect.top

        for sprite in self.colision_superior:
            if sprite.rect.colliderect(self.rect):
                if eje == 'horizontal':
                    pass
                else:
                    #abajo
                    if self.rect.bottom >= sprite.rect.top and self.rect_anterior.bottom <= sprite.rect_anterior.top :
                        self.rect.bottom = sprite.rect.top

    def update(self, dt):
        self.rect_anterior = self.rect.copy()
        self.input()
        self.movimiento(dt)
        

class Sprite(pygame.sprite.Sprite):
        def __init__(self, posicion, superficie, groups):
            super().__init__(groups)
            self.image = superficie
            self.rect = self.image.get_rect(topleft = posicion)
            self.group = groups
            self.rect_anterior = self.rect.copy()


class Fase:
    def __init__(self, tmx_mapa):
        self.superficie_ventana = pygame.display.get_surface()
        self.cualquier_sprite = pygame.sprite.Group()
        self.colision_completa = pygame.sprite.Group() 
        self.colision_superior = pygame.sprite.Group()
        self.dibujar(tmx_mapa)

    def dibujar(self, tmx_mapa):
        for x, y, superficie in tmx_mapa.get_layer_by_name('Fondo').tiles():
            Sprite((x*TAMAÑO_TILE, y*TAMAÑO_TILE), superficie, (self.cualquier_sprite))

        for x, y, superficie in tmx_mapa.get_layer_by_name('Solido').tiles():
            Sprite((x*TAMAÑO_TILE, y*TAMAÑO_TILE), superficie, (self.cualquier_sprite, self.colision_completa))

        for x, y, superficie in tmx_mapa.get_layer_by_name('Semi').tiles():
            Sprite((x*TAMAÑO_TILE, y*TAMAÑO_TILE), superficie, (self.cualquier_sprite, self.colision_superior))
        
        for objeto in tmx_mapa.get_layer_by_name('Jugador'):
            Jugador((objeto.x, objeto.y), self.cualquier_sprite, self.colision_completa, self.colision_superior)

    def run(self, dt):
        self.cualquier_sprite.update(dt)
        self.superficie_ventana.fill('grey')
        self.cualquier_sprite.draw(self.superficie_ventana)

    def eventos(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclasPulsadas = pygame.key.get_pressed()
        if teclasPulsadas[pygame.K_ESCAPE]:
            return True 



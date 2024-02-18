from ajustes import *


class Jugador(pygame.sprite.Sprite):
    def __init__(self, posicion, groups, colision_completa, colision_superior):
        super().__init__(groups)
        self.image = pygame.Surface((16, 16))
        self.image.fill('green')

        
        self.rect = self.image.get_rect(topleft = posicion)
        self.rect_anterior = self.rect.copy()

        self.direccion = vector(0,0)
        self.velocidad = 200

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
        
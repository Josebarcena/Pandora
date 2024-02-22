import pygame
import constantes

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        # Primero invocamos al constructor de la clase padre
        pygame.sprite.Sprite.__init__(self)
        # Se carga la hoja
        self.hoja = pygame.image.load("images/sprites/pandora/SpriteSheet/Warrior_SheetnoEffect.png")
        self.hoja = self.hoja.convert_alpha()
        # El rectangulo y la posicion que tendra
        self.rect = pygame.Rect((7,25), (30, 40))
        self.posicionx = 100
        self.posiciony = 100
        # El movimiento que esta realizando
        self.movimiento = constantes.QUIETO

    def cambiar_movimiento(self, direccion):
        self.movimiento = direccion

    def dibujar(self, pantalla):
        if self.movimiento == constantes.IZQUIERDA:
            pantalla.blit(
                self.hoja.subsurface(
                    (self.posicionx, self.posiciony, 30, 40)),
                (self.posicionx, self.posiciony))
        elif self.movimiento == constantes.DERECHA:
            pantalla.blit(
                pygame.transform.flip(
                    self.hoja.subsurface(
                        (self.posicionx, self.posiciony, 30, 40)),
                    True, False),
                (self.posicionx, self.posiciony))

    def update(self):
        # Si vamos a la izquierda
        if self.movimiento == constantes.IZQUIERDA:
            # Actualizamos la posicion
            self.posicionx -= 2
            # Su siguiente movimiento (si no se pulsa mas) sera estar quieto
            self.movimiento = constantes.QUIETO
        # Si vamos a la derecha
        elif self.movimiento == constantes.DERECHA:
            # Actualizamos la posicion
            self.posicionx += 2
            # Su siguiente movimiento (si no se pulsa mas) sera estar quieto
            self.movimiento = constantes.QUIETO

import pygame
import sys

ALTURA, ANCHURA = 640, 480
RAQUETA_VELOCIDAD = 20


class OBJETO(pygame.sprite.Sprite):

    def __init__(self, IMAGE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMAGE).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()


class RAQUETA(OBJETO):

    def __init__(self, IMAGE):
        OBJETO.__init__(self, IMAGE)
        self.rect.bottom = ANCHURA
        self.rect.left = (ALTURA - self.image.get_width()) / 2

    def MoverIzquierda(self):
        if self.rect.left > 0:
            self.rect.move_ip(-RAQUETA_VELOCIDAD, 0)

    def MoverDerecha(self):
        if self.rect.right < ALTURA:
            self.rect.move_ip(RAQUETA_VELOCIDAD, 0)


class MOTOR:
    _titulo = "jeu de casse-ladrillos"
    _longitud = 400
    _anchura = 400
    _fondo = (255, 255, 255)

    _ventana = pygame.display.set_mode((ALTURA, ANCHURA))
    pygame.display.set_caption(_titulo)
    pygame.key.set_repeat(400, 30)
    pygame.display.set_caption('Juego de rompe ladrillos')
    _reloj = pygame.time.Clock()

    _lista = pygame.sprite.Group()
    _raqueta = RAQUETA("RAQUETA.png")
    _lista.add(_raqueta)
    print(_raqueta)

    def BUCLE_DE_JUEGO(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Salida")
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self._raqueta.MoverIzquierda()
                    elif event.key == pygame.K_2:
                        self._raqueta.MoverDerecha()

            self._ventana.fill((0, 0, 0))
            self._lista.draw(self._ventana)
            self._lista.update()
            self._reloj.tick(60)
            pygame.display.flip()

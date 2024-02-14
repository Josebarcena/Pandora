import pygame

ALTURA, ANCHURA = 640, 480
PELOTA_ALTURA, PELOTA_ANCHURA = 16, 16
LADRILLO_ALTURA, LADRILLO_ANCHURA = 64, 16
RAQUETA_ALTURA, RAQUETA_ANCHURA = 64, 16
RAQUETA_VELOCIDAD = 20
PELOTA_VELOCIDAD = 2


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


class LADRILLO(OBJETO):

    def __init__(self, IMAGE, x, y):
        OBJETO.__init__(self, IMAGE)
        self.rect.x, self.rect.y = x, y


class PELOTA(OBJETO):

    def __init__(self, IMAGE, VELOCIDAD_X, VELOCIDAD_Y):
        OBJETO.__init__(self, IMAGE)
        self.rect.bottom = ANCHURA - RAQUETA_ALTURA
        self.rect.left = ANCHURA / 2
        self.VELOCIDAD_X = VELOCIDAD_X
        self.VELOCIDAD_Y = VELOCIDAD_Y

    def update(self):
        self.rect = self.rect.move(self.VELOCIDAD_X, self.VELOCIDAD_Y)

        if self.rect.x > ALTURA - self.image.get_width() or self.rect.x < 0:
            self.VELOCIDAD_X *= -1
        if self.rect.y < 0:
            self.VELOCIDAD_Y *= -1
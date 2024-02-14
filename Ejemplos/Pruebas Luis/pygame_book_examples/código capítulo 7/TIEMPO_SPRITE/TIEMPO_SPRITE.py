import sys, pygame

COLOR_ROJO = 255, 0, 0
COLOR_AZUL = 0, 0, 255

# ----------------
#
# clase CUADRADO
#
# ----------------
class CUADRADO(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill(COLOR_ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

        self.DESPLAZAMIENTO = 3

    def update(self):
        self.rect.x += self.DESPLAZAMIENTO

        if  self.rect.x >= 320:
            self.rect.x = 320
            self.DESPLAZAMIENTO = -3
        elif  self.rect.x <= 0:
            self.rect.x = 0
            self.DESPLAZAMIENTO = 3

# ----------------
#
# Código
#
# ----------------
pygame.init()
screen = pygame.display.set_mode((400, 400))
background = pygame.Surface(screen.get_size())
background.fill(COLOR_AZUL)
screen.blit(background, (0, 0))

pygame.display.set_caption("El cuadrado que rebota")

reloj = pygame.time.Clock()

XX = 300
DESPLAZAMIENTO = 3

all_sprites = pygame.sprite.Group()
cuadrado = CUADRADO()
all_sprites.add(cuadrado)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    all_sprites.clear(screen, background)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()

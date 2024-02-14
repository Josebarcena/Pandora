import pygame;
import sys

WIDTH = 1920
HEIGHT = 1080

posX = 1
posY = 909
velocidadX = 3
velocidadY = 3
gravity = 5


def Escenario():
    grounded = False
    jugador = pygame.draw.rect(screen,(0,0,255),(posX,posY,90,90))
    base = pygame.draw.line(screen, (0,255,0),[0,1000], [1920,1000],5)
    collide = pygame.Rect.colliderect(jugador,base)
    if collide:
        grounded = True
    else:
        grounded = False

    print(grounded)

    pygame.draw.line(screen, (255,0,0),[300,880], [500,880],5)
    pygame.draw.line(screen, (255,0,0),[700,680], [900,680],5)
    pygame.draw.line(screen, (255,0,0),[800,480], [1080,480],5)
    pygame.draw.line(screen, (255,0,0),[1080,680], [1300,680],5)
    pygame.draw.line(screen, (255,0,0),[1350,880], [1500,880],5)


pygame.init()
size = (WIDTH,HEIGHT)
running = True
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        posY -= velocidadY
    if pressed[pygame.K_DOWN]:
        posY += velocidadY
    if pressed[pygame.K_LEFT]:
        posX -= velocidadX
    if pressed[pygame.K_RIGHT]:
        posX += velocidadX
    #fondo
    #bg = pygame.image.load("bg.jpeg")      
    #screen.blit(bg, (0,0))


    #escenario
    Escenario()
    
    pygame.display.update()
    clock.tick(60)




    
from CLASES import *
import pygame, sys
pygame.init()

VENTANA = pygame.display.set_mode((ALTURA, ANCHURA))
pygame.key.set_repeat(400, 30)
pygame.display.set_caption('Juego rompe labrillos')
reloj = pygame.time.Clock()
marcador = 0

LISTA_GLOBAL_SPRITES = pygame.sprite.Group()
LISTA_RAQUETA_LADRILLOS = pygame.sprite.Group()
LISTA_LADRILLOS = pygame.sprite.Group()

pelota = PELOTA('PELOTA.png', PELOTA_VELOCIDAD, -PELOTA_VELOCIDAD)
LISTA_GLOBAL_SPRITES.add(pelota)

raqueta = RAQUETA('RAQUETA.png')
LISTA_GLOBAL_SPRITES.add(raqueta)
LISTA_RAQUETA_LADRILLOS.add(raqueta)

for i in range(8):
    for j in range(8):
        ladrillo = LADRILLO('LADRILLO.png', (i+1)*LADRILLO_ALTURA + 5, (j+3)*LADRILLO_ANCHURA + 5)
        LISTA_GLOBAL_SPRITES.add(ladrillo)
        LISTA_RAQUETA_LADRILLOS.add(ladrillo)
        LISTA_LADRILLOS.add(ladrillo)

while True:
    if pelota.rect.y > ANCHURA:
        print ("Perdido:)")
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                raqueta.MoverIzquierda()
            elif event.key == pygame.K_RIGHT:
                raqueta.MoverDerecha()

    REBOTES = pygame.sprite.spritecollide(pelota, LISTA_RAQUETA_LADRILLOS, False)
    if REBOTES:
        RECT = REBOTES[0].rect
        if RECT.left > pelota.rect.left or pelota.rect.right < RECT.right:
            pelota.VELOCIDAD_Y *= -1
        else:
            pelota.VELOCIDAD_X *= -1

        if pygame.sprite.spritecollide(pelota, LISTA_LADRILLOS, True):
            marcador += len(REBOTES)
            print( "%s puntos" % marcador)

        if len(LISTA_LADRILLOS) == 0:
          print("Ganado, bravo :)")
          pygame.quit()
          sys.exit()

    VENTANA.fill((0, 0, 0))
    LISTA_GLOBAL_SPRITES.draw(VENTANA)

    LISTA_GLOBAL_SPRITES.update()
    reloj.tick(60)
    pygame.display.flip()
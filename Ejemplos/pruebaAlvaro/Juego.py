import pygame
import sys
import constantes
from Pandora import Jugador
from pygame.locals import *

pygame.init()

# Pantalla
W, H = 1280, 720
PANTALLA = pygame.display.set_mode((W, H))
RELOJ = pygame.time.Clock()
pygame.display.set_caption(constantes.nombre_juego)

# Cargar imágenes
icono = pygame.image.load("images/4614158.png")
fondo = pygame.image.load("images/fondo2.jpg").convert()

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (int(w*scale), int(h*scale)))
    return new_image

# Cargar animaciones del jugador
animaciones_idle = []
for i in range(6):
    img_idle = pygame.image.load(f"images//sprites//pandora//Individual Sprite//idle//Warrior_Idle_{i}.png")
    img_idle = escalar_img(img_idle, constantes.ESCALA_PERSONAJE)
    animaciones_idle.append(img_idle)

animaciones_run = []
for i in range(8):
    img_run = pygame.image.load(f"images//sprites//pandora//Individual Sprite//Run//Warrior_Run_{i}.png")
    img_run = escalar_img(img_run, constantes.ESCALA_PERSONAJE)
    animaciones_run.append(img_run)

jugador = Jugador(animaciones_idle, animaciones_run)

# Establecer icono y fondo
pygame.display.set_icon(icono)
PANTALLA.blit(fondo, (0, 0))

# Bucle del juego
run = True
while run:
    # Controlar el frame rate
    RELOJ.tick(constantes.FPS)

    PANTALLA.fill(constantes.AZUL)

    # Eventos del jugador
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                jugador.cambiar_movimiento(constantes.IZQUIERDA)
            elif event.key == K_RIGHT:
                jugador.cambiar_movimiento(constantes.DERECHA)

    # Actualizar jugador
    jugador.update()

    # Dibujar jugador en la pantalla
    jugador.dibujar(PANTALLA)

    # Actualizar pantalla
    pygame.display.update()

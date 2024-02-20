import pygame
import sys
import constantes
from personaje import Personaje
from pygame.locals import *

pygame.init()

# Pantalla
W, H = 1280, 720
PANTALLA = pygame.display.set_mode((W, H))
RELOJ = pygame.time.Clock()
pygame.display.set_caption(constantes.nombre_juego)

# Cargar imagenes
icono = pygame.image.load("images/4614158.png")
fondo = pygame.image.load("images/fondo2.jpg").convert()

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w*scale, h*scale))
    return new_image

animaciones_idle = []
for i in range(6):
    img_idle = pygame.image.load(f"images//sprites//pandora//Individual Sprite//idle//Warrior_Idle_{i}.png")
    img_idle = escalar_img(img_idle, constantes.ESCALA_PERSONAJE)
    animaciones_idle.append(img_idle)

# Cargar imágenes para la animación de correr (RUN)
animaciones_run = []
for i in range(8):
    img_run = pygame.image.load(f"images//sprites//pandora//Individual Sprite//Run//Warrior_Run_{i}.png")
    img_run = escalar_img(img_run, constantes.ESCALA_PERSONAJE)
    animaciones_run.append(img_run)

animaciones_jump = []
for i in range(3):
    img_jump = pygame.image.load(f"images//sprites//pandora//Individual Sprite//Jump//Warrior_Jump_{i}.png")
    img_run = escalar_img(img_jump, constantes.ESCALA_PERSONAJE)
    animaciones_jump.append(img_run)

jugador = Personaje(50, 50, animaciones_idle, animaciones_run)

# Establecer iconos y background
pygame.display.set_icon(icono)
x = 0
PANTALLA.blit(fondo, (0,0))

# Variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# Bucle del juego
run = True
while run:
    # Controlar el frame rate
    RELOJ.tick(constantes.FPS)

    PANTALLA.fill(constantes.AZUL)

    # Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    # Evento de movimiento de jugador
    if mover_derecha:
        delta_x = constantes.velocidad
        jugador.set_animacion_run()
    elif mover_izquierda:
        delta_x = -constantes.velocidad
        jugador.set_animacion_run()
    elif mover_arriba:
        delta_y = -constantes.velocidad
    elif mover_abajo:
        delta_y = constantes.velocidad
    else:
        jugador.set_animacion_idle()

    # Mover jugador
    jugador.movimiento(delta_x, delta_y)

    # Update de la imagen
    jugador.update()

    # Update del movimiento
    jugador.update_run()

    # Dibujar personaje
    jugador.dibujar(PANTALLA)

    for event in pygame.event.get():
        # Evento de salirse del juego
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            elif event.key == pygame.K_d:
                mover_derecha = True
            elif event.key == pygame.K_w:
                mover_arriba = True
            elif event.key == pygame.K_s:
                mover_abajo = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            elif event.key == pygame.K_d:
                mover_derecha = False
            elif event.key == pygame.K_w:
                mover_arriba = False
            elif event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()
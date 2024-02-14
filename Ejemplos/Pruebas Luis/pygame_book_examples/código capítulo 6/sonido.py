import pygame
import sys

pygame.init()
pygame.mixer.init()

# COLORES
COLOR_BLANCO = pygame.Color(255, 255, 255)

# VENTANA DE 400 POR 400
PANTALLA = pygame.display.set_mode((400, 400))
PANTALLA.fill(COLOR_BLANCO)
pygame.display.set_caption("Capítulo 5, del sonido")

CONTINUAR = True

# FONDO SONORO
SIFFLEMENT = pygame.mixer.music.load("silbido.ogg")
pygame.mixer.music.play(1, 0.0)

# EFECTOS SONOROS
GALLO = pygame.mixer.Sound("gallo.ogg")
CUERVO = pygame.mixer.Sound("cuervo.ogg")
BICI = pygame.mixer.Sound("timbre.ogg")

# BUCLE DE JUEGO
while CONTINUAR:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CONTINUAR = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                CONTINUAR = False
            elif event.key == pygame.K_o:
                GALLO.play()
            elif event.key == pygame.K_c:
                CUERVO.play()
            elif event.key == pygame.K_v:
                BICI.play()
            elif event.key == pygame.K_DOWN:
                VOLUMEN = pygame.mixer.music.get_volume() - 0.1
                pygame.mixer.music.set_volume(VOLUMEN)
                GALLO.set_volume(VOLUMEN)
                CUERVO.set_volume(VOLUMEN)
                BICI.set_volume(VOLUMEN)
            elif event.key == pygame.K_UP:
                VOLUMEN = pygame.mixer.music.get_volume() + 0.1
                pygame.mixer.music.set_volume(VOLUMEN)
                GALLO.set_volume(VOLUMEN)
                CUERVO.set_volume(VOLUMEN)
                BICI.set_volume(VOLUMEN)

    pygame.display.flip()

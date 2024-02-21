import pygame, sys
from pygame.math import Vector2 as vector

ANCHO_VENTANA, ALTO_VENTANA  = 1280, 720
FRAMES_JUMP = 25
TAMAÑO_TILE = 16
VELOCIDAD_ANIMACION = 6
GRAVITY = 2
JUMP_HEIGHT = 48
PANDORA_SPEED = 48
ESCALA_BASE = 3

# Limites en el eje x e y (el limite de la izq es SCROLL_LIMIT_X y el de la derecha será WIN_WIDTH - SCROLL_LIMIT_X)
SCROLL_LIMIT_X = 106
SCROLL_LIMIT_Y = 80

# capas
CAPAS = {
    'Fondo': 0,
    'Solido':1,
    'Semi':2,
    'Jugador':3
}
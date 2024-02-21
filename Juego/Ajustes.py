import pygame, sys
from pygame.math import Vector2 as vector

ANCHO_VENTANA, ALTO_VENTANA  = 1280, 720
TAMAÑO_TILE = 16
VELOCIDAD_ANIMACION = 6
GRAVITY = 2
JUMP_HEIGHT = 13
PANDORA_SPEED = 4
ESCALA_BASE = 3.5

# capas
CAPAS = {
    'Fondo': 0,
    'Solido':1,
    'Semi':2,
    'Jugador':3
}
import sys
import pygame
from pygame import mixer
#DECLARACIÓN DE VARIABLES
CHUNK_LOAD_RADIUS = 1
CHUNK_SIZE = 26
SCALE = 3
DEBUG = False
# Tamaño de la ventana
WIN_WIDTH = 1280
WIN_HEIGHT = 720
# Tamaño de los cubos usados y FPS que usará el reloj del programa
TILESIZE = 16
FPS = 60
# Limites en el eje x e y (el limite de la izq es SCROLL_LIMIT_X y el de la derecha será WIN_WIDTH - SCROLL_LIMIT_X)
SCROLL_LIMIT_X = 106 * SCALE
SCROLL_LIMIT_Y = 80 * SCALE

# Fuerza de la gravedad, velocidad del dash, numero de frames que dura el salto y dash
GRAVITY = 3 * SCALE
JUMPING_SPEED = 3 * SCALE
DASH_SPEED = 8 * SCALE
FRAMES_JUMP = 25
FRAMES_DASH = 10

# Diferentes capas para el juego
PLAYER_LAYER = 2
BLOCK_LAYER = 1
PLAYER_SPEED = 3 * SCALE

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Diferentes configuraciones del mapa a usar en las pruebas. Las B serán los bloques, los puntos se ignoran y la P será
# la posición del jugador
titlemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B..................................BBBBB',
    'B.........................BBBBB.BBB....B',
    'B........................B.............B',
    'B.......................B..............B',
    'B............BBBB..BBBBB...............B',
    'B...........B..........................B',
    'B..........B...........................B',
    'B..P......B............................B',
    'B........B.............................B',
    'B.......B..............................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]

titlemap2 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B......................................B',
    'B......................................B',
    'B...P..................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B..BBB.............BBBBBBBB..BBBBBB....B',
    'B....B.................B..........B....B',
    'B......................B..........B....B',
    'B......................B...............B',
    'B....B.................B......BB.......B',
    'B....B.................BBBB...BB.......B',
    'B....BBBB..BBB................BB.......B',
    'B............B................BB.......B',
    'B............B................BB.......B',
    'B..........BBB..............BB..BB.....B',
    'B...........................BB..BB.....B',
    'B......................................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]
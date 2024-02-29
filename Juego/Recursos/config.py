import sys
import pygame
from pygame import mixer

#DECLARACIÓN DE VARIABLES
CHUNK_LOAD_RADIUS = 1
CHUNK_SIZE = 26
SCALE = 3

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
ENEMY_LAYER = 2
PLAYER_LAYER = 3
BLOCK_LAYER = 1
PLAYER_SPEED = 3 * SCALE

# Cantidad de pixeles para que los enemigos cambien al estado agro
PIXELS_ENEMIES_AGRO_X = 400
PIXELS_ENEMIES_AGRO_Y = 150

# Variables para controlar la cantidad de frames que dura el salto de los enemigos, velocidades de salto y velocidad
ENEMIES_JUMP_FRAMES = 10
ENEMIES_JUMP_SPEED = 2
ENEMIES_SPEED_AGRO = 2 * SCALE
ENEMY_SPEED = 1 * SCALE

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

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
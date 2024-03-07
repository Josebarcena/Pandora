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

ATTACK_WIDTH = 35
ATTACK_HEIGHT = 35

# Limites en el eje x e y (el limite de la izq es SCROLL_LIMIT_X y el de la derecha será WIN_WIDTH - SCROLL_LIMIT_X)
SCROLL_LIMIT_X_LEFT = 106 * SCALE
SCROLL_LIMIT_X_RIGHT = WIN_WIDTH - (106 * SCALE)
SCROLL_LIMIT_Y_BOTTOM = 80 * SCALE
SCROLL_LIMIT_Y_TOP = WIN_HEIGHT - (80 * SCALE)

# Variables de escalado de imagen del personaje
RUN_SCALE = TILESIZE * 1.5 * SCALE, TILESIZE * 2 * SCALE
JUMP_SCALE = TILESIZE * SCALE, TILESIZE * 2 * SCALE
IDLE_SCALE = TILESIZE * SCALE, TILESIZE * 2 * SCALE
ATTACK_SCALE = TILESIZE * 2.9 * SCALE, TILESIZE * 2 * SCALE

# Variables de escalado de imagen del enemigo
RUN_SCALE_ENEMY = TILESIZE * SCALE, TILESIZE * 2 * SCALE

# Fuerza de la gravedad, velocidad del dash, numero de frames que dura el salto y dash
GRAVITY = 3 * SCALE
JUMPING_SPEED = 2.5 * SCALE
DASH_SPEED = 8 * SCALE
FRAMES_JUMP = 25
FRAMES_DASH = 10
FRAMES_ATTACK = 35

# Diferentes capas para el juego
ATTACK_LAYER = 4
PLAYER_LAYER = 3
ENEMY_LAYER = 2
BLOCK_LAYER = 1
PLAYER_SPEED = 3 * SCALE

# Cantidad de pixeles para que los enemigos cambien al estado agro
PIXELS_ENEMIES_AGRO_X = 400
PIXELS_ENEMIES_AGRO_Y = 150

# Variables para controlar la cantidad de frames que dura el salto de los enemigos, velocidades de salto y velocidad
ENEMIES_JUMP_FRAMES = 10
ENEMIES_JUMP_SPEED = 0.5
ENEMIES_SPEED_AGRO = 0.5 * SCALE
ENEMY_SPEED = 0.75 * SCALE

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
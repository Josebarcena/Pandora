import sys
import pygame
from os.path import join
from pygame import mixer

#DECLARACIÓN DE VARIABLES
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
SCROLL_LIMIT_X_RIGHT = WIN_WIDTH - (206 * SCALE)
SCROLL_LIMIT_Y_TOP = 72 * SCALE
SCROLL_LIMIT_Y_BOTTOM = WIN_HEIGHT - (100 * SCALE)

# Variables de escalado de imagen del personaje
RUN_SCALE = TILESIZE * 1.5 * SCALE, TILESIZE * 2 * SCALE
JUMP_SCALE = TILESIZE * SCALE, TILESIZE * 2 * SCALE
IDLE_SCALE = TILESIZE * SCALE, TILESIZE * 2 * SCALE
ATTACK_SCALE = TILESIZE * 3 * SCALE, TILESIZE * 2 * SCALE
DASH_SCALE = TILESIZE* 1.5 * SCALE, TILESIZE * 1.5 * SCALE
DEAD_SCALE = TILESIZE* 1.5 * SCALE, TILESIZE * 1.5 * SCALE

# Variables de escalado de imagen del enemigo
RUN_SCALE_ENEMY = TILESIZE * SCALE, TILESIZE * 2 * SCALE
DEAD_SCALE_ENEMY = TILESIZE * 1.2 * SCALE, TILESIZE * 2 * SCALE

# Fuerza de la gravedad, velocidad del dash, numero de frames que dura el salto y dash
GRAVITY = 3 * SCALE
JUMPING_SPEED = 2.5 * SCALE
DASH_SPEED = 8 * SCALE
FRAMES_JUMP = 25
FRAMES_DASH = 10
FRAMES_ATTACK = 35
MAX_HEALTH = 5
UNSTOPBLE_FRAMES = 15

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
ENEMIES_SPEED_AGRO = 0.75 * SCALE
ENEMY_SPEED = 0.5 * SCALE
ENEMY_HEALTH = 3
FRAMES_ENEMIES_HIT = 25
ENEMIES_SPEED_HIT = 2 * SCALE
FRAMES_COOLDOWN_ATTACK = 50

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 255, 255)
GREEN = (0, 255, 0)
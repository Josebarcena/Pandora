import pygame
from Ajustes import *

# Clase implementada para permitir el control del personaje
class Control:
    def __init__(self):
        # Para implementar el control del personaje se han implementado estas variables, que nos indican el estado del personaje:
        # self.state-> 'normal' en caso de que no esté en medio de ninguna animación
        #               'jumping' en caso de que esté saltando, se usa para evitar el doble salto entre otras cosas
        # self.bool_air-> booleano que almacena si personaje se encuentra sobre el aire, True, o si está sobre una
        #               plataforma, False
        # self.jump_frames-> en ella almacenamos el numero de frames que ocupará la animación de salto durante
        #                la ejecución, se usará como contador
        # Ya que empezamos con nuestro personaje en el aire, sin realizar el salto así es como se inicializan.

        self.state = 'normal'
        self.bool_air = True
        self.jump_frames = 0
        self.facing = 'right'

    def change_state(self, newstate, facing= None):
        if newstate == 'jumping':
            # Para evitar que se pueda saltar en el aire/ doble salto, el jugador dede de haber terminado con la
            # animación de saltar y estar apoyado en una superficie, se inicializa a 30 el contador de frames
            # para la animación de saltar
            if self.state == 'normal' and self.bool_air == False:
                self.state = 'jumping'
                self.jump_frames = FRAMES_JUMP
        if newstate == 'ground':
            # Se llama a este estado cuando el personaje a tenido una colisión con el Top de alguno de
            # los bloques del nivel
            self.bool_air = False
            self.bool_dash = True
        if newstate == 'air':
            # Se llama a este estado cuando no se ha detectado ninguna colisión vertical
            self.bool_air = True

    # Según el estado en el que nos encontremos debemos de añadir a las variables auxiliares la fuerza de gravedad,
    # positiva en caso de estar en un estado 'normal', lo que hará que el jugador "se pegue" al suelo, y negativa en
    # caso de que el jugador haya saltado, haciendo que "se despegue" del suelo
    def update_character(self, x_change, y_change):
        if self.state == 'normal':
            y_change += GRAVITY
        if self.state == 'jumping':
            if self.jump_frames > 0:
                self.jump_frames -= 1
                self.bool_air = True
                y_change -= JUMP_HEIGHT
            else:
                self.state = 'normal'
                self.bool_air = True
        return x_change, y_change

    # En este método capturamos las teclas pulsadas por el usuario y añadimos el movimiento necesario a las variables
    # auxiliares x_change y y_change, implementé el salto con SPACE
    def movement(self):
        x_change, y_change = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x_change -= PANDORA_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            x_change += PANDORA_SPEED
            self.facing = 'right'
        if keys[pygame.K_SPACE]:
            self.change_state('jumping')

        return x_change, y_change
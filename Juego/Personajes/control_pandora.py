import pygame
from Juego.Recursos.config import *

# Clase implementada para permitir el control del personaje
class Control:
    def __init__(self, game, player):
        # Para implementar el control del personaje se han implementado estas variables, que nos indican el estado del personaje:
        # self.state-> 'normal' en caso de que no esté en medio de ninguna animación
        #               'jumping' en caso de que esté saltando, se usa para evitar el doble salto entre otras cosas
        #               'dashing' en caso de estar dasheando, cancela la animación de salto
        # self.bool_dash-> booleano que almacena si el personaje ha dasheado o no, esto se implementa para evitar dashes
        #                   infinitos, se resetea a true cada vez que se toca el suelo
        # self.bool_air-> booleano que almacena si personaje se encuentra sobre el aire, True, o si está sobre una
        #               plataforma, False
        # self.cont_frames-> en ella almacenamos el numero de frames que ocuparán las distintas animaciónes, se usará
        #               de contador
        # self.facing -> pensada para las animaciones , no tiene uso de momento
        # self.dash_face-> almacena la ultima direccion del personaje (left o right) para realizar el dash en esa direccion
        # Ya que empezamos con nuestro personaje en el aire, sin realizar el salto así es como se inicializan.
        self.cooldown = 0
        self.state = 'normal'
        self.bool_air = True
        self.bool_dash = False
        self.cont_frames = 0
        self.facing = 'right'
        self.dash_face = 'right'
        self.game = game
        self.player = player

    #Retraso para evitar saltar varias veces de golpe
    def update_cd(self):
        if self.cooldown > 0:
            self.cooldown -=1

    def change_state(self, newstate, facing= None):
        if newstate == 'jumping':
            # Para evitar que se pueda saltar en el aire/ doble salto, el jugador dede de haber terminado con la
            # animación de saltar y estar apoyado en una superficie, se inicializa a 30 el contador de frames
            # para la animación de saltar
            if self.state == 'normal' and self.bool_air == False and self.cooldown == 0:
                self.state = 'jumping'
                self.cont_frames = FRAMES_JUMP
                self.bool_dash = True
                self.cooldown = 30
        if newstate == 'ground':
            # Se llama a este estado cuando el personaje a tenido una colisión con el Top de alguno de
            # los bloques del nivel
            self.bool_air = False
        if newstate == 'air':
            # Se llama a este estado cuando no se ha detectado ninguna colisión vertical
            self.bool_air = True
        if newstate == 'dashing':
            # Se transita al estado de dashing en caso de que el jugador este saltando, cancelando esta animacion
            if self.state == 'jumping' and self.bool_dash:
                self.state = 'dashing'
                self.bool_dash = False
                self.cont_frames = FRAMES_DASH
            # Se transita al estado dashing en caso de que el personaje esté en el aire(cayendo) y aún no se ha realizado
            # el dash enesta caída
            elif self.state == 'normal' and self.bool_air and self.bool_dash:
                self.state = 'dashing'
                self.bool_dash = False
                self.cont_frames = FRAMES_DASH


    # Según el estado en el que nos encontremos debemos de añadir a las variables auxiliares la fuerza de gravedad,
    # positiva en caso de estar en un estado 'normal', lo que hará que el jugador "se pegue" al suelo, y negativa en
    # caso de que el jugador haya saltado, haciendo que "se despegue" del suelo. En caso de que se esté dasheando
    # se eliminan los desplazamientos que el usuario haya querido hacer (llamada a self.movimiento()) y se añade
    # la velocidad del dash a la posicion del jugador en la direccion de self.dash_face.
    def update_character(self, x_change, y_change):
        if self.state == 'normal' and self.bool_air:
            y_change += GRAVITY
        if self.state == 'jumping':
            if self.cont_frames > 0:
                self.cont_frames -= 1
                self.bool_air = True
                y_change -= JUMPING_SPEED
            else:
                self.state = 'normal'
                self.bool_air = True
        if self.state == 'dashing':
            if self.cont_frames > 0:
                self.cont_frames -= 1
                self.bool_air = True
                if self.dash_face == 'left':
                    x_change = -DASH_SPEED
                if self.dash_face == 'right':
                    x_change = DASH_SPEED
            else:
                self.state = 'normal'
                self.bool_air = True

        return x_change, y_change

    # En este método capturamos las teclas pulsadas por el usuario y añadimos el movimiento necesario a las variables
    # auxiliares x_change y y_change, implementé el salto con SPACE
    def movement(self):
        x_change, y_change = 0, 0
        keys = pygame.key.get_pressed()

        # Verificar si ninguna tecla de dirección está presionada
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and self.bool_air is False:
            self.player.set_animacion_idle()

        if keys[pygame.K_LEFT]:
            x_change -= PLAYER_SPEED
            self.facing = 'left'
            if self.state != 'jumping' and self.bool_air is False:
                self.player.set_animacion_run()
            if self.state != 'dashing':
                self.dash_face = 'left'
        if keys[pygame.K_RIGHT]:
            x_change += PLAYER_SPEED
            self.facing = 'right'
            if self.state != 'jumping' and self.bool_air is False:
                self.player.set_animacion_run()
            if self.state != 'dashing':
                self.dash_face = 'right'

        if keys[pygame.K_SPACE]:
            self.change_state('jumping')
            self.player.set_animacion_jump()

        # Se evita que se pueda dashear y saltar a la vez
        elif keys[pygame.K_TAB]:
            self.change_state('dashing')

        return x_change, y_change


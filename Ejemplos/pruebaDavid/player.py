import pygame
from config import *
from control_pandora import *
import math
import random

# Definimos la clase Player en la que está implementada la mayoría de funcionalidad del código,
# debería de encapsularse y quitarle "responsabilidades"
class Player(pygame.sprite.Sprite):
    # Método con el que iniciamos el objeto, partimos de las coordenadas iniciales del juego y el propio juego
    def __init__(self, game, x, y):
        # Iniciamos las variables del jugador para poder acceder a ellas más adelante
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Posiciones iniciales del cubo y tamaño
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.heigh = TILESIZE

        # Variables auxiliares que nos ayudarán a actualizar la posición del personaje
        self.x_change = 0
        self.y_change = 0

        # Para las animaciones, sin implementar
        self.facing = 'lef'
        self.animaciones_idle = self.animaciones_idle()
        self.animaciones_run = self.animaciones_run()
        self.animaciones_jump = self.animaciones_jump()
        self.animacion_actual = self.animaciones_idle  # Inicialmente, el personaje está en estado de reposo
        # Actualizacion de IDLE
        self.frame_index_idle = 0
        self.update_time_idle = pygame.time.get_ticks()  # Temporizador para animaciones de IDLE
        self.image = self.animaciones_idle[self.frame_index_idle]
        # Actualizacion de RUN
        self.frame_index_run = 0
        self.update_time_run = pygame.time.get_ticks()  # Temporizador para animaciones de RUN

        # Control del personaje
        self.control = Control()

        # Inicializamos el rect del Sprite, ya que es un objeto importado de la libreria debemos de inicializar el rect
        # para poder usar estas librerias correctamente, véase en las colisiones
        self.image = pygame.Surface([self.width, self.heigh])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # Método en el que se actualiza el cubo
    def update(self):
        self.x_change, self.y_change = self.control.movement()

        self.x_change, self.y_change = self.control.update_character(self.x_change, self.y_change)
        # Colisiones con el eje x
        self.rect.x += self.x_change
        self.collide_blocks('x')

        # Colisiones con el eje y
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.screen_check()

        self.x_change = 0
        self.y_change = 0

    # Comprobamos la posición del jugador al final de la actualización de pantalla, si se sale de los márgenes
    # establecidos, moveremos la lista de sprites que conforman el nivel en dirección contraria a la que va el jugador
    # y a la velocidad del jugador
    def screen_check(self):
        if self.rect.x <= SCROLL_LIMIT_X:
            self.rect.x = SCROLL_LIMIT_X
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
        elif self.rect.x >= WIN_WIDTH - SCROLL_LIMIT_X:
            self.rect.x = WIN_WIDTH - SCROLL_LIMIT_X
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
        if self.rect.y <= SCROLL_LIMIT_Y:
            self.rect.y = SCROLL_LIMIT_Y
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
        elif self.rect.y >= WIN_HEIGHT - SCROLL_LIMIT_Y:
            self.rect.y = WIN_HEIGHT - SCROLL_LIMIT_Y
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED

    # Se estudian las colisiones del jugador con los sprites almacenados en game.blocks, que son los distintos bloques
    # con los que se crea el nivel
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    self.control.change_state('ground')
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
            # En caso de que no se haya colisiones verticalmente y bool_air era falso en el anterior frame significa que
            # debemos de aplicar la gravedad, el jugador se cayó de la plataforma
            else:
                self.control.change_state('air')

    # MODIFICACIONES CAINZOS LAS DE ABAJO

    #    def escalar_img(image, scale):
    #        w = image.get_width()
    #        h = image.get_height()
    #        new_image = pygame.transform.scale(image, (w * scale, h * scale))
    #        return new_image

    # Metodos para las animaciones IDLE
    @staticmethod
    def animaciones_idle():
        animaciones_idle = []
        for i in range(6):
            img_idle = pygame.image.load(f"images//sprites//pandora//Individual Sprite//idle//Warrior_Idle_{i}.png")
            # img_idle = escalar_img(img_idle, constantes.ESCALA_PERSONAJE)
            animaciones_idle.append(img_idle)
        return animaciones_idle

    def set_animacion_idle(self):
        self.animacion_actual = self.animaciones_idle
        if self.frame_index_idle >= len(self.animacion_actual):
            self.frame_index_idle = 0
        self.update()

    # Metodos para animaciones de RUN
    @staticmethod
    def animaciones_run():
        animaciones_run = []
        for i in range(8):
            img_run = pygame.image.load(f"images//sprites//pandora//Individual Sprite//Run//Warrior_Run_{i}.png")
            # img_run = escalar_img(img_run, constantes.ESCALA_PERSONAJE)
            animaciones_run.append(img_run)
        return animaciones_run

    def set_animacion_run(self):
        self.animacion_actual = self.animaciones_run
        if self.frame_index_run >= len(self.animacion_actual):
            self.frame_index_run = 0
        self.update()

    @staticmethod
    def animaciones_jump():
        animaciones_jump = []
        for i in range(3):
            img_jump = pygame.image.load(f"images//sprites//pandora//Individual Sprite//Jump//Warrior_Jump_{i}.png")
            # img_run = escalar_img(img_jump, constantes.ESCALA_PERSONAJE)
            animaciones_jump.append(img_jump)
        return animaciones_jump

    # Metodo de actualizacion de sprites
    def update_animation(self):
        cooldown_animacion = 100  # Cooldown para las animaciones
        if pygame.time.get_ticks() - self.update_time_idle >= cooldown_animacion:
            self.frame_index_idle += 1
            self.update_time_idle = pygame.time.get_ticks()
            if self.frame_index_idle >= len(self.animacion_actual):
                self.frame_index_idle = 0
        # Se asegura de que frame_index_idle no exceda el tamaño de la lista de animaciones
        if self.frame_index_idle < len(self.animacion_actual):
            self.image = self.animacion_actual[self.frame_index_idle]
        else:
            self.frame_index_idle = 0

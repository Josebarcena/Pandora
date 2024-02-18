import pygame
from config import *
import math
import random

# Definimos la clase Player en la que está implementada la mayoría de funcionalidad del código, debería de encapsularse y quitarle "responsabilidades"
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

        # Para implementar la gravedad se hace uso de estás variables, que nos indican el estado del personaje:
        # self.state-> 'normal' en caso de que no esté en medio de ninguna animación
        #               'jumping' en caso de que esté saltando, se usa para evitar el doble salto entre otras cosas
        # self.bool_air-> booleano que almacena si personaje se encuentra sobre el aire, True, o si está sobre una
        #               plataforma, False
        # self.jump_frames-> en ella almacenamos el numero de frames que ocupará la animación de salto durante
        # la ejecución, se usará de contador
        # Ya que empezamos con nuestro personaje en el aire, sin realizar el salto así es como se inicializan.
        self.state = 'normal'
        self.bool_air = True
        self.jump_frames = 0

        # Inicializamos el rect del Sprite, ya que es un objeto importado de la libreria debemos de inicializar el rect
        # para poder usar estas librerias correctamente, véase en las colisiones
        self.image = pygame.Surface([self.width, self.heigh])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # Método en el que se actualiza el cubo
    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.collide_blocks('x')

        self.check_state()
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.screen_check()

        self.x_change = 0
        self.y_change = 0

    # Según el estado en el que nos encontremos debemos de añadir a las variables auxiliares la fuerza de gravedad,
    # positiva en caso de estar en un estado 'normal', lo que hará que el jugador "se pegue" al suelo, y negativa en
    # caso de que el jugador haya saltado, haciendo que "se despegue" del suelo
    def check_state(self):
        if self.state == 'normal' and self.bool_air:
            self.y_change += GRAVITY
        elif self.state == 'jumping':
            if self.jump_frames > 0:
                self.jump_frames -= 1
                self.bool_air = True
                self.y_change -= GRAVITY
            else:
                self.state = 'normal'
                self.bool_air = True


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

    # En este método capturamos las teclas pulsadas por el usuario y añadimos el movimiento necesario a las variables
    # auxiliares x_change y y_change, implementé el salto con SPACE pero sigues pudiendo desplazarte libremente por el
    # nivel con 'S' y 'D'
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
        if keys[pygame.K_SPACE]:
            # Para evitar que se pueda saltar en el aire/ doble salto, el jugador dede de haber terminado con la
            # animación de saltar y estar apoyado en una superficie, se inicializa a 30 el contador de frames
            # para la animación de saltar
            if self.state == 'normal' and self.bool_air == False:
                self.state = 'jumping'
                self.jump_frames = FRAMES_JUMP

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
                    if self.bool_air:
                        self.bool_air = False
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
            # En caso de que no se haya colisiones verticalmente y bool_air era falso en el anterior frame significa que
            # debemos de aplicar la gravedad, el jugador se cayó de la plataforma
            elif self.bool_air == False:
                self.bool_air =True


# Defino los diferentes bloques que formarán parte del nivel
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, color):
        self.game = game
        self._layer = BLOCK_LAYER
        # Se añade el bloque a las distintas listas del juego
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Colocamos el bloque según las posición que se nos indica y le damos el size oportuno
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # Añadimos color y superficio al bloque
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)

        # Inicializamos el rect del Sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
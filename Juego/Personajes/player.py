import pygame
from Recursos.config import *
from Personajes.control_pandora import *
from Personajes.Viewers import *
from Recursos.Gestor_recursos import GestorRecursos


# Definimos la clase Player en la que está implementada la mayoría de funcionalidad del código, debería de encapsularse y quitarle "responsabilidades"
class Player(pygame.sprite.Sprite):
    # Método con el que iniciamos el objeto, partimos de las coordenadas iniciales del juego y el propio juego
    def __init__(self, game, x, y, group):
        # Iniciamos las variables del jugador para poder acceder a ellas más adelante
        self.animation_image = None
        self.final_height = None
        self.final_width = None
        self.game = game
        self.groups = (self.game.all_sprites,group)
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Posiciones iniciales del cubo y tamaño
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE * SCALE
        self.heigh = TILESIZE * 2 * SCALE

        # Viewers
        self.viewers = [Life_Bar()]
        # Variables auxiliares que nos ayudarán a actualizar la posición del personaje
        self.x_change = 0
        self.y_change = 0

        # Variables de animación
        self.animaciones_idle = GestorRecursos.almacenar_animacion_fila(6, 20, 33, 49, 18, 10, 0, 0)
        self.animaciones_run = GestorRecursos.almacenar_animacion_fila(8, 29, 29, 41, 12, 58, 11, 101)
        self.animaciones_jump = GestorRecursos.almacenar_animacion_fila(6, 20, 33, 49, 88, 316, 18, 361)
        self.animacion_actual = self.animaciones_idle  # Inicialmente, el jugador está en estado quieto
        self.frame_index_idle = 0  # Índice del fotograma actual para la animación de estar quieto
        self.frame_index_run = 0  # Índice del fotograma actual para la animación de correr
        self.frame_index_jump = 0  # Índice del fotograma actual para la animación de saltar
        self.update_time = 0  # Tiempo de última actualización de la animación de estar quieto

        # Para las animaciones, sin implementar
        self.facing = 'left'

        # Control del personaje
        self.control = Control(game, self)

        #TIMER DONDE NO RECIBE DAÑO
        self.invul = 0
        self.hp = 5

        # Cargar la imagen del personaje
        self.update_image(self.animacion_actual)

        # Crear el rectángulo de colisión con las dimensiones del personaje recortado
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.previous_rect = self.rect

    def update_image(self, animation_array):
        tiempo_actual = pygame.time.get_ticks()

        # Actualizamos las variables dependiendo del tipo de animacion que se esta realizando
        if animation_array == self.animaciones_idle:
            cooldown_animacion = 180
            frame_index = self.frame_index_idle
        elif animation_array == self.animaciones_run:
            cooldown_animacion = 120
            frame_index = self.frame_index_run
        elif animation_array == self.animaciones_jump:
            cooldown_animacion = 150
            frame_index = self.frame_index_jump

        if tiempo_actual - self.update_time >= cooldown_animacion:
            frame_index += 1
            self.update_time = tiempo_actual
            if frame_index >= len(animation_array):
                frame_index = 0

        # Actualizar la animación actual y la imagen del personaje
        if animation_array == self.animaciones_idle:
            self.frame_index_idle = frame_index
            self.animation_image = animation_array[frame_index]

            if self.control.facing == 'left':
                self.image = pygame.transform.flip(self.animation_image, True, False)
            else:
                self.image = self.animation_image

        elif animation_array == self.animaciones_run:
            self.frame_index_run = frame_index
            self.animation_image = animation_array[frame_index]

            if self.control.facing == 'left':
                self.image = pygame.transform.flip(self.animation_image, True, False)
            else:
                self.image = self.animation_image

        elif animation_array == self.animaciones_jump:
            self.frame_index_jump = frame_index
            self.animation_image = animation_array[frame_index]

            if self.control.facing == 'left':
                self.image = pygame.transform.flip(self.animation_image, True, False)
            else:
                self.image = self.animation_image


        # Escalar la imagen según el tamaño final deseado
        if animation_array == self.animaciones_run:
            self.image = pygame.transform.scale(self.image, (TILESIZE *1.5 * SCALE, TILESIZE * 2* SCALE))
        elif animation_array == self.animaciones_jump or animation_array == self.animaciones_idle:
            self.image = pygame.transform.scale(self.image, (TILESIZE * SCALE, TILESIZE * 2 * SCALE))

    # Método en el que se actualiza el cubo
    def update(self):
        self.control.update_cd()

        if self.invul != 0: #Durante este tiempo no se puede recibir daño de nuevo
            self.invul += 1
            if self.invul >= 300: #Si se llega a 5 segundos puedes recibir otra vez daño
                self.invul = 0

        self.x_change, self.y_change = self.control.movement()

        self.x_change, self.y_change = self.control.update_character(self.x_change, self.y_change)
        self.rect.x += self.x_change
        #Se pregunta al nivel si chocamos con algo y con que
        self.collide_blocks(self.game.collide_Fase(self),"x")

        self.rect.y += self.y_change
        self.collide_blocks(self.game.collide_Fase(self),"y")

        self.previous_rect = self.rect
        self.x_change = 0
        self.y_change = 0
    

    def viewers_update(self): #Se avisa de los eventos al observador 
        for viewer in self.viewers:
            viewer.update(self)

    # Comprobamos la posición del jugador al final de la actualización de pantalla, si se sale de los márgenes
    # establecidos, moveremos la lista de sprites que conforman el nivel en dirección contraria a la que va el jugador
    # y a la velocidad del jugador
    

    # Se estudian las colisiones del jugador con los sprites almacenados en game.blocks, que son los distintos bloques
    # con los que se crea el nivel
    def collide_blocks(self, collision, direction):
        
        #Comprobamos con que choca
        if collision[0] == "Solid":
            self.solid_Collision(collision[1],direction)

        elif collision[0] == "Platform":
            self.platform_Collision(collision[1], direction)

        elif collision[0] == "Damage":
            if self.invul == 0:
                self.hp -= 1
                self.viewers_update()
            self.invul += 1
        
        elif collision[0] == "Stairs":
            self.stairs_Collision(collision[1], direction)
        
        elif collision[0] != None:
            pass
        else:
            self.control.change_state('air')
            
    def solid_Collision(self,blocks, direction):
        if  direction == "x":
            if self.x_change > 0:
                self.rect.x = blocks[0].rect.left - self.rect.width
            if self.x_change < 0:
                self.rect.x = blocks[0].rect.right
        if  direction == "y":
            if self.y_change > 0:
                self.rect.y = blocks[0].rect.top - self.rect.height
                self.control.change_state('ground')
            if self.y_change < 0:
                self.rect.y = blocks[0].rect.bottom


    def platform_Collision(self, platforms, direction):
        if direction == "y":
                player_necessary_y = self.rect.bottom
                platform_necessary_y = platforms[0].rect.top + 0.75 * platforms[0].rect.height
            
                # Verificar si el jugador está por encima del 75% de la plataforma
                if player_necessary_y < (platform_necessary_y):
                    if self.y_change > 0 and self.previous_rect.y < platforms[0].rect.top:
                        self.rect.y = platforms[0].rect.top - self.rect.height
                        self.control.change_state('ground')


    def stairs_Collision(self, ramps, direction):
                    # Si el jugador está sobre la rampa y su centro vertical está por encima del borde superior de la rampa
                if self.rect.colliderect(ramps[0].rect) and self.rect.centery < ramps[0].rect.centery:
                    # Calcular la nueva posición vertical del jugador para subir la rampa
                    new_y = ramps[0].rect.top - self.rect.height + (self.rect.centerx - ramps[0].rect.left) * 0.5  # Pendiente del 45%
                    self.control.change_state('ground')
                    # Mover al jugador a la nueva posición
                    self.rect.y = new_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_animacion_idle(self):
        self.animacion_actual = self.animaciones_idle
        self.update_image(self.animaciones_idle)

    def set_animacion_run(self):
        self.animacion_actual = self.animaciones_run
        self.update_image(self.animaciones_run)

    def set_animacion_jump(self):
        self.animacion_actual = self.animaciones_jump
        self.update_image(self.animaciones_jump)

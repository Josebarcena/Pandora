import pygame
from Recursos.config import *
from Personajes.control_pandora import *
from Personajes.Viewers import *
from Recursos.Gestor_recursos import GestorRecursos
from Personajes.attack import *

# Definimos la clase Player en la que está implementada la mayoría de funcionalidad del código, debería de encapsularse y quitarle "responsabilidades"
class Player(pygame.sprite.Sprite):
    # Método con el que iniciamos el objeto, partimos de las coordenadas iniciales del juego y el propio juego
    def __init__(self, game, x, y, group):
        # Iniciamos las variables del jugador para poder acceder a ellas más adelante
        self.animation_image = None
        self.final_height = None
        self.final_width = None
        self.game = game
        self._layer = 5
        self.groups = (self.game.all_sprites,group)
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Viewers
        self.viewers = [Life_Bar()]
        # Variables auxiliares que nos ayudarán a actualizar la posición del personaje
        self.x_change = 0
        self.y_change = 0

        # Variables de animación -> Arrays con las imagenes que se usaran para mostrar la animacion del personaje
        self.idle_animations = GestorRecursos.almacenar_animacion_fila(6, 20, 33, 49, 18, 10, 0, 0, 0, 0)
        self.run_animations = GestorRecursos.almacenar_animacion_fila(8, 29, 29, 41, 12, 58, 11, 101, 0, 0)
        self.jump_animations = GestorRecursos.almacenar_animacion_fila(6, 20, 33, 49, 88, 316, 18, 361, 0, 0)
        self.attack_animations = GestorRecursos.almacenar_animacion_fila(9, 55, 42, 10, 150, 89, 15, 133, 0, 179)
        self.dash_animations = GestorRecursos.almacenar_animacion_fila(4, 31, 21, 39, 151, 641, 0, 0, 0, 0)
        self.actual_animation = self.idle_animations  # Inicialmente, el jugador está en estado quieto
        # Variables de animacion -> Variables para recorrer cada uno de los arrays con las imagenes
        self.frame_index_idle = 0  # Índice del fotograma actual para la animación de estar quieto
        self.frame_index_run = 0  # Índice del fotograma actual para la animación de correr
        self.frame_index_jump = 0  # Índice del fotograma actual para la animación de saltar
        self.frame_index_attack = 0 # Índice del fotograma actual para la animación de atacar
        self.frame_index_dash = 0   # Índice del fotograma actual para la animación de dash
        self.update_time = 0  # Tiempo de última actualización de la animación de estar quieto

        self.facing = 'left'
        self.unstopable = 0
        self.health = PLAYER_HEALTH
        # Control del personaje
        self.control = Control(game, self)
        self.attack = Attack(x, y, game, self)

        #TIMER DONDE NO RECIBE DAÑO
        self.invul = 0
        self.hp = 5

        # Cargar la imagen del personaje
        self.update_image(self.actual_animation)

        # Crear el rectángulo de colisión con las dimensiones del personaje recortado
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.previous_rect = self.rect
        print("player",self.rect)

    def update_image(self, animation_array):
        # Recogemos el tiempo actual en el juego
        actual_time = pygame.time.get_ticks()

        # Actualizamos las variables dependiendo del tipo de animacion que se esta realizando
        if animation_array == self.idle_animations:
            cooldown_animation = 180
            frame_index = self.frame_index_idle
        elif animation_array == self.run_animations:
            cooldown_animation = 80
            frame_index = self.frame_index_run
        elif animation_array == self.jump_animations:
            cooldown_animation = 150
            frame_index = self.frame_index_jump
        elif animation_array == self.attack_animations:
            cooldown_animation = 60
            frame_index = self.frame_index_attack
        elif animation_array == self.dash_animations:
            cooldown_animation = 60
            frame_index = self.frame_index_dash


        # Si se ha cumplido el tiempo de cooldown entre animacion se modifica la imagen
        if actual_time - self.update_time >= cooldown_animation:
            frame_index += 1
            self.update_time = actual_time
            if frame_index >= len(animation_array):
                frame_index = 0

        # Actualizar la animación actual y la imagen del personaje
        if animation_array == self.idle_animations:
            self.frame_index_idle = frame_index
            self.animation_image = animation_array[frame_index]
        elif animation_array == self.run_animations:
            self.frame_index_run = frame_index
            self.animation_image = animation_array[frame_index]
        elif animation_array == self.jump_animations:
            self.frame_index_jump = frame_index
            self.animation_image = animation_array[frame_index]
        elif animation_array == self.attack_animations:
            self.frame_index_attack = frame_index
            self.animation_image = animation_array[frame_index]
        elif animation_array == self.dash_animations:
            self.frame_index_dash = frame_index
            self.animation_image = animation_array[frame_index]

        # Analizamos en que sentido esta mirando el personaje para hacer flip o no a la imagen
        if self.control.facing == 'left':
            self.image = pygame.transform.flip(self.animation_image, True, False)
        else:
            self.image = self.animation_image


        # Escalar la imagen según el tamaño final deseado
        if animation_array == self.run_animations:
            self.image = pygame.transform.scale(self.image, RUN_SCALE)
        elif animation_array == self.jump_animations:
            self.image = pygame.transform.scale(self.image, JUMP_SCALE)
        elif animation_array == self.idle_animations:
            self.image = pygame.transform.scale(self.image, IDLE_SCALE)
        elif animation_array == self.attack_animations:
            self.image = pygame.transform.scale(self.image, ATTACK_SCALE)
        elif animation_array == self.dash_animations:
            self.image = pygame.transform.scale(self.image, DASH_SCALE)

    # Método en el que se actualiza el cubo
    def update(self):
        self.control.update_cd()

        if self.invul != 0:
            self.idle_animations[0].set_alpha(0) #Se cambia el alpha a 0 para dar sensacion de parpadeo
            self.run_animations[0].set_alpha(0) # se cambia en todas porque puede cambiar la animacion a cualquiera en este estado
            self.jump_animations[0].set_alpha(0)
            self.invul += 1
            if self.invul >= 300: #Si se llega a 5 segundos puedes recibir otra vez daño
                self.invul = 0
                self.idle_animations[0].set_alpha(255) #se ajusta de nuevo el valor por si cambio durante el invul
                self.run_animations[0].set_alpha(255)
                self.jump_animations[0].set_alpha(255)

        self.x_change, self.y_change = self.control.movement()

        self.x_change, self.y_change = self.control.update_character(self.x_change, self.y_change)
        self.rect.x += self.x_change
        #Se pregunta al nivel si chocamos con algo y con que
        self.collide_blocks(self.game.collide_Fase(self),"x")

        self.rect.y += self.y_change
        self.collide_blocks(self.game.collide_Fase(self),"y")
        self.collide_enemies()
        self.previous_rect = self.rect
        self.x_change = 0
        self.y_change = 0
    def collide_enemies(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies_layer, False)
        self.unstopable -= 1
        if hits and self.unstopable < 0:
            #print("--DAMAGE, helath: " + str(self.health - 1))
            self.health -= 1
            self.unstopable = UNSTOPBLE_FRAMES

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
        elif collision[0] == "Potion":
            self.hp += collision[1][0].utility()
            collision[1][0].kill()
            self.viewers_update()

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

    # Funcion para establecer la animacion de IDLE (parado)
    def set_animacion_idle(self):
        self.actual_animation = self.idle_animations
        self.update_image(self.idle_animations)

    # Funcion para establecer la animacion de RUN (corriendo)
    def set_animacion_run(self):
        self.actual_animation = self.run_animations
        self.update_image(self.run_animations)

    # Funcion para establecer la animacion de JUMP (saltando)
    def set_animacion_jump(self):
        self.actual_animation = self.jump_animations
        self.update_image(self.jump_animations)

    # Funcion para establecer la animacion de ATTACK (atacando)
    def set_animacion_attack(self):
        self.actual_animation = self.attack_animations
        self.update_image(self.attack_animations)

    def set_animacion_dash(self):
        self.actual_animation = self.dash_animations
        self.update_image(self.dash_animations)
    def damage_attack(self):
        return 1

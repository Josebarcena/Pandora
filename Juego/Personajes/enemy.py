import pygame
from Recursos.config import *
from Personajes.Viewers import *
import numpy as np
from Recursos.Gestor_recursos import GestorRecursos

class Enemy(pygame.sprite.Sprite):
    def __init__(self, fase, x, y, group):
        self.fase = fase
        self.groups = (self.fase.all_sprites, group)
        pygame.sprite.Sprite.__init__(self, self.groups)

        # Se crea un nuevo grupo por cada enemigo para poder tratar las colisiones con el ataque individualmente, no
        # nos sirve el grupo de fase.enemies_layer ya que restariamos vida a todos los enemigos
        self.owngroup = pygame.sprite.Group()
        self.owngroup.add(self)

        # Tamaño del enemigo
        self.width = TILESIZE * SCALE
        self.heigh = TILESIZE * 2 * SCALE
        
        # Variables auxiliares
        self.x_change = 0
        self.y_change = 0
        self.frames_hit = 0

        # Variables para representar su facing, su vida y el estado del enemigo, puede ser:
        #               -> 'normal': el enemigo no tiene cerca al personaje, estado de patrulla si se choca con algo 
        #                           en el eje X cambia de direccion 
        #               -> 'agro': el enemigo está cerca del jugador, su direccion de desplazamiento será en la que esté
        #                           el jugador, se aumenta su velocidad
        #               -> 'hitted': el jugador atacó al enemigo y le quita vida, se desplaza al enemigo para atrás 
        self.health = ENEMY_HEALTH
        self.isdeath = False
        self.facing = 'left'
        self.state = 'normal'
        
        
        # Variables de animación -> Arrays con las imagenes que se usaran para mostrar la animacion del enemigo
        # Si en la siguiente linea se modifica Enemies_Sheet-Effect.png por Enemies_Sheet-Effect2.png y viceversa se muestra otro sprite para el enemigo
        self.idle_animations = GestorRecursos.loadSpritesEnemies('Enemies_Sheet-Effect.png', 8, 25, 27, 51, 13, 22)
        self.idle_animations_angry = GestorRecursos.loadSpritesEnemies('EnemiesAngry_Sheet-Effect.png', 8, 25, 27, 51, 13, 22)
        self.actual_animation = self.idle_animations
        # Variables de animacion -> Variables para recorrer cada uno de los arrays con las imagenes
        self.frame_index_idle = 0  # Índice del fotograma actual para la animación de estar quieto
        self.frame_index_run = 0  # Índice del fotograma actual para la animación de correr
        self.update_time = 0  # Tiempo de última actualización de la animación de estar quieto
        self.animation_dead_frames = 200
        # Cargar la imagen del personaje
        self.update_image(self.actual_animation)

        self.rect = self.image.get_rect(bottomleft = (x,y + self.heigh))

    # Funcion que actualiza la imagen del sprite de los distintos enemigos, se encarga principalmente de gestionar las
    # animaciones, se llama en cada actualización
    def update_image(self, animation_array):
        actual_time = pygame.time.get_ticks()

        # Cooldown entre cada una de las imagenes
        cooldown_animation = 180
        frame_index = self.frame_index_idle

        # Si se ha cumplido el tiempo de cooldown entre animacion se modifica la imagen
        if actual_time - self.update_time >= cooldown_animation:
            frame_index += 1
            self.update_time = actual_time
            if frame_index >= len(animation_array):
                frame_index = 0

        self.frame_index_idle = frame_index
        self.animation_image = animation_array[frame_index]

        # Analizamos en que sentido esta mirando el personaje para hacer flip o no a la imagen
        if self.facing == 'left':
            self.image = pygame.transform.flip(self.animation_image, True, False)
        else:
            self.image = self.animation_image


        self.image = pygame.transform.scale(self.image, (RUN_SCALE_ENEMY))


    # Se actualiza cada personaje, primero se calcula el movimiento que este realiza según su estado y su posición,
    # luego se calculan las posiciones con el ataque del jugador y por último las colisiones los objetos del nivel,
    # aqui también se comprueba si el enemigo está 'vivo', nótese que necesitan estar en pantalla para que se lleguen
    # a actualizar
    def update(self):
        if self.in_screen():
            self.movement()
            self.collide_enemies()
            self.rect.x += self.x_change
            self.collide_blocks(self.fase.collide_Fase(self),"x")

            self.rect.y += self.y_change
            self.collide_blocks(self.fase.collide_Fase(self),"y")

        if self.health <= 0:
            self.death()

        self.x_change = 0
        self.y_change = 0

    # Se llama a esta función cuando el enemigo está muerto, se tarda un poco el kill() el personaje para
    # poder añadir las animaciones de muerte
    def death(self):
        self.isdeath = True
        if self.animation_dead_frames <= 0:
            self.kill()
        else:
            self.animation_dead_frames -= 1

    # Función booleana que devuelve si el enemigo está o no en la pantalla
    def in_screen(self):
        if self.rect.x + self.width < 0 or self.rect.x > WIN_WIDTH:
            return False
        elif self.rect.y + self.heigh < 0 or self.rect.y > WIN_HEIGHT:
            return False
        else:
            return True

    # Función booleana que devuelve si el enemigo está cerca del jugador, además se encarga se actualizar la dirección
    # del enemigo, necesario para que el enemigo vaya en la direccion en la que está el personaje
    def checkPlayer(self):
        dx = np.sqrt((self.fase.player.rect.x - self.rect.x)**2) < PIXELS_ENEMIES_AGRO_X
        dy = np.sqrt((self.fase.player.rect.y - self.rect.y)**2) < PIXELS_ENEMIES_AGRO_Y
        if dx and dy:
            if self.fase.player.rect.x > self.rect.x:
                self.facing = 'right'
            else:
                self.facing = 'left'
        return dx and dy

    # Función que en base a la dirección del personaje y su estado, mueve a los distintos personajes en el mapa
    # nótese que necesitan estar en pantalla para que se lleguen a mover
    def movement(self):
        if self.frames_hit <= 0:
            self.y_change += GRAVITY
        if self.state == 'hitted':
            self.frames_hit -= 1
            if self.frames_hit > 0:
                if self.facing == 'right':
                    self.x_change -= ENEMIES_SPEED_HIT
                elif self.facing == 'left':
                    self.x_change += ENEMIES_SPEED_HIT
            else:
                self.state = 'normal'
        elif self.facing == 'left' and self.health > 0:
            if self.checkPlayer():
                self.actual_animation = self.idle_animations_angry
                self.update_image(self.actual_animation)
                self.state = 'agro'
                self.x_change -= ENEMIES_SPEED_AGRO
            else:
                self.actual_animation = self.idle_animations
                self.state = 'normal'
                self.update_image(self.actual_animation)
                self.x_change -= ENEMY_SPEED
        elif self.facing == 'right' and self.health > 0:
            if self.checkPlayer():
                self.actual_animation = self.idle_animations_angry
                self.state = 'agro'
                self.update_image(self.actual_animation)
                self.x_change += ENEMIES_SPEED_AGRO
            else:
                self.actual_animation = self.idle_animations
                self.state = 'normal'
                self.update_image(self.actual_animation)
                self.x_change += ENEMY_SPEED

    # Distintas funciones de colisión de los enemigos, con los bloques que limitan su rango de acción y con los bloques
    # que conforman el nivel del juego
    def collide_blocks(self, collision, direction):
         #Comprobamos con que choca
        if collision[0] == "Solid":
            self.solid_Collision(collision[1],direction)
        elif collision[0] == "Limit":
            self.solid_Collision(collision[1],direction)
    def solid_Collision(self, blocks, direction):
        if  direction == "x":
            if self.x_change > 0:
                self.rect.x = blocks[0].rect.left - self.rect.width
                if self.state == 'normal':
                    self.facing = 'left'
            if self.x_change < 0:
                self.rect.x = blocks[0].rect.right
                if self.state == 'normal':
                    self.facing = 'right'
        if  direction == "y":
            if self.y_change > 0:
                self.rect.y = blocks[0].rect.top - self.rect.height
            if self.y_change < 0:
                self.rect.y = blocks[0].rect.bottom

    # Función de colisión de cada uno de los enemigos con el sprite de ataque, en caso de que haya se cambia el estado a
    # 'hitted' y se resta vida al enemigo.
    def collide_enemies(self):
        if self.fase.player.attack.attacking:
            hits = pygame.sprite.spritecollide(self.fase.player.attack, self.owngroup, False)
            if hits and self.state != 'hitted':
                self.state = 'hitted'
                self.frames_hit = FRAMES_ENEMIES_HIT
                self.health -= self.fase.player.damage_attack()
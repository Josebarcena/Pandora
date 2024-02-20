import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones_idle, animaciones_run):
        self.flip = False
        self.animaciones_idle = animaciones_idle
        self.animaciones_run = animaciones_run
        self.animacion_actual = self.animaciones_idle  # Inicialmente, el personaje está en estado de reposo
        # Actualizacion de IDLE
        self.frame_index_idle = 0
        self.update_time_idle = pygame.time.get_ticks()  # Temporizador para animaciones de IDLE
        self.image = animaciones_idle[self.frame_index_idle]
        # Actualizacion de RUN
        self.frame_index_run = 0
        self.update_time_run = pygame.time.get_ticks()  # Temporizador para animaciones de RUN
        # Forma del personaje
        self.shape = pygame.Rect(0, 0, constantes.TAMANHO, constantes.TAMANHO)
        self.shape.center = (x, y)

    def movimiento(self, delta_x, delta_y):
        # Determinar si hay que voltear al personaje o no
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False

        self.shape.x += delta_x
        self.shape.y += delta_y

    def update(self):
        cooldown_animacion_idle = 150
        self.image = self.animacion_actual[self.frame_index_idle]
        if pygame.time.get_ticks() - self.update_time_idle >= cooldown_animacion_idle:
            self.frame_index_idle += 1
            self.update_time_idle = pygame.time.get_ticks()
            if self.frame_index_idle >= len(self.animacion_actual):
                self.frame_index_idle = 0

    def update_run(self):
        cooldown_animacion_run = 100  # Cooldown para las animaciones de RUN
        if pygame.time.get_ticks() - self.update_time_run >= cooldown_animacion_run:
            self.frame_index_run += 1
            self.update_time_run = pygame.time.get_ticks()
            if self.frame_index_run >= len(self.animacion_actual):
                self.frame_index_run = 0
        # Se asegura de que frame_index_run no exceda el tamaño de la lista de animaciones
        if self.frame_index_run < len(self.animacion_actual):
            self.image = self.animacion_actual[self.frame_index_run]
        else:
            self.frame_index_run = 0

    def dibujar(self, interfaz):
        # Flipear la imagen según la dirección del personaje
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.shape)

    def set_animacion_idle(self):
        self.animacion_actual = self.animaciones_idle
        if self.frame_index_idle >= len(self.animacion_actual):
            self.frame_index_idle = 0
        self.update()

    def set_animacion_run(self):
        self.animacion_actual = self.animaciones_run
        if self.frame_index_run >= len(self.animacion_actual):
            self.frame_index_run = 0
        self.update_run()

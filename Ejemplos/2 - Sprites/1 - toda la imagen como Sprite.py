# -*- coding: utf-8 -*-

# -------------------------------------------------
# Importar las librerías
# -------------------------------------------------

import pygame, sys, os
from pygame.locals import *

# -------------------------------------------------
# Funciones auxiliares
# -------------------------------------------------

# El colorkey es es color que indicara la transparencia
#  Si no se usa, no habra transparencia
#  Si se especifica -1, el color de transparencia sera el del pixel (0,0)
#  Si se especifica un color, ese sera la transparencia

def load_image(name, colorkey=None):
    fullname = os.path.join('imagenes', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

# -------------------------------------------------
# Clases de los objetos del juego
# -------------------------------------------------

class Jugador(pygame.sprite.Sprite):
    "Jugador"

    def __init__(self):
        # Primero invocamos al constructor de la clase padre
        pygame.sprite.Sprite.__init__(self);
        # Se carga la imagen
        self.imagen = load_image('Jugador.png', -1)
        self.imagen = self.imagen.convert_alpha()
        # El rectangulo y la posicion que tendra
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (100,100)
        

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
        

# -------------------------------------------------
# Funcion principal del juego
# -------------------------------------------------

def main():

    # Inicializar pygame
    pygame.init()

    # Crear la pantalla
    pantalla = pygame.display.set_mode((800, 600), 0, 32)

    # Creamos el objeto reloj para sincronizar el juego
    reloj = pygame.time.Clock()

    # Poner el título de la ventana
    pygame.display.set_caption('Ejemplo de uso de Sprites')

    # Cargar la imagen del hombre
    jugador = Jugador()

    # Variable que controla la posición del Sprite (horizontal)
    pos = 100

    # El bucle de eventos
    while True:

        # Hacemos que el reloj espere a un determinado fps
        reloj.tick(60)

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Modificar posición en función de la tecla pulsada
        teclasPulsadas = pygame.key.get_pressed()
        if teclasPulsadas[K_LEFT]:
            jugador.rect.centerx -= 1
        if teclasPulsadas[K_RIGHT]:
            jugador.rect.centerx += 1
        # Si la tecla es Escape
        if teclasPulsadas[K_ESCAPE]:
            # Se sale del programa
            pygame.quit()
            sys.exit()

        # Dibujar el fondo de color
        pantalla.fill((133,133,133))

        # Dibujar el Sprite
        jugador.dibujar(pantalla)

        # Actualizar la pantalla
        pygame.display.update()


if __name__ == "__main__":
    main()

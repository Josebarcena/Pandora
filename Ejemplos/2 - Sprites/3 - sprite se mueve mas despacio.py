# -*- coding: utf-8 -*-

# -------------------------------------------------
# Importar las librerías
# -------------------------------------------------

import pygame, sys, os
from pygame.locals import *

QUIETO = 0
IZQUIERDA = 1
DERECHA = 2

RETARDO_ANIMACION_JUGADOR = 5 # updates que durará cada imagen del personaje
                              # debería de ser un valor distinto para cada postura

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
        # Se carga la hoja
        self.hoja = load_image('Jugador.png',-1)
        self.hoja = self.hoja.convert_alpha()
        # El rectangulo y la posicion que tendra
        self.rect = pygame.Rect((7,25), (30, 40))
        self.posicionx = 100
        self.posiciony = 100
        # El movimiento que esta realizando
        self.movimiento = QUIETO

        # Leemos las coordenadas de un archivo de texto
        pfile=open('imagenes/coordJugador.txt','r')
        datos=pfile.read()
        pfile.close()
        datos = datos.split()
        self.numPostura = 1;
        self.numImagenPostura = 0;
        cont = 0;
        numImagenes = [6, 12]        
        self.coordenadasHoja = [];
        for linea in range(0, 2):
            self.coordenadasHoja.append([])
            tmp = self.coordenadasHoja[linea]
            for postura in range(1, numImagenes[linea]+1):
                tmp.append(pygame.Rect((int(datos[cont]), int(datos[cont+1])), (int(datos[cont+2]), int(datos[cont+3]))))
                cont += 4

        # El retardo a la hora de cambiar la imagen del Sprite (para que no se mueva demasiado rápido)
        self.retardoMovimiento = 0;


    def dibujar(self, pantalla):
        # 
        # Parametros de blit:
        #  Imagen
        #  Posicion en la pantalla
        #  Rectangulo dentro de la imagen
        pantalla.blit(self.hoja, (self.posicionx, self.posiciony), self.coordenadasHoja[self.numPostura][self.numImagenPostura])


    def actualizarPostura(self, siguientePostura):
        self.retardoMovimiento -= 1
        # Miramos si ha pasado el retardo
        if (self.retardoMovimiento < 0):
            self.retardoMovimiento = RETARDO_ANIMACION_JUGADOR
            # Si ha pasado, actualizamos la postura
            self.numImagenPostura += siguientePostura
            if self.numImagenPostura >= len(self.coordenadasHoja[self.numPostura]):
                self.numImagenPostura = 0;
            if self.numImagenPostura < 0:
                self.numImagenPostura = len(self.coordenadasHoja[self.numPostura])-1

    
    def mover(self, direccion):
        self.movimiento = direccion


    def update(self):
        # Si vamos a la izquierda
        if self.movimiento == IZQUIERDA:
            # Actualizamos la posicion
            self.posicionx -= 2
            # Actualizamos la imagen a mostrar
            self.actualizarPostura(1)
            # Su siguiente movimiento (si no se pulsa mas) sera estar quieto
            self.movimiento = QUIETO
        # Si vamos a la derecha
        elif self.movimiento == DERECHA:
            # Actualizamos la posicion
            self.posicionx += 2
            # Actualizamos la imagen a mostrar
            self.actualizarPostura(-1)
            # Su siguiente movimiento (si no se pulsa mas) sera estar quieto
            self.movimiento = QUIETO
        return
        
    


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

    # Creamos el objeto jugador
    jugador = Jugador()

    # El bucle de eventos
    while True:

        # Hacemos que el reloj espere a un determinado fps
        reloj.tick(60)

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        teclasPulsadas = pygame.key.get_pressed()

        # Si la tecla es Escape
        if teclasPulsadas[K_ESCAPE]:
            # Se sale del programa
            pygame.quit()
            sys.exit()

        # Indicamos la acción a realizar segun la tecla pulsada
        elif teclasPulsadas[K_LEFT]:
            jugador.mover(IZQUIERDA)
        elif teclasPulsadas[K_RIGHT]:
            jugador.mover(DERECHA)


        # Actualizamos el jugador
        jugador.update()


        # Dibujar el fondo de color
        pantalla.fill((133,133,133))

        # Dibujar el Sprite
        jugador.dibujar(pantalla)

        # Actualizar la pantalla
        pygame.display.update()


if __name__ == "__main__":
    main()

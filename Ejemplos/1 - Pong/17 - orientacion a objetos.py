# -*- coding: utf-8 -*-
# -------------------------------------------------
# Importar las librerías
# -------------------------------------------------
import pygame, sys, time
from pygame.locals import *

# -------------------------------------------------
# Constantes
# -------------------------------------------------

BLANCO = (255,255,255)

# Frames por segundo
fps = 60

# Resolución de la pantalla
MaxX = 800
MaxY = 600

# Tamano de cada raqueta
tamanoRaquetaX = 10
tamanoRaquetaY = 50

# Movimiento de la raqueta
velocidadRaquetaY = 5

# -------------------------------------------------
# Clases de los objetos del juego
# -------------------------------------------------

# -------------------------------------------------
# Raqueta

class Raqueta():
    "Las raquetas de ambos jugadores"

    def __init__(self, posicion, tamano, posicionMarcador):
        self.posicion = posicion
        self.tamano = tamano
        self.puntos = 0
        self.posicionMarcador = posicionMarcador
        self.tipoLetra = pygame.font.SysFont('arial', 96)

    # Controla que ninguna raqueta se vaya por arriba o por abajo
    def controlaY(self):
        # Si se sale por arriba
        if self.posicion[1] < 0:
            self.posicion[1] = 0
        # Si se sale por abajo
        if self.posicion[1] > MaxY - self.tamano[1]:
            self.posicion[1] = MaxY - self.tamano[1]

    # Controla a ver si hay colision con la pelota
    def colision(self, pelota):
        return pelota.posicion[0] - pelota.radio < self.posicion[0] + self.tamano[0] and pelota.posicion[0] + pelota.radio > self.posicion[0] and pelota.posicion[1] - pelota.radio < self.posicion[1] + self.tamano[1] and pelota.posicion[1] + pelota.radio > self.posicion[1]

    # Dibuja la raqueta
    def dibuja(self, pantalla, color):
        pygame.draw.rect(pantalla, color, (self.posicion[0], self.posicion[1], self.tamano[0], self.tamano[1]))

    # Dibuja el marcador
    def marcador(self, pantalla, color):
        marcador = self.tipoLetra.render(str(self.puntos), True, color)
        pantalla.blit(marcador, (self.posicionMarcador[0], self.posicionMarcador[1], 50, 50))


# -------------------------------------------------
# Pelota
    
class Pelota():
    "La pelota y su comportamiento"

    def __init__(self, radio, sonidoRaqueta, sonidoPunto):
        self.posicion = [100, 100];
        self.radio = radio
        self.velocidad = [2, 2];
        self.sonidoRaqueta = sonidoRaqueta
        self.sonidoPunto = sonidoPunto

    # Actualiza la posicion de la pelota y controla la puntuacion y que no se salga
    def update(self, jugador1, jugador2):

        # Miramos a ver si hay colision con la raqueta de algún jugador
        if jugador1.colision(self) or jugador2.colision(self):
            # Invertimos la velocidad en el eje X
            self.velocidad[0] = -self.velocidad[0]
            # Reproducimos el sonido de la raqueta
            self.sonidoRaqueta.play();

        # Miramos a ver si la pelota está en el límite en el eje X
        if self.posicion[0] <= self.radio or self.posicion[0] >= MaxX - self.radio:
            # Sumamos los puntos al jugador correspondiente
            if self.posicion[0] <= self.radio:
                jugador2.puntos += 1
            else:
                jugador1.puntos += 1
            # Reproducimos el sonido de los aplausos
            self.sonidoPunto.play();

            # Realizamos una pausa
            time.sleep(1)
            # Ponemos la pelota en el centro
            self.posicion[0] = MaxX / 2;
            self.posicion[1] = MaxY / 2;
            # Invertimos la velocidad en el eje X (para que vaya contra el otro jugador)
            self.velocidad[0] = -self.velocidad[0]
                
        # Miramos a ver si la pelota está en el límite en el eje Y
        if self.posicion[1] < self.radio or self.posicion[1] > MaxY - self.radio:
            # Invertimos la velocidad en el eje Y
            self.velocidad[1] = -self.velocidad[1]
        
        # Actualizamos la posición de la pelota
        self.posicion[0] += self.velocidad[0]
        self.posicion[1] += self.velocidad[1]
        

    # Dibuja la pelota
    def dibuja(self, pantalla, color):
        pygame.draw.circle(pantalla, color, (self.posicion[0],self.posicion[1]),self.radio,0)


    
# -------------------------------------------------
# Funcion principal del juego
# -------------------------------------------------

def main():

    # Inicializar la librería de pygame
    pygame.init()

    # Sonidos del juego (tomados de http://soungle.com/ )
    sonidoRaqueta = pygame.mixer.Sound('Ping_Pong.wav');
    sonidoAplausos = pygame.mixer.Sound('Aplausos.wav');

    # Creamos ambos jugadores
    jugador1 = Raqueta([50, MaxY/2], [tamanoRaquetaX, tamanoRaquetaY], [MaxX/4, MaxY/8])
    jugador2 = Raqueta([MaxX-50-tamanoRaquetaX, MaxY/2], [tamanoRaquetaX, tamanoRaquetaY], [MaxX*3/4, MaxY/8])

    # Creamos la pelota
    pelota = Pelota(4, sonidoRaqueta, sonidoAplausos)


    # Creamos la pantalla
    pantalla = pygame.display.set_mode((MaxX,MaxY))


    # Creamos el objeto reloj para sincronizar el juego
    reloj = pygame.time.Clock()

    # Permitimos que la tecla este pulsada
    pygame.key.set_repeat(1, 25)

    # Eliminamos el raton
    pygame.mouse.set_visible(False)

    # Imagen de fondo
    imagenFondo = pygame.image.load('pistaTenis.jpg').convert();

    # Se muestra el mensaje inicial
    tipoLetra = pygame.font.SysFont('arial', 96)
    pantalla.blit(tipoLetra.render('PONG', True, BLANCO), (50, MaxY/4, 200, 100))
    pantalla.blit(tipoLetra.render('Pulse cualquier tecla', True, BLANCO), (20, MaxY/2, 200, 100))
    pygame.display.update()
    # Y se espera hasta que se pulse alguna tecla
    esperar = True
    while esperar:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                esperar = False



    # Bucle infinito: aqui comienza el juego
    while True:

        # Hacemos que el reloj espere a un determinado fps
        reloj.tick(60)

        # Para cada evento posible
        for evento in pygame.event.get():

            # Si el evento es la pulsación de una tecla
            if evento.type == KEYDOWN:

                # Si la tecla es Escape
                if evento.key == K_ESCAPE:
                    # Se sale del programa
                    pygame.quit()
                    sys.exit()

                # si no, si es la tecla 'q'
                elif evento.key == K_q:
                    # Se mueve la raqueta del jugador 1 arriba
                    jugador1.posicion[1] -= velocidadRaquetaY

                # si no, si es la tecla 'a'
                elif evento.key == K_a:
                    # Se mueve la raqueta del jugador 1 abajo
                    jugador1.posicion[1] += velocidadRaquetaY

                # si no, si es la tecla 'o'
                elif evento.key == K_o:
                    # Se mueve la raqueta del jugador 2 arriba
                    jugador2.posicion[1] -= velocidadRaquetaY

                # si no, si es la tecla 'l'
                elif evento.key == K_l:
                    # Se mueve la raqueta del jugador 2 abajo
                    jugador2.posicion[1] += velocidadRaquetaY





        # Comprobamos que ninguna de las dos raquetas se hayan ido por arriba o abajo
        jugador1.controlaY()
        jugador2.controlaY()

        # Actualizamos el comportamiento de la pelota
        pelota.update(jugador1, jugador2)





        # Ponemos la imagen de fondo
        pantalla.blit( imagenFondo, (0, 0))

        # Mostramos los marcadores
        jugador1.marcador(pantalla, BLANCO);
        jugador2.marcador(pantalla, BLANCO);
            
        # Dibujamos cada raqueta
        jugador1.dibuja(pantalla, BLANCO)
        jugador2.dibuja(pantalla, BLANCO)

        # Dibujamos la pelota
        pelota.dibuja(pantalla, BLANCO)

        
        # Actualizamos la pantalla
        pygame.display.update()


if __name__ == "__main__":
    main()

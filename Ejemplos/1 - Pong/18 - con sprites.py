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

# Movimiento de la raqueta
velocidadRaquetaY = 5

# -------------------------------------------------
# Clases de los objetos del juego
# -------------------------------------------------

# -------------------------------------------------
# Raqueta

class Raqueta(pygame.sprite.Sprite):
    "Las raquetas de ambos jugadores"

    def __init__(self, posicion, posicionMarcador):
        # Primero invocamos al constructor de la clase padre
        pygame.sprite.Sprite.__init__(self);
        # Cargamos la imagen
        self.imagen = pygame.image.load("raqueta.png");
        # El rectangulo donde estara la imagen
        self.rect = self.imagen.get_rect()
        self.rect.centerx = posicion[0];
        self.rect.centery = posicion[1];
        # El resto de atributos
        self.puntos = 0
        self.posicionMarcador = posicionMarcador
        self.tipoLetra = pygame.font.SysFont('arial', 96)

    # Controla que ninguna raqueta se vaya por arriba o por abajo
    def controlaY(self):
        # Si se sale por arriba
        if self.rect.top <= 0:
            self.rect.top = 0
        # Si se sale por abajo
        if self.rect.bottom >= MaxY:
            self.rect.bottom = MaxY


    # Controla a ver si hay colision con la pelota
    def colision(self, pelota):
        return self.rect.colliderect(pelota.rect)

    # Dibuja la raqueta
    def dibuja(self, pantalla):
        pantalla.blit(self.imagen, self.rect);

    # Dibuja el marcador
    def marcador(self, pantalla, color):
        marcador = self.tipoLetra.render(str(self.puntos), True, color)
        pantalla.blit(marcador, (self.posicionMarcador[0], self.posicionMarcador[1], 50, 50))


# -------------------------------------------------
# Pelota
    
class Pelota(pygame.sprite.Sprite):
    "La pelota y su comportamiento"

    def __init__(self, sonidoRaqueta, sonidoPunto):
        # Primero invocamos al constructor de la clase padre
        pygame.sprite.Sprite.__init__(self);
        # Cargamos la imagen
        self.imagen = pygame.image.load('pelota.png');
        # El rectangulo donde estara la imagen
        self.rect = self.imagen.get_rect()
        self.rect.centerx = MaxX/2;
        self.rect.centery = MaxY/2;
        # El resto de atributos
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
        if self.rect.left <= 0 or self.rect.right >= MaxX:
            # Sumamos los puntos al jugador correspondiente
            if self.rect.left <= 0:
                jugador2.puntos += 1
            else:
                jugador1.puntos += 1
            # Reproducimos el sonido de los aplausos
            self.sonidoPunto.play();

            # Realizamos una pausa
            time.sleep(1)
            # Ponemos la pelota en el centro
            self.rect.centerx = MaxX / 2;
            self.rect.centery = MaxY / 2;
            # Invertimos la velocidad en el eje X (para que vaya contra el otro jugador)
            self.velocidad[0] = -self.velocidad[0]
                
        # Miramos a ver si la pelota está en el límite en el eje Y
        if self.rect.top <= 0 or self.rect.bottom >= MaxY:
            # Invertimos la velocidad en el eje Y
            self.velocidad[1] = -self.velocidad[1]
        
        # Actualizamos la posición de la pelota
        self.rect.move_ip((self.velocidad[0], self.velocidad[1]))
        

    # Dibuja la pelota
    def dibuja(self, pantalla):
        pantalla.blit(self.imagen, self.rect);


    
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
    jugador1 = Raqueta([50,      MaxY/2], [MaxX/4,   MaxY/8])
    jugador2 = Raqueta([MaxX-50, MaxY/2], [MaxX*3/4, MaxY/8])

    # Creamos la pelota
    pelota = Pelota(sonidoRaqueta, sonidoAplausos)


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
                    jugador1.rect.centery -= velocidadRaquetaY

                # si no, si es la tecla 'a'
                elif evento.key == K_a:
                    # Se mueve la raqueta del jugador 1 abajo
                    jugador1.rect.centery += velocidadRaquetaY

                # si no, si es la tecla 'o'
                elif evento.key == K_o:
                    # Se mueve la raqueta del jugador 2 arriba
                    jugador2.rect.centery -= velocidadRaquetaY

                # si no, si es la tecla 'l'
                elif evento.key == K_l:
                    # Se mueve la raqueta del jugador 2 abajo
                    jugador2.rect.centery += velocidadRaquetaY





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
        jugador1.dibuja(pantalla)
        jugador2.dibuja(pantalla)

        # Dibujamos la pelota
        pelota.dibuja(pantalla)

        
        # Actualizamos la pantalla
        pygame.display.update()


if __name__ == "__main__":
    main()

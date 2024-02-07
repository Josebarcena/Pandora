# -*- encoding: utf-8 -*-

# Modulos
import pygame, pyglet
import sys
from escena import *
from pygame.locals import *

FPS = 60

class Director():

    def __init__(self):
        # Pila de escenas
        self.pila = []
        # Flag que nos indica cuando quieren salir de la escena de pygame
        self.salir_escena_pygame = False

    def buclePygame(self, escena):

        # Cogemos el reloj de pygame
        reloj = pygame.time.Clock()

        # Ponemos el flag de salir de la escena a False
        self.salir_escena_pygame = False

        # Eliminamos todos los eventos producidos antes de entrar en el bucle
        pygame.event.clear()
        
        # El bucle del juego, las acciones que se realicen se harán en cada escena
        while not self.salir_escena_pygame:

            # Sincronizar el juego a 60 fps
            tiempo_pasado = reloj.tick(FPS)
            
            # Pasamos los eventos a la escena
            escena.eventos(pygame.event.get())

            # Actualiza la escena
            escena.update(tiempo_pasado)

            # Se dibuja en pantalla
            escena.dibujar(escena.screen)
            pygame.display.flip()




    def ejecutar(self):

        # Inicializamos la libreria de pygame (si no esta inicializada ya)
        pygame.init()
        # Creamos la pantalla de pygame (si no esta creada ya)
        self.screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        # Estas dos lineas realmente no son necesarias, se ponen aqui por seguridad,

        # Mientras haya escenas en la pila, ejecutaremos la de arriba
        while (len(self.pila)>0):

            # Se coge la escena a ejecutar como la que este en la cima de la pila
            escena = self.pila[len(self.pila)-1]

            # Si la escena es de pyame
            if isinstance(escena, EscenaPygame):

                # Ejecutamos el bucle
                self.buclePygame(escena)

            # Si no, si la escena es de pyglet
            elif isinstance(escena, EscenaPyglet):

                # Ejecutamos la aplicacion de pyglet
                pyglet.app.run()

                # Cuando hayamos terminado la animacion con pyglet, cerramos la ventana
                escena.close()

            else:
                raise Exception('No se que tipo de escena es')

        # Finalizamos la libreria de pygame y cerramos las ventanas
        pygame.quit()


    def pararEscena(self):
        if (len(self.pila)>0):
            escena = self.pila[len(self.pila)-1]
            # Si la escena es de pygame
            if isinstance(escena, EscenaPygame):
                # Indicamos en el flag que se quiere salir de la escena
                self.salir_escena_pygame = True
            # Si es una escena de pyglet
            elif isinstance(escena, EscenaPyglet):
                # Salimos del bucle de pyglet
                pyglet.app.exit()
            else:
                raise Exception('No se que tipo de escena es')

    def salirEscena(self):
        self.pararEscena()
        # Eliminamos la escena actual de la pila (si la hay)
        if (len(self.pila)>0):
            self.pila.pop()

    def salirPrograma(self):
        self.pararEscena()
        # Vaciamos la lista de escenas pendientes
        self.pila = []

    def cambiarEscena(self, escena):
        self.pararEscena()
        # Eliminamos la escena actual de la pila (si la hay)
        if (len(self.pila)>0):
            self.pila.pop()
        # Ponemos la escena pasada en la cima de la pila
        self.pila.append(escena)

    def apilarEscena(self, escena):
        self.pararEscena()
        # Ponemos la escena pasada en la cima de la pila
        #  (por encima de la actual)
        self.pila.append(escena)


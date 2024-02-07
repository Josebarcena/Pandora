#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importar modulos
import pygame
import fase
from fase import *



if __name__ == '__main__':

    # Inicializar pygame
    pygame.init()

    # Crear la pantalla
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA), 0, 32)

    # Creamos el objeto reloj para sincronizar el juego
    reloj = pygame.time.Clock()

    # Creamos la fase
    fase = Fase()


    # El bucle de eventos
    while True:

        # Sincronizar el juego a 60 fps
        tiempo_pasado = reloj.tick(60)

        # Coge la lista de eventos y se la pasa a la escena
        # Devuelve si se debe parar o no el juego
        if (fase.eventos(pygame.event.get())):
            pygame.quit()
            sys.exit()

        # Actualiza la escena
        # Devuelve si se debe parar o no el juego
        if (fase.update(tiempo_pasado)):
            pygame.quit()
            sys.exit()

        # Se dibuja en pantalla
        fase.dibujar(pantalla)
        pygame.display.flip()


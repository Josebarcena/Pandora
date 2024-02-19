import pygame
import sys

ANCHO = 1080
ALTO = 720
FASE = 1

if __name__ == '__main__': #Funcion necesaria para definir el main

    # Inicializar pygame
    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO, ALTO), 0, 32)
    reloj = pygame.time.Clock()

    fase = Fase()
    
    while True:

        tempo = reloj.tick(60)
        if (fase.eventos(pygame.event.get())):
            pygame.quit()
            sys.exit()

        fase.dibujar(pantalla)
        pygame.display.flip()
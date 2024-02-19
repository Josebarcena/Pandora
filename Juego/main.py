import pygame
import sys
import main_menu

ANCHO = 1080
ALTO = 720
FASE = 0


if __name__ == '__main__': #Funcion necesaria para definir el main

    # Inicializar pygame
    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO, ALTO), 0, 32)
    reloj = pygame.time.Clock()

    menu = main_menu.Menu_principal(pantalla)

    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if(FASE == 0):
            tempo = reloj.tick(30)
            menu.dibujar_fondo()   
            if (menu.eventos(pygame.event.get())):
                FASE = 1   
        if(FASE == 1):
            tempo = reloj.tick(60)
            print(FASE)
            
        pygame.display.flip()


import pygame
import sys

ANCHO = 1080
ALTO = 720
FASE = 1


class Menu_principal:

    

    def __init__(self, pantalla):
        self.fondo = pygame.image.load("Juego/Imagenes/bg.png")
        self.pantalla = pantalla
        self.fuente = pygame.font.SysFont("Barron", 40)
        self.color_fuente = (255, 255, 255)

    def dibujar_texto(self, text, x, y):
        img = self.fuente.render(text, True, self.color_fuente)
        pantalla.blit(img, (x,y))
    
    def dibujar_fondo(self):
        self.pantalla.blit(self.fondo, (0,0))
        self.dibujar_texto("Pulsa ESPACIO para empezar", ANCHO/(2.75), ALTO/1.25)
    
    

if __name__ == '__main__': #Funcion necesaria para definir el main

    # Inicializar pygame
    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO, ALTO), 0, 32)
    reloj = pygame.time.Clock()

    menu = Menu_principal(pantalla)

    
    while True:

        tempo = reloj.tick(120)

        menu.dibujar_fondo()   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

        pygame.display.flip()


import pygame
import sys
from pygame import mixer

ANCHO = 1080
ALTO = 720
FASE = 0


class Menu_principal:

    def __init__(self, pantalla):
        self.fondo = pygame.image.load("Juego/Imagenes/bg.png")
        self.pantalla = pantalla
        self.fuente = pygame.font.SysFont("Barron", 40)
        self.color_fuente = (255, 255, 255)
        mixer.init()
        mixer.music.load('Juego/Sonidos/intro.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play()

    def dibujar_texto(self, text, x, y):
        img = self.fuente.render(text, True, self.color_fuente)
        pantalla.blit(img, (x,y))
    
    def dibujar_fondo(self):
        self.pantalla.blit(self.fondo, (0,0))
        self.dibujar_texto("Pulsa ESPACIO para empezar", ANCHO/(2.75), ALTO/1.25)
    
    def eventos(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclasPulsadas = pygame.key.get_pressed()
        if teclasPulsadas[pygame.K_SPACE]:
            mixer.music.stop()
            return True 

if __name__ == '__main__': #Funcion necesaria para definir el main

    # Inicializar pygame
    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO, ALTO), 0, 32)
    reloj = pygame.time.Clock()

    menu = Menu_principal(pantalla)

    
    while True:

        tempo = reloj.tick(120)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if(FASE == 0):
            menu.dibujar_fondo()   
            if (menu.eventos(pygame.event.get())):
                FASE = 1   
        if(FASE == 1):
            print(FASE)
        pygame.display.flip()


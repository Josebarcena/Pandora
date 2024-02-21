import pygame
import sys
from pygame import mixer

ANCHO = 1280
ALTO = 720
FASE = 0


class Menu_principal:

    def __init__(self, pantalla): # constructor de la clase donde tambien se inicializa la musica
        self.fondo = pygame.image.load("Imagenes/bg.png")
        self.pantalla = pantalla
        self.fuente = pygame.font.SysFont("Barron", 40)
        self.color_fuente = (255, 255, 255)
        self.frame = 1

        mixer.init()
        mixer.music.load('Sonidos/intro.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play()

    def dibujar_texto(self, text, x, y): # escribimos el texto pasado por parametro con la fuente del menu y color que cambia de opacidad por frames
        img = self.fuente.render(text, True, self.color_fuente)
        img.set_alpha(255/(self.frame/40))

        self.frame += 1
        if (self.frame == 60):
                self.frame = 1
        self.pantalla.blit(img, (x,y))
        
    def dibujar_fondo(self): # dibujamos el fondo con el texto encima

        self.pantalla.blit(self.fondo, (0,0))
        self.dibujar_texto("Pulsa ENTER para empezar", ANCHO/(2.75), ALTO/1.25)
    
    def eventos(self,lista_eventos): # controlamos eventos por si el jugador sale o si inicia el juego
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclasPulsadas = pygame.key.get_pressed()
        if teclasPulsadas[pygame.K_RETURN]:
            mixer.music.stop()
            return True 

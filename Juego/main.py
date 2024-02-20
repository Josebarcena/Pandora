import pygame
import sys
import main_menu
from pytmx.util_pygame import load_pygame
from os.path import join
from Fase import *

ANCHO = 1280
ALTO = 720
FASE = 0

class Juego:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pandora\'s Fate")
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO), 0, 32)
        self.reloj = pygame.time.Clock()
        self.tempo = self.reloj.tick(60) / 1000
        self.fase = 0
        self.nivel_1 = {0: load_pygame(join(".","Fases","fase11.tmx"))}
        
        self.nivel_2 = join("Fases")
        self.nivel_3 = join("Fases")
        self.nivel_cargado = main_menu.Menu_principal(self.pantalla)

    def actualizar_menu_principal(self, menu):
        menu.dibujar_fondo()
        print(self.tempo)
        if (menu.eventos(pygame.event.get())):
            self.fase = 1
            self.nivel_cargado = Fase(self.nivel_1[0]) 

    def actualizar_fase_1(self, fase):
        fase.run(self.tempo/2)
        if (fase.eventos(pygame.event.get())):
            self.fase = 2
    
    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        
        while True:
            juego.eventos()

            if(self.fase == 0):
                print(self.tempo)
                self.actualizar_menu_principal(self.nivel_cargado)

            if(self.fase == 1):
                print(self.tempo)
                self.actualizar_fase_1(self.nivel_cargado)
            
            if(self.fase == 2):
                pass
                
            pygame.display.update()
    


if __name__ == '__main__': #Funcion necesaria para definir el main

    juego = Juego()
    juego.run()
    


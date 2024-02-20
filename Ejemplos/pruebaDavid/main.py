import sys
import pygame
from game import *

# Creamos nuestra instancia juego y comenzamos el juego
if __name__ == '__main__':
    g = Game()
    g.intro_screen()
    g.new()
    while g.running:
        g.main()

    pygame.quit()
    sys.exit()
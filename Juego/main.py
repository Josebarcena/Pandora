from Recursos.game import *
from Niveles.Menus import *
from Recursos.Gestor_recursos import *

# Creamos nuestra instancia juego y comenzamos el juego
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Pandora\'s Fate')

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    
    game = Game(screen, "SPLASH")
    game.run()

    pygame.quit()
    sys.exit() 
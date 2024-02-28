from Recursos.game import *
from Niveles.Menus import *

# Creamos nuestra instancia juego y comenzamos el juego
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Pandora\'s Game')

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    #creas el objeto game
    game = Game(screen, Splash(Main_menu(Fase1("fase13.tmx","fase12.png","fase1.mp3"))))
    game.run()

    pygame.quit()
    sys.exit()
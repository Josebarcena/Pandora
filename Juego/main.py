from game import *

# Creamos nuestra instancia juego y comenzamos el juego
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Pandora\'s Game')

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    states = {
        "Splash": Splash(),
        "MENU": Main_menu(),
        "FASE1": Fase1(),
    }
    game = Game(screen, states, "Splash")
    game.run()

    pygame.quit()
    sys.exit()
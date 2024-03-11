from Recursos.game import *
from Niveles.Menus import *
from Recursos.Gestor_recursos import *

# Creamos nuestra instancia juego y comenzamos el juego
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Pandora\'s Game')

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    GestorRecursos.create_xml([("score",0)])


    game = Game(screen, "FASE4")
    game.run()

    pygame.quit()
    sys.exit() 
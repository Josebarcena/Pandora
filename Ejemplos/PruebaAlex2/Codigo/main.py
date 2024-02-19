from ajustes import *
from nivel import Nivel
from pytmx.util_pygame import load_pygame
from os.path import join

class Juego:
    def __init__(self):
        pygame.init()
        self.superficie_ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption('Pandora\'s Fate')
        self.clock = pygame.time.Clock()

        ruta = join('..', 'Graficos', 'niveles', 'Mundo.tmx')

        self.tmx_mapas = {0: load_pygame(ruta)}
    
        self.nivel_actual = Nivel(self.tmx_mapas[0])

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.nivel_actual.run(dt)

            pygame.display.update()

if __name__ == '__main__':
    juego = Juego()
    juego.run()            

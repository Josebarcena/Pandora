from Niveles.Menus import *
from Niveles.Fase1 import *
from Niveles.fase3 import *
from Niveles.fase2 import *
from Niveles.fase4 import *

class Factory:
    def create_state(name, director):
        if name == "SPLASH":
            return Splash(director)
        elif name == "MAIN_MENU":
            return Main_menu(director)
        elif name == "FASE1":
            return Fase1(director)
        elif name == "FASE2":
            return Fase2(director)
        elif name == "FASE3":
            return Fase3(director)
        elif name == "FASE4":
            return Fase4(director)
        elif name == "PAUSE":
            return Pause_menu(director)
        elif name == "GAME_OVER":
            return Game_over(director)
        elif name == "WIN":
            return Win_menu(director)


from Niveles.Menus import *
from Niveles.Fase1 import *

class Factory:
    def create_state(name, director):
        if name == "SPLASH":
            return Splash(director)
        elif name == "MAIN_MENU":
            return Main_menu(director)
        elif name == "FASE1":
            return Fase1(director)
        elif name == "PAUSE":
            return Pause_menu(director)
        elif name == "GAME_OVER":
            return Game_Over(director)
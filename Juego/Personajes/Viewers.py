from Recursos.config import *

class Life_Bar(): #CLASE OBSERVADORA PARA LA VIDA
    def __init__(self):
        self.x = 40
        self.y = 40
        self.witdh = 300 
        self.height = 40 
        self.max_health = MAX_HEALTH
        self.hp = MAX_HEALTH

    def update(self, player):
        self.hp = player.health

    def draw(self, surface):
        ratio = self.hp/self.max_health
        pygame.draw.rect(surface, "red", (self.x, self.y, self.witdh, self.height))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.witdh * ratio, self.height))
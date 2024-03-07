from Recursos.config import *

class Life_Bar(): #CLASE OBSERVADORA PARA LA VIDA
    def __init__(self):
        self.x = 40
        self.y = 40
        self.width = 300 
        self.height = 40 
        self.max_health = MAX_HEALTH
        self.hp = MAX_HEALTH

    def update(self, player):
        self.hp = player.health

    def draw(self, surface):
        ratio = self.hp/self.max_health
        unit_width = self.width / self.max_health
        pygame.draw.rect(surface, "red", (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.width * ratio, self.height))
        for i in range(self.max_health):
            pygame.draw.rect(surface, "black", (self.x+(unit_width*i), self.y, 2, self.height))
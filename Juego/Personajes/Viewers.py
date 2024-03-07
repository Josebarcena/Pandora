from Recursos.config import *
from Recursos.Gestor_recursos import GestorRecursos

class Life_Bar(): #CLASE OBSERVADORA PARA LA VIDA
    def __init__(self):
        self.x = 40
        self.y = 40
        self.width = 64 * SCALE 
        self.height = 16 * SCALE
        self.max_health = MAX_HEALTH
        self.hp = MAX_HEALTH
        
        self.bar_width = 45 * SCALE
        self.bar_height = 2 * SCALE

        self.image = GestorRecursos.LoadImage("Imagenes","health.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.bar = GestorRecursos.LoadImage("Imagenes","health_bar.png")
        self.bar = pygame.transform.scale(self.bar, (self.bar_width, self.bar_height))


    def update(self, player):
        self.hp = player.health

    def draw(self, surface):
        ratio = self.hp/self.max_health
        unit_width = self.bar_width / self.max_health
        surface.blit(self.image, (self.x, self.y))
        self.bar = pygame.transform.scale(self.bar, ((self.bar_width/MAX_HEALTH) * self.hp, self.bar_height))
        surface.blit(self.bar, (self.x + 16 * SCALE, self.y + 5 *SCALE))
        for i in range(1, self.max_health):
            pygame.draw.rect(surface, "black", (self.x + 16 * SCALE+(unit_width*i), self.y + 5 * SCALE, 2, self.bar_height))





class Score(): #CLASE OBSERVADORA PARA LA VIDA
    def __init__(self, player):
        self.x = WIN_WIDTH - 80
        self.y = 40
        self.score = player.score
        self.font = pygame.font.SysFont(None, 36)

    def update(self, player):
        self.score = player.score

    def draw(self, surface):
        text_surface = self.font.render(str(self.score), True, LIGHT_BLUE)
        text_rect = text_surface.get_rect(bottomright=(self.x, self.y))

        # Dibujar el texto en la pantalla
        surface.blit(text_surface, text_rect)


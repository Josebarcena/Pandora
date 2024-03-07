class Life_Bar(): #CLASE OBSERVADORA PARA LA VIDA
    def __init__(self):
        self.hp = 5
    
    def update(self, player):
        self.hp = player.hp
class Life_Bar(): #CLASE OBSERVADORA PARA LA VIDA
    def __init__(self):
        self.hp = 0
    
    def update(self, player):
        print("VIDA = ",self.hp)
        self.hp = player.hp
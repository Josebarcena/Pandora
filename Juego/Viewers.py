class Life_Bar(): #CLASE OBSERVADORA PARA LA VIDA
    def __init__(self, player):
        self.hp = 5
        self.player = player
    
    def update(self, message):
        if message[0]:
            self.hp -= 1
            print("VIDA = ", self.hp)
            if self.hp <= 0:
                self.game_over()
    
    def game_over(self):
        self.player.recieve_update("DEATH")
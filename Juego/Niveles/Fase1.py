from Niveles.Fase import *
from Recursos.Gestor_recursos import *
from Niveles.blocks import *
from Niveles.Menus import *
from Personajes.player import *


class Fase1(Fase): #Clase para el primer nivel del juego
    def __init__(self, next_state = None):
        super(Fase1,self).__init__()
        self.all_sprites = pygame.sprite.Group() #Los grupos de sprites dependiendo de su fisica de colision
        self.upper_collision = pygame.sprite.Group()
        self.full_collision = pygame.sprite.Group()
        self.damage_collision = pygame.sprite.Group()
        self.stairs_collision = pygame.sprite.Group()
        self.meta = pygame.sprite.Group() #Especial si chocas es porque se cosidera completo el nivel

        self.player_layer = pygame.sprite.Group() #Otra especial para definir el jugador
        self.player = None
        self.enemies = pygame.sprite.Group()
        self.attacks = pygame.sprite.Group()


        self.stage_image = GestorRecursos.LoadImage("Imagenes", "fase12.png") #Se carga el png que hace de fondo del nivel (por encima del esqueleto)
        
        self.next_state = next_state # se define que nivel va despues si todo va bien

        self.sound = ("fase1.mp3") # el mp3 que sonara en la fase
        self.level = GestorRecursos.LoadImage("Fases","fase13.tmx") #El esqueleto del nivel
    

        self.createTilemap(self.level) #se llama para dibujar el mapa desde tiled


    def update(self, tick):
        if(self.player.hp <= 0):
            self.gameover()

    def createTilemap(self, tmx_map): #crea el mapa desde tiled
        collision_layers = { #las capas de los tiles segun sus fisicas
        'Solido': self.full_collision,
        'Semi': self.upper_collision,
        'Pincho': self.damage_collision,
        'Escalera': self.stairs_collision,
        'Meta': self.meta
        }

        for layer_name, collision_func in collision_layers.items(): #bucle para agregarlo en sus grupos
            for x, y, surface in tmx_map.get_layer_by_name(layer_name).tiles():
                Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites, collision_func))

        Stage(self, 0, 0, self.stage_image, self.all_sprites) #una vez cargado el esqueleto se pinta el png por encima
        
        for objeto in tmx_map.get_layer_by_name('Jugador'): #se carga el jugador por encima
            Player(self, objeto.x *SCALE, objeto.y*SCALE,self.player_layer)
            self.player = self.player_layer.sprites()[0]

    def get_event(self, event): # si se quiere cerrar el juego
            if event.type == pygame.QUIT:
                self.quit = True     

    def draw(self, surface): #la funcion que llama en bucle game para pintar cada frame la fase
        surface.fill((123,211,247))
        sprites = self.all_sprites
        sprites.update()
        self.screen_check(sprites)
        sprites.draw(surface)
        
        pygame.display.update()


    def collide_Fase(self, player): # chequea las colisiones con los bloques de las fases
        if ((hits := pygame.sprite.spritecollide(player, self.full_collision, False))):
            return ("Solid", hits)
        elif((hits := pygame.sprite.spritecollide(player, self.upper_collision, False))):
            return ("Platform", hits)
        elif((hits := pygame.sprite.spritecollide(player, self.damage_collision, False))):
            return ("Damage", hits)
        elif((hits := pygame.sprite.spritecollide(player, self.stairs_collision, False))):
            return ("Stairs", hits)
        elif((hits := pygame.sprite.spritecollide(player, self.meta, False))):
            self.done = True
            return (None,None)
        else:
            return (None,None)

    def gameover(self): #GAMEOVER se cambia el siguiente estado a game over y se marca la condicion en true
        self.next_state = Game_Over(Main_menu(Fase1()))
        self.done = True
from Niveles.Fase import *
from Recursos.Gestor_recursos import *
from Niveles.blocks import *
from Niveles.Menus import *
from Personajes.player import *
from Personajes.enemy import *
from Personajes.Objects import *
import random
import math


class Fase3(Fase): #Clase para el primer nivel del juego
    def __init__(self, director):
        super(Fase3,self).__init__()
        self.director = director
        self.all_sprites = pygame.sprite.Group() #Los grupos de sprites dependiendo de su fisica de colision
        self.visible_sprites = pygame.sprite.Group() #sprites que se pintaran
        self.upper_collision = pygame.sprite.Group()
        self.full_collision = pygame.sprite.Group()
        self.damage_collision = pygame.sprite.Group()
        self.stairs_collision = pygame.sprite.Group()
        self.objects_layer = pygame.sprite.Group()
        self.hope_layer = pygame.sprite.Group()
        self.limit = pygame.sprite.Group()
        self.meta = pygame.sprite.Group() #Especial si chocas es porque se cosidera completo el nivel
        self.stage = pygame.sprite.Group() #Para limitar la camara


        self.player_layer = pygame.sprite.Group() #Otra especial para definir el jugador
        self.player = None
        self.enemies_layer = pygame.sprite.Group()
        self.max_enemies = None
        self.enemies_pos = [(0,0)]
        self.range = None
        
        self.attacks = pygame.sprite.Group()


        self.stage_image = GestorRecursos.LoadImage("Imagenes", "fase31.png") #Se carga el png que hace de fondo del nivel (por encima del esqueleto)
        
        self.sound = ("fase3.mp3") # el mp3 que sonara en la fase
        self.level = GestorRecursos.LoadImage("Fases","fase3.tmx") #El esqueleto del nivel
    

        self.createTilemap(self.level) #se llama para dibujar el mapa desde tiled


    def update(self, tick, events):
        for event in events:
            self.get_event(event)
        if self.done:
            self.director.unstack_state()
        elif self.player.isdeath():
            self.gameover()

    def createTilemap(self, tmx_map): #crea el mapa desde tiled
        collision_layers = { #las capas de los tiles segun sus fisicas
        'Solido': self.full_collision,
        'Semi': self.upper_collision,
        'Pincho': self.damage_collision,
        'Escalera': self.stairs_collision,
        'Meta': self.meta,
        'Limite': self.limit
        }

        object_layers = {
            'Jugador': (self.player_layer, self.visible_sprites),
            'Enemigos': (self.enemies_layer, self.visible_sprites),
            'Pociones': (self.objects_layer, self.visible_sprites),
            'Esperanza': (self.hope_layer, self.visible_sprites)
        }

        Stage(self, 0, 0, self.stage_image, (self.visible_sprites,self.all_sprites, self.stage)) #una vez cargado el esqueleto se pinta el png por encima

        for layer_name, collision_func in collision_layers.items(): #bucle para agregarlo en sus grupos
            for x, y, surface in tmx_map.get_layer_by_name(layer_name).tiles():
                Sprite(self, x*TILESIZE*SCALE, y*TILESIZE*SCALE, surface, (self.all_sprites, collision_func))

        
        
        for object_name, group in object_layers.items(): 
            for objeto in tmx_map.get_layer_by_name(object_name): #se carga el jugador por encima
                if object_name == "Pociones":
                    small_Potion(self, objeto.x * SCALE, objeto.y * SCALE, group)
                elif object_name == "Esperanza":
                    Hope(self, objeto.x * SCALE, objeto.y * SCALE, group)
                elif object_name == "Jugador":
                    Player(self, objeto.x * SCALE, objeto.y * SCALE, group)
                    self.player = self.player_layer.sprites()[0]
               


            enemies = tmx_map.get_layer_by_name("Enemigos")
            self.range = list(range(0,len(enemies)))
            self.max_enemies = len(self.range) - 3

            while(len(self.enemies_layer) < self.max_enemies) and len(self.range)>0:
                index = random.choice(self.range)
                enemy = enemies[index]
                can_add = True

                for x , y in self.enemies_pos:
                    dist = abs(math.sqrt((enemy.x * SCALE - x)**2 + (enemy.y * SCALE - y)**2))
                    if dist <= 1000:
                        can_add = False
                        break
                
                if can_add:
                    self.enemies_pos.append((enemy.x * SCALE ,enemy.y * SCALE ))
                    Enemy(self, enemy.x * SCALE, enemy.y * SCALE, (self.enemies_layer, self.visible_sprites))
                self.range.remove(index)

    def get_event(self, event): # si se quiere cerrar el juego
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == KEYDOWN:
            # Verificar si se presiona una tecla específica
                if event.key == K_ESCAPE:
                    self.director.add_state("PAUSE", True)
                    self.director.flip_state()

    def draw(self, surface): #la funcion que llama en bucle game para pintar cada frame la fase
        surface.fill((123,211,247))
        sprites = self.all_sprites
        sprites.update()
        self.screen_check(sprites, self.player, self.stage.sprites()[0])
        self.visible_sprites.draw(surface)
        for viewer in self.player.viewers:
            viewer.draw(surface)
        pygame.display.update()


    def collide_Fase(self, player): # chequea las colisiones con los bloques de las fases

        if self.player_layer.has(player):
            if ((hits := pygame.sprite.spritecollide(player.hitbox, self.full_collision, False))):
                return ("Solid", hits)
            if((hits := pygame.sprite.spritecollide(player.hitbox, self.upper_collision, False))):
                return ("Platform", hits)
            elif((hits := pygame.sprite.spritecollide(player.hitbox, self.damage_collision, False))):
                self.gameover()
                return (None,None)
            elif((hits := pygame.sprite.spritecollide(player.hitbox, self.stairs_collision, False))):
                return ("Stairs", hits)
            elif((hits := pygame.sprite.spritecollide(player.hitbox, self.meta, False))):
                self.done = True
                return (None,None)
            elif((hits:= pygame.sprite.spritecollide(player.hitbox, self.objects_layer, False))):
                return ("Potion",hits)
            elif((hits:= pygame.sprite.spritecollide(player.hitbox, self.hope_layer, False))):
                return ("Hope",hits)
            elif((hits := pygame.sprite.spritecollide(player.hitbox, self.enemies_layer, False))):
                if(not hits[0].isdeath):
                    return("Damage",hits)
                else:
                    return(None,None)
            else:
                return (None,None)
        
        elif self.enemies_layer.has(player): 
            if ((hits := pygame.sprite.spritecollide(player, self.full_collision, False))):
                return ("Solid", hits)
            if((hits := pygame.sprite.spritecollide(player, self.limit, False))):
                    return ("Limit", hits)
            else:
                return (None,None)


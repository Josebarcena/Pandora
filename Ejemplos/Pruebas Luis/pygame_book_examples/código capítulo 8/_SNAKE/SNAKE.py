import pygame, random, sys

pygame.mixer.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

BALDOSA_TAMANIO = 32
BALDOSA_NUMERO = 15
MARCADOR_ANCHURA = 32

ALTURA = BALDOSA_TAMANIO * BALDOSA_NUMERO
ANCHURA = BALDOSA_TAMANIO * BALDOSA_NUMERO + MARCADOR_ANCHURA

PUNTO_UNIDAD = 1
DURACION_COMIDA_DESAPARECE = 5500

# CLASE SERPIENTE
class SERPIENTE(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.SONIDO_COMIDA = pygame.mixer.Sound('COMIDA.wav')
    self.SONIDO_COMIDA.set_volume(1.0)

    self.CABEZA = pygame.image.load("CABEZA.png").convert_alpha()
    self.image = self.CABEZA

    self.rect = self.image.get_rect()
    self.rect.y = (BALDOSA_NUMERO / 2) * BALDOSA_TAMANIO
    self.rect.x = (BALDOSA_NUMERO / 2) * BALDOSA_TAMANIO

    self.PUNTOS = 0
    self.DIRECCION = 'I'
    self.TERMINA = False

  def AGREGAR_NUEVO_CUERPO(self):
    nuevo_cuerpo = CUERPOS(self.rect.x, self.rect.y)
    LISTA_SERPIENTE.add(nuevo_cuerpo)
    LISTA_GLOBAL_SPRITES.add(nuevo_cuerpo)

  def update(self):
    COORD_ACTUAL_X = self.rect.x
    COORD_ACTUAL_Y = self.rect.y

    if self.DIRECCION == 'I':
      self.image = pygame.transform.rotate(self.CABEZA, 90)
      self.rect.x -= BALDOSA_TAMANIO
    elif self.DIRECCION == 'D':
      self.image = pygame.transform.rotate(self.CABEZA, -90)
      self.rect.x += BALDOSA_TAMANIO
    elif self.DIRECCION == 'A':
      self.image = pygame.transform.rotate(self.CABEZA, 0)
      self.rect.y -= BALDOSA_TAMANIO
    elif self.DIRECCION == 'B':
      self.image = pygame.transform.rotate(self.CABEZA, 180)
      self.rect.y += BALDOSA_TAMANIO

    for ELT in LISTA_SERPIENTE:
      x = ELT.GET_X()
      y = ELT.GET_Y()
      ELT.set_xy(COORD_ACTUAL_X, COORD_ACTUAL_Y)
      COORD_ACTUAL_X = x
      COORD_ACTUAL_Y = y

    if self.rect.x >= ALTURA:
      self.rect.x = 0
    elif self.rect.x < 0:
      self.rect.x = ALTURA - BALDOSA_TAMANIO
    elif self.rect.y >= ANCHURA:
      self.rect.y = MARCADOR_ANCHURA
    elif self.rect.y < MARCADOR_ANCHURA:
      self.rect.y = ANCHURA - MARCADOR_ANCHURA

    LISTA_COLISION_SERPIENTE = pygame.sprite.spritecollide(self, LISTA_SERPIENTE, False)
    if len(LISTA_COLISION_SERPIENTE):
      print("Perdido")
      self.TERMINA = True

    LISTA_COLISION_COMIDA = pygame.sprite.spritecollide(self, LISTA_COMIDA, False)
    for comida in LISTA_COLISION_COMIDA:
      comida.kill()
      self.AGREGAR_NUEVO_CUERPO()
      self.SONIDO_COMIDA.play()
      self.PUNTOS += PUNTO_UNIDAD


# CLASE CUERPOS
class CUERPOS(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load("CUERPOS.png").convert_alpha()

    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def GET_X(self):
    return self.rect.x

  def GET_Y(self):
    return self.rect.y

  def set_xy(self, x, y):
    self.rect.x = x
    self.rect.y = y

# CLASE COMIDA
class COMIDA(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load("COMIDA.png").convert_alpha()

    self.rect = self.image.get_rect()
    self.rect.y = random.randint(0, BALDOSA_NUMERO - 1) * BALDOSA_TAMANIO + MARCADOR_ANCHURA
    self.rect.x = random.randint(0, BALDOSA_NUMERO - 1) * BALDOSA_TAMANIO

    self.time = pygame.time.get_ticks()

  def update(self):
    if pygame.time.get_ticks() - self.time > DURACION_COMIDA_DESAPARECE:
      self.kill()

# VER_MARCADOR
def VER_MARCADOR():
  font = pygame.font.SysFont('Arial', BALDOSA_TAMANIO - 5)
  background = pygame.Surface((ALTURA, MARCADOR_ANCHURA))
  background = background.convert()
  background.fill(BLANCO)
  text = font.render("Puntos = %d" % _serpiente.PUNTOS, 1, NEGRO)
  textpos = text.get_rect(centerx=ALTURA / 2, centery=MARCADOR_ANCHURA / 2)
  background.blit(text, textpos)
  screen.blit(background, (0, 0))

pygame.init()

screen = pygame.display.set_mode([ALTURA, ANCHURA])
pygame.display.set_caption('El juego de la serpiente')

LISTA_SERPIENTE = pygame.sprite.Group()
LISTA_COMIDA = pygame.sprite.Group()
LISTA_GLOBAL_SPRITES = pygame.sprite.Group()

SONIDO_COMIDA = pygame.mixer.Sound('COMIDA.wav')
SONIDO_COMIDA.set_volume(1.0)

SONIDO_PERDIDO = pygame.mixer.Sound('PERDIDO.wav')
SONIDO_PERDIDO.set_volume(1.0)

_serpiente = SERPIENTE()
LISTA_GLOBAL_SPRITES.add(_serpiente)

reloj = pygame.time.Clock()

print("Empezamos...")

TERMINA = False

while not TERMINA:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      TERMINA = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT and _serpiente.DIRECCION != 'D':
        _serpiente.DIRECCION = 'I'
        break
      elif event.key == pygame.K_RIGHT and _serpiente.DIRECCION != 'I':
        _serpiente.DIRECCION = 'D'
        break
      elif event.key == pygame.K_UP and _serpiente.DIRECCION != 'B':
        _serpiente.DIRECCION = 'A'
        break
      elif event.key == pygame.K_DOWN and _serpiente.DIRECCION != 'A':
        _serpiente.DIRECCION = 'B'
        break

  if random.randint(0, 18) == 0:
    _comida = COMIDA()

    LISTA_CONFLICTO = pygame.sprite.spritecollide(_comida, LISTA_GLOBAL_SPRITES, False)
    if len(LISTA_CONFLICTO) == 0:
      SONIDO_COMIDA.play()
      LISTA_GLOBAL_SPRITES.add(_comida)
      LISTA_COMIDA.add(_comida)

  LISTA_GLOBAL_SPRITES.update()
  screen.fill(BLANCO)

  LISTA_GLOBAL_SPRITES.draw(screen)
  VER_MARCADOR()

  if _serpiente.TERMINA:
    SONIDO_PERDIDO.play()
    pygame.time.wait(5000)
    TERMINA = True

  pygame.display.flip()
  reloj.tick(7)

print("Su marcador : %d puntos" % _serpiente.PUNTOS)
pygame.quit()

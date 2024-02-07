# -*- encoding: utf-8 -*-

import pyglet
from escena import *
from fase import Fase
import random


VELOCIDAD_TANQUE = 100 # Pixels por segundo
VELOCIDAD_ROTACION_TANQUE = 10 # Grados por segundo
VELOCIDAD_CORREDOR = 150 # Pixels por segundo

# Funcion auxiliar que crea una animacion a partir de una imagen que contiene la animacion
#  dividida en filas y columnas
def crearFramesAnimacion(nombreImagen, filas, columnas):
    # Cargamos la secuencia de imagenes del archivo
    secuenciaImagenes = pyglet.image.ImageGrid(pyglet.image.load(nombreImagen), filas, columnas)
    # Creamos la secuencia de frames
    secuenciaFrames = []
    # Para cada fila, del final al principio
    for fila in range(filas, 0, -1):
        end = fila * columnas
        start = end - (columnas -1) -1
        # Para cada imagen de la fila
        for imagen in secuenciaImagenes[start:end:1]:
            # Creamos un frame con esa imagen, indicandole que tendra una duracion de 0.5 segundos
            frame = pyglet.image.AnimationFrame(imagen, 0.1)
            #  y la anadimos a la secuencia de frames
            secuenciaFrames.append(frame)

    # Devolvemos la secuencia de frames
    return secuenciaFrames




# -------------------------------------------------
# Clase para las animaciones que solo ocurriran una vez
#  (sin bucles)

class EscenaAnimacion(EscenaPyglet, pyglet.window.Window):

    def __init__(self, director):
        # Constructores de las clases padres
        EscenaPyglet.__init__(self, director)
        pyglet.window.Window.__init__(self, ANCHO_PANTALLA, ALTO_PANTALLA)

        # La imagen de fondo
        self.imagen = pyglet.image.load('imagenes/campo.jpg')
        self.imagen = pyglet.sprite.Sprite(self.imagen)
        self.imagen.scale = float(ANCHO_PANTALLA) / self.imagen.width

        # Las animaciones que habra en esta escena
        # No se crean aqui las animaciones en si, porque se empiezan a reproducir cuando se crean
        # Lo que se hace es cargar los frames de disco para que cuando se creen ya esten en memoria

        # Creamos el batch de las animaciones
        self.batch = pyglet.graphics.Batch()
        # Y los grupos para ponerlas por pantalla
        self.grupoDetras =  pyglet.graphics.Group(order=0)
        self.grupoMedio =   pyglet.graphics.Group(order=1)
        self.grupoDelante = pyglet.graphics.Group(order=2)

        # La animacion del tanque la creamos a partir de un gif animado
        self.tanque = pyglet.sprite.Sprite(pyglet.resource.animation('imagenes/tanque.gif'), batch=self.batch, group=self.grupoMedio)
        # Esta si que se crea porque estara desde el principio
        self.tanque.scale = 1.2
        self.tanque.rotation = -4
        self.tanque.x=0
        self.tanque.y=80


        # La animacion del humo
        self.animacionHumoFrames = [
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0001.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0002.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0003.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0004.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0005.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0006.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0007.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0008.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0009.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0010.png'), None),
            ]
        # El ultimo frame se pone con una duracion de None, porque el humo no se reproduce en bucle,
        #  sino solo una vez
        # Por ahora no creamos la animacion, porque se empezaria a reproducir,
        #  solo cargamos los frames de disco
        # Esta animacion aparecera en el segundo determinado
        pyglet.clock.schedule_once(self.aparecerHumo, 3.5)


        # La animacion de la explosion
        self.animacionExplosionFrames = crearFramesAnimacion('imagenes/fuego.png', 9, 5)
        self.animacionExplosion = None
        # Esta animacion aparecera en el segundo determinado
        pyglet.clock.schedule_once(self.aparecerExplosion, 4)
        # Esta animacion la tenemos que guardar como variable porque hay que mover su posicion


        # La animacion del fuego: creamos los frames
        self.animacionFuegoFrames = [
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0001.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0002.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0003.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0004.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0005.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0006.png'), 0.1) ]
        # Esta animacion aparecera cuando termine la del fuego, asi que se programa su aparicion
        #  cuando empiece esa


        # Registramos que aparezcan animaciones de humo por pantalla cada 0.8 segundos
        #  para dar la impresion de un bombardeo
        pyglet.clock.schedule_interval(self.aparecerHumoCielo, 0.4)


        # La animacion del corredor: hay que leerlo de la hoja de Sprite

        # Leemos la hoja del Sprite del fichero
        hoja = pyglet.image.load('imagenes/Jugador.png')

        # Introducimos manualmente el valor del canal alpha:
        #  Aquellos pixels cuyo RGB sea igual al pixel de la posicion (0, 0) no se veran
        rawimage = hoja.get_image_data()
        format = 'RGBA'
        pitch = rawimage.width * len(format)
        pixels = rawimage.get_data(format, pitch)
        pixels = list( pixels )
        r = pixels[0]
        g = pixels[1]
        b = pixels[2]
        for i in range(0, len(pixels), 4):
            if (pixels[i]==r) and (pixels[i+1]==g) and (pixels[i+2]==b):
                pixels[i+3] = str(chr(0))
            else:
                pixels[i+3] = str(chr(255))
        pixels = [str(p) for p in pixels]  # Convertir todos los elementos a cadena
        hoja.set_data('RGBA', pitch, "".join(pixels))

        # Leemos las coordenadas de un archivo de texto
        numImagenes = [6, 12, 6]
        pfile=open('imagenes/coordJugador.txt','r')
        datos=pfile.read()
        pfile.close()
        datos = datos.split()
        corredorFrames = []
        for coord in range(12):
            corredorFrames.append(pyglet.image.AnimationFrame(hoja.get_region(int(datos[24 + coord*4]), hoja.height-int(datos[24 + coord*4 + 1])-int(datos[24 + coord*4 + 3]), int(datos[24 + coord*4 + 2]), int(datos[24 + coord*4 + 3])), 0.1))
        # A partir de los frames, se crea la animacion
        self.animacionCorredor = pyglet.sprite.Sprite(pyglet.image.Animation(corredorFrames), batch=self.batch, group=self.grupoDetras)
        self.animacionCorredor.x=700
        self.animacionCorredor.y=40
        self.animacionCorredor.scale = 1.2
        # Se podria, igual que las anteriores, no haberla creado, sino haberlo hecho
        #  cuando fuese necesario que apareciera, pero en este caso se crea aqui y se
        #  pone como invisible hasta cuandos ea necesario que aparezca
        self.animacionCorredor.visible = False

        # Registramos que se actualice una vez por frame
        pyglet.clock.schedule_interval(self.update, 1/float(60))



    # El metodo para eliminar una animacion determinada
    def eliminarAnimacion(self, tiempo, animacion):
        animacion.delete()

    # Metodo que hace aparecer una animacion de humo en el cielo
    def aparecerHumoCielo(self, tiempo):
        animacionHumo = pyglet.sprite.Sprite(pyglet.image.Animation(self.animacionHumoFrames), batch=self.batch, group=self.grupoDetras)
        # La escalamos un factor aleatorio para dar sensacion de profundidad
        animacionHumo.scale = random.uniform(0.2, 1)
        # Decimos que aparezca en un sitio aleatorio del cielo
        animacionHumo.x = random.uniform(0, ANCHO_PANTALLA)
        animacionHumo.y = random.uniform(ALTO_PANTALLA/4, ALTO_PANTALLA)
        # Programamos que se elimine la animacion cuando termine
        pyglet.clock.schedule_once(self.eliminarAnimacion, animacionHumo.image.get_duration(), animacionHumo)

    # Metodo para hacer aparecer la animacion del humo en el tanque
    def aparecerHumo(self, tiempo):
        animacionHumo = pyglet.sprite.Sprite(pyglet.image.Animation(self.animacionHumoFrames), batch=self.batch, group=self.grupoDelante)
        animacionHumo.scale = 1.2
        animacionHumo.x = self.tanque.x
        animacionHumo.y = self.tanque.y
        # Programamos que se elimine la animacion cuando termine
        pyglet.clock.schedule_once(self.eliminarAnimacion, animacionHumo.image.get_duration(), animacionHumo)

    # Metodo para hacer aparecer la animacion de la explosion en el tanque
    def aparecerExplosion(self, tiempo):
        # Creamos la animacion de la explosion
        self.animacionExplosion = pyglet.sprite.Sprite(pyglet.image.Animation(self.animacionExplosionFrames), batch=self.batch, group=self.grupoDelante)
        self.animacionExplosion.scale = 1
        self.animacionExplosion.x = self.tanque.x-10
        self.animacionExplosion.y = self.tanque.y-15
        # Programamos para que aparezca el fuego cuando esta termine
        pyglet.clock.schedule_once(self.aparecerFuegoYCorredor, self.animacionExplosion.image.get_duration())

    # Metodo para hacer aparecer la animacion del fuego y del corredor
    def aparecerFuegoYCorredor(self, tiempo):
        # Creamos la animacion del fuego
        animacionFuego = pyglet.sprite.Sprite(pyglet.image.Animation( self.animacionFuegoFrames ), batch=self.batch, group=self.grupoDelante)
        animacionFuego.scale = 2
        animacionFuego.x = self.tanque.x-50
        animacionFuego.y = self.tanque.y-20
        # Eliminamos la variable de la animacion de la explosion
        self.animacionExplosion.delete()
        self.animacionExplosion = None
        # Y decimos que el corredor ya es visible
        self.animacionCorredor.visible = True


    
    # El evento relativo a la pulsacion de una tecla
    def on_key_press(self, symbol, modifiers):
        # Si se pulsa Escape, se sale del programa
        if symbol == pyglet.window.key.ESCAPE:
            self.terminarEscena()


    # el evento que se ejecuta cada vez que hay que dibujar la pantalla
    def on_draw(self):
        # Si la ventana esta visible
        if self.visible:
            # Borramos lo que hay en pantalla
            self.clear()
            # Dibujamos la imagen
            if self.imagen!=None:
                self.imagen.draw()
            # Y, para cada animacion, la dibujamos
            # Para hacer esto, le decimos al batch que se dibuje
            self.batch.draw()


    # Si intentan cerrar esta ventana, saldremos de la escena
    def on_close(self):
        self.terminarEscena()


    # El evento relativo al clic del raton
    def on_mouse_press(self, x, y, button, modifiers):
        # Si se pulsa el boton izquierdo
        if (pyglet.window.mouse.LEFT == button):
            self.terminarEscena()
        return


    # El evento que sera llamado periodicamente
    def update(self, tiempo):
        # Moveremos el tanque a la derecha hasta llegar al pixel 800
        if self.tanque.x<650:
            self.tanque.x = self.tanque.x + tiempo*VELOCIDAD_TANQUE
            if self.tanque.x>200 and self.tanque.x<300:
                self.tanque.rotation += VELOCIDAD_ROTACION_TANQUE*tiempo
            elif self.tanque.x>=300 and self.tanque.x<=600:
                self.tanque.y = self.tanque.y - tiempo*20
        else:
            # Si el tanque ya ha pasado ese pixel, paramos la animacion
            # Paramos la animacion: le ponemos al frame en el que este una duracion de None
            # Como no se sabe en cual esta, se ponen todos
            for frame in self.tanque.image.frames:
                frame.duration = None

        # Ademas, si existe la animacion de la explosion, hacemos que de desplace con el tanque
        if self.animacionExplosion!=None:
            self.animacionExplosion.x = self.tanque.x-10
            self.animacionExplosion.y = self.tanque.y-15
            
        # Y si la animacion del corredor es visible, la movemos hacia la izquierda
        if self.animacionCorredor.visible:
            self.animacionCorredor.x -= tiempo*VELOCIDAD_CORREDOR
            # Ademas, si llega al limite izquierdo terminamos esta escena
            if self.animacionCorredor.x<0:
                self.terminarEscena()


    def terminarEscena(self):
        # Restablecemos la duracion de cada frame del tanque
        for frame in self.tanque.image.frames:
            frame.duration = 0.05
        # Indicamos que la funcion programada no se vuelva a llamar
        pyglet.clock.unschedule(self.update)
        # Creamos la nueva escena
        escena = Fase(self.director)
        # Y cambiamos la actual por la nueva
        self.director.cambiarEscena(escena)



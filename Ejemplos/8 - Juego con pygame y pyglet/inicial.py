# -*- encoding: utf-8 -*-

import pyglet
from pygame.locals import *
from personajes import load_image
from escena import *


class EscenaMenu(EscenaPyglet, pyglet.window.Window):

    def __init__(self, director):

        # Constructores de las clases padres
        EscenaPyglet.__init__(self, director)
        pyglet.window.Window.__init__(self, ANCHO_PANTALLA, ALTO_PANTALLA)

        # La imagen de fondo
        self.imagen = pyglet.image.load('imagenes/portada.jpg')
        self.imagen = pyglet.sprite.Sprite(self.imagen)
        self.imagen.scale = float(ANCHO_PANTALLA) / self.imagen.width
        self.imagen.set_position(0, (ALTO_PANTALLA - self.imagen.height)/2)

        # Los botones
        self.botonJugar = pyglet.sprite.Sprite(pyglet.image.load('imagenes/boton_verde.png'))
        self.botonSalir = pyglet.sprite.Sprite(pyglet.image.load('imagenes/boton_rojo.png'))
        self.botonJugar.scale = 0.05
        self.botonSalir.scale = 0.05
        self.botonJugar.set_position(580, 70)
        self.botonSalir.set_position(580, 40)

        # El texto para cada boton
        self.etiquetaJugar = pyglet.text.Label('Jugar',
                          font_name='Times New Roman', bold=True, color=(0,0,0,255),
                          font_size=18, x=600, y=70)
        self.etiquetaSalir = pyglet.text.Label('Salir',
                          font_name='Times New Roman', bold=True, color=(0,0,0,255),
                          font_size=18, x=605, y=40)

        # Las animaciones en esta imagen inicial
        # Estas animaciones las cargamos a partir de imagenes sueltas

        # Creamos el batch de las animaciones
        self.batch = pyglet.graphics.Batch()

        # La animacion del fuego
        self.animacionFuego = pyglet.sprite.Sprite(pyglet.image.Animation([
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0001.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0002.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0003.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0004.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0005.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/flame_a_0006.png'), 0.1),
            ]), batch=self.batch)
        self.animacionFuego.scale = 1.5
        self.animacionFuego.set_position(50, 300)

        # La animacion del rayo
        self.animacionRayo = pyglet.sprite.Sprite(pyglet.image.Animation([
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0001.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0002.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0003.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0004.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0005.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0006.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0007.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0008.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0009.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/bolt_strike_0010.png'), 0.1),
            ]), batch=self.batch)
        self.animacionRayo.scale = 0.8
        self.animacionRayo.rotation = -26
        self.animacionRayo.set_position(567, 305)

        # La animacion del humo
        self.animacionHumo = pyglet.sprite.Sprite(pyglet.image.Animation([
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0001.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0002.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0003.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0004.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0005.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0006.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0007.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0008.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0009.png'), 0.1),
            pyglet.image.AnimationFrame(pyglet.image.load('imagenes/smoke_puff_0010.png'), 0.1),
            ]), batch=self.batch)
        self.animacionHumo.scale = 0.7
        self.animacionHumo.set_position(720, 70)

    # El evento relativo a la pulsacion de una tecla
    def on_key_press(self, symbol, modifiers):
        # Si se pulsa Escape, se sale del programa
        if symbol == pyglet.window.key.ESCAPE:
            self.director.salirPrograma()


    # el evento que se ejecuta cada vez que hay que dibujar la pantalla
    def on_draw(self):
        # Si la ventana esta visible
        if self.visible:
            # Borramos lo que hay en pantalla
            self.clear()
            # Dibujamos la pantalla
            self.imagen.draw()
            # Dibujamos los botones
            self.botonJugar.draw()
            self.botonSalir.draw()
            # Ponemos el texto para cada boton
            self.etiquetaJugar.draw()
            self.etiquetaSalir.draw()
            # Ponemos las animaciones
            self.batch.draw()

    # Si intentan cerrar esta ventana, saldremos del programa
    def on_close(self):
        self.director.salirPrograma()

    # El evento relativo al clic del raton
    def on_mouse_press(self, x, y, button, modifiers):
        # Si se pulsa el boton izquierdo
        if(pyglet.window.mouse.LEFT == button):
            # Miramos a ver en que boton se ha pulsado, y se hace la accion correspondiente
            if  (x>=self.botonJugar.x) and (x<=(self.botonJugar.x + self.botonJugar.width)) and (y>=self.botonJugar.y) and (y<=(self.botonJugar.y + self.botonJugar.height)):
                self.director.salirEscena()
            elif  (x>=self.botonSalir.x) and (x<=(self.botonSalir.x + self.botonSalir.width)) and (y>=self.botonSalir.y) and (y<=(self.botonSalir.y + self.botonSalir.height)):
                self.director.salirPrograma()
    
    def update(self, *args):
        return


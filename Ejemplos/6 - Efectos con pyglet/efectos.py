import pyglet
from pyglet.image import Animation, AnimationFrame

VELOCIDAD_CAIDA = 100 # Pixels/segundo
VELOCIDAD_X = 20 # Pixels/segundo


# Funcion auxiliar que crea una animacion a partir de una imagen que contiene la animacion
#  dividida en filas y columnas
def crearAnimacion(nombreImagen, filas, columnas):
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
            # Creamos un frame con esa imagen, indicandole que tendra una duracion de 0.1 segundos
            frame = AnimationFrame(imagen, 0.1)
            #  y la anadimos a la secuencia de frames
            secuenciaFrames.append(frame)

    # Devolvemos el objeto animacion, creado con la secuencia de frames
    return Animation(secuenciaFrames)


# -------------------------------------------------
# Clase efecto: una subclase de Sprite
# Esta clase la creamos solamente para que una animacion se elimine cuando termine
# En el siguiente ejemplo se puede ver otra forma de eliminar la animacion

class Efecto(pyglet.sprite.Sprite):

    def __init__(self, ventana, batch, grupo, *args):
        # Constructor de la clase padre
        pyglet.sprite.Sprite.__init__(self, batch=batch, group=grupo, *args)
        # Guardamos la ventana porque contiene la lista donde esta este efecto,
        #  para poder eliminarlo cuando termine
        self.ventana = ventana

    # -------------------------------------------------
    # Eventos del efecto

    # Cuando termine la animacion
    def on_animation_end(self):
        # Eliminamos el efecto de la lista de efectos que estan en pantalla
        self.ventana.efectosEnPantalla.remove(self)
        self.delete()


# -------------------------------------------------
# Clase VentanaEfectos: la ventana donde se vera todo

class VentanaEfectos(pyglet.window.Window):
    
    def __init__(self, resolucionx, resoluciony):
        # Constructor dela clase padre
        pyglet.window.Window.__init__(self, resolucionx, resoluciony)

        # Creamos el batch de las animaciones
        self.batch = pyglet.graphics.Batch()
        # Y los grupos para ponerlas por pantalla
        self.grupoDetras =  pyglet.graphics.Group(order=0)
        self.grupoDelante = pyglet.graphics.Group(order=1)

        # Creamos las animaciones disponibles
        self.efectosDisponibles = [
                crearAnimacion('efectos/explosion.png', 6, 5),
                crearAnimacion('efectos/fuego.png', 9, 5),
                crearAnimacion('efectos/circulo.png', 10, 5),
                crearAnimacion('efectos/circulo_fuego.png', 5, 5),
                crearAnimacion('efectos/llama_azul.png', 8, 5) ]

        # Que efectos tenemos actualmente en pantalla
        # Es necesario guardar referenciaas a las animaciones, porque las vamos a mover
        self.efectosEnPantalla = []

        # que velocidad en el ejex tienen los efectos
        self.velocidadx = VELOCIDAD_X

    # Le decimos a la ventana que inicie una nueva animacion
    def reproducirAnimacion(self, x, y, tipoAnimacion, grupo):
        # Creamos el efecto correspondiente al que nos digan
        efecto = Efecto(self, self.batch, grupo, self.efectosDisponibles[tipoAnimacion])
        # Lo situamos en la posicion indicada
        efecto.position = (x, y, 1)
        # Y lo anadimos a la lista de efectos en pantalla
        self.efectosEnPantalla.append(efecto)

    # -------------------------------------------------
    # Eventos de la ventana

    # El evento relativo a la pulsacion de un boton del raton
    def on_mouse_press(self, x, y, button, modifiers):
        # Si se pulsa el boton izquierdo
        if(pyglet.window.mouse.LEFT == button):
            # Creamos el efecto del primer tipo, en la posicion del raton
            #  y en el grupo de delante
            self.reproducirAnimacion(
                x-(self.efectosDisponibles[0].get_max_width()/2),
                y-(self.efectosDisponibles[0].get_max_height()/2), 0,
                self.grupoDelante
                )


    # El evento relativo a la pulsacion de una tecla
    def on_key_press(self, symbol, modifiers):
        # Si se pulsa Escape
        if symbol == pyglet.window.key.ESCAPE:
            # Se termina la aplicacion pyglet
            pyglet.app.exit()


    # El evento relativo al dibujo en pantalla
    # Este evento se llama automaticamente una vez por cada frame
    def on_draw(self):
        # Limpiamos la pantalla
        self.clear()
        # Dibujamos todos los efectos que haya en pantalla
        # Para ello, utilizamos el batch
        self.batch.draw()

    # -------------------------------------------------
    # Eventos programados que se ejecutaran en un
    #  intervalo determinado de tiempo

    def update(self, tiempo):
        # Calculamos cuantos pixels hay que desplazarlas en horizontal
        desplazamientox = self.velocidadx * tiempo
        # Calculamos cuantos pixels hay que desplazarlas hacia abajo
        desplazamientoy = VELOCIDAD_CAIDA * tiempo
        # Para cada efecto en pantalla
        for efecto in self.efectosEnPantalla:
            efecto.x += desplazamientox
            efecto.y -= desplazamientoy

    def anadirAnimacion(self, tiempo, tipoAnimacion):
        # Creamos la animacion en las posiciones (150*tipoAnimacion, 500), en el grupo de detras
        self.reproducirAnimacion(150*tipoAnimacion, 500, tipoAnimacion, self.grupoDetras)

    def cambiarDireccionMovimientoHorizontal(self, tiempo):
        self.velocidadx = - self.velocidadx

# -------------------------------------------------
# Cuerpo principal


if __name__ == '__main__':

    # Se podria poner el numero de frames por segundo, pero en este caso
    #  no es necesario, puesto que la animacion ya lleva el tiempo marcada
    #  en cada frame, y ya se temporizan las llamadas que se quieran hacer
#    pyglet.clock.set_fps_limit(600)

    # Creamos la pantalla con los efectos con la resolucion indicada
    ventana = VentanaEfectos(800,600)

    # Dado que no se puede alcanzar el framerate deseado, se programa para que
    # una vez por frame actualizamos la ventana: moveremos todas las animaciones
    pyglet.clock.schedule(ventana.update)

    # Cada 2 segundos anadimos una animacion
    pyglet.clock.schedule_interval(ventana.anadirAnimacion, 2, 0)
    pyglet.clock.schedule_interval(ventana.anadirAnimacion, 2, 1)
    pyglet.clock.schedule_interval(ventana.anadirAnimacion, 2, 2)
    pyglet.clock.schedule_interval(ventana.anadirAnimacion, 2, 3)
    pyglet.clock.schedule_interval(ventana.anadirAnimacion, 2, 4)

    # Cada segundo cambiaremos la velocidad horizontal de las animaciones
    pyglet.clock.schedule_interval(ventana.cambiarDireccionMovimientoHorizontal, 1)

    # Comenzamos el bucle de eventos de pyglet
    pyglet.app.run()

    # Cuando hayamos terminado la animacion con pyglet, cerramos la ventana
    ventana.close()


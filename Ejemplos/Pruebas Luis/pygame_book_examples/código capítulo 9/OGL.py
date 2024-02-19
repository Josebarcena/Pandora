import pygame
try:
    import OpenGL as ogl
    try:
        import OpenGL.GL
    except ImportError:
        print('Patch para MacOS')
        from ctypes import util
        orig_util_find_library = util.find_library

        def new_util_find_library(name):
            res = orig_util_find_library(name)
            if res:
                return res
            return '/System/Library/Frameworks/'+name+'.framework/'+name
        util.find_library = new_util_find_library
except ImportError:
    pass
from OpenGL.GL import *
from OpenGL.GLU import *

VERTICES = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

ARISTAS = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def Cubo():
    glBegin(GL_LINES)
    for arista in ARISTAS:
        for vertice in arista:
            glVertex3fv(VERTICES[vertice])
    glEnd()


pygame.init()
ZONA = (800, 800)
pygame.display.set_mode(ZONA, pygame.DOUBLEBUF | pygame.OPENGL)

gluPerspective(45, (ZONA[0]/ZONA[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Cubo()
    pygame.display.flip()
    pygame.time.wait(10)

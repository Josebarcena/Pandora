import pygame

azul = (0, 0, 255)
rojo = (255, 0, 0)

pygame.init()
pygame.display.set_caption(u'Surface')
ventana = pygame.display.set_mode((400, 400))

azul_surface = pygame.Surface((400, 400))
azul_surface.fill(azul)

rojo_surface = pygame.Surface((120, 240))
rojo_surface.fill(rojo)

ventana.blit(azul_surface, (0, 0))
ventana.blit(rojo_surface, (50, 100))

pygame.display.flip()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

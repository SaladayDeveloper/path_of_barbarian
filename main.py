from data.functions import *

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
info = pygame.display.Info()
size = width, height = info.current_w, info.current_h
running = True
fps = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()

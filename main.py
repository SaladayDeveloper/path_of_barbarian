from classes.barbarian import Barbarian, screen, width, height
from data.functions import *

running = True
fps = 60
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
main_hero = pygame.sprite.Group()
barbarian = Barbarian(all_sprites, main_hero)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()

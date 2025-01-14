import pygame

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
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a]:
                barbarian.move(event.key, 1)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a]:
                barbarian.move(event.key, 0)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()

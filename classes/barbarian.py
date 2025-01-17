import pygame

from data.functions import load_image

pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((400, 400))
info = pygame.display.Info()
size = width, height = info.current_w, info.current_h


class Barbarian(pygame.sprite.Sprite):
    image = load_image("barbarian.jpeg", -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Barbarian.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed_x = self.speed_y = 0
        self.old_coord = [0, 0]

    def update(self):
        self.old_coord[0] += self.speed_x
        self.old_coord[1] += self.speed_y
        self.rect.x = self.old_coord[0]
        self.rect.y = self.old_coord[1]

    def move(self, keys, speed):
        if keys == pygame.K_a:
            self.speed_x = -speed
        if keys == pygame.K_d:
            self.speed_x = speed
        if keys == pygame.K_s:
            self.speed_y = speed
        if keys == pygame.K_w:
            self.speed_y = -speed

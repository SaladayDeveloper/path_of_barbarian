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
        self.rect.x = 500
        self.rect.y = 500
        self.speed_x = self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def move(self, keys, speed):
        if keys == pygame.K_a:
            self.speed_x = -speed
        if keys == pygame.K_d:
            self.speed_x = speed
        if keys == pygame.K_s:
            self.speed_y = speed
        if keys == pygame.K_w:
            self.speed_y = -speed

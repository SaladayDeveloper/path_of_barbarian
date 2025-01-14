import pygame

from data.functions import load_image

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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
        self.speed = 1

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= width or self.rect.x <= 0:
            self.speed = -self.speed

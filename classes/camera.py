from classes.barbarian import width, height


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.old_coord[0] + target.rect.w // 2 - width // 2)
        self.dy = -(target.old_coord[1] + target.rect.h // 2 - height // 2)

    def get_d(self):
        return  self.dx, self.dy
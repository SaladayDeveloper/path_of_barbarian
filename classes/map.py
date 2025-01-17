import pytmx

MAPS_DIR = 'maps'


class Map:
    def __init__(self, file_name, free_tiles):
        self.map = pytmx.load_pygame(f'{MAPS_DIR}/{file_name}')
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tiles

    def render(self, screen):
        for row in range(self.width):
            for col in range(self.height):
                image = self.map.get_tile_image(row, col, 0)
                screen.blit(image, (row * self.tile_size, col * self.tile_size))

    def get_tile_id(self, position):
        return self.map.tiledgidmap(self.map.get_tile_gid(*position, 0))

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles

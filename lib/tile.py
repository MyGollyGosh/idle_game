import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, path_to_tile):
        super().__init__()
        self.image = pygame.image.load(path_to_tile).convert_alpha()
        self.rect = self.image.get_rect(bottomleft = (x, y))

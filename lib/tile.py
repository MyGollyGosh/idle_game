import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, path_to_tile=None):
        super().__init__()
        self.image = None
        self.rect = pygame.Rect(x+8,y+8,1,1)
        if path_to_tile:
            self.image = pygame.image.load(path_to_tile).convert_alpha()
            self.rect = self.image.get_rect(bottomleft = (x, y))

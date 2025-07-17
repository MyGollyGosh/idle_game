import pygame

class House(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/house.png').convert_alpha()
        self.rect = pygame.Rect((x-35, y-115), (0, 0))
        self.collision_rect = self.rect

        '''
        y = up
        x = across
        '''
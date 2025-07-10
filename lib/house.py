import pygame

class House(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/house.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (x, y))


        '''
        y = up
        x = across
        '''
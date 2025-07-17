import pygame

class TransitionTile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = None
        self.rect = pygame.Rect(x,y,1,1)
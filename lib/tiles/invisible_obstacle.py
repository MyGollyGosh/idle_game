import pygame

class InvisibleObstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = None
        self.rect = pygame.Rect(x+5,y+10,1,1)
import pygame

class Player():
    def __init__(self):
        self.asset = pygame.image.load('assets/adventurer.png').convert_alpha()
        self.rect = self.asset.get_rect(midbottom = (0, 0))
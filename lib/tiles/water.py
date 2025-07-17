import pygame

class Water(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('free_art/Cute_Fantasy_Free/Tiles/Water_Middle.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.collision_rect = self.rect
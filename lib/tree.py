import pygame

class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('free_art/Cute_Fantasy_Free/Outdoor decoration/Oak_Tree.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.collision_rect = pygame.Rect(x-3,y+19, 8,8)
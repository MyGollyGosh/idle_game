import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/adventurer.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (350, 360))
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000

    def move(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.rect.top -= 300 * self.dt
        if key_pressed[pygame.K_s]:
            self.rect.bottom += 300 * self.dt
        if key_pressed[pygame.K_a]:
            self.rect.left -= 300 * self.dt
        if key_pressed[pygame.K_d]:
            self.rect.right += 300 * self.dt

    def update(self):
        self.move()
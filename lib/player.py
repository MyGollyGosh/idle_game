import pygame

class Player():
    def __init__(self):
        self.asset = pygame.image.load('assets/adventurer.png').convert_alpha()
        self.rect = self.asset.get_rect(midbottom = (350, 360))
        self.position = pygame.Vector2(640,360)
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000

    def move(self, key_pressed):
        if key_pressed[pygame.K_w]:
            self.position.y -= 300 * self.dt
            self.rect.y -= 300 * self.dt
        if key_pressed[pygame.K_s]:
            self.position.y += 300 * self.dt
            self.rect.y += 300 * self.dt
        if key_pressed[pygame.K_a]:
            self.position.x -= 300 * self.dt
            self.rect.x -= 300 * self.dt
        if key_pressed[pygame.K_d]:
            self.position.x += 300 * self.dt
            self.rect.x += 300 * self.dt
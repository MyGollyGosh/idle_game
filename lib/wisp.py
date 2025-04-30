import pygame

class Wisp:
    def __init__(self):
        self.asset = pygame.image.load('assets/wisp.png').convert_alpha()
        self.rect = self.asset.get_rect(midbottom=(500, 100))
        self.hit_bottom = False
        self.float_speed = 20
        self.base_y = float(self.rect.top)
        self.top_limit = self.base_y - 4
        self.bottom_limit = self.base_y + 4

    def wisp_movement(self, dt):
        if not self.hit_bottom:
            self.base_y += self.float_speed * dt
            if self.base_y >= self.bottom_limit:
                self.hit_bottom = True
        else:
            self.base_y -= self.float_speed * dt
            if self.base_y <= self.top_limit:
                self.hit_bottom = False

        self.rect.top = round(self.base_y)

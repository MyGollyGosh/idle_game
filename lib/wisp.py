import pygame

class Wisp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/wisp.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(500, 100))
        self.hit_bottom = False
        self.float_speed = 15
        self.base_y = float(self.rect.top)
        self.top_limit = self.base_y - 4
        self.bottom_limit = self.base_y + 4
        pygame.font.init()
        self.font = pygame.font.SysFont("old english text mt", 30)
        self.text = self.font.render('Hi', True, (0,0,0))

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

    def update(self, dt):
        self.wisp_movement(dt)
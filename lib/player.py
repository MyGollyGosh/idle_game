import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/adventurer.png').convert_alpha()
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000

        #animations:
        self.idle_animation = self.extract_frames(6, 1, 0)
        self.move_up_animation = self.extract_frames(6, 1, 5)
        self.move_down_animation = self.extract_frames(6, 1, 3)
        self.move_left_animation = [pygame.transform.flip(frame, True, False) for frame in self.extract_frames(6, 1, 4)]
        self.move_right_animation = self.extract_frames(6,1, 4)

        self.current_animation = self.idle_animation
        self.frame_index = 0
        self.animation_speed = 0.1
        self.time_accumulator = 0

        self.image = self.current_animation[self.frame_index]
        self.rect = self.image.get_rect(midbottom = (350, 360))

    def extract_frames(self, columns, rows, start_row=0):
        sheet_width, sheet_height = self.sprite_sheet.get_size()
        frame_width = sheet_width // columns
        frame_height = sheet_height // 10

        frames = []
        for row in range(start_row, start_row + rows):
            for col in range(columns):
                frame_rect = pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height)
                frame = self.sprite_sheet.subsurface(frame_rect)
                frames.append(frame)

        return frames
    
    def move(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.current_animation = self.move_up_animation
            self.rect.top -= 100 * self.dt
        if key_pressed[pygame.K_s]:
            self.current_animation = self.move_down_animation
            self.rect.bottom += 100 * self.dt
        if key_pressed[pygame.K_a]:
            self.current_animation = self.move_left_animation
            self.rect.left -= 100 * self.dt
        if key_pressed[pygame.K_d]:
            self.current_animation = self.move_right_animation
            self.rect.right += 100 * self.dt
        
    def animate(self):
        self.time_accumulator += self.dt
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_a] or key_pressed[pygame.K_s] or key_pressed[pygame.K_d]:
            self.move()
        else:
            self.current_animation = self.idle_animation
        if self.time_accumulator > self.animation_speed:
            self.time_accumulator = 0
            self.frame_index = (self.frame_index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.frame_index]

    def update(self):
        self.animate()
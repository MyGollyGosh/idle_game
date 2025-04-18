import pygame

class Wisp:
    def __init__(self):
        self.asset = pygame.image.load('assets/wisp.png').convert_alpha()
        self.x_pos = 500
        self.y_pos = 20
        self.at_bottom = False
        self.pos = (self.x_pos, self.y_pos)

    def move_down(self):
        self.y_pos+=.25
        if self.y_pos==30:
            self.at_bottom = True
        self.pos = (self.x_pos, self.y_pos)

    def move_up(self):
        self.y_pos-=.25
        if self.y_pos==20:
            self.at_bottom = False
        self.pos = (self.x_pos, self.y_pos)

    def wisp_movement(self):
        if self.at_bottom:
            self.move_up()
        else:
            self.move_down()

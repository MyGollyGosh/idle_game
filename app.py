import pygame
from lib.wisp import Wisp
from lib.player import Player

pygame.init()



class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0 
        self.house = pygame.image.load('assets/house.png').convert_alpha()
        self.tavern = pygame.image.load('assets/tavern.png').convert_alpha()
        self.blacksmith = pygame.image.load('assets/blacksmith.png').convert_alpha()
        self.background = pygame.image.load('assets/grass.png').convert_alpha()
        self.wisp = Wisp()
        self.player = Player()
        self.player_pos = pygame.Vector2(640, 360)
        

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill('white')


            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.wisp.asset, (self.wisp.pos))
            self.wisp.wisp_movement()
            self.screen.blit(self.house, (10 ,10))
            self.screen.blit(self.tavern, (850, 10))
            self.screen.blit(self.blacksmith, (10, 475))
            self.screen.blit(self.player.asset, self.player_pos)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= 300 * self.dt
            if keys[pygame.K_s]:
                self.player_pos.y += 300 * self.dt
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * self.dt
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * self.dt


            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

    pygame.quit()

if __name__=='__main__':
    game = Game()
    game.run()
import pygame
from lib.wisp import Wisp
from lib.player import Player
from lib.house import House

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0 
        self.tavern = pygame.image.load('assets/tavern.png').convert_alpha()
        self.blacksmith = pygame.image.load('assets/blacksmith.png').convert_alpha()
        self.background = None
        self.wisp = pygame.sprite.GroupSingle()
        self.wisp.add(Wisp())
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.house = pygame.sprite.GroupSingle()
        self.house.add(House())
        self.in_overworld = True
        self.in_house = False


    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.in_overworld:
                self.background = pygame.image.load('assets/grass.png').convert_alpha()
                self.screen.fill('white')

                self.screen.blit(self.background, (0,0))
                self.wisp.draw(self.screen)
                self.wisp.update(self.dt)
                self.house.draw(self.screen)
                self.screen.blit(self.tavern, (850, 10))
                self.screen.blit(self.blacksmith, (10, 475))
                #screen.blit(surface, rect -> places the surface inside the rect)
                self.player.draw(self.screen)
                self.player.update()

                if pygame.sprite.collide_rect(self.player.sprite, self.wisp.sprite):
                    self.screen.blit(self.wisp.sprite.text, (535,30))
                
                if pygame.sprite.collide_rect(self.player.sprite, self.house.sprite):
                    self.in_overworld = False
                    self.in_house = True
                    self.player.sprite.rect.bottom = 700
                    self.player.sprite.rect.right = 700

            if self.in_house:
                self.background = pygame.image.load('assets/floorboards.png')
                self.screen.fill('white')
                self.screen.blit(self.background, (0,0))
                self.player.draw(self.screen)
                self.player.update()
                
                

            self.dt = self.clock.tick(60) / 1000

            pygame.display.flip()
            
    pygame.quit()

if __name__=='__main__':
    game = Game()
    game.run()
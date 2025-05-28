import pygame
from lib.wisp import Wisp
from lib.player import Player
from lib.house import House

pygame.init()

town_layout = [
    [("grass", 0), ("grass", 0), ("grass", 0)],
    [("path", 0), ("path", 1), ("path", 0)],
    [("cliff", 0), ("cliff", 0), ("cliff", 0)]
]

tilesets = {
    "grass": "assets/Tiles/Grass_Middle.png",
    "path": "assets/Tiles/Path_Middle.png",
    "cliff": "assets/Tiles/Cliff_Tile.png"
}

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
        self.obstacles = pygame.sprite.Group()

        self.state = 'in overworld'


    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    

            
            if self.state == 'in overworld':
                self.obstacles.add(self.house)
                self.player.sprite.obstacles = self.obstacles

                self.screen.fill('white')

                self.background = pygame.image.load('assets/map.png')
                self.screen.blit(self.background, (0,0))
                self.wisp.draw(self.screen)
                self.wisp.update(self.dt)
                self.house.draw(self.screen)

                if pygame.sprite.collide_rect(self.player.sprite, self.wisp.sprite):
                    self.screen.blit(self.wisp.sprite.text, (535,30))
                
                # if pygame.sprite.collide_rect(self.player.sprite, self.house.sprite):
                #     self.state = 'in house'
                #     self.player.sprite.rect.bottom = 700
                #     self.player.sprite.rect.right = 700

            if self.state == 'in house':
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
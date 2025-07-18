import pygame
from lib.tiles.wisp import Wisp
from lib.player import Player
from lib.house import House
from lib.tiles.tree import Tree
from lib.tiles.water import Water
from lib.tiles.invisible_obstacle import InvisibleObstacle
from lib.tiles.transition_tile import TransitionTile
from lib.tile_map.map import overworld_map

pygame.init()




class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0 
        self.background = None

        self.wisp = pygame.sprite.GroupSingle()
        self.wisp.add(Wisp())

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())

        self.house1 = pygame.sprite.GroupSingle()
        self.house2 = pygame.sprite.GroupSingle()
        self.house3 = pygame.sprite.GroupSingle()
        self.house4 = pygame.sprite.GroupSingle()
        self.house1.add(House(185, 150))
        self.house2.add(House(105, 485))
        self.house3.add(House(825, 215))
        self.house4.add(House(825, 455))
        
        self.obstacles = pygame.sprite.Group()
        self.invisible_obstacles = pygame.sprite.Group()
        self.transition_tiles = pygame.sprite.Group()

        self.state = 'in overworld'

    def make_map(self):
        y = -16
        for row in overworld_map:
            y+=16
            x=-16
            for item in row:
                x+=16
                if item == 1:
                    water = Water(x,y)
                    self.obstacles.add(water)

                if item == 2:
                    tree = Tree(x,y)
                    self.obstacles.add(tree)

                if item == 3:
                    invis_obstacle = InvisibleObstacle(x,y)
                    self.invisible_obstacles.add(invis_obstacle)

                if item == 4:
                    transition_tile = TransitionTile(x,y)
                    self.transition_tiles.add(transition_tile)

    def run(self):

        self.make_map()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            if self.state == 'in overworld':
                if self.house1 not in self.obstacles:
                    self.obstacles.add(self.house1)
                if self.house2 not in self.obstacles:
                    self.obstacles.add(self.house2)
                if self.house3 not in self.obstacles:
                    self.obstacles.add(self.house3)
                if self.house4 not in self.obstacles:
                    self.obstacles.add(self.house4)

                self.player.sprite.obstacles = self.obstacles
                self.player.sprite.invisible_obstacles = self.invisible_obstacles
                self.player.sprite.transition_tiles = self.transition_tiles

                self.background = pygame.image.load('assets/map.png')
                self.screen.blit(self.background, (0,0))
                self.player.draw(self.screen)
                self.player.update()
                self.obstacles.draw(self.screen)
                # Uncomment to draw invis obstacles
                # for obstacle in self.invisible_obstacles:
                #     pygame.draw.rect(self.screen, (255,0,0), obstacle.rect)
                self.wisp.draw(self.screen)
                self.wisp.update(self.dt)

                if pygame.sprite.collide_rect(self.player.sprite, self.wisp.sprite):
                    self.screen.blit(self.wisp.sprite.text, (535,30))

                for tile in self.transition_tiles:
                    if pygame.sprite.collide_rect(self.player.sprite, tile):
                        self.state = self.state
                        self.player.sprite.rect.bottom = 700
                        self.player.sprite.rect.right = 700
                
                # if pygame.sprite.collide_rect(self.player.sprite, self.house1.sprite):
                #     self.state = 'in house'

            if self.state == 'in house':
                self.background = pygame.image.load('assets/floorboards.png')
                self.screen.fill('white')
                self.screen.blit(self.background, (0,0))
                
            self.dt = self.clock.tick(60) / 1000

            pygame.display.flip()
            
    pygame.quit()

if __name__=='__main__':
    game = Game()
    game.run()
import pygame
from lib.tiles.wisp import Wisp
from lib.player import Player
from lib.house import House
from lib.tiles.tree import Tree
from lib.tiles.water import Water
from lib.tiles.invisible_obstacle import InvisibleObstacle
from lib.tiles.transition_tile import TransitionTile
from lib.tile_maps.overworld import overworld_map
from lib.tile_maps.house import house_map

pygame.init()



class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0 
        self.game_time_accumulator = 0
        self.background = None
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 40)

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
        self.map_made = False

        self.state = 'starting'

    def make_map(self, map):
        if not self.map_made:
            self.obstacles.empty()
            self.invisible_obstacles.empty()
            self.transition_tiles.empty()
            y = -16
            for row in map:
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
            
            if self.state == 'in overworld' or self.state == 'starting':
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

            self.map_made = True

    def check_for_transition(self):
        for tile in self.transition_tiles:
            if pygame.sprite.collide_rect(self.player.sprite, tile):
                self.map_made = False
                if self.state == 'in overworld':
                    self.state = 'in house'
                    self.player.sprite.rect.bottom = 450
                    self.player.sprite.rect.right = 660
                    self.make_map(house_map)

                elif self.state == 'in house':
                    self.state = 'in overworld'
                    self.player.sprite.rect.bottom = 350
                    self.player.sprite.rect.right = 510
                    self.make_map(overworld_map)

    def display_message(self):
        if self.state == 'starting':
            textbox_width = 1300
            textbox_height = 80
            textbox_x = 1280 // 2 - textbox_width // 2
            textbox_y = 720 - textbox_height - 30
            textbox_values = (textbox_x, textbox_y, textbox_width, textbox_height)
            text = self.font.render("I've been busy while you've been away!", True, self.BLACK)

            pygame.draw.rect(self.screen, self.WHITE, (textbox_values), border_radius=10)
            text_rect = text.get_rect(center=(1280 // 2, textbox_y + textbox_height // 2))
            self.screen.blit(text, text_rect)
        elif self.state == 'in house':
            textbox_width = 1300
            textbox_height = 80
            textbox_x = 1280 // 2 - textbox_width // 2
            textbox_y = 720 - textbox_height - 30
            textbox_values = (textbox_x, textbox_y, textbox_width, textbox_height)
            text = self.font.render("I guess no one lives here?", True, self.BLACK)

            pygame.draw.rect(self.screen, self.WHITE, (textbox_values), border_radius=10)
            text_rect = text.get_rect(center=(1280 // 2, textbox_y + textbox_height // 2))
            self.screen.blit(text, text_rect)

    def run(self):

        self.make_map(overworld_map)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.game_time_accumulator < 1:
                self.display_message()
                self.game_time_accumulator += self.dt
                if self.game_time_accumulator > 1:
                    if self.state == 'starting':
                        self.state = 'in overworld'
            self.check_for_transition()

            if self.state == 'in overworld' and self.game_time_accumulator > 1:
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
             
            if self.state == 'in house':
                self.display_message()
                self.background = pygame.image.load('assets/floor.png')
                self.screen.fill('black')
                self.screen.blit(self.background, (565,280))
                self.player.draw(self.screen)
                self.player.update()
                self.obstacles.draw(self.screen)
                # Uncomment to draw invis obstacles
                # for obstacle in self.invisible_obstacles:
                #     pygame.draw.rect(self.screen, (255,0,0), obstacle.rect)
                
            self.dt = self.clock.tick(60) / 1000

            pygame.display.flip()
            
    pygame.quit()

if __name__=='__main__':
    game = Game()
    game.run()
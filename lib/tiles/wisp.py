import pygame
from sqlite_story_script import insert_story
import sqlite3

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
        self.text = self.font.render(self.get_last_story(), True, (0,0,0))

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

    def get_last_story(self):
        """
        Retrieve the story text from the last entry in the stories table.
        
        Returns:
            str: The story text of the last entry, or "No stories found" if no entries exist
        """
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('stories.db')
            cursor = conn.cursor()
            
            # Get just the story text from the last entry
            cursor.execute('''
                SELECT story_text 
                FROM stories 
                ORDER BY id DESC 
                LIMIT 1
            ''')
            
            result = cursor.fetchone()
            conn.close()
            
            # Return the story text or default message
            return result[0] if result else "No stories found"
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return "Database error occurred"
        except Exception as e:
            print(f"Error: {e}")
            return "Error retrieving story"
    
    def update(self, dt):
        self.wisp_movement(dt)
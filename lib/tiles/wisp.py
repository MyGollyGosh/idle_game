import pygame
import sqlite3
from datetime import datetime, timedelta
from sqlite_story_script import insert_story

class Wisp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/wisp.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(500, 200))
        self.hit_bottom = False
        self.float_speed = 15
        self.base_y = float(self.rect.top)
        self.top_limit = self.base_y - 4
        self.bottom_limit = self.base_y + 4
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 40)
        self.BLACK = (0,0,0)
        self.last_time_stamp = datetime.strptime(self.get_last_time_stamp(), "%Y-%m-%d %H:%M:%S.%f")
        self.text = self.get_text()
        self.text_split = self.split_text_into_chunks(self.text)

    def get_text(self):
        if datetime.now() - self.last_time_stamp > timedelta(hours=6):
            insert_story(datetime.now())
            
        return self.get_last_story()

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
            
            cursor.execute('''
                SELECT story_text 
                FROM stories 
                ORDER BY id DESC 
                LIMIT 1
            ''')
            
            result = cursor.fetchone()
            conn.close()

            return result[0] if result else "No stories found"
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return "Database error occurred"
        except Exception as e:
            print(f"Error: {e}")
            return "Error retrieving story"
        
    def get_last_time_stamp(self):
        try:
            conn = sqlite3.connect('stories.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT *
                FROM stories
                ORDER BY timestamp DESC
                LIMIT 1;
            ''')

            result = cursor.fetchone()
            conn.close()

            return result[1] if result else 'No stories found'
        
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return "Database error occurred"
        except Exception as e:
            print(f"Error: {e}")
            return "Error retrieving story"

        
    def split_text_into_chunks(self, text):
        rect = pygame.Rect((550,40),(400,200))
        words = text.split(' ')
        lines = []
        line = ''

        for word in words:
            test_line = f'{line} {word}'.strip()
            test_surface = self.font.render(test_line, True, self.BLACK)
            if test_surface.get_width() <= rect.width:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)
        return lines
    
    def update(self, dt):
        self.wisp_movement(dt)
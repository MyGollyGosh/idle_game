import pygame
import sqlite3

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
        self.text = self.get_last_story()
        # self.text = '''
        #             This is a long string. A very long string. Infact, this string is far too long.
        #             So too long that it won't fit in the text box provided. This is an issue. An
        #             issue that is currently being fixed but, required a nice easy to use string to
        #             work with that won't vary in length or anything of the sort. This very long string
        #             this is too long to fit in the text box is actually too long for the express purpose
        #             of being very long so that is can be fixed. The fix should make it so that you can
        #             scroll through the text in the text box, without going over it. I'm going to need a
        #             function for it and that is what I am doing right now. To fix this too long string.
        #             And fit it in a text box. Thank you for coming to my Ted talk. xoxo'''
        self.text_split = self.split_text_into_chunks(self.text)

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
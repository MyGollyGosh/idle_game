import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Box Demo")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXTBOX_BG = (200, 200, 200)

# Fonts
font = pygame.font.SysFont(None, 40)

# Create the text
message = "hi"
text = font.render(message, True, BLACK)

# Text box settings
textbox_width = 200
textbox_height = 80
textbox_x = WIDTH // 2 - textbox_width // 2
textbox_y = HEIGHT - textbox_height - 30

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw text box
    pygame.draw.rect(screen, TEXTBOX_BG, (textbox_x, textbox_y, textbox_width, textbox_height), border_radius=10)
    
    # Draw text in the box
    text_rect = text.get_rect(center=(WIDTH // 2, textbox_y + textbox_height // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
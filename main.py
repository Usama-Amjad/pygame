import os
import spacy
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
fps = 60
width, height = 1020, 890
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kids Game")

# Background image
backimage = pygame.image.load(os.path.join("assets", "pattern.jpg"))

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Character properties
character_size = 26
character_pos = [417, 480]
character_color = (255, 0, 0)

# Jump properties
gravity = 0.8
is_jumping = False
jump_velocity = 0
jump_strength = -15

# Screen fps property
clock = pygame.time.Clock()

def keep_character_in_bounds():
    global character_pos
    character_pos[0] = max(character_size, min(character_pos[0], width - character_size))
    character_pos[1] = max(character_size, min(character_pos[1], height - character_size))
    
# Function to process commands
def process_command(command):
    global character_pos, character_color, is_jumping, jump_velocity
    doc = nlp(command.lower())
    
    for token in doc:
        if token.text == "move":
            for child in token.children:
                if child.text == "left":
                    character_pos[0] -= 64.45
                elif child.text == "right":
                    character_pos[0] += 64.45
                elif child.text == "up":
                    character_pos[1] -= 64.45
                elif child.text == "down":
                    character_pos[1] += 64.45
        elif token.text == "jump" and not is_jumping:
            is_jumping = True
            jump_velocity = jump_strength
        elif token.text == "change":
            for child in token.children:
                if child.text == "color":
                    character_color = (random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255))

def main():
    running = True
    input_text = ""
    font = pygame.font.Font(None, 40)
    global character_pos, is_jumping, jump_velocity
    
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process_command(input_text)
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        
        # Apply jump
        if is_jumping:
            character_pos[1] += jump_velocity
            jump_velocity += gravity
            
            if character_pos[1] >= 480: 
                character_pos[1] = 480
                is_jumping = False
                jump_velocity = 0
        
        # Keep character in bounds
        keep_character_in_bounds()

        # Background image
        screen.blit(backimage,(0, 0))
        
        # Character
        pygame.draw.circle(screen, character_color, character_pos, character_size)
        
        # Draw the input text
        text_surface = font.render(input_text, True, (255, 0, 0))
        screen.blit(text_surface, (10, height - 40))
        
        # Update the display
        pygame.display.update()
    
    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
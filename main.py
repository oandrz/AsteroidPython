import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill("black")
        
        # Update the display
        pygame.display.flip()
    
    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    # Set up the clock for controlling frame rate
    clock = pygame.time.Clock()
    dt = 0  # delta time in seconds
    
    # Create player
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill("black")
        
        # Draw player
        player.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Control the frame rate and get delta time
        dt = clock.tick(60) / 1000  # Convert to seconds
    
    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()

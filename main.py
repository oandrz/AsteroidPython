import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from pygame.sprite import Group
import sys

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
    
    # Create sprite groups
    updatables = Group()
    drawables = Group()
    asteroids = Group()
    shots = Group()
    
    # Set up container classes
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)
    asteroid_field = AsteroidField()
    
    # Create player and add to groups
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    updatables.add(player)
    drawables.add(player)
    
    # Create asteroid field
    
    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update all updatable objects
        updatables.update(dt)
        
        # Collision detection
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill("black")
        
        # Draw all drawable objects
        for drawable in drawables:
            drawable.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Control the frame rate and get delta time
        dt = clock.tick(60) / 1000  # Convert to seconds
    
    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()

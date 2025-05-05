import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def split(self):
        # Remove this asteroid
        self.kill()
        # If too small, do not split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Determine split angles
        angle = random.uniform(20, 50)
        # Create two new velocities
        vel1 = self.velocity.rotate(angle) * 1.2
        vel2 = self.velocity.rotate(-angle) * 1.2
        # Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Spawn new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2

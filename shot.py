import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, angle, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.angle = angle
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), int(self.radius), 0)

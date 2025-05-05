import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
    
        self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, screen):
        # This will be overridden by child classes
        pass

    def update(self, dt):
        # sub-classes must override
        pass
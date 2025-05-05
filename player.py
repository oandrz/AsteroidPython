import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.position = pygame.Vector2(x, y)
        self.shoot_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt, forward=True):
        direction = 1 if forward else -1
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward_vector * PLAYER_SPEED * dt * direction
        
        # Keep player on screen
        self.position.x = max(0, min(self.position.x, SCREEN_WIDTH))
        self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT))
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Decrease shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            if self.shoot_timer < 0:
                self.shoot_timer = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left (negative dt for counter-clockwise)
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate right (positive dt for clockwise)
        if keys[pygame.K_w]:
            self.move(dt, forward=True)  # Move forward
        if keys[pygame.K_s]:
            self.move(dt, forward=False)  # Move backward
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_timer > 0:
            return
        # Create a shot at the player's position, in the direction the player is facing
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, self.rotation, velocity)
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

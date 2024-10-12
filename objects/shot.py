import pygame
from constants import SHOT_RADIUS
from objects.circleshape import CircleShape

# Shot class for game objects
class Shot(CircleShape):
    def __init__(self, x, y, color = "white",radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
import pygame
from objects.circleshape import CircleShape
from constants import POWER_UP_RADIUS

class PowerUp(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, POWER_UP_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def on_activated(self, player):
        # to be overriden by sub class
        pass
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SMALL_ASTEROID_POINTS, MEDIUM_ASTEROID_POINTS, LARGE_ASTEROID_POINTS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return SMALL_ASTEROID_POINTS

        kind = self.radius / ASTEROID_MIN_RADIUS
        points = MEDIUM_ASTEROID_POINTS
        if kind == 3:
            points = LARGE_ASTEROID_POINTS

        angle = random.uniform(20, 50)
        first_vector = self.velocity.rotate(-angle)
        second_vector = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_vector * 1.2
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = second_vector * 1.2

        return points

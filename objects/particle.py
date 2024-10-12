import pygame
from constants import INITIAL_EXPLOSION_PARTICLE_RADIUS, EXPLOSION_AMOUNT_OF_PARTICLES
from objects.circleshape import CircleShape

# Particle class for game objects
class Particle(CircleShape):
    def __init__(self, x, y, radius, on_disappear_callback):
        super().__init__(x, y, radius)
        self.initial_position = self.position
        self.on_disappear_callback = on_disappear_callback

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.radius -= dt
        distance = self.initial_position.distance_to(self.position)
        if distance > 50:
            self.on_disappear_callback(self)
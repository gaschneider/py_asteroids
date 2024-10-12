import pygame
from constants import INITIAL_EXPLOSION_PARTICLE_RADIUS, EXPLOSION_AMOUNT_OF_PARTICLES
from objects.circleshape import CircleShape
from objects.particle import Particle

# Explosion class for game objects
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.particles = []

        angle = 0
        angle_space = 360 / EXPLOSION_AMOUNT_OF_PARTICLES
        while angle <= 360:
            particle = Particle(x, y, INITIAL_EXPLOSION_PARTICLE_RADIUS, self.clean_particle)
            particle.velocity = pygame.Vector2(1,0) * 50
            particle.velocity = particle.velocity.rotate(angle)
            self.particles.append(particle)
            angle += angle_space

    def clean_particle(self, particle):
        index_of_particle = self.particles.index(particle)
        del self.particles[index_of_particle]
        if len(self.particles) == 0:
            self.kill()
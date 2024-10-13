import pygame
from objects.circleshape import CircleShape
from constants import POWER_UP_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.active = False
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, POWER_UP_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        left, right, bottom, top = self.position.x - self.radius, self.position.x + self.radius, self.position.y - self.radius, self.position.y + self.radius

        if not self.active:
            if (right < SCREEN_WIDTH and
                 left > 0 and
                 top < SCREEN_HEIGHT and
                 bottom > 0):
                self.active = True

        if self.active:
            if left <= 0 or right >= SCREEN_WIDTH:
                self.velocity.x = -self.velocity.x  # Reverse horizontal direction
            if bottom <= 0 or top >= SCREEN_HEIGHT:
                self.velocity.y = -self.velocity.y  # Reverse vertical direction

    def on_activated(self, player):
        # to be overriden by sub class
        pass
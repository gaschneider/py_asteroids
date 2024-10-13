import pygame
from objects.powerup import PowerUp
from constants import POWER_UP_RADIUS

class PowerUpLife(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, POWER_UP_RADIUS, 2)
        horiz_line = [pygame.Vector2(self.position.x - POWER_UP_RADIUS / 2, self.position.y), pygame.Vector2(self.position.x + POWER_UP_RADIUS / 2, self.position.y)]
        vert_line = [pygame.Vector2(self.position.x, self.position.y - POWER_UP_RADIUS / 2), pygame.Vector2(self.position.x, self.position.y + POWER_UP_RADIUS / 2)]
        for line in [horiz_line, vert_line]:
            pygame.draw.line(screen, "green", line[0], line[1], 2)

    def on_activated(self, player):
        player.add_life()
        self.kill()

import pygame
from objects.powerup import PowerUp
from constants import POWER_UP_RADIUS

class PowerUpSpeed(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, POWER_UP_RADIUS, 2)
        lt1_line = [pygame.Vector2(self.position.x - POWER_UP_RADIUS / 2, self.position.y + 5), pygame.Vector2(self.position.x, self.position.y - POWER_UP_RADIUS / 2 + 5)]
        lt2_line = [pygame.Vector2(self.position.x - POWER_UP_RADIUS / 2, self.position.y), pygame.Vector2(self.position.x, self.position.y - POWER_UP_RADIUS / 2)]
        rt1_line = [pygame.Vector2(self.position.x + POWER_UP_RADIUS / 2, self.position.y + 5), pygame.Vector2(self.position.x, self.position.y - POWER_UP_RADIUS / 2 + 5)]
        rt2_line = [pygame.Vector2(self.position.x + POWER_UP_RADIUS / 2, self.position.y), pygame.Vector2(self.position.x, self.position.y - POWER_UP_RADIUS / 2)]
        for line in [lt1_line, rt1_line, lt2_line, rt2_line]:
            pygame.draw.line(screen, "yellow", line[0], line[1], 2)

    def on_activated(self, player):
        player.boost_speed()
        self.kill()
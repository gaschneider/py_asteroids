import pygame
from objects.powerup import PowerUp
from constants import POWER_UP_RADIUS

class PowerUpShield(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, POWER_UP_RADIUS, 2)
        pygame.draw.circle(screen, "orange", self.position, POWER_UP_RADIUS / 2, 2)

    def on_activated(self, player):
        player.active_shield()
        self.kill()

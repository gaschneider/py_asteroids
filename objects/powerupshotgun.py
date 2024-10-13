import pygame
from objects.powerup import PowerUp
from constants import POWER_UP_RADIUS, SHOTGUN_WEAPON_SHOOT_COLOR
from objects.shotgunweapon import ShotgunWeapon

class PowerUpShotgun(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, POWER_UP_RADIUS, 2)
        font = pygame.font.SysFont("Times New Roman", 18)
        letter_w = font.render("W", 1, SHOTGUN_WEAPON_SHOOT_COLOR)
        screen.blit(letter_w, (self.position.x - 10, self.position.y - 10))
        
    def update(self, dt):
        self.position += self.velocity * dt

    def on_activated(self, player):
        player.upgrade_weapon(ShotgunWeapon())
        self.kill()
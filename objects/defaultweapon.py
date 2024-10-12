import pygame
from constants import DEFAULT_WEAPON_SHOOT_SPEED, DEFAULT_WEAPON_SHOOT_COOLDOWN
from objects.weapon import Weapon
from objects.shot import Shot

# Base class for Weapons
class DefaultWeapon(Weapon):
    def __init__(self):
        super().__init__()

    def shoot(self, x, y, angle):
        if self.timer > 0:
            return
        
        shot = Shot(x, y)
        shot.velocity = pygame.Vector2(0, 1).rotate(angle) * DEFAULT_WEAPON_SHOOT_SPEED
        self.timer = DEFAULT_WEAPON_SHOOT_COOLDOWN
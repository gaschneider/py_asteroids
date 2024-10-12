import pygame
from constants import SHOTGUN_WEAPON_SHOOT_SPEED, SHOTGUN_WEAPON_SHOOT_COOLDOWN, SHOTGUN_WEAPON_SHOOT_COLOR
from objects.weapon import Weapon
from objects.shot import Shot

# Base class for Weapons
class ShotgunWeapon(Weapon):
    def __init__(self):
        super().__init__()

    def shoot(self, x, y, angle):
        if self.timer > 0:
            return
        
        angles = [angle - 10, angle - 5, angle, angle + 5, angle + 10]

        for a in angles:
            shot = Shot(x, y, SHOTGUN_WEAPON_SHOOT_COLOR)
            shot.velocity = pygame.Vector2(0, 1).rotate(a) * SHOTGUN_WEAPON_SHOOT_SPEED
            self.timer = SHOTGUN_WEAPON_SHOOT_COOLDOWN
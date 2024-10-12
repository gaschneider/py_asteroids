import pygame
from constants import PIERCE_WEAPON_SHOOT_SPEED, PIERCE_WEAPON_SHOOT_COOLDOWN, PIERCE_WEAPON_SHOOT_COLOR, PIERCE_WEAPON_SHOOT_INITIAL_RADIUS, PIERCE_WEAPON_SHOOT_MIN_RADIUS
from objects.weapon import Weapon
from objects.shot import Shot

# Base class for Weapons
class PierceWeapon(Weapon):
    def __init__(self):
        super().__init__()

    def shoot(self, x, y, angle):
        radius = PIERCE_WEAPON_SHOOT_INITIAL_RADIUS * (PIERCE_WEAPON_SHOOT_COOLDOWN - max(0, self.timer))
        if radius < PIERCE_WEAPON_SHOOT_MIN_RADIUS:
            return
        
        shot = Shot(x, y, PIERCE_WEAPON_SHOOT_COLOR, radius)
        shot.velocity = pygame.Vector2(0, 1).rotate(angle) * PIERCE_WEAPON_SHOOT_SPEED
        
        self.timer = PIERCE_WEAPON_SHOOT_COOLDOWN

    def on_shot_collide(self, shot):
        new_shot = Shot(shot.position.x, shot.position.y, PIERCE_WEAPON_SHOOT_COLOR, shot.radius / 2)
        new_shot.velocity = shot.velocity * 1.3
        shot.kill()
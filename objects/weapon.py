import pygame

# Base class for Weapons
class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.timer = 0

    def update(self, dt):
        self.timer -= dt

    def shoot(self, x, y, rotation):
        # sub-classes must override
        pass

    def on_shot_collide(self, shot):
        # by default all shots will be removed when collided
        shot.kill()
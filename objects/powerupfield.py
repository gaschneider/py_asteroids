import pygame
import random
from objects.poweruplife import PowerUpLife
from objects.powerupshield import PowerUpShield
from objects.powerupspeed import PowerUpSpeed
from objects.powerupshotgun import PowerUpShotgun
from objects.poweruppierce import PowerUpPierce
from constants import *


class PowerUpField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-POWER_UP_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + POWER_UP_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -POWER_UP_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + POWER_UP_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.types = [PowerUpLife, PowerUpShield, PowerUpSpeed, PowerUpShotgun, PowerUpPierce]

    def spawn(self, kind, position, velocity):
        power_up_type = self.types[kind]
        power_up = power_up_type(position.x, position.y)
        power_up.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > POWER_UP_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new power up at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(0, POWER_UP_KINDS - 1)
            self.spawn(kind, position, velocity)
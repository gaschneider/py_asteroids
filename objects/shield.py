import pygame
from constants import POWER_UP_SHIELD_RADIUS, POWER_UP_SHIELD_TIMER
from objects.asteroid import Asteroid

# Shot class for game objects
class Shield():
    def __init__(self):
        self.has_shield = False
        self.shield_timer = 0
        self.shield_state = False
        self.last_shield_state_toggle = pygame.time.get_ticks()

    def draw(self, position, screen):
        if self.has_shield:
            color = "orange"
            if self.shield_timer < 2:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_shield_state_toggle >= 100:
                    self.shield_state = not self.shield_state  # Toggle the state
                    self.last_shield_state_toggle = current_time 
                if self.shield_state:
                    color = "black"
            pygame.draw.circle(screen, color, position, POWER_UP_SHIELD_RADIUS, 2)

    def update(self, dt):
        self.shield_timer -= dt
        if self.shield_timer <= 0:
            self.has_shield = False

    def check_collision(self, position, asteroid):
        if self.has_shield and isinstance(asteroid, Asteroid):
            distance = position.distance_to(asteroid.position)
            return distance <= (POWER_UP_SHIELD_RADIUS + asteroid.radius)
        
    def active(self):
        self.has_shield = True
        self.shield_timer = POWER_UP_SHIELD_TIMER
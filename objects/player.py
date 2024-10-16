import pygame
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_MAX_ACCELERATION, SCREEN_WIDTH, SCREEN_HEIGHT, POWER_UP_SPEED_BOOST, POWER_UP_SPEED_TIMER, UPGRADED_WEAPON_TIMER
from objects.circleshape import CircleShape
from objects.defaultweapon import DefaultWeapon
from objects.shield import Shield

# Player class for game objects
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.__lives = 3
        self.rotation = 0
        self.accelaration = 1
        self.__previous_dt = 0
        self.current_weapon = DefaultWeapon()
        self.boost_speed_timer = 0
        self.shield = Shield()
        self.weapon_timer = 0
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.get_color(), self.triangle(), 2)
        self.shield.draw(self.position, screen)

    def get_color(self):
        if self.__lives == 3:
            return "green"
        if self.__lives == 2:
            return "yellow"
        
        return "red"

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):  
        if (dt < 0 and self.__previous_dt < 0) or (dt >= 0 and self.__previous_dt >= 0):
            if self.accelaration < PLAYER_MAX_ACCELERATION:
                self.accelaration = self.accelaration + abs(dt) if self.accelaration + abs(dt) < PLAYER_MAX_ACCELERATION else PLAYER_MAX_ACCELERATION

        
        self.__previous_dt = dt
            
        boost_speed_acceleration = POWER_UP_SPEED_BOOST if self.boost_speed_timer > 0 else 1
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * self.accelaration * boost_speed_acceleration * dt
        new_x = self.position.x
        new_y = self.position.y
        if new_x < 0:
            new_x = 0
        elif new_x > SCREEN_WIDTH:
            new_x = SCREEN_WIDTH
        
        if new_y < 0:
            new_y = 0
        elif new_y > SCREEN_HEIGHT:
            new_y = SCREEN_HEIGHT

        self.position = pygame.Vector2(new_x, new_y)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.current_weapon.shoot(self.position.x, self.position.y, self.rotation)

        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.__previous_dt = 0
            self.accelaration = 1

        self.shield.update(dt)
        self.boost_speed_timer -= dt
        self.weapon_timer -= dt

        if self.weapon_timer <= 0 and not isinstance(self.current_weapon, DefaultWeapon):
            self.current_weapon = DefaultWeapon()

    def take_damage(self):
        if self.shield.has_shield:
            return
        self.__lives -= 1

    def add_life(self):
        if self.__lives < 3:
            self.__lives += 1

    def upgrade_weapon(self, weapon):
        self.current_weapon = weapon
        self.weapon_timer = UPGRADED_WEAPON_TIMER

    def is_alive(self):
        return self.__lives > 0
    
    def boost_speed(self):
        self.boost_speed_timer = POWER_UP_SPEED_TIMER
    
    def active_shield(self):
        self.shield.active()

    def on_shoot_collision(self, shot):
        self.current_weapon.on_shot_collide(shot)

    def check_collision(self, other):
        if self.shield.check_collision(self.position, other):
            return True

        polygon_points = self.triangle()
        
        # Check collision with each vertex
        for point in polygon_points:
            if other.position.distance_to(point) < other.radius:
                return True  # Collision with a vertex
            
        # Check collision with each edge
        num_points = len(polygon_points)
        for i in range(num_points):
            p1 = polygon_points[i]
            p2 = polygon_points[(i + 1) % num_points]

            # Vector from p1 to p2
            edge = p2 - p1
            edge_length_squared = edge.length_squared()
            if edge_length_squared == 0:  # p1 and p2 are the same point
                continue

            # Project circle center onto the edge
            t = ((other.position - p1).dot(edge)) / edge_length_squared
            # Clamp t to the segment
            t = max(0, min(1, t))
            closest_point = p1 + t * edge

            # Check distance from circle center to the closest point
            if other.position.distance_to(closest_point) < other.radius:
                return True  # Collision with an edge

        return False  # No collision detected
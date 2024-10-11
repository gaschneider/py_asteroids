# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for o in updatable:
            o.update(dt)

        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                return
            
            for s in shots:
                if a.check_collision(s):
                    a.split()
                    s.kill()
                    break

        screen.fill((0, 0, 0))
            
        for o in drawable:
            o.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
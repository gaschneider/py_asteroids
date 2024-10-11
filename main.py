# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from gamestate import GameState

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
    AsteroidField()

    Player.containers = (updatable, drawable)

    game_state = GameState(asteroids, shots)

    dt = 0  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        if game_state.check_game_over():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                game_state.start_again()
            if keys[pygame.K_ESCAPE]:
                return
            
        else: 
            for o in updatable:
                o.update(dt)

            game_state.check_collisions()

            screen.fill((0, 0, 0))
                
            for o in drawable:
                o.draw(screen)

        game_state.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
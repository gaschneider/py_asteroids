# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from objects.player import Player
from objects.asteroid import Asteroid
from objects.asteroidfield import AsteroidField
from objects.particle import Particle
from objects.shot import Shot
from objects.weapon import Weapon
from state.gamestate import GameState

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg = pygame.image.load("assets/bg.jpg")
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Weapon.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Particle.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    AsteroidField()

    Player.containers = (updatable, drawable)

    game_state = GameState(asteroids, shots)

    dt = 0  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

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
                
            for o in drawable:
                o.draw(screen)

        game_state.draw(screen)
        

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
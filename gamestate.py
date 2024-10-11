
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

class GameState():
    def __init__(self, asteroids, shots):
        self.__game_is_over = False
        self.__current_score = 0
        self.__best_score = 0
        self.__player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.__asteroids = asteroids
        self.__shots = shots

    def check_game_over(self):
        if not self.__player.is_alive():
            self.__game_is_over = True
            if self.__current_score > self.__best_score:
                self.__best_score = self.__current_score

        return self.is_game_over()
    
    def is_game_over(self):
        return self.__game_is_over
    
    def start_again(self):
        self.__game_is_over = False
        self.__current_score = 0
        self.__player.kill()
        self.__player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        for a in self.__asteroids:
            a.kill()

        for s in self.__shots:
            s.kill()

    def draw(self, screen):
        font = pygame.font.SysFont("Times New Roman", 18)
        if self.is_game_over():
            game_over_message = font.render("Game Over!", 1, "white")
            screen.blit(game_over_message, (SCREEN_WIDTH / 2 - 80, SCREEN_HEIGHT / 2 - 30))
            your_score_message = font.render(f"Your score was: {self.__current_score}", 1, "white")
            screen.blit(your_score_message, (SCREEN_WIDTH / 2 - 110, SCREEN_HEIGHT / 2))
            best_score_message = font.render("You got the best score!", 1, "white")
            if self.__best_score != self.__current_score:
                best_score_message = font.render(f"Current best score is: {self.__best_score}", 1, "white")
            
            screen.blit(best_score_message, (SCREEN_WIDTH / 2 - 135, SCREEN_HEIGHT / 2 + 30))
            return
        
        current_score_message = font.render(f"Score: {self.__current_score}", 1, "white")
        screen.blit(current_score_message, (0, SCREEN_HEIGHT - 20))

    def add_to_score(self, points):
        self.__current_score += points

    def check_collisions(self):
        for a in self.__asteroids:
            if a.check_collision(self.__player):
                self.__player.take_damage()
                
            for s in self.__shots:
                if a.check_collision(s):
                    points_for_hit = a.split()
                    self.add_to_score(points_for_hit)
                    s.kill()
                    break
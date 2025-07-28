import pygame
from character import *
from score import Score
from display import Display

# split this into a separate tracker inheriting from display

class Score_Display(Display):
    def __init__(self, x, y, score_object):
        super().__init__(x, y)
        self.position = pygame.Vector2(x, y)
        self.score_object = score_object
        self.score = 0

    def update(self, dt):
        self.score = self.score_object.get_current_score()

    def draw(self, screen):
        needed = ["S", "C", "O", "R", "E"]
        letters = []
        spacing = 0
        for item in needed:
            letter = character(self.position.x + spacing, self.position.y, item, "blue")
            letters.append(letter)
            spacing += 30
        for letter in letters:
            letter.draw(screen)
        spacing += 20
        
        score_str = str(self.score)
        split_score = []
        for char in score_str:
            split_score.append(char)
        score_to_print = []
        for item in split_score:
            number = character(self.position.x + spacing, self.position.y, item, "blue")
            score_to_print.append(number)
            spacing += 30
        for number in score_to_print:
            number.draw(screen)
            
    
            
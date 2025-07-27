import pygame
from alphabet import *

class display(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.type = type

    def draw(self, screen):
        if self.type == "score_display":
            needed = ["S", "C", "O", "R"]
            letters = []
            spacing = 0
            for item in needed:
                letter = character(self.position.x + spacing, self.position.y, item)
                letters.append(letter)
                spacing += 30
            for letter in letters:
                letter.draw(screen)
    
            
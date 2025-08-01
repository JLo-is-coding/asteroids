import pygame
from display import Display
from player import Player
from character import Character
from heartshape import Heartshape

class Life_Display(Display):
    def __init__(self, x, y, player_object):
        super().__init__(x, y)
        self.player_object = player_object
        self.life_tracker = player_object.get_life()

    def update(self, dt):
        self.life_tracker = self.player_object.get_life()

    def draw(self, screen):
        spacing = 50
        heart_icon = Heartshape(self.position.x + 20, self.position.y - 40)
        heart_icon.draw(screen)
        life_str = str(self.life_tracker)
        number = Character(self.position.x + spacing, self.position.y, life_str, "blue")
        number.draw(screen)
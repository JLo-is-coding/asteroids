import pygame
import random

class Pickup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.width = 20
        self.height = 35
        self.rect = pygame.Rect(x - self.width//2, y - self.height//2, self.width, self.height)

    def draw(self, screen):
        #to be overwritten
        pass

class Shotgun_Pickup(Pickup):
    def __init__(self, x, y):
        super().__init__(x, y)
        

    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", self.rect, 2, 0, 10, 10 )

import pygame
import random

class Pickup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.width = 20
        self.height = 35
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen):
        #to be overwritten
        pass

    def collide(self, player):
        closest_x = max(self.position.x, min(player.position.x, self.position.x + self.width))
        closest_y = max(self.position.y, min(player.position.y, self.position.y + self.height))
        
        distance_x = player.position.x - closest_x
        distance_y = player.position.y - closest_y
        distance_squared = distance_x * distance_x + distance_y * distance_y
        
        return distance_squared < (player.radius * player.radius)

class Shotgun_Pickup(Pickup):
    def __init__(self, x, y):
        super().__init__(x, y)
        

    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", self.rect, 2, 0, 10, 10 )

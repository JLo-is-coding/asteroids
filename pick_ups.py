import pygame
import random
from player import Player

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
    
    def grant_buff(self, player):
        # overwrite
        pass

# crack on with weapon state code
class Shotgun_Pickup(Pickup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.buff = "shotgun"
        

    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", self.rect, 2, 0, 10, 10 )

    def grant_buff(self, player):
        player.weapon_state_timer = 8
        player.weapon_state = "shotgun"

class Ghost_pickup(Pickup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.buff = "ghost"

    def draw(self, screen):
        pygame.draw.rect(screen, "grey", self.rect, 2, 0, 10, 10, 10, 10)

    def grant_buff(self, player):
        player.buff_timer = 5
        player.immune_timer = 5
        player.colour = "blue"
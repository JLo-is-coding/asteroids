import pygame
import random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PICKUP_SPAWN_RATE
from pick_ups import Shotgun_Pickup, Ghost_pickup
from main import *

class Spawnfield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.pickup_cooldown = 0.0

    def spawn(self, x, y):
        pickups = [Shotgun_Pickup(x,y), Ghost_pickup(x,y)]
        item_pack = random.choice(pickups)
        self.pickup_group.add(item_pack)
        self.drawable_group.add(item_pack)

    def update(self, dt):
        self.pickup_cooldown += dt
        if self.pickup_cooldown > PICKUP_SPAWN_RATE:
            pos_x = random.randint(30, SCREEN_WIDTH-30)
            pos_y = random.randint(30, SCREEN_HEIGHT-30)
            self.spawn(pos_x, pos_y)
            self.pickup_cooldown = 0.0

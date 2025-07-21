import pygame
import random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PICKUP_SPAWN_RATE
from pick_ups import Shotgun_Pickup
from main import *

class Spawnfield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.pickup_cooldown = 0.0

    def spawn(self, x, y):
        shot_pack = Shotgun_Pickup(x, y)
        self.pickup_group.add(shot_pack)
        self.drawable_group.add(shot_pack)

    def update(self, dt):
        self.pickup_cooldown += dt
        if self.pickup_cooldown > PICKUP_SPAWN_RATE:
            pos_x = random.randint(0, SCREEN_WIDTH)
            pos_y = random.randint(0, SCREEN_HEIGHT)
            self.spawn(pos_x, pos_y)
            self.pickup_cooldown = 0.0

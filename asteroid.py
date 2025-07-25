import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from score import Score

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_1.velocity = (pygame.Vector2(new_velocity_1) * 1.2)
        Asteroid_2.velocity = (pygame.Vector2(new_velocity_2) * 1.2)

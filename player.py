import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import random

from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, score_object):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.life = 1
        self.immune_timer = 0
        self.boosted = False
        self.boost_timer = 0
        self.score_object = score_object
        self.bonus_tracker = score_object.get_current_bonus()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
         self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        # ------Shot cooldown------
        self.shot_timer -= dt
        # ------State management------
        if self.boost_timer > 0:
            self.boost_timer -= dt
            if self.boost_timer <= 0:
                self.boosted = False
        
        if self.immune_timer > 0:
            self.immune_timer -= dt
        # ------Bonus Tracker-----
        self.bonus_tracker = self.score_object.get_current_bonus()
        if self.bonus_tracker >= 500:
            self.score_object.reset_bonus()
            self.life += 1 if (self.life < 3) else 0
        # ------Movement management------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_timer > 0:
                pass
            else:
                self.shoot()
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        if self.boosted:
            shot2 = Shot(self.position.x, self.position.y)
            shot3 = Shot(self.position.x, self.position.y)
            shot2.velocity = pygame.Vector2(0, 1).rotate(self.rotation + 20) * PLAYER_SHOOT_SPEED
            shot3.velocity = pygame.Vector2(0, 1).rotate(self.rotation - 20) * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def get_life(self):
        return self.life

        
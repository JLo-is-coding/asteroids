import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import random
from shot import Shot

#rejigg how this works, this pissin me off!
deactivate = [0]
#-------------------------------------------

class Player(CircleShape):
    def __init__(self, x, y, score_object):
        super().__init__(x, y, PLAYER_RADIUS)
        self.colour = "white"
        self.rotation = 0
        self.shot_timer = 0
        self.life = 1
        self.immune_timer = 0
        self.buff_state = "normal"
        self.buff_timer = 0
        self.weapon_state = "basic"
        self.weapon_state_timer = 0
        self.score_object = score_object

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.colour, self.triangle(), 2)

    def rotate(self, dt):
         self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_timer -= dt
        self.manage_state(dt)
        self.check_for_bonus(deactivate)
        
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

    #------Shoot Package-------
    def shoot_shotgun(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot2 = Shot(self.position.x, self.position.y)
        shot2.velocity = pygame.Vector2(0, 1).rotate(self.rotation + 20) * PLAYER_SHOOT_SPEED
        shot3 = Shot(self.position.x, self.position.y)
        shot3.velocity = pygame.Vector2(0, 1).rotate(self.rotation - 20) * PLAYER_SHOOT_SPEED

    def shoot_basic(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def shoot(self):
        if self.weapon_state != "basic":
            print(f"weapon state is {self.weapon_state}")
            if self.weapon_state == "shotgun":
                self.shoot_shotgun() 
        else:
            self.shoot_basic()
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    #------State Management Package-----
    def revert_buff_state(self):
        self.colour = "white"
        self.buff_state = "normal"

    def revert_weapon_state(self):
        self.weapon_state = "basic"  
    
    def manage_state(self, dt):
        if self.buff_timer > 0:
            self.buff_timer -= dt
        if self.buff_timer  <= 0:
            self.revert_buff_state()
        
        if self.weapon_state_timer > 0:
            self.weapon_state_timer -= dt
        if self.weapon_state_timer <= 0:
            self.revert_weapon_state()

        if self.immune_timer > 0:
            self.immune_timer -= dt

    #------Life Package------
    def get_life(self):
        return self.life
    
    def gain_bonus_life(self):
        self.life += 1 if (self.life < 3) else 0

    # Use recursive function to create next bonus item (from modulo) then give the bonus when its equal to 
    # or greater than the bonus (calling recursion again to find the next bonus number)
    def check_for_bonus(self, deactivate_for_bonus):
        if (self.score_object.get_current_bonus() % 20 == 0) and (self.score_object.get_current_bonus() not in deactivate_for_bonus):
            deactivate_for_bonus.append(self.score_object.get_current_bonus())
            print(f"the updated vrsion of deactivate is {deactivate_for_bonus}")
            self.gain_bonus_life()
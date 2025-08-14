import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from spawnfield import *
from pick_ups import *
from shot import Shot
from score import Score
from character import *
from score_display import *
from life_display import Life_Display

from heartshape import Heartshape

def main():
    # ----- Game Start-up -----
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # ----- Initialisation code -----
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    pickups = pygame.sprite.Group()

    Player.containers =  (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Spawnfield.containers = (updatable)
    Pickup.containers = (pickups, drawable)
    Score_Display.containers = (drawable, updatable)
    Life_Display.containers = (drawable, updatable)

    score_total = Score()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, score_total )
    score_display = Score_Display(20, 700, score_total)
    life_display = Life_Display(20, 60, player)
    asteroid_field = AsteroidField()
    spawn_field = Spawnfield()
    spawn_field.pickup_group = pickups
    spawn_field.drawable_group = drawable

    heart = Heartshape(160, 60)

    # ----- Game Loop -----
    while 0 < 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for object in asteroids:
            collision = object.collide(player)
            if collision:
                if player.immune_timer <= 0:
                    player.immune_timer = 2
                    player.life -= 1
            if player.life <= 0:
                print ("Game over!")
                print (f"You Destroyed {score_total.score} Asteroids")
                sys.exit()
        for object in asteroids:
            for shot in shots:
                collision = object.collide(shot)
                if collision:
                    score_total.add()
                    object.split()
                    shot.kill()
        for object in pickups:
            collision = object.collide(player)
            if collision:
                player.buff_state = object.grant_buff(player)
                object.kill()
        screen.fill("black") 
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()

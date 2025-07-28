import pygame

class Display(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)

    def update(self, dt):
        # overwrite
        pass

    def draw(self, screen):
        # overwrite
        pass
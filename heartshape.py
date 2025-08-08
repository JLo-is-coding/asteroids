import pygame

class Heartshape:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.position.x - 10, self.position.y + 10), 10)
        pygame.draw.circle(screen, "red", (self.position.x + 10, self.position.y + 10), 10)
        pygame.draw.polygon(screen, "red",
            [(self.position.x -20, self.position.y +11),
            (self.position.x -20, self.position.y +15),
            (self.position.x, self.position.y + 40),
            (self.position.x +19.9, self.position.y +15),
            (self.position.x +19.9, self.position.y +11),
            (self.position.x, self.position.y + 10)] 
        )

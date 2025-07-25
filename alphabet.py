import pygame

class character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        # Will be replaced by individual letters
        pass

class S_letter(character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        pygame.draw.lines(
            screen, 
            "purple", 
            False, 
            [
                (self.position.x, self.position.y), 

                ],
            2
        )

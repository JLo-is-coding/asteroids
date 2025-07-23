import pygame

class letter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        # Will be replaced by individual letters
        pass

class P_letter(letter):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        print ("about to draw letter")
        pygame.draw.lines(
            screen, 
            "purple", 
            False, 
            [
                (self.position.x, self.position.y), 
                (self.position.x + 24, self.position.y),
                (self.position.x + 24, self.position.y +26),
                (self.position.x, self.position.y + 26)
                ],
            2
        )

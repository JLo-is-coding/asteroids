import pygame

class character(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.type = type
        self.characters = {
        "C" :   [(self.position.x, self.position.y), 
                (self.position.x +20, self.position.y),  
                (self.position.x, self.position.y), 
                (self.position.x, self.position.y -40),   
                (self.position.x +20, self.position.y -40)],
        
        "O" :   [(self.position.x, self.position.y),
                (self.position.x + 20, self.position.y),
                (self.position.x + 20, self.position.y - 40),
                (self.position.x, self.position.y - 40),
                (self.position.x, self.position.y)],

        "R" :   [(self.position.x, self.position.y),
                (self.position.x, self.position.y -40),
                (self.position.x +20, self.position.y -40),
                (self.position.x +20, self.position.y -20),
                (self.position.x, self.position.y -20),
                (self.position.x + 10, self.position.y -20),
                (self.position.x +20, self.position.y)],

        "S" :   [(self.position.x, self.position.y), 
                (self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -20),
                (self.position.x, self.position.y -20),
                (self.position.x, self.position.y -40),
                (self.position.x +20, self.position.y -40)]

    }
    

    def draw(self, screen):
        pygame.draw.lines(
            screen, 
            "purple", 
            False, 
            self.characters[self.type],
            3
        )



class S(character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        pygame.draw.lines(
            screen, 
            "purple", 
            False, 
            [
                
                ],
            3
        )

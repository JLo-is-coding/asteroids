import pygame

class character(pygame.sprite.Sprite):
    def __init__(self, x, y, type, colour):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.type = type
        self.colour = colour
        self.characters = {
# ===========================================================================
# A L P H A B E T
# ===========================================================================    
        "C" :   [(self.position.x, self.position.y), 
                (self.position.x +20, self.position.y),  
                (self.position.x, self.position.y), 
                (self.position.x, self.position.y -40),   
                (self.position.x +20, self.position.y -40)],

        "E" :   [(self.position.x, self.position.y),
                (self.position.x +20, self.position.y),
                (self.position.x, self.position.y),
                (self.position.x, self.position.y -20),
                (self.position.x +20, self.position.y -20),
                (self.position.x, self.position.y -20),
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
                (self.position.x +20, self.position.y -40)],

# ============================================================================
# N U M B E R S
# ============================================================================
        "1" :   [(self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -40)],

        "2" :   [(self.position.x, self.position.y),
                (self.position.x +20, self.position.y),
                (self.position.x, self.position.y),
                (self.position.x, self.position.y -20),
                (self.position.x +20, self.position.y -20),
                (self.position.x +20, self.position.y -40),
                (self.position.x, self.position.y -40)],

        "3" :   [(self.position.x, self.position.y),
                (self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -20),
                (self.position.x, self.position.y -20),
                (self.position.x +20, self.position.y -20),
                (self.position.x +20, self.position.y -40),
                (self.position.x, self.position.y -40)],

        "4" :   [(self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -40),
                (self.position.x +20, self.position.y -20),
                (self.position.x, self.position.y -20),
                (self.position.x, self.position.y -40)],

        "5" :   [(self.position.x, self.position.y), 
                (self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -20),
                (self.position.x, self.position.y -20),
                (self.position.x, self.position.y -40),
                (self.position.x +20, self.position.y -40)],

        "6" :  [(self.position.x, self.position.y -20),
                (self.position.x + 20, self.position.y -20),
                (self.position.x + 20, self.position.y),
                (self.position.x, self.position.y),
                (self.position.x, self.position.y -40),
                (self.position.x +20, self.position.y -40)],
        
        "7" :   [(self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -40),
                (self.position.x, self.position.y -40)],

        "8" :   [(self.position.x, self.position.y -20),
                (self.position.x, self.position.y),
                (self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -40),
                (self.position.x, self.position.y -40),
                (self.position.x, self.position.y -20),
                (self.position.x +20, self.position.y -20)],

        "9" :   [(self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -40),
                (self.position.x, self.position.y -40),
                (self.position.x, self.position.y -20),
                (self.position.x +20, self.position.y -20)],
                
        "0" :   [(self.position.x, self.position.y),
                (self.position.x +20, self.position.y),
                (self.position.x +20, self.position.y -40),
                (self.position.x, self.position.y -40),
                (self.position.x, self.position.y),
                (self.position.x +20, self.position.y -40)]
    }
    

    def draw(self, screen):
        pygame.draw.lines(
            screen, 
            self.colour, 
            False, 
            self.characters[self.type],
            3
        )

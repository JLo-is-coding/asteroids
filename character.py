import pygame
from constants import *

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, type, colour, font_width=20, font_height=40, line_width=3):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.type = type
        self.colour = colour
        self.font_width = font_width   
        self.font_height = font_height
        self.line_width = line_width
        self.characters = {
# ===========================================================================
# A L P H A B E T
# ===========================================================================    
        "C" :   [(self.position.x, self.position.y), 
                (self.position.x +self.font_width, self.position.y),  
                (self.position.x, self.position.y), 
                (self.position.x, self.position.y -self.font_height),   
                (self.position.x +self.font_width, self.position.y -self.font_height)],

        "E" :   [(self.position.x, self.position.y),
                (self.position.x +self.font_width, self.position.y),
                (self.position.x, self.position.y),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x +self.font_width, self.position.y -self.font_height)],

        "G" :   [(self.position.x+self.font_width, self.position.y-self.font_height),
                (self.position.x, self.position.y-self.font_height),
                (self.position.x, self.position.y),
                (self.position.x+self.font_width, self.position.y),
                (self.position.x+self.font_width, self.position.y-self.font_height/2),
                (self.position.x+self.font_width/2, self.position.y-self.font_height/2)],

        "H" :   [(self.position.x, self.position.y),
                (self.position.x, self.position.y-self.font_height),
                (self.position.x, self.position.y-self.font_height/2),
                (self.position.x+self.font_width, self.position.y-self.font_height/2),
                (self.position.x+self.font_width, self.position.y-self.font_height),
                (self.position.x+self.font_width, self.position.y)],

        "N" :   [(self.position.x, self.position.y),
                (self.position.x, self.position.y-self.font_height),
                (self.position.x+self.font_width, self.position.y),
                (self.position.x+self.font_width, self.position.y-self.font_height)],

        "O" :   [(self.position.x, self.position.y),
                (self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x, self.position.y)],

        "Q" :   [(self.position.x, self.position.y),
                (self.position.x +(self.font_width/2), self.position.y),
                (self.position.x +self.font_width, self.position.y -(self.font_height/4)),
                (self.position.x +((self.font_width/4)*3), self.position.y -(self.font_height/8)),
                (self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width/2, self.position.y -self.font_height/4),
                (self.position.x +((self.font_width/4)*3), self.position.y -(self.font_height/8)),
                (self.position.x +self.font_width, self.position.y -(self.font_height/4)),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x, self.position.y)],

        "R" :   [(self.position.x, self.position.y),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x + 10, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y)],

        "S" :   [(self.position.x, self.position.y), 
                (self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x +self.font_width, self.position.y -self.font_height)],

        "T" :   [(self.position.x+font_width/2, self.position.y),
                (self.position.x+font_width/2, self.position.y-self.font_height),
                (self.position.x+font_width, self.position.y-self.font_height),
                (self.position.x, self.position.y-self.font_height)],

        "U" :   [(self.position.x, self.position.y-self.font_height),
                (self.position.x, self.position.y),
                (self.position.x+font_width, self.position.y),
                (self.position.x+font_width, self.position.y-self.font_height)],

# ============================================================================
# N U M B E R S
# ============================================================================
        "1" :   [(self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -self.font_height)],

        "2" :   [(self.position.x, self.position.y),
                (self.position.x +self.font_width, self.position.y),
                (self.position.x, self.position.y),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x, self.position.y -self.font_height)],

        "3" :   [(self.position.x, self.position.y),
                (self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x, self.position.y -self.font_height)],

        "4" :   [(self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -self.font_height)],

        "5" :   [(self.position.x, self.position.y), 
                (self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x +self.font_width, self.position.y -self.font_height)],

        "6" :  [(self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y),
                (self.position.x, self.position.y),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x +self.font_width, self.position.y -self.font_height)],
        
        "7" :   [(self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x, self.position.y -self.font_height)],

        "8" :   [(self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x, self.position.y),
                (self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2))],

        "9" :   [(self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x, self.position.y -(self.font_height/2)),
                (self.position.x +self.font_width, self.position.y -(self.font_height/2))],
                
        "0" :   [(self.position.x, self.position.y),
                (self.position.x +self.font_width, self.position.y),
                (self.position.x +self.font_width, self.position.y -self.font_height),
                (self.position.x, self.position.y -self.font_height),
                (self.position.x, self.position.y),
                (self.position.x +self.font_width, self.position.y -self.font_height)]
    }
    

    def draw(self, screen):
        #draw from the bottom left corner of the display
        pygame.draw.lines(
            screen, 
            self.colour, 
            False, 
            self.characters[self.type],
            self.line_width
        )

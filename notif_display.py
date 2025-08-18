from display import Display
from character import Character

class Notification(Display):
    def __init__(self, x, y, characters):
        super().__init__(x, y)
        self.characters = characters
        self.timer = 2.5

    def update(self, dt):
        self.timer -= dt
        print(self.timer)
        if self.timer <= 0:
            self.kill()

    def draw(self, screen):
        spacing = 0
        for character in self.characters: 
            character = Character(self.position.x+spacing, self.position.y, character, "purple", line_width=4)
            character.draw(screen)
            spacing += 30
            
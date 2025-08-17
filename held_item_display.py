import pygame
from display import Display
from character import Character
from pick_ups import Ghost_pickup
from player import Player

class Held_Item_Display(Display):
    def __init__(self, x, y, hotkey, player, inventory_slot):
        super().__init__(x, y)
        self.width = 80
        self.height = 80
        self.hotkey = hotkey
        self.inventory_slot = inventory_slot
        self.outer_rect = (x, y, self.width, self.height)
        self.inner_rect = (x+5, y+5, self.width-10, self.height-10)
        self.player_object = player

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.outer_rect, 1, 1, 1, 1, 1)
        pygame.draw.rect(screen, "white", self.inner_rect, 3, 1, 1, 1, 1)
        key_press = Character(self.position.x+((self.width/2)-5), self.position.y+self.height+30, self.hotkey, "white", 10, 20)
        key_press.draw(screen)
        if self.player_object.inventory[self.inventory_slot]:
            buff_item = self.player_object.inventory[self.inventory_slot]
            buff_item.draw_icon(screen, self.position.x+40-(buff_item.width/2), self.position.y+40-(buff_item.height/2))
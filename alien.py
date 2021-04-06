
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""


    def __init__(self, ai_game):
        """initialize alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #load alien image set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien exact horizontal position
        self.x = float(self.rect.x)
        
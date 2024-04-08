import pygame
from constant import SCREENHEIGHT, SCREENWIDTH








class backround:


    def __init__(self, screen):
        self.image = pygame.image.load('assets/stan is hot.png')
        self.height = SCREENHEIGHT
        self.width = SCREENWIDTH
        self.backround = pygame.transform.scale(self.image, (self.width, self.height))
        self.screen = screen

    def draw (self):
        self.screen.blit(self.backround, (0, 0))

    def resize_to(self, x, y):
        self.height = x
        self.width = y
        self.background = pygame.transform.scale(self.image, (x, y))
        

    

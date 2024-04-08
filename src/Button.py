import pygame

from constant import BLUE
from constant import SCREENHEIGHT
from constant import SCREENWIDTH










#button class

class Button():
    def __init__(self, x, y, image_path, scale, screen, dark_image_path):
        self.screen = screen
        self.x = x
        self.y = y

        self.start_img = pygame.image.load(image_path)
        self.dark_start_img = pygame.image.load(dark_image_path)
        width = self.start_img.get_width()
        height = self.start_img.get_height()
        self.image = pygame.transform.scale(self.start_img, (int(width * scale), int(height * scale)))
        self.darker_image = pygame.transform.scale(self.dark_start_img, (int(width * scale) -2, int(height * scale)-2))

    def draw (self):

        
        if self.mouse_hover():
            
            self.screen.blit(self.darker_image, (self.x, self.y))
        else:
          self.screen.blit(self.image, (self.x, self.y))


    def get_rekt (self):
        return self.image.get_rect(topleft=(self.x, self.y))

    def mouse_hover(self):
        return self.get_rekt().collidepoint(pygame.mouse.get_pos())

    def collision (self):
        return self.mouse_hover() and pygame.mouse.get_pressed()[0]
            
            



    
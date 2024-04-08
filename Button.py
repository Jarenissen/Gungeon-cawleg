import pygame

from constant import BLUE
from constant import SCREENHEIGHT
from constant import SCREENWIDTH










#button class

class Button():
    def __init__(self, x, y, image_path, scale, screen):
        self.screen = screen
        self.x = x
        self.y = y
        
        self.start_img = pygame.image.load(image_path)
        width = self.start_img.get_width()
        height = self.start_img.get_height()
        self.image = pygame.transform.scale(self.start_img, (int(width * scale), int(height * scale)))
        

    def draw (self):

        #draw button on screen
        self.screen.blit(self.image, (self.x, self.y))

    


    def get_rekt (self):

        return self.image.get_rect(topleft=(self.x, self.y))

    def collision (self):

        pos = pygame.mouse.get_pos()
    
        return self.get_rekt().collidepoint(pos) and pygame.mouse.get_pressed()[0]
            
            



    
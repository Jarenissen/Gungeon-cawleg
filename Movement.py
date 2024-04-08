import pygame




from constant import BLUE



class Player:
    def __init__(self, screen):
        self.screen = screen
        self.player = pygame.Rect((500, 250, 30, 30))
        

    def draw(self):
        pygame.draw.rect(self.screen, (BLUE), self.player)
      


    def move(self, key):

        multiplier = 1

        if key[pygame.K_LSHIFT]:
            multiplier = 2

        if key[pygame.K_w] and key[pygame.K_a]:
            self.translate_by(-multiplier, -multiplier)
        elif key[pygame.K_w] and key[pygame.K_d]:
            self.translate_by(multiplier, -multiplier)
        elif key[pygame.K_s] and key[pygame.K_d]:
            self.translate_by(multiplier, multiplier)
        elif key[pygame.K_s] and key[pygame.K_a]:
            self.translate_by(-multiplier, multiplier)
        elif key[pygame.K_a] == True:
            self.translate_by(-multiplier, 0)
        elif key[pygame.K_d] == True:
            self.translate_by(multiplier, 0)
        elif key[pygame.K_w] == True:
            self.translate_by(0, -multiplier)
        elif key[pygame.K_s] == True:
            self.translate_by(0, multiplier)

    def translate_by(self, x, y):
        self.player.x += x
        self.player.y += y
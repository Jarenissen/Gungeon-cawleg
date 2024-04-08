import pygame
import sys

from constant import SCREENHEIGHT, SCREENWIDTH

from Movement import Player
from Button import Button
from backround import backround






class Game:

    

    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Gungeon Crawler')
    
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.RESIZABLE)
        

        self.clock = pygame.time.Clock()

       

        
        self.gameStateManager = GameStateManager('start')  
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)

        self.state = {'start':self.start, 'level':self.level}

    def run(self):

        ticks = 0
        



        while True:

            ticks +=1

            ticks = ticks % 60

            

            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
        
            self.state[self.gameStateManager.get_state()].run(ticks, self.screen.get_width(), self.screen.get_height())

            pygame.display.update()

         

        

            

class Level:
    def __init__(self, display, gameStateManager):
       self.display = display
       self.player = Player(display)
       self.gameStateManager = gameStateManager  
       

    def run(self, ticks, width, height):
        self.display.fill ('grey') 

        self.player.draw()

        if ticks % 5 == 0:
            key = pygame.key.get_pressed()
            self.player.move(key)

        

        
        

        
        
        



class Start:

    


    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager  
        self.start_button = Button(300, 300, 'pixil-frame-0 (1).png', 3, display)
        self.backround = backround(display)
        

    def run(self, _ticks, width, height):
        
        
        self.backround.resize_to(width, height)
        
        
        if self.start_button.collision():
            self.gameStateManager.set_state('level') 
        
        
        self.backround.draw()
        self.start_button.draw()
        



           



class GameStateManager:
    def __init__(self, currenState):
        self.currenState = currenState
    def get_state(self):
        return self.currenState
    def set_state(self, state):
        self.currenState = state
         


if __name__ == '__main__':
    game = Game()
    game.run()
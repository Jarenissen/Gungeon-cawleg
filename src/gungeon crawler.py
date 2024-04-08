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

        key = pygame.key.get_pressed()

        if ticks % 5 == 0:
            
            self.player.move(key)

        if key[pygame.K_ESCAPE]:
            self.gameStateManager.set_state('start') 


        

        

        
        

        
        
        



class Start:

    


    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager  
        self.start_button = Button(200, 300, 'assets/pixil-frame-0 (1).png', 3, display, 'assets/Start darker.png')
        self.exit_button = Button(700, 300, 'assets/Exit button.png', 3, display, 'assets/darker exit button.png')
        self.backround = backround(display)
        

    def run(self, _ticks, width, height):
        
        
        self.backround.resize_to(width, height)
        
        if self.exit_button.collision():
            sys.exit()
        
        if self.start_button.collision():
            self.gameStateManager.set_state('level') 
        
        
        self.backround.draw()
        self.start_button.draw()
        self.exit_button.draw()



           



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
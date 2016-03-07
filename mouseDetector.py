#Click Detector

import random, pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
BOXSIZE = 40 # size of box height & width in pixels

#            R    G    B
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
YELLOW = (255, 255,   0)
PURPLE = (255,   0, 255)
BLACK = (0,0,0)

BACKGROUND = BLACK
TARGET = RED
SEEKER = GREEN

def main():
    global FPSCLOCK, DISPLAYSURF, BACKGROUND
    pygame.init()
    FPSCLOCK = pygame.time.Clock() #NOTA BENE: Clock must be Capitalized
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    mousex = -1
    mousey = -1
    
    pygame.display.set_caption("MOUSE DETECTER")
    
    
    while True:
        DISPLAYSURF.fill(BACKGROUND)
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif (event.type == KEYDOWN):
                BACKGROUND = PURPLE
            elif event.type == KEYUP:
                BACKGROUND = BLACK
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                print("X: %i  Y: %i"%(mousex,mousey))
               
        pygame.display.update()
        FPSCLOCK.tick(FPS)    
        
        
if __name__ == '__main__':
    main()
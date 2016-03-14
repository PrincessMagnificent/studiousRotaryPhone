#Click Detector

import random, pygame, sys
from pygame.locals import *
import pygame.gfxdraw

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
BOXSIZE = 40 # size of box height & width in pixels
skitting = 10

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
def skitterDot(x):
    return x+random.randint(-skitting,skitting)

def main():
    global FPSCLOCK, DISPLAYSURF, BACKGROUND
    pygame.init()
    FPSCLOCK = pygame.time.Clock() #NOTA BENE: Clock must be Capitalized
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    mousex = -1
    mousey = -1
    lastmousex = 100
    lastmousey = 100
    
    pygame.display.set_caption("MOUSE DETECTER")
    
    
    while True:
        DISPLAYSURF.fill(BACKGROUND)
        pygame.draw.line(DISPLAYSURF, WHITE, (lastmousex,lastmousey), (mousex,mousey))
        ##line(Surface, color, start_pos, end_pos, width=1) -> Rect
        pygame.gfxdraw.pixel(DISPLAYSURF, skitterDot(mousex), skitterDot(mousey), RED)
        pygame.gfxdraw.pixel(DISPLAYSURF, skitterDot(lastmousex), skitterDot(lastmousey), RED)
        ##For a joke, added two jumping red dots at either end of the drawn line
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif (event.type == KEYDOWN):
                BACKGROUND = PURPLE
            elif event.type == KEYUP:
                BACKGROUND = BLACK
            elif event.type == MOUSEBUTTONUP:
                lastmousex = mousex
                lastmousey = mousey
                mousex, mousey = event.pos
                print("X: %i  Y: %i"%(mousex,mousey))
                
                
               
        pygame.display.update()
        FPSCLOCK.tick(FPS)    
        
        
if __name__ == '__main__':
    main()
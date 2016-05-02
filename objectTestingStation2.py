##This is now interesting because I have ordered him to do obey an object with the characteristics 


import pygame, sys, random
from pygame.locals import *
from math import sqrt, fabs

##This is for python.draw.circle, so you can feed an entire list of them
class Idoru(object):
    def __init__(self, color, center, radius):
        self.color = color
        self.center = center
        self.radius = radius
        
def checkRangeBetwixPoints(a,b):
    return int(sqrt(fabs((a[0]-b[0])**2+(a[1]-b[1])**2)))

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

#            R    G    B
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
YELLOW = (255, 255,   0)
PURPLE = (255,   0, 255)
BLACK = (0,0,0)

BACKGROUND = RED

dotList = []


##create a list of the custom object defined upstairs
for x in range(10):
    dotList.append(Idoru(WHITE, [random.randint(100,600),random.randint(100,400)], 10))


def main():
    ##global FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock() #NOTA BENE: Clock must be Capitalized
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))    
    
    pygame.display.set_caption("ObjectTester")

    while True:
        
        DISPLAYSURF.fill(BACKGROUND)
        
        myBoy = Idoru(WHITE, [100,100], 20)
        
        pygame.draw.circle(DISPLAYSURF, myBoy.color, myBoy.center, myBoy.radius)
        
        for dot in dotList:
            pygame.draw.circle(DISPLAYSURF, dot.color, dot.center, dot.radius)
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        
            elif event.type == MOUSEBUTTONUP:    
                mousex, mousey = event.pos
                print("X: %i  Y: %i"%(mousex,mousey))
                
                for dot in dotList:
                    if dot.radius >= checkRangeBetwixPoints(event.pos,dot.center):
                        print("event.pos" + str(event.pos) + ",  dot.center" + str(dot.center) + ",  RANGE:" + str(checkRangeBetwixPoints(event.pos,dot.center)) + ",  radius:" + str(dot.radius))
                        print("AND IT'S IN A GODDAMN DOTTTTT")
                        dot.color = RED
                    
                
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
if __name__ == '__main__':
    main()
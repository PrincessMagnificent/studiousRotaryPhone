import pygame, sys
##from pygame.locals import *
##if you import the above, you don't need to go pygame.MOUSEBUTTONUP for events
import math

screenSize = screenW, screenH = 640, 480
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (111,111,111)

mousex, mousey = 0,0
multiplier = 50

pygame.init()
screen = pygame.display.set_mode(screenSize)
screen.fill(WHITE)

##line(Surface, color, start_pos, end_pos, width=1) -> Rect



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(WHITE)
            print(event)
            multiplier = screenH - event.pos[1]
            
    for x in range(0,screenW):
        y = int(math.sin(x/float(screenW) * 4 * math.pi) * multiplier + 240)
        pygame.draw.rect(screen, BLACK, [x,y,1,1],1)
        pygame.draw.line(screen, GREY, (0,screenH/2), (screenW,screenH/2))
    
    pygame.display.flip()        
print("successfully completed! Have a nice day.")
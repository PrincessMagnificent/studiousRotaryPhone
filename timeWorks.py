#timeWorks

import pygame, time
from pygame.locals import *
from time import gmtime, strftime


FPS = 1 # frames per second, the general speed of the program

def main():

    FPSCLOCK = pygame.time.Clock()
    numba = 0
    createFile = open("timeLog.txt", "w")
    createFile.write(strftime("%a, %d %b %Y %H:%M:%S \n", gmtime()))
    createFile.close()
    while True:
        #Notice how we avoid the newline
        print("#", end="", flush=True)
        myLog = open("timeLog.txt", "a")
        myLog.write(str(numba))
        print(numba)
        numba += 1
        if numba % 10 == 0:
            myLog.write(strftime("\n%a, %d %b %Y %H:%M:%S \n", gmtime()))
            print("reachedMARKER!!!")
            print(strftime("\n\n%a, %d %b %Y %H:%M:%S \n\n", gmtime()))
        myLog.close()
        
        FPSCLOCK.tick(FPS)
        
        
if __name__ == '__main__':
    main()
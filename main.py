import pygame
import obj
from const import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Fly ball")
    clock = pygame.time.Clock()

    #HERE

    while True:
        screen.fill(SKY)
        
        #HERE

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                exit()
        pygame.display.flip()
        clock.tick(FPS)
#"""


if __name__ == "__main__":
    main()
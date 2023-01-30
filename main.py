import pygame
from sprite import *
from Ball import Ball
from Gun import Gun
from const import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fly ball")
    clock = pygame.time.Clock()

    s = Ball(screen)
    #g = Gun()

    while True:
        screen.fill(SKY)
        
        for i in sprites:
            screen.blit(i.image, i.rect)
            i.Update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                exit()
        clock.tick(FPS)
        pygame.display.update()
#"""


if __name__ == "__main__":
    main()
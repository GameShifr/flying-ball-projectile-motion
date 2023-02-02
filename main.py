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

    g = Gun(screen)
    g.size = (160, 100)
    g.MoveTo(700, 300)

    while True:
        screen.fill(SKY)
        
        for i in sprites:
            screen.blit(i.image, i.rect)
            i.Update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                g.cursorPos = event.pos
        clock.tick(FPS)
        pygame.display.update()
#"""


if __name__ == "__main__":
    main()
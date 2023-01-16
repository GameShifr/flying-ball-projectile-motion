import pygame
from sprite import *
from const import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fly ball")
    clock = pygame.time.Clock()

    s = GameObj("sprites/ball.png")

    while True:
        screen.fill(SKY)
        
        screen.blit(s.image, s.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                exit()
        clock.tick(FPS)
        pygame.display.update()
#"""


if __name__ == "__main__":
    main()
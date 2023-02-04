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

    gun = Gun(screen)
    gun.Resize((80, 50))
    gun.MoveTo((20, invertY(20)))
    #gun.Resize((160, 100))

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
                gun.cursorPos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.fShoot = True
        clock.tick(FPS)
        pygame.display.update()
#"""


if __name__ == "__main__":
    main()
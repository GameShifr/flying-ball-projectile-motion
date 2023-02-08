import pygame
from sprite import *
from Ball import Ball
from Gun import Gun
from data import * 


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fly ball")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)

    gun = Gun(screen)
    gun.Resize((80, 50))
    gun.MoveTo((60, invertY(100)))
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
                cursorPos.clear()
                cursorPos.append(event.pos[0])
                cursorPos.append(event.pos[1])
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.fShoot = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    t = "backspace"
                else:
                    t = event.unicode

        clock.tick(FPS)
        pygame.display.update()
#"""


if __name__ == "__main__":
    main()
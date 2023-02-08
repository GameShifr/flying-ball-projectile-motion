import pygame
from sprite import *
from Ball import Ball
from Gun import Gun
from text import Text
from const import *


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
    size_txt = 24
    a_txt = Text(screen, textRange=(-180, 180), size=size_txt)
    v_txt = Text(screen, textRange=(0, None), size=size_txt)

    while True:
        screen.fill(SKY)

        gun._a = a_txt.update(str(round(gun.a, 1)), (10, 10))
        gun._v = v_txt.update(str(round(gun.F, 1)), (10, 34))

        for i in sprites:
            screen.blit(i.image, i.rect)
            i.Update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                exit()

            if event.type == pygame.MOUSEMOTION:
                gun.cursorPos = event.pos
                a_txt.cursorPos = event.pos
                v_txt.cursorPos = event.pos
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if a_txt.Click():pass
                elif v_txt.Click():pass
                else: gun.fShoot = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    t = "backspace"
                else:
                    t = event.unicode
                if (a_txt.cursorCollide):
                    a_txt.Input(t)
                elif (v_txt.cursorCollide):
                    v_txt.Input(t)

        clock.tick(FPS)
        pygame.display.update()
#"""


if __name__ == "__main__":
    main()
from Data import *
import pygame
from resourses.ball import Ball
from resourses.gun import Gun
from resourses.sprite import Sprite, sprites
from resourses.ui import Entry
from resourses.target import Target


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fly ball")
    clock = pygame.time.Clock()

    gun = Gun(screen, pos=(30, HEIGHT-30), size=(80, 50))
    gun.balls = [Ball(screen) for i in range(10)]
    a_t = Entry(screen, pos=(70, 15), editRange=(-180, 180))
    v_t = Entry(screen, pos=(70, 40), editRange=(1, None))
    ia_t = Entry(screen, pos=(210, 15), editRange=(1, 360), oneText=True)
    iv_t = Entry(screen, pos=(210, 40), editRange=(1, None), oneText=True)
    target = Target(screen, size=(50, 50))
    target.RandPos()

    while True:
        screen.fill(SKY)

        a_t.change_text(str(round(gun.a, 0)))
        v_t.change_text(str(round(gun.v, 0)))
        gun.lock_a = a_t.GetInp()
        gun.lock_v = v_t.GetInp()
        gun.iter_a = ia_t.GetInp()
        gun.iter_v = iv_t.GetInp()

        for i in sprites:
            i.Update()
            screen.blit(i.image, i.rect)

        if GameData.clicked:
            gun.Action()
            GameData.clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEMOTION:
                GameData.cursorPos = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                GameData.clicked = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    t = "backspace"
                else:
                    t = event.unicode
                GameData.key = t
        
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()
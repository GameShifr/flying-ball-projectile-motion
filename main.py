import pygame
from sprite import *
from ui import Button
from Gun import Gun
from data import * 
from target import Target
from random import randrange


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fly ball")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)

    gun = Gun(screen, balls=5)
    gun.Resize((80, 50))
    gun.MoveTo((60, invertY(100)))
    gun = Gun(screen, balls=5)
    gun.Resize((80, 50))
    gun.MoveTo((WIDTH-60, invertY(100)))
    GameData.gun = gun
    
    a_b = Button(screen, canEdit=True, editRange=(-180, 180))
    a_b.MoveTo((10, 10), "topleft")
    f_b = Button(screen, canEdit=True, editRange=(1, None))
    f_b.MoveTo((10, 35), "topleft")
    ia_b = Button(screen, canEdit=True, editRange=(1, 360), oneText=True)
    ia_b.MoveTo((130, 10), "topleft")
    if_b = Button(screen, canEdit=True, editRange=(1, None), oneText=True)
    if_b.MoveTo((130, 35), "topleft")

    target = Target(screen, )
    target.MoveTo((randrange(0, WIDTH), randrange(0, HEIGHT)))

    while True:
        screen.fill(SKY)
        gun = GameData.gun
        gun.active = True

        for i in sprites:
            screen.blit(i.image, i.rect)
            i.Update()

        a_b.text = str(round(gun.a, 0))
        f_b.text = str(round(gun.F, 0))
        #a_b.Update()
        #f_b.Update()
        gun.lock_a = a_b.GetInput()
        gun.lock_v = f_b.GetInput()
        gun.iter_a = ia_b.GetInput()
        gun.iter_v = if_b.GetInput()

        if (GameData.click == True):
            gun.fShoot = True
            GameData.click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                exit()

            if event.type == pygame.MOUSEMOTION:
                GameData.cursorPos = event.pos
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                GameData.click = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    t = "backspace"
                else:
                    t = event.unicode
                GameData.key = t

        clock.tick(FPS)
        pygame.display.update()
#"""


if __name__ == "__main__":
    main()
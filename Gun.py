from const import *
from sprite import *
from Ball import Ball
import threading
from pygame import draw
from math import atan2, degrees, sqrt, sin, cos

class Gun(GameObj):
    sprite = "sprites/guns/gun.png"
    #sprite = "sprites/balls/ball.png"#del
    cursorPos = (0, 0)
    fShoot = False

    def __init__(self, screen, x=WIDTH/2, y=HEIGHT/2, layer=-1) -> None:
        super().__init__(screen, x, y, layer)
        self.ball = None
        #self.image.fill(WHITE)

    def DrawArrow(self, startPos, drawXY=False, invert=False, maxLine=False):
        endPos = self.rect.center #(self.rect.right, self.rect.centery)
        maxL = 300

        draw.line(self.screen, GREEN, startPos, endPos, 3)

        xCat = startPos[0] - endPos[0]
        yCat = startPos[1] - endPos[1]
        self.a = degrees(atan2(yCat, xCat))
        hip = sqrt(xCat**2 + yCat**2)
        
        if (invert):
            self.a -= 180
            if (maxLine):
                pass
            XEndPos = endPos[0] - xCat
            YEndPos = endPos[1] - yCat
            EEndPos = (XEndPos, YEndPos)
            draw.line(self.screen, GREEN, endPos, EEndPos, 3)

        if (drawXY):
            draw.line(self.screen, BLACKGREEN, (startPos), (endPos[0], startPos[1]), 1)
            draw.line(self.screen, BLACKGREEN, (endPos[0], startPos[1]), (endPos), 1)
            if (invert):
                draw.line(self.screen, BLACKGREEN, (endPos), (EEndPos[0], endPos[1]), 1)
                draw.line(self.screen, BLACKGREEN, (EEndPos[0], endPos[1]), (EEndPos), 1)
        
        return hip

    def Update(self):
        super().Update()

        c = self.DrawArrow(self.cursorPos, True)
        self.RotateTo(-self.a)

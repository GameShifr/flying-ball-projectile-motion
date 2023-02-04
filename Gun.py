from const import *
from sprite import *
from Ball import Ball
import threading
from pygame import draw
from math import atan2, degrees, sqrt, sin, cos, radians

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
            
    def PlaceBall(self):
        if (self.ball != None):
            h = self.size[0] /2
            yCat = sin(radians(self.a)) * h
            xCat = cos(radians(self.a)) * h

            x = self.GetCoord()[0] + xCat
            y = self.GetCoord()[1] + yCat

            self.ball.MoveTo((x, y))
            self.ball.start_x = x
            self.ball.start_y = self.invertY(y)
    def Action(self):
        if (self.ball != None): #shoot
            self.ball.a = -self.a
            self.ball.F = 50               #re
            self.ball.fShoot = True
            self.ball = None
        else: #recharge
            l = self.get_layer() - 1
            if l < 0 : l = 0
            self.ball = Ball(self.screen, layer=l)

    def Update(self):
        super().Update()

        c = self.DrawArrow(self.cursorPos, True)
        self.RotateTo(-self.a)
        if (self.fShoot == True):
            self.Action()
            self.fShoot = False
        self.PlaceBall()

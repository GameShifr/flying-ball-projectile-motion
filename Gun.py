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
        self.a = 0
        self.F = 0
        self.ia = None
        self.iv = None
        #self.image.fill(WHITE)

    def DrawArrow(self, cursorPos, drawXY=False, invert=False, a=None, c=None):
        startPos = self.rect.center #(self.rect.right, self.rect.centery)
        xCat = cursorPos[0] - startPos[0]
        yCat = cursorPos[1] - startPos[1]
        self.a = degrees(atan2(yCat, xCat))
        hip = sqrt(xCat**2 + yCat**2)

        if (c != None):
            hip = c*10
        elif (self.iv != None):
            hip = hip//self.iv
        if (a != None):
            self.a = a
        elif (self.ia != None):
            self.a = self.a//self.ia
        yCat = sin(radians(self.a)) * hip
        xCat = cos(radians(self.a)) * hip

        endPos = (startPos[0] + xCat, startPos[1] + yCat)

        draw.line(self.screen, GREEN, startPos, endPos, 3)

        
        if (invert):
            self.a -= 180
            XEndPos = endPos[0] - xCat
            YEndPos = endPos[1] - yCat
            EEndPos = (XEndPos, YEndPos)
            draw.line(self.screen, GREEN, endPos, EEndPos, 3)

        if (drawXY):
            draw.line(self.screen, GREEN, (startPos), (endPos[0], startPos[1]), 1)
            draw.line(self.screen, GREEN, (endPos[0], startPos[1]), (endPos), 1)
            if (invert):
                draw.line(self.screen, GREEN, (endPos), (EEndPos[0], endPos[1]), 1)
                draw.line(self.screen, GREEN, (EEndPos[0], endPos[1]), (EEndPos), 1)
        
        return hip
            
    def PlaceBall(self):
        h = self.size[0] /2
        yCat = sin(radians(self.a)) * h
        xCat = cos(radians(self.a)) * h

        x = self.GetCoord()[0] + xCat
        y = self.GetCoord()[1] + yCat

        if (self.ball != None):
            self.ball.MoveTo((x, y))
            self.ball.start_x = x
            self.ball.start_y = invertY(y)
        return (x, y)
    def Action(self):
        if (self.ball != None): #shoot
            self.ball.a = -self.a
            self.ball.F = self.F              #re
            self.ball.fShoot = True
            self.ball = None
        else: #recharge
            l = self.get_layer() - 1
            if l < 0 : l = 0
            self.ball = Ball(self.screen, layer=l)
            s = self.size[1] /2
            self.ball.Resize((s, s))

    def Update(self):
        super().Update()

        self.F = self.DrawArrow(self.cursorPos, True, a=self._a, c=self._v)/10
        self.RotateTo(-self.a)
        if (self.fShoot == True):
            self.Action()
            self.fShoot = False
        self.PlaceBall()

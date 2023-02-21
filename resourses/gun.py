from Data import *
from resourses.sprite import *
from resourses.ball import Ball
from pygame import draw
from math import atan2, degrees, sqrt, sin, cos, radians

class Gun(Sprite):
    sprite = "sprites/guns/gun.png"

    def __init__(self, screen, rot=0, pos=(0, 0), size=(1, 1), layer=-1, collider=True, clickable=False) -> None:
        super().__init__(screen, rot, pos, size, layer, collider, clickable)
        self.ball = None
        self.balls = []
        self.v = 0
        self.a = 0
        
        self.lock_a = None
        self.lock_v = None
        self.iter_a = None
        self.iter_v = None

    def Arrow(self, cursorPos, drawArrow=True,  drawXY=False, invert=False, lock_a=None, lock_c=None, step_a=None, step_c=None):
        startPos = self.rect.center
        xCat = cursorPos[0] - startPos[0]
        yCat = cursorPos[1] - startPos[1]
        self.a = degrees(atan2(yCat, xCat))
        hip = sqrt(xCat**2 + yCat**2)

        if (lock_c != None):
            hip = lock_c*10
        elif (step_c != None):
            hip -= hip%(step_c * 10)
        if (lock_a != None):
            self.a = lock_a
        elif (step_a != None):
            self.a -= self.a%step_a
        yCat = sin(radians(self.a)) * hip
        xCat = cos(radians(self.a)) * hip

        endPos = (startPos[0] + xCat, startPos[1] + yCat)

        if (drawArrow):
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

    def Recharge(self):
        if (self.ball == None) and (self.balls != []):
            l = self.get_layer() - 1
            if (l < 0): l = 0
            self.ball = self.balls.pop(-1)
            self.ball.change_layer(l)
            s = self.size[1] /2
            self.ball.Resize((s, s))
            self.ball.gun = self
            return True
        return False
    
    def Shoot(self):
        if (self.ball != None):
            self.ball.Shoot()
            self.ball = None
            return True
        return False
    
    def Action(self):
        if (self.ball == None):
            self.Recharge()
        else:
            self.Shoot()

    def PlaceBall(self):
        h = self.size[0] /2
        yCat = sin(radians(self.a)) * h
        xCat = cos(radians(self.a)) * h

        x = self.pos[0] + xCat
        y = self.pos[1] + yCat

        if (self.ball != None):
            
            start = False
            if ((self.ball.rotation != self.rotation)
                or (self.ball.V != self.v)
                or (self.ball.start_pos != (x, y))):
                start = True

            self.ball.rotation = self.rotation
            self.ball.V = self.v
            self.ball.Move((x, y))
            self.ball.start_pos = (x, y)

            self.ball.Traect(start=start)
        #return (x, y)

    def Update(self) -> None:
        self.v = self.Arrow(GameData.cursorPos, lock_a=self.lock_a, lock_c=self.lock_v, step_a=self.iter_a, step_c=self.iter_v)/10
        self.RotateTo(-self.a)
        self.PlaceBall()
        super().Update()
    
    def Click(self) -> None:
        super().Click()
        if (self.ball == None):
            self.Recharge()
        else:
            self.Shoot()
    
    def Select(self) -> None:
        super().Select()


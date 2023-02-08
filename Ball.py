from data import *
from math import sin, cos, radians
from ui import Text
from sprite import *
from pygame import draw

class Ball(GameObj):
    T = 0
    sprite = "sprites/balls/ball.png"
    markPath = True
    fShoot = False
    
    def __init__(self, screen, x=500, y=300, layer=-1) -> None:
        super().__init__(screen, x, y, layer)
        self.size = (30, 30)
        self.a = 0
        self.F = 50
        self.path = []
        self.t = Text(self.screen, x, y)

    def calculate(self, a, V, t):
        Vx = V * cos(radians(a))
        x = self.start_x + Vx * t

        Vy = V * sin(radians(a))
        y = self.start_y + Vy * t - G * t**2 / 2

        return x, y

    def collide(self, pos):
        if ((pos[0] > WIDTH) or (pos[0] < 0)) or ((pos[1] > HEIGHT) or (pos[1] < 0)):
            return True
        return False

    def Update(self):
        super().Update()
        if (self.fShoot):
            if not(self.collide(self.GetCoord())):
                self.T += 1 /FPS
                x, y = self.calculate(self.a, self.F, self.T)
                self.MoveTo((x, invertY(y)))
            self.DrawPath(self.path)

            self.t.MoveTo((self.GetCoord()[0], self.GetCoord()[1]-self.rect.height/2-self.t.rect.height/2))
            self.t.change_text(str(self.GetCoord()))
    
    def DrawPath(self, arr):
        if (len(arr) < 1):
            arr.append((self.start_x, invertY(self.start_y)))

        if (arr[-1] != self.GetCoord()):
            arr.append(self.GetCoord())
        draw.lines(self.screen, RED, False, arr, 3)
        

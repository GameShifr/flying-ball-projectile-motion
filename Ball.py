from const import *
from math import sin, cos
from sprite import *
from pygame import draw

class Ball(GameObj):
    T = 0
    sprite = "sprites/balls/ball.png"
    markPath = True
    fShoot = False
    
    def __init__(self, screen, x=30, y=500, layer=-1) -> None:
        super().__init__(screen, x, y, layer)
        self.size = (30, 30)
        self.path = [[self.rect.x, self.rect.y]]

    def calculate(self, a, V, t):
        Vx = V * cos(a)
        x = self.start_x + Vx * t

        Vy = V * sin(a)
        y = self.start_y + Vy * t - G * t**2 / 2

        return x, y

    def Update(self):
        if (self.fShoot == True):
            self.T += 1 /FPS
            super().Update()
            x, y = self.calculate(0, 70, self.T)
            self.MoveTo(x, y)

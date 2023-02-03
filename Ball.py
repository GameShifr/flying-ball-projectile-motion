from const import *
from math import sin, cos, radians
import math
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

    def calculate(self, a, V, t):
        Vx = V * cos(radians(a))
        x = self.start_x + Vx * t

        Vy = V * sin(radians(a))
        y = self.start_y + Vy * t - G * t**2 / 2

        return x, y

    def Update(self):
        super().Update()
        self.T += 1 /FPS
        x, y = self.calculate(self.a, 50, self.T)
        self.MoveTo((x, HEIGHT-y))

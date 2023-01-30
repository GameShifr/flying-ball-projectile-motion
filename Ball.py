from const import *
from math import sin, cos
from sprite import *
from pygame import draw

class Ball(GameObj):
    T = 0
    sprite = "sprites/ball.png"
    markPath = True
    
    def __init__(self, screen, x=0, y=800, layer=-1) -> None:
        super().__init__(screen, x, y, layer)
        self.path = [[self.start_x, self.start_y]]

    def calculate(self, a, V, t):
        Vx = V * cos(a)
        x = self.start_x + Vx * t

        Vy = V * sin(a)
        y = self.start_y + Vy * t - G * t**2 / 2

        return x, y

    def Update(self):
        self.T += 1 /FPS
        super().Update()
        x, y = self.calculate(0, 70, self.T)
        self.MoveTo(x, y)

        if (self.markPath):
            self.path.append([self.x, self.y])
            draw.lines(self.screen, RED, False, self.path, 3)
from const import *
from math import sin, cos
from sprite import *

class Ball(GameObj):
    T = 0
    sprite = "sprites/ball.png"

    def calculate(self, a, V, t):
        Vx = V * cos(a)
        x = self.start_x + Vx * t

        Vy = V * sin(a)
        y = self.start_y + Vy * t - G * t**2 / 2

        return x, y

    def Update(self):
        self.T += 1 /FPS
        super().Update()
        x, y = self.calculate(0, 10, self.T)
        self.MoveTo(x, y)
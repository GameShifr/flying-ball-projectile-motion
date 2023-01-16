from const import *
from math import sin, cos
from sprite import *

class Ball(GameObj):
    T = 0

    def calculate(self, x, y, a, F, T):
        rx = self.x + F
        return rx, y

    def Update(self):
        self.T += 10/100
        super().Update()
        x, y = self.calculate(self.x, self.y, 0, 1, self.T)
        self.MoveTo(x, y)
from const import *
from math import sin, cos

class Ball():
    def calculate(self, x, y, a, F, T):
        rx = x + F * cos(a) * T
        ry = y + F * sin(a) * T - (G * T**2)/2
        return rx, ry
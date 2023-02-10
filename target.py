from data import *
from sprite import GameObj
from math import sqrt

class Target(GameObj):
    sprite = "sprites/targets/target.png"

    def IsCollide(self, pos):
        r = self.size[0] / 2
        x = self.GetCoord()[0] - pos[0]
        y = self.GetCoord()[1] - pos[1]
        c = sqrt(x**2 + y**2)
        if (c <= r):
            return True
        return False
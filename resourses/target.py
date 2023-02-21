from Data import *
from resourses.sprite import Sprite
from math import sqrt
from random import randrange
from resourses.ball import Ball

class Target(Sprite):
    sprite = "sprites/targets/target.png"

    def IsCollide(self, pos, obj):
        r = self.size[0] / 2
        x = self.pos[0] - pos[0]
        y = self.pos[1] - pos[1]
        c = sqrt(x**2 + y**2)
        if (c <= r):
            return True
        return False
    
    def RandPos(self):
        x = randrange(0, WIDTH)
        y = randrange(0, HEIGHT)
        self.Move((x, y))

    def Collide(self, obj):
        print(str(type(obj)))
        if isinstance(obj, Ball):
            self.RandPos()
from const import *
from math import sin, cos

class GameObj:
    
    def __init__(self, x=0, y=0, a=0) -> None:
        self._x = x
        self._y = y
        self._a = a

class Ball(GameObj):
    g = 9.81
    

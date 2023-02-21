from Data import *
from math import sin, cos, radians
from resourses.sprite import Sprite
from resourses.game_object import colliders
from pygame import draw

class Ball(Sprite):
    sprite = "sprites/balls/ball.png"

    def __init__(self, screen, rot=0, pos=(0, 0), size=(50, 50), layer=-1, collider=True, clickable=False) -> None:
        super().__init__(screen, rot, pos, size, layer, collider, clickable)
        self.Hide()
        self.start_pos = self.pos
        self.V = 0
        self.fShoot = False
        self.T = 0
        self.path = []
        self.t_T = 0
        self.t_path = []
        self.gun = None

    def calculate(self, t):
        Vx = self.V * cos(radians(self.rotation))
        Vy = self.V * sin(radians(self.rotation))

        x = self.start_pos[0] + Vx * t
        y = HEIGHT-self.start_pos[1] + Vy * t - G * t**2 / 2 #- -

        return x, y

    def Shoot(self):
        self.fShoot = True

    def DynamicCollide(self, pos):
        if ((pos[0] > WIDTH) or (pos[0] < 0)) or ((pos[1] > HEIGHT) or (pos[1] < 0)):
            self.fShoot = False
            return True
        
        r = self.size[0] /2
        d = 5
        for obj in colliders:
            for i in range(0, 360, d):
                yCat = sin(radians(i)) * r
                xCat = cos(radians(i)) * r

                x = pos[0] + xCat
                y = pos[1] + yCat 

                if (obj.IsCollide((x, y), self)) and (obj != self) and (obj != self.gun):
                    self.Collide(obj)
                    return True
                
        return False
    
    def Collide(self, obj):
        if (self.fShoot):
            #self.fShoot = False
            if not(isinstance(obj, Ball)):  #del
                obj.Collide(self)
            self.start_pos = self.pos

            self.RotateTo(self.rotation + 90)
            self.T = 0

    def Update(self) -> None:
        if self.fShoot:
            self.DynamicCollide(self.pos)
            self.T += 1/FPS
            x, y = self.calculate(self.T)
            y = HEIGHT-y
            self.Move((x, y))
            self.DrawPath(self.path, self.pos)
        super().Update()

    def Traect(self, ite=10, start=False):
        if (start):
            self.t_T = 0
            self.t_path = []
        while True:
            x, y = self.calculate(self.t_T)
            y = HEIGHT-y
            if (not self.DynamicCollide((x, y))):
                self.t_T += 1/FPS * ite
            else:
                break
            self.DrawPath(self.t_path, (x, y))
        self.DrawPath(self.t_path, (x, y))
    
    def DrawPath(self, path, coord):
        if (len(path) < 1):
            path.append(self.start_pos)

        if (path[-1] != coord):
            path.append(coord)

        try:
            draw.lines(self.screen, RED, False, path, 3)
        except:pass
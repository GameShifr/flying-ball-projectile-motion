from data import *
from math import sin, cos, radians
from ui import Text
from sprite import *
from pygame import draw

class Ball(GameObj):
    sprite = "sprites/balls/ball.png"
    
    def __init__(self, screen, x=500, y=300, layer=-1, collider=True) -> None:
        super().__init__(screen, x, y, layer, collider=collider)
        self.size = (30, 30)
        self.a = 0
        self.F = 50
        self.path = []
        self.t = Text(self.screen, x, y)
        self.t_T = 0
        self.t_path = []
        self.T = 0
        self.overT = 0
        self.markPath = True
        self.fShoot = False

    def calculate(self, a, V, t):
        Vx = V * cos(radians(a))
        x = self.start_x + Vx * t

        Vy = V * sin(radians(a))
        y = self.start_y + Vy * t - G * t**2 / 2

        return x, y

    def collide(self, pos):
        if ((pos[0] > WIDTH) or (pos[0] < 0)) or ((pos[1] > HEIGHT) or (pos[1] < 0)):
            return True
        
        r = self.size[0] /2
        d = 5
        for obj in colliders:
            for i in range(0, 360, d):
                yCat = sin(radians(i)) * r
                xCat = cos(radians(i)) * r

                x = self.GetCoord()[0] + xCat
                y = self.GetCoord()[1] + yCat 

                if (obj.IsCollide((x, y), self)) and (obj != self):
                    return True

        return False

    def Update(self):
        super().Update()
        if (self.fShoot):
            if not(self.collide(self.GetCoord())):
                self.T += 1 /FPS
                x, y = self.calculate(self.a, self.F, self.T)
                self.MoveTo((x, invertY(y)))
            else:
                self.overT += 1 /FPS
                
            if (self.overT <= 5):
                self.DrawPath(self.path, self.GetCoord())
                self.t.MoveTo((self.GetCoord()[0], self.GetCoord()[1]-self.rect.height/2-self.t.rect.height/2))
                self.t.change_text(str(self.GetCoord()))
            else: #delete self.t
                pass
    
    def Traect(self, ite=10):
        if (self.GetCoord() != (self.start_x, self.start_y)):
            self.t_T = 0
            self.t_path = []
        while True:
            x, y = self.calculate(self.a, self.F, self.t_T)
            y = invertY(y)
            if (not self.collide((x, y))):
                self.t_T += 1/FPS * ite
            else:
                break
            if (len(self.t_path) < 1):
                self.t_path.append((self.start_x, invertY(self.start_y)))

            if (self.t_path[-1] != (x, y)):
                self.t_path.append((x, y))

        try:draw.lines(self.screen, RED, False, self.t_path, 3)
        except:print("e")
    
    def DrawPath(self, arr, pos):
        if (len(arr) < 1):
            arr.append((self.start_x, invertY(self.start_y)))

        if (arr[-1] != pos):
            arr.append(pos)
        try: draw.lines(self.screen, RED, False, arr, 3)
        except: print("e")
        

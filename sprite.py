from data import *
import pygame

sprites = []
colliders = []

class GameObj(pygame.sprite.Sprite):
    sprite = "sprites/balls/ball.png" #default image

    def change_sprite(self, filename=None):
        if filename == None: filename = self.sprite
        self.image = pygame.image.load(filename).convert_alpha() #Surface
        self.start_image = self.image
        self.rect = self.image.get_rect()

    def change_layer(self, layer=-1):
        try: sprites.pop(sprites.index(self))
        except:pass
        if layer == -1:
            sprites.append(self)
        else:
            sprites.insert(layer, self)
    def get_layer(self):
        return sprites.index(self)

    def __init__(self, screen, x:float=WIDTH/2, y:float=HEIGHT/2, layer=-1, collider=True) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.change_sprite()
        self.MoveTo((x, y))
        self.start_x = x
        self.start_y = y
        self.change_layer(layer)
        self.screen = screen
        self.size = self.image.get_size()
        if (collider):
            colliders.append(self)

    def Delete(self):
        try:sprites.pop(sprites.index(self))
        except: pass

    def MoveTo(self, pos, type="center"):
        if type == "center":
            self.rect.center=pos
        elif type == "topleft":
            self.rect.topleft=pos
        elif type == "bottomcenter":
            self.rect.bottom=pos[1]
            self.rect.centerx = pos[0]
        elif type == "bottomright":
            self.rect.bottomright=pos
        elif type == "bottomleft":
            self.rect.bottomleft=pos
            
    def Move(self, x, y):
        self.MoveTo(self.x + x, self.y - y)
    def GetCoord(self): #NOTE!!!: add array of coord systems in other pos of rect
        return (self.rect.centerx, self.rect.centery)

    def Update(self):
        pass

    def IsCollide(self, pos, obj):
        if (self.rect.collidepoint(pos)):
            return True
        return False

    def Resize(self, size):
        self.size = size
        center = self.rect.center
        self.image = pygame.transform.scale(self.image, size)
        self.start_image = pygame.transform.scale(self.start_image, size)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def RotateTo(self, angle:float):
        center = self.rect.center
        self.image = pygame.transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = center


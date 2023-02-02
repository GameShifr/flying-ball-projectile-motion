from const import *
import pygame

sprites = []

class GameObj(pygame.sprite.Sprite):
    sprite = "sprites/ball.png" #default image

    def change_sprite(self, filename):
        self.image = pygame.image.load(filename).convert_alpha() #Surface
        self.start_image = self.image
        self.rect = self.image.get_rect()

    def change_layer(self, layer=-1):
        if layer == -1:
            sprites.append(self)
        else:
            sprites.insert(layer, self)


    def __init__(self, screen, x=WIDTH/2, y=HEIGHT/2, layer=-1) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.change_sprite(self.sprite)
        self.MoveTo(x, y)
        self.start_x = x
        self.start_y = y
        self.change_layer(layer)
        self.screen = screen
        self.size = self.GetSize()

    def MoveTo(self, x, y):
        self.rect.centerx = x
        self.rect.centery = HEIGHT - y
    def MoveToCoord(self, center):
        self.rect.center = center
    def Move(self, x, y):
        self.MoveTo(self.x + x, self.y - y)

    def Update(self):
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.Resize(self.size)

    def Resize(self, size):
        center = self.rect.center
        self.image = pygame.transform.scale(self.image, size)
        self.start_image = pygame.transform.scale(self.start_image, size)
        self.rect = self.image.get_rect()
        self.rect.center = center
    def GetSize(self):
        size = self.image.get_size()
        return size

    def RotateTo(self, angle:float):
        center = self.rect.center
        self.image = pygame.transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = center


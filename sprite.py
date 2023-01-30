from const import *
import pygame

sprites = []

class GameObj(pygame.sprite.Sprite):
    sprite = "sprites/ball.png" #default image

    def change_sprite(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()

    def change_layer(self, layer=-1):
        if layer == -1:
            sprites.append(self)
        else:
            sprites.insert(layer, self)


    def __init__(self, screen, x=0, y=800, layer=-1) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.change_sprite(self.sprite)
        self.MoveTo(x, y)
        self.start_x = x
        self.start_y = y
        self.change_layer(layer)
        self.screen = screen

    def MoveTo(self, x, y):
        self.rect.centerx = x
        self.rect.centery = HEIGHT - y
    def Move(self, x, y):
        self.MoveTo(self.x + x, self.y - y)

    def Update(self):
        self.x = self.rect.centerx
        self.y = self.rect.centery

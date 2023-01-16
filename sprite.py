from const import *
import pygame

sprites = []

class GameObj(pygame.sprite.Sprite):

    def __init__(self, filename, layer=None, x=0, y=HEIGHT) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.start_x = x
        self.start_y = y

        if layer == None:
            sprites.append(self)
        else:
            sprites.insert(layer, self)

    def MoveTo(self, x, y):
        self.rect.x = x
        self.rect.y = y
    def Move(self, x, y):
        self.MoveTo(self.x + x, self.y + y)

    def Update(self):
        self.x = self.rect.x
        self.y = self.rect.y

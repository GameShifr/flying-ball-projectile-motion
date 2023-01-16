from const import *
import pygame

sprites = pygame.sprite.Group()

class GameObj(pygame.sprite.Sprite):

    def __init__(self, filename, x=WIDTH/2, y=HEIGHT/2) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def MoveTo(self, x, y):
        self.rect.center = (x, y)
    def Move(self, x, y):
        self.MoveTo(self.rect.x + x, self.rect.y + y)

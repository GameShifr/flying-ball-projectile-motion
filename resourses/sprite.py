from Data import *
from resourses.game_object import GameObject
import pygame

sprites = []

class Sprite(GameObject):
    sprite = "sprites/balls/ball.png" #default sprite

    def change_layer(self, layer=-1):
        self.Hide()
        if layer == -1:
            sprites.append(self)
        else:
            sprites.insert(layer, self)
    def get_layer(self):
        return sprites.index(self)
    def Hide(self):
        try: sprites.pop(sprites.index(self))
        except: pass
        
    def change_sprite(self, filename=None):
        if (filename == None):
            filename = self.sprite
        self.image = pygame.image.load(filename).convert_alpha() #Surface
        self.start_image = self.image#pygame.image.load(filename).convert_alpha() #change
        self.rect = self.image.get_rect()

    def __init__(self, screen, rot=0, pos=(0, 0), size=(1, 1), layer=-1, collider=True, clickable=False) -> None:
        super().__init__(screen, rot, pos, size, collider)
        self.clickable = clickable
        self.change_layer(layer)

    def Update(self) -> None:
        if self.rect.collidepoint(GameData.cursorPos):
            self.Select()

    def Click(self) -> None:
        GameData.clicked = False

    def Select(self) -> None:
        if (GameData.clicked) and (self.clickable):
            self.Click()


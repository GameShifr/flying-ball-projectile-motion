from data import *
from sprite import GameObj
from pygame import font as pygameFont, rect as pygameRect

class Text(GameObj):
    text = ""

    def __init__(self, screen, x: float=0, y: float=0, layer=-1) -> None:
        self.rect = pygameRect.Rect(x, y, 0, 0)
        super().__init__(screen, x, y, layer)

    def change_sprite(self, size=24, font="arial", color=BLACK, bgcolor=None):
        f = pygameFont.SysFont(font, size)
        self.image = f.render(self.text, True, color, bgcolor)
        #self.rect = self.image.get_rect()
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()
    
    def change_text(self, text:str):
        self.text = text
        self.change_sprite()

    def Resize(self, size):
        self.size = size
        self.change_sprite()


class Button(Text):
    ...

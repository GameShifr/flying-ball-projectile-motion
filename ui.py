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
    clicked = False
    inp_text = ""
    def __init__(self, screen, x: float = 0, y: float = 0, layer=-1, canEdit=False, colors=((WHITE, None), (RED, BLUE), (GREEN, None)), editRange=None, oneText=False) -> None:
        self.colors = colors #(color, bgcolor): normal, chose, click
        self.canEdit = canEdit
        self.editRange = editRange
        super().__init__(screen, x, y, layer)

    def Input(self, sim):
        if (sim == "backspace"):
            self.inp_text = self.inp_text[:-1]
            if (self.inp_text == "") or (self.inp_text == "-"):self.text = "0"
        else:
            t = self.inp_text + sim
            if (self.editRange != None):
                if (sim == "-"):
                    t = t[:-1]*-1
                try:
                    t = int(t)
                    if (self.editRange[0] != None):
                        if not(t >= self.editRange[0]):
                            t = self.editRange[0]
                    if (self.editRange[1] != None):
                        if not(t <= self.editRange[1]):
                            t = self.editRange[1]
                except:
                    t = self.inp_text
            
            self.inp_text = str(t)

    def Click(self):
        self.clicked = not self.clicked

    def Update(self):
        if (self.clicked):
            self.change_sprite(color=self.colors[2][0], bgcolor=self.colors[2][1])
        elif (self.rect.collidepoint(cursorPos)):
            self.change_sprite(color=self.colors[1][0], bgcolor=self.colors[1][1])
            self.Input(key)
        else:
            self.change_sprite(color=self.colors[0][0], bgcolor=self.colors[0][1])

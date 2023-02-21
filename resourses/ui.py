from Data import *
from resourses.sprite import Sprite
from pygame import font as pygameFont, Rect as pygameRect

class Text(Sprite):

    def __init__(self, screen, rot=0, pos=(0, 0), size=(24, 24*5), collider=False, clickable=True) -> None:
        self.text = ""
        self.rect = pygameRect(0, 0, 0, 0)
        super().__init__(screen, rot, pos, size, collider=collider, clickable=clickable)

    def change_sprite(self, font="arial", color=BLACK, bgcolor=None):
        f = pygameFont.SysFont(font, self.size[0])
        self.image = f.render(self.text, True, color, bgcolor)
        self.rect.width = self.size[1]
        self.rect.height = self.image.get_height()
    
    def change_text(self, text:str):
        self.text = text
        self.change_sprite()

    def Resize(self, size):
        self.size = size
        self.change_sprite()
    
    def RotateTo(self, angle: float):
        pass


class Entry(Text):

    def __init__(self, screen, rot=0, pos=(0, 0), size=(24, 24*5), colors=((BLACK, None), (RED, BLUE), (RED, None)), editRange=None, oneText=False, collider=False, clickable=True) -> None:
        self.inp_text = "0"
        self.colors = colors
        self.editRange = editRange
        self.active = False
        self.oneText = oneText
        super().__init__(screen, rot, pos, size, collider=collider, clickable=clickable)
    
    def GetInp(self):
        if (self.active == True):
            if (self.editRange[0] != None):
                if (int(self.inp_text) < self.editRange[0]):
                    return self.editRange[0]
            return int(self.inp_text)
        return None
    
    def Input(self, sim):
        if (sim != ""):
            if (sim == "backspace"):
                self.inp_text = self.inp_text[:-1]
                if (self.inp_text == "") or (self.inp_text == "-"):
                    self.inp_text = "0"
            else:
                t = self.inp_text + sim
                if (self.editRange != None):
                    if (sim == "-"):
                        t = int(t[:-1])*-1
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
    
    def Select(self) -> None:
        #self.rect.collidepoint(GameData.cursorPos)
        self.change_text(self.inp_text)
        self.change_sprite(color=self.colors[1][0], bgcolor=self.colors[1][1])
        self.Input(GameData.key)
        GameData.key = ""
        super().Select()

    def Click(self) -> None:
        self.active = not self.active
        super().Click()

    def Update(self) -> None:
        if (self.active):
            self.change_text(self.inp_text)
            self.change_sprite(color=self.colors[2][0], bgcolor=self.colors[2][1])
        else:
            if (self.oneText):
                self.change_text(self.inp_text)
            else:
                self.change_text(self.text)
            self.change_sprite(color=self.colors[0][0], bgcolor=self.colors[0][1])
        super().Update()

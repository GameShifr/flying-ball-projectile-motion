from const import *
from pygame import font, Rect

class Text():
    text = "0"

    def __init__(self,screen, size=24, font="arial", textRange=(-1, 1), colors=((BLACK, RED), (BLACKGREEN, GREEN))) -> None:
        self.changeFont(font, size)
        self.screen = screen
        self.colors = colors
        self.cursorPos = (0, 0)
        self.cursorCollide = False
        self.Lock = False
        self.text_range = textRange
        
    def changeFont(self, name, size):
        self.font = font.SysFont(name, size)
        self.rect = Rect(0, 0, size*5, size)
    
    def Click(self):
        if (self.cursorCollide):
            self.Lock = not self.Lock
        return self.cursorCollide
    
    def Input(self, sim):
        if (sim == "backspace"):
            self.text = self.text[:-1]
            if (self.text == "") or (self.text == "-"):self.text = "0"
        else:
            t = self.text + sim
            if (self.text_range != None):
                if (sim == "-"):
                    t = t[:-1]*-1
                try:
                    t = int(t)
                    if (self.text_range[0] != None):
                        if not(t >= self.text_range[0]):
                            t = self.text_range[0]
                    if (self.text_range[1] != None):
                        if not(t <= self.text_range[1]):
                            t = self.text_range[1]
                except:
                    t = self.text
            
            self.text = str(t)

    def update(self, text:str, pos, to="topleft"):
        if (self.Lock):
            color = self.colors[1]
            text = self.text
            r = int(self.text)
        else:
            color = self.colors[0]
            r = None

        if (self.rect.collidepoint(self.cursorPos[0], self.cursorPos[1])):
            self.bgcolor = BLUE
            self.cursorCollide = True
            self.color = color[1]
            text = self.text
        else:
            self.color = color[0]
            self.bgcolor = None
            self.cursorCollide = False
        
        surf = self.font.render(text, True, self.color, self.bgcolor)

        if to == "center":
            self.rect.center=pos
        elif to == "topleft":
            self.rect.topleft=pos
        elif to == "bottomcenter":
            self.rect.bottom=pos[1]
            self.rect.centerx = pos[0]
        elif to == "bottomright":
            self.rect.bottomright=pos
        elif to == "bottomleft":
            self.rect.bottomleft=pos

        self.screen.blit(surf, self.rect)
        return r

        

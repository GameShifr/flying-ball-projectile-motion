from const import *
from pygame import font, Rect

class Text():
    text = ""

    def __init__(self,screen, size=24, font="arial", colors=((BLACK, RED), (BLACKGREEN, GREEN))) -> None:
        self.changeFont(font, size)
        self.screen = screen
        self.colors = colors
        self.cursorPos = (0, 0)
        self.cursorCollide = False
        self.Lock = False
        
    def changeFont(self, name, size):
        self.font = font.SysFont(name, size)
        self.rect = Rect(0, 0, size*5, size)
    
    def Click(self):
        if self.cursorCollide:
            self.Lock = not self.Lock
        return self.cursorCollide

    def update(self, text:str, pos, to="topleft"):
        if (self.Lock):
            color = self.colors[1]
        else:
            color = self.colors[0]

        if (self.rect.collidepoint(self.cursorPos[0], self.cursorPos[1])):
            self.bgcolor = BLUE
            self.cursorCollide = True
            self.color = color[1]
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

        

from pygame import Rect

class BoxCollider():

    def __init__(self, x=0, y=0, width=50, height=50) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    
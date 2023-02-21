from Data import *
import pygame

colliders = []

class GameObject(pygame.sprite.Sprite):

    def change_sprite(self):
        self.image = pygame.Surface(self.size)
        self.start_image = self.image
        self.rect = self.image.get_rect()

    def __init__(self, screen, rot=0, pos=(0, 0), size=(1, 1), collider=True) -> None:
        pygame.sprite.Sprite.__init__(self)
        if (collider):
            colliders.append(self)
        self.screen = screen
        self.size = size
        self.change_sprite()
        self.RotateTo(rot)
        self.Move(pos)
        self.Resize(size)

    def Move(self, pos):
        self.pos = pos
        self.rect.center = pos

    def Resize(self, size):
        self.size = size
        center = self.rect.center
        self.image = pygame.transform.scale(self.image, size)
        self.start_image = pygame.transform.scale(self.start_image, size)
        self.rect = self.image.get_rect()
        self.rect.center = center
    
    def RotateTo(self, angle:float):
        self.rotation = angle
        center = self.rect.center
        self.image = pygame.transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def Delete(self):
        try:colliders.pop(colliders.index(self))
        except: pass

    def DynamicCollide(self, pos):
        if ((pos[0] > WIDTH) or (pos[0] < 0)) or ((pos[1] > HEIGHT) or (pos[1] < 0)):
            return True
        
        for obj in colliders:
            if (obj != self):
                if (self.rect.colliderect(obj.rect)):
                    self.Collide(obj)
                    return True

        return False
    
    def IsCollide(self, pos, obj):
        if (self.rect.collidepoint(pos)):
            #self.Collide(obj)
            return True
        return False
    
    def Collide(self, obj):
        pass


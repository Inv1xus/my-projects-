import pygame
pygame.init()

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,screen_height):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('White')
        self.rect = self.image.get_rect(center= pos)
        self.speed = speed
        self.heighty_constraint = screen_height
    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.heighty_constraint+50:
            self.kill()
    def update(self):
        self.rect.y += self.speed
        self.destroy()
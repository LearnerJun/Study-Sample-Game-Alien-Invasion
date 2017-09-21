import pygame

class Ship():
    def __init__(self, screen):
        #set the start position
        self.screen = screen

        #get the image of Ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()


        #set the position of ship to the mid screen
        self.rect = self.image.get_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #draw the ship
        self.screen.blit(self.image, self.rect)
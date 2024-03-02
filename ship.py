import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 30

        #movement
        self.is_moving_right = False
        self.is_moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.is_moving_right:
            self.rect.centerx += 1
        elif self.is_moving_left:
            self.rect.centerx -= 1

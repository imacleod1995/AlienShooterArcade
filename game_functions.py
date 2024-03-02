import pygame.event
import sys

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, ship, settings):
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()
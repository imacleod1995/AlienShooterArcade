import pygame.event
import sys

def check_events(ship, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(screen, ship, settings):
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.is_moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.is_moving_left = False


import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)

    while True:
        gf.check_events(ship, ai_settings)
        ship.update()
        gf.update_screen(screen, ship, ai_settings)


run_game()

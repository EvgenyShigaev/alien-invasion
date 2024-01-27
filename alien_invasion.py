import pygame
from settings import Settings
from ship import Ship
import game_fuctions as gf
from pygame.sprite import Group


def run_game():
    """Запуск игры"""
    # инициализирует настройки, необходимые Pygame для нормальной работы
    pygame.init()
    ai_settings = Settings()
    # создает отображаемую область и задает ей размеры в tuple(w, h)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    ship = Ship(ai_settings, screen)
    # группа для хранения пуль
    bullets = Group()
    pygame.display.set_caption("Alien Invasion")
    # запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

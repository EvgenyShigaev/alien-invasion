import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Управление  выпущенными пулями"""

    def __init__(self, ai_settings, screen, ship):
        """Создает объект пули в текущей позиции корабля"""
        # super используется для наследования от Sprite
        super().__init__()
        self.screen = screen
        # так как картинки пули нет, она создается прямоугольником
        # он инициализируется в точке 0, 0 и после этого ему задаются размеры
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        # место появления пули = верхняя центральная точка корабля
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # позиция пули хранится в формате float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Перемещение пули вверх по экрану"""
        # обновление позиции пули
        self.y -= self.speed_factor
        # обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)

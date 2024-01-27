import pygame


class Ship:
    # screen здесь это то, где будет выводиться корабль
    def __init__(self, ai_settings, screen) -> None:
        """Инициализирует начальное положение корабля"""
        self.screen = screen
        self.ai_settings = ai_settings
        # загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load("images/spaceship.bmp")
        # rect от rectangle(прямоугольник)
        # метод get_rect() задает положение объекта
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # флаги перемещения
        self.moving_right = False
        self.moving_left = False
        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # обновляет атрибут center, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # обновление атрибута rect на основании self.center
        self.rect.centerx = self.center

    # метод blitme выводит изображение на экран в позиции, заданной self.rect
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

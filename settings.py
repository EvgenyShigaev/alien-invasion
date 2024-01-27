class Settings():
    """Класс для хранения настроек игры"""

    def __init__(self):
        """Инициализирует найстройки игры"""
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        # параметры пуль
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

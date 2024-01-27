# sys нужен для завершения игры по команде
import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Движение корабля при нажатии кнопок"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_d:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Останановка корабля при отпускании кнопок"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Обрабатывает нажатия кнопок с клавиатуры и мыши"""
    # pygame.event.get() - получение доступа к событиям, обнаруженным pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    # перерисовывает экран при каждом проходе цикла
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Отображение последнего отрисованного экрана
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиций пуль.
    bullets.update()
    # удаление пуль за краем экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(bullets, ai_settings, screen, ship):
    """Выпускает пулю, если максимум еще не достигнут."""
    # создание новой пули и включение ее в группу
    # проверка количества допустимых пуль на экране
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

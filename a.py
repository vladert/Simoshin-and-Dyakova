import pygame
import math

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размеры окна
WIDTH = 500
HEIGHT = 500

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("360 Degrees Bullet")

# Загрузка изображения пули
bullet_image = pygame.image.load("bullet.png")

# Позиционирование пули
bullet_rect = bullet_image.get_rect()
bullet_rect.center = (WIDTH // 2, HEIGHT // 2)

# Определение скорости пули
bullet_speed = 5

# Главный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Определение координат клика мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Расчет угла между пулей и кликом мыши
            dx = mouse_x - bullet_rect.centerx
            dy = bullet_rect.centery - mouse_y
            angle = math.degrees(math.atan2(dy, dx))

            # Поворот пули в направлении клика мыши
            bullet_image_rotated = pygame.transform.rotate(bullet_image, angle)

            # Обновление позиции и направления пули
            bullet_rect = bullet_image_rotated.get_rect(center=bullet_rect.center)
            bullet_direction = pygame.Vector2(1, 0).rotate(-angle)

    # Очистка экрана
    screen.fill(WHITE)

    # Обновление позиции пули
    bullet_rect.move_ip(bullet_direction * bullet_speed)

    # Отрисовка пули
    screen.blit(bullet_image_rotated, bullet_rect)

    # Обновление экрана
    pygame.display.flip()

# Выход из игры
pygame.quit()

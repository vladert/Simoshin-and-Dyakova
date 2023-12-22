# Импорт библиотек
import os
import random
import sys
import pygame

# Инициализация окна
pygame.init()
# Обработка повторного срабатывания клавиш
# delay задержка перед первым срабатыванием
# interval между срабатыванием
pygame.key.set_repeat(200, 70)
sk_right = ['skeleton-move_0.png',
            'skeleton-move_1.png',
            'skeleton-move_2.png',
            'skeleton-move_3.png',
            'skeleton-move_4.png',
            'skeleton-move_5.png',
            'skeleton-move_6.png',
            'skeleton-move_7.png',
            'skeleton-move_8.png',
            'skeleton-move_9.png',
            'skeleton-move_10.png',
            'skeleton-move_11.png',
            'skeleton-move_12.png',
            'skeleton-move_13.png',
            'skeleton-move_14.png',
            'skeleton-move_15.png',
            'skeleton-move_16.png']
FPS = 60
WIDTH = 800
HEIGHT = 600
STEP = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


# Функция загрузки изображения
def load_image(name, transparent=False):
    fullname = os.path.join('resources', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if transparent:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


# Функция загрузки уровня
def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


# Генерация уровня на основе загруженной карты
def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


# Функция закрытия приложения
def terminate():
    pygame.quit()
    sys.exit()


# Стартовое окно


# Реестр изображений
tile_images = {'wall': load_image('rock.png'), 'empty': load_image('floor.png')}
player_image = load_image('skeleton-move_0.png', transparent=True)
# Размер блоков
tile_width = tile_height = 50


# Класс блока/плитки
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


# Класс персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)


# Класс камеры
class Camera:
    # зададим начальный сдвиг камеры и размер поля для возможности реализации циклического сдвига
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        # вычислим координату плитки, если она уехала влево за границу экрана
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * obj.rect.width
        # вычислим координату плитки, если она уехала вправо за границу экрана
        if obj.rect.x >= (self.field_size[0]) * obj.rect.width:
            obj.rect.x += -obj.rect.width * (1 + self.field_size[0])
        obj.rect.y += self.dy
        # вычислим координату плитки, если она уехала вверх за границу экрана
        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * obj.rect.height
        # вычислим координату плитки, если она уехала вниз за границу экрана
        if obj.rect.y >= (self.field_size[1]) * obj.rect.height:
            obj.rect.y += -obj.rect.height * (1 + self.field_size[1])

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, *args):
        super().__init__(all_sprites)
        self.frames = []
        self.frames.extend(args)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


# Загрузка и генерация уровня
print(load_level("levelex.txt"))
player, level_x, level_y = generate_level(load_level("levelex.txt"))
# Создание камеры
camera = Camera((level_x, level_y))
count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= STEP
            if event.key == pygame.K_RIGHT:
                a = [load_image("skeleton-move_0"),
                     load_image("skeleton-move_1"),
                     load_image("skeleton-move_2"),
                     load_image("skeleton-move_3"),
                     load_image("skeleton-move_4"),
                     load_image("skeleton-move_5"),
                     load_image("skeleton-move_6"),
                     load_image("skeleton-move_7"),
                     load_image("skeleton-move_8"),
                     load_image("skeleton-move_9"),
                     load_image("skeleton-move_10"),
                     load_image("skeleton-move_11"),
                     load_image("skeleton-move_12"),
                     load_image("skeleton-move_13"),
                     load_image("skeleton-move_14"),
                     load_image("skeleton-move_15"),
                     load_image("skeleton-move_16")]
                dragon = AnimatedSprite(load_image("skeleton-move_0"), 50, 50, a)
                player.rect.x += STEP
            if event.key == pygame.K_UP:
                player.rect.y -= STEP
            if event.key == pygame.K_DOWN:
                player.rect.y += STEP

    for key, sprite in enumerate(all_sprites):
        camera.apply(sprite)

    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)


# Выход из игры
terminate()


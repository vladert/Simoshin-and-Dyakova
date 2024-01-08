import math
import os
import sys
import pygame

import tile
from camera import Camera
from player import Player
from tile import Tile


def a():
    # Инициализация окна
    pygame.init()
    # Обработка повторного срабатывания клавиш
    # delay задержка перед первым срабатыванием
    # interval между срабатыванием
    pygame.key.set_repeat(200, 70)
    idle_path_images = ['player\idle\skeleton-move_0.png']
    sk = ['player\movement\skeleton-move_0.png',
          'player\movement\skeleton-move_1.png',
          'player\movement\skeleton-move_2.png',
          'player\movement\skeleton-move_3.png',
          'player\movement\skeleton-move_4.png',
          'player\movement\skeleton-move_5.png',
          'player\movement\skeleton-move_6.png',
          'player\movement\skeleton-move_7.png',
          'player\movement\skeleton-move_8.png',
          'player\movement\skeleton-move_9.png',
          'player\movement\skeleton-move_10.png',
          'player\movement\skeleton-move_11.png',
          'player\movement\skeleton-move_12.png',
          'player\movement\skeleton-move_13.png',
          'player\movement\skeleton-move_14.png',
          'player\movement\skeleton-move_15.png',
          'player\movement\skeleton-move_16.png']
    FPS = 60
    WIDTH = 800
    HEIGHT = 600
    STEP = 2
    BULLET_SPEED = 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

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

    # Генерация уровня на основе загруженной карты
    def generate_level(level):
        new_player, x, y = None, None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y, tiles_group, all_sprites, tile_images, tile_width, tile_height)
                elif level[y][x] == '#':
                    print(y, x)
                    Tile('wall', x, y, tiles_group, all_sprites, tile_images, tile_width, tile_height, wall_group)
                elif level[y][x] == '@':
                    Tile('empty', x, y, tiles_group, all_sprites, tile_images, tile_width, tile_height)
                    params = {
                        'tile_width': tile_width,
                        'tile_height': tile_height,
                        'pos_x': x,
                        'pos_y': y,
                    }
                    new_player = Player(player_images, params)
        # вернем игрока, а также размер поля в клетках
        return new_player, x, y


    # Функция закрытия приложения
    def terminate():
        pygame.quit()
        sys.exit()


    # Стартовое окно

    def proverka_left():
        if pygame.sprite.spritecollideany(player, wall_group):
            h = pygame.sprite.spritecollideany(player, wall_group)
            print(h.rect.x, h.rect.y, player.rect.x, player.rect.y)
            player.rect.x = h.rect.x + 50

    def proverka_right():
        if pygame.sprite.spritecollideany(player, wall_group):
            h = pygame.sprite.spritecollideany(player, wall_group)
            print(h.rect.x, h.rect.y, player.rect.x, player.rect.y)
            player.rect.x = h.rect.x - 70

    def proverka_up():
        if pygame.sprite.spritecollideany(player, wall_group):
            h = pygame.sprite.spritecollideany(player, wall_group)
            print(h.rect.x, h.rect.y, player.rect.x, player.rect.y)
            player.rect.y = h.rect.y + 50

    def proverka_down():
        if pygame.sprite.spritecollideany(player, wall_group):
            h = pygame.sprite.spritecollideany(player, wall_group)
            print(h.rect.x, h.rect.y, player.rect.x, player.rect.y)
            player.rect.y = h.rect.y - 70
    # Реестр изображений
    tile_images = {'wall': load_image('rock.png'), 'empty': load_image('floor.png')}
    player_image = load_image('player\movement\skeleton-move_0.png', transparent=True)
    # Размер блоков
    tile_width = tile_height = 50

    player_images = {'idle': [load_image(im, transparent=True) for im in idle_path_images],
                     'movement': [load_image(im, transparent=True) for im in sk]}
    # Загрузка изображения пули
    bullet_image = pygame.image.load("bullet.png")
    # Позиционирование пули
    bullet_rect = bullet_image.get_rect()

    class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, x, y, *args):
            self.image = self.frames[self.cur_frame]
            self.rect = pygame.Rect(0, 0, 50, 54)


        def update(self):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]


    # Загрузка и генерация уровня
    print(load_level("levelex.txt"))
    player, level_x, level_y = generate_level(load_level("levelex.txt"))
    player_group.add(player)
    # Создание камеры
    camera = Camera((level_x, level_y), WIDTH, HEIGHT)
    count = 0
    running = True
    bullet_rect.center = (player.rect.x, player.rect.y)
    while running:
        #screen.fill(pygame.Color(0, 0, 0))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if keys[pygame.K_LEFT]:
            player.rect.x -= STEP
            player.current_animation = 'movement'
            proverka_left()

        if keys[pygame.K_RIGHT]:
            player.rect.x += STEP
            player.current_animation = 'movement'
            proverka_right()

        if keys[pygame.K_UP]:
            player.rect.y -= STEP
            player.current_animation = 'movement'
            proverka_up()

        if keys[pygame.K_DOWN]:
            player.rect.y += STEP
            player.current_animation = 'movement'
            proverka_down()

        if not any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]):
            player.current_animation = 'idle'

        for key, sprite in enumerate(all_sprites):
            camera.apply(player)


        tiles_group.draw(screen)
        wall_group.draw(screen)
        mouse_pos = pygame.mouse.get_pos()
        player.update(mouse_pos)
        player_group.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)


    # Выход из игры
    terminate()
a()
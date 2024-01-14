import os
import sqlite3
import sys
import pygame
from bullet_title import BulletTile
from enemy import Enemy
from camera import Camera
from finaly import finaly
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

    idle_path_images_enemy = ['zombi\idle\enemy1.png']
    ck = ['zombi\movement\enemy1.png',
          'zombi\movement\enemy2.png',
          'zombi\movement\enemy3.png',
          'zombi\movement\enemy4.png',
          'zombi\movement\enemy5.png',
          'zombi\movement\enemy6.png',
          'zombi\movement\enemy7.png',
          'zombi\movement\enemy8.png',
          'zombi\movement\enemy9.png',
          'zombi\movement\enemy10.png',
          'zombi\movement\enemy11.png',
          'zombi\movement\enemy12.png',
          'zombi\movement\enemy13.png',
          'zombi\movement\enemy14.png',
          'zombi\movement\enemy15.png',
          'zombi\movement\enemy16.png',
          'zombi\movement\enemy17.png',
          'zombi\movement\enemy18.png',
          'zombi\movement\enemy19.png',
          'zombi\movement\enemy20.png',]
    FPS = 60
    WIDTH = 800
    HEIGHT = 600
    STEP = 3
    HEALTH = 100
    HEALTH_ENEMY = 100
    GAME = True
    All_ENEMY = 0
    KOL_ENEMY = 0
    KOL_BULLET = 0
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res2 = cur.execute('SELECT gun FROM person WHERE id == 1').fetchall()
    print(res2)
    res = cur.execute(f'SELECT health FROM weapons WHERE id == {res2[0][0]}').fetchall()
    HEALTH_BULLET = res[0][0]
    con.close()
    bullet_list = []
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()

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
    def generate_level(ALL_ENEMY, level):
        enemy_list = []
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
                elif level[y][x] == '*':
                    Tile('empty', x, y, tiles_group, all_sprites, tile_images, tile_width, tile_height)
                    params = {
                        'tile_width': tile_width,
                        'tile_height': tile_height,
                        'pos_x': x,
                        'pos_y': y,
                    }
                    ALL_ENEMY += 1
                    enemy = Enemy(enemy_images, HEALTH_ENEMY, params)
                    enemy_list.append(enemy)
                    enemy_group.add(enemy)
        # вернем игрока, а также размер поля в клетках
        return new_player, enemy_list, x, y

    # Функция закрытия приложения
    def terminate():
        pygame.quit()
        sys.exit()

    # def bullet():
    #     for event in pygame.event.get():
    #         print(1)
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             mouse_pos = pygame.mouse.get_pos()
    #             X, Y = mouse_pos[0], mouse_pos[1]
    #             bullet = BulletTile('bullet', player.rect.x, player.rect.y, bullet_group, all_sprites, tile_images, X, Y)
    #             bullet_group.add(bullet)


    def proverka(KOL_ENEMY):
        x = player.rect.x
        y = player.rect.y
        for i in enemy_group:
            x1 = i.rect.x
            y1 = i.rect.y
            if x1 > x: i.rect.x -= 1
            if x1 < x: i.rect.x += 1
            if y1 > y: i.rect.y -= 1
            if y1 < y: i.rect.y += 1

            if pygame.sprite.spritecollideany(i, wall_group):
                if x1 > x: i.rect.x += 1
                if x1 < x: i.rect.x -= 1
                if y1 > y: i.rect.y += 1
                if y1 < y: i.rect.y -= 1
            if pygame.sprite.spritecollideany(i, bullet_group):
                c = pygame.sprite.spritecollideany(i, bullet_group)
                c.kill()
                h = Enemy.battle(i, HEALTH_BULLET)
                if h <= 0:
                    enemy_list.remove(i)
                    KOL_ENEMY += 1
                print(h)

            if Enemy.health(i) < 0:
                i.kill()




    # Реестр изображений
    tile_images = {'wall': load_image('rock.png'), 'empty': load_image('floor.png'),
                   'bullet': load_image('fireball.png')}
    player_image = load_image('player\movement\skeleton-move_0.png', transparent=True)
    # Размер блоков
    tile_width = tile_height = 50

    player_images = {'idle': [load_image(im, transparent=True) for im in idle_path_images],
                     'movement': [load_image(im, transparent=True) for im in sk]}
    enemy_images = {'movement': [load_image(im, transparent=True) for im in ck]}


    # Загрузка и генерация уровня
    print(load_level("levelex.txt"))
    player, enemy_list, level_x, level_y = generate_level(All_ENEMY, load_level("levelex.txt"))
    player_group.add(player)
    # Создание камеры
    camera = Camera((level_x, level_y), WIDTH, HEIGHT)
    count = 0
    running = True
    while running:
        # screen.fill(pygame.Color(0, 0, 0))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                X, Y = mouse_pos[0], mouse_pos[1]
                bullet = BulletTile('bullet', player.rect.x, player.rect.y, bullet_group, all_sprites, tile_images, X, Y)
                bullet_group.add(bullet)
                bullet_list.append(bullet)
                KOL_BULLET += 1

        if keys[pygame.K_LEFT]:
            player.rect.x -= STEP
            player.current_animation = 'movement'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.x += STEP

        if keys[pygame.K_RIGHT]:
            player.rect.x += STEP
            player.current_animation = 'movement'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.x -= STEP

        if keys[pygame.K_UP]:
            player.rect.y -= STEP
            player.current_animation = 'movement'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.y += STEP

        if keys[pygame.K_DOWN]:
            player.rect.y += STEP
            player.current_animation = 'movement'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.y -= STEP


        if keys[pygame.K_k]:
            return 0

        if not any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]):
            player.current_animation = 'idle'

        for key, sprite in enumerate(all_sprites):
            camera.apply(player)

        tiles_group.draw(screen)
        wall_group.draw(screen)
        mouse_pos = pygame.mouse.get_pos()
        player.update(mouse_pos)
        for i in enemy_list:
            i.update(player.rect.x, player.rect.y)
        if not bool(enemy_list):
            finaly(HEALTH, KOL_BULLET, KOL_ENEMY, All_ENEMY)
        for i in bullet_list:
            X, Y = BulletTile.upp(i)
            x1 = i.rect.x
            y1 = i.rect.y
            for j in range(5):
                if x1 > X: i.rect.x -= 1
                if x1 < X: i.rect.x += 1
                if y1 > Y: i.rect.y -= 1
                if y1 < Y: i.rect.y += 1
                for g in range(-6, 6):
                    for t in range(-6, 6):
                        if y1 + t == Y and x1 + g == X: i.kill()
                if y1 > WIDTH or x1 > HEIGHT: i.kill()
                if y1 < 0 or x1 > HEIGHT: i.kill()
                if y1 > WIDTH or x1 < 0: i.kill()
                if y1 < 0 or x1 < 0: i.kill()
        for i in bullet_list:
            if pygame.sprite.spritecollideany(i, wall_group):
                i.kill()
        if pygame.sprite.spritecollideany(player, enemy_group):
            if GAME:
                HEALTH -= 20
                GAME = False
            print(HEALTH)
        else:
            GAME = True
        if HEALTH <= 0:
            finaly(HEALTH, KOL_BULLET, KOL_ENEMY, All_ENEMY)
        bullet_group.draw(screen)
        enemy_group.draw(screen)
        player_group.draw(screen)
        proverka(KOL_ENEMY)
        pygame.display.flip()

        clock.tick(FPS)

    # Выход из игры
    terminate()

a()


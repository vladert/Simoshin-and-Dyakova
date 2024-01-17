import os
import sqlite3
import sys
import pygame
from Enemy import Enemy
from bullet_title import BulletTile
from player import Player
from tile import Tile

# Функция финального окна
def finaly(HEALTH, KOL_BULLET, KOL_ENEMY, All_ENEMY, file, HEALTH_ENEMY=100, name=''):
    # Функция создания кнопки
    def get_component_button2(screen_width, screen_height, text, step=0, x=0):
        font = pygame.font.Font(None, 50) # Размер шрифта
        text_surface = font.render(text, True, (255, 255, 255))
        button_width = text_surface.get_width() + 40 # ширина кнопки
        button_height = text_surface.get_height() + 20 # длина кнопки
        button_x = (screen_width - button_width) // 2 + x # координата х
        button_y = (screen_height - button_height) // 2 + step # координата у
        # Прямоугольник, на кнопке
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        text_rect = text_surface.get_rect(center=button_rect.center)
        return (text_surface, text_rect, button_rect, text)

    # Функция добавления результов уровня (монеты) в базу данных
    def add_bd(result):
        # Подключение к бд
        con = sqlite3.connect('weapon.db')
        cur = con.cursor()

        # Извлечение и изменение данных
        cost = cur.execute('SELECT coins FROM person WHERE id == 1').fetchall()
        cur.execute(f'UPDATE person SET coins = {result + cost[0][0]}')

        # сохранение данных
        con.commit()
        con.close()

    if file == 'levelex.txt':
        name = 'Уровень 1'
    if file == 'levx2':
        name = 'Уровень 2'
    if file == 'levx3':
        name = 'Уровень 3'
    if file == 'levx4':
        name = 'Уровень 4'
    if file == 'levx5':
        name = 'Уровень 5'
    print(name, file)
    # Подсчет полученных монет за уровень по передаваемым данным
    res_hea = HEALTH
    res_enemy = 0
    if HEALTH_ENEMY == 500 and KOL_ENEMY == 1:
        res_enemy = 1000
    else:
        if KOL_ENEMY == All_ENEMY:
            res_enemy += 100
        res_enemy += KOL_ENEMY * 100
    if KOL_BULLET < 5:
        res_bullet = 200
    if 8 > KOL_ENEMY > 5:
        res_bullet = 100
    else:
        res_bullet = 50

    # Изменение данных в бд
    add_bd(res_hea+res_bullet+res_enemy)
    # Добавление переменных и осуществление "общего" вида игрового окна
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Результаты')
    running = True
    LOADING_BG = pygame.image.load("finaly_open.jpg")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 280))
    screen_width, screen_height = 800, 600
    color = (22, 26, 30)

    # Создание окна
    screen = pygame.display.set_mode((screen_width, screen_height))
    name = get_component_button2(screen_width, screen_height, name, -270)

    # Кнопки, отвечающие за данные
    res_cost2 = get_component_button2(screen_width, screen_height, f'{res_hea + res_bullet + res_enemy}', -150, 100)
    res_b2 = get_component_button2(screen_width, screen_height, str(KOL_BULLET), -50, 100)
    res_h2 = get_component_button2(screen_width, screen_height, str(HEALTH), 50, 100)
    res_en2 = get_component_button2(screen_width, screen_height, str(KOL_ENEMY), 150, 100)

    # Кнопки отвечающие за описание результатов
    res_cost = get_component_button2(screen_width, screen_height, 'Заработанные монеты', -150, - 200)
    res_b = get_component_button2(screen_width, screen_height, 'Потрачено пуль', -50, - 200)
    res_h = get_component_button2(screen_width, screen_height, 'Здоровье', 50, - 200)
    res_en = get_component_button2(screen_width, screen_height, 'Убитых зомби', 150, - 200)

    # Кнопки перемещения по игре
    exitt = get_component_button2(screen_width, screen_height, 'В главное меню', 250, - 230)
    lev = get_component_button2(screen_width, screen_height, 'Уровни', 250, 40)
    again = get_component_button2(screen_width, screen_height, 'Переиграть', 250, 270)

    # Основной цикл программы
    while running:
        for event in pygame.event.get():
            # При нажатии крестика, закрытия окна
            if event.type == pygame.QUIT:
                exit()
            # Обработка нажатия мыши, на какую кнопку
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        screen.fill((0, 0, 0))
                        kill_all_zombie()
                    if lev[2].collidepoint(mouse_pos):
                        screen.fill((0, 0, 0))
                        levels()
                    if again[2].collidepoint(mouse_pos):
                        a(file, All_ENEMY, HEALTH_ENEMY=100)
                        screen.fill((0, 0, 0))

        # Отрисовка кнопок
        screen.fill((0, 0, 0))
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        screen.blit(name[0], name[1])
        pygame.draw.rect(screen, color, exitt[2])
        pygame.draw.rect(screen, color, res_en[2])
        screen.blit(res_en[0], res_en[1])
        pygame.draw.rect(screen, color, res_cost[2])
        screen.blit(res_cost[0], res_cost[1])
        pygame.draw.rect(screen, color, res_b[2])
        screen.blit(res_b[0], res_b[1])
        pygame.draw.rect(screen, color, res_h[2])
        screen.blit(res_h[0], res_h[1])
        screen.blit(exitt[0], exitt[1])

        pygame.draw.rect(screen, (0, 0, 0), res_en2[2])
        screen.blit(res_en2[0], res_en2[1])
        pygame.draw.rect(screen, (0, 0, 0), res_cost2[2])
        screen.blit(res_cost2[0], res_cost2[1])
        pygame.draw.rect(screen, (0, 0, 0), res_b2[2])
        screen.blit(res_b2[0], res_b2[1])
        pygame.draw.rect(screen, (0, 0, 0), res_h2[2])
        screen.blit(res_h2[0], res_h2[1])

        pygame.draw.rect(screen, color, lev[2])
        screen.blit(lev[0], lev[1])
        pygame.draw.rect(screen, color, again[2])
        screen.blit(again[0], again[1])
        clock.tick(50)
        pygame.display.flip()

# Функция подсчета денег на данный момент
def cost():
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()

    # Извлечение данных и закрытие бд
    res = cur.execute('SELECT coins FROM person WHERE id == 1').fetchall()
    con.close()

    # Создание кнопки, отвечающей за количество денег
    font = pygame.font.Font(None, 50)
    text_surface = font.render(f'{res[0][0]} zom', True, (255, 255, 255))
    button_width = text_surface.get_width() + 40
    button_height = text_surface.get_height() + 20
    button_x = screen_width - button_width
    button_y = button_height - 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)
    return (text_surface, text_rect, button_rect, f'{res[0][0]} zom')

# Функция создания кнопки
def get_component_button(screen_width, screen_height, text, step=0, x=1, stepx=0):
    # Установка размера шрифта
    font = pygame.font.Font(None, 50)
    # Определение по тексту какой размер
    if text == 'Kill all Zombie' or text == 'Оружия':
        font = pygame.font.Font(None, 75)
    text_surface = font.render(text, True, (255, 255, 255))
    # Для кнопки назад определенные координаты
    if text == 'Назад':
        button_width = text_surface.get_width() + 40 + x
        button_height = text_surface.get_height() + 20
        button_x = 0
        button_y = (screen_height - button_height) // 2 + step
    else:
        button_width = text_surface.get_width() + 40 + x
        button_height = text_surface.get_height() + 20
        button_x = (screen_width - button_width) // 2 + stepx
        button_y = (screen_height - button_height) // 2 + step

    # Создание прямоугольника для кнопки
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)
    return (text_surface, text_rect, button_rect, text)


def weapon1():
    # Подключение определенной картинке кк определенному оружию
    LOADING_BG = pygame.image.load("weapon/G22.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))

    color = (22, 26, 30)
    clock = pygame.time.Clock()
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    # Извлечение данных
    res = cur.execute('SELECT gun, characteristics FROM weapons WHERE id == 1').fetchall()
    res2 = cur.execute('SELECT gun FROM person').fetchall()

    # Добавление переменных и осуществление "общего" вида игрового окна
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)
    text_surface = font.render(res[0][1], True, (255, 255, 255))
    button_width = text_surface.get_width() + 20
    button_height = text_surface.get_height() + 20
    button_x = 10
    button_y = 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Создание кнопок
    gun1 = get_component_button(screen_width, screen_height, 'G22', -270)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)

    # Отслеживание есть ли пистолет в инвинторе, от этого зависит надпись на кнопке
    if res2[0][0] == 1:
        yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
    else:
        yst = get_component_button(screen_width, screen_height, 'Взять', 200, 1, 300)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
                    if yst[2].collidepoint(mouse_pos):
                        if yst[3] == 'Взять':
                            yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
                            cur.execute('UPDATE person SET gun = 1')
                            con.commit()
                            con.close()

        # Отрисовка кнопок
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        clock.tick(50)
        pygame.display.flip()


def weapon2():
    LOADING_BG = pygame.image.load("weapon/UMP.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))
    color = (22, 26, 30)
    clock = pygame.time.Clock()
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    # Извлечение данных из бд
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 2').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()

    # разделение текста
    text1 = ' '.join(res[0][1].split()[:8])
    text2 = ' '.join(res[0][1].split()[8:16])
    text3 = ' '.join(res[0][1].split()[16:])

    # Добавление переменных и осуществление "общего" вида игрового окна
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

    # Создание кнопок
    text_surface = font.render(text1, True, (255, 255, 255))
    button_width = text_surface.get_width() + 20
    button_height = text_surface.get_height() + 20
    button_x = 10
    button_y = 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)

    text_surface1 = font.render(text2, True, (255, 255, 255))
    button_width1 = text_surface1.get_width() + 20
    button_height1 = text_surface1.get_height() + 20
    button_x1 = 10
    button_y1 = 90
    button_rect1 = pygame.Rect(button_x1, button_y1, button_width1, button_height1)
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)

    text_surface2 = font.render(text3, True, (255, 255, 255))
    button_width2 = text_surface2.get_width() + 20
    button_height2 = text_surface2.get_height() + 20
    button_x2 = 10
    button_y2 = 130
    button_rect2 = pygame.Rect(button_x2, button_y2, button_width2, button_height2)
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)

    gun1 = get_component_button(screen_width, screen_height, 'UMP', -270)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)

    # Проверка есть оружие или нет
    if res[0][2] == 1:
        if res2[0][0] == 2:
            yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
        else:
            yst = get_component_button(screen_width, screen_height, 'Взять', 200, 1, 300)
    else:
        yst = get_component_button(screen_width, screen_height, '1500 Zom', 200, 1, 300)
    # return (text_surface, text_rect, button_rect)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
                    if yst[2].collidepoint(mouse_pos):
                        if res[0][2] == 1:
                            if yst[3] == 'Взять':
                                yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
                                cur.execute('UPDATE person SET gun = 2')
                                con.commit()
                                con.close()
                        else:
                            if res2[0][1] >= 1500:
                                yst = get_component_button(screen_width, screen_height, 'Взять', 200, 50, 300)
                                summ = res2[0][1] - 1500
                                cur.execute(f'UPDATE person SET coins = {summ}')
                                cur.execute('UPDATE weapons SET open = 1 WHERE gun == "UMP"')
                                con.commit()

        # Отрисовка кнопок
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon3():
    LOADING_BG = pygame.image.load("weapon/P90.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))
    color = (22, 26, 30)
    clock = pygame.time.Clock()
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    # Извлечение данных из бд
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 3').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    # Разделение текста
    text1 = ' '.join(res[0][1].split()[:8])
    text2 = ' '.join(res[0][1].split()[8:16])
    text3 = ' '.join(res[0][1].split()[16:])
    # Добавление переменных и осуществление "общего" вида игрового окна
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)
    # Создание кнопок
    text_surface = font.render(text1, True, (255, 255, 255))
    button_width = text_surface.get_width() + 20
    button_height = text_surface.get_height() + 20
    button_x = 10
    button_y = 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)

    text_surface1 = font.render(text2, True, (255, 255, 255))
    button_width1 = text_surface1.get_width() + 20
    button_height1 = text_surface1.get_height() + 20
    button_x1 = 10
    button_y1 = 90
    button_rect1 = pygame.Rect(button_x1, button_y1, button_width1, button_height1)
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)

    text_surface2 = font.render(text3, True, (255, 255, 255))
    button_width2 = text_surface2.get_width() + 20
    button_height2 = text_surface2.get_height() + 20
    button_x2 = 10
    button_y2 = 130
    button_rect2 = pygame.Rect(button_x2, button_y2, button_width2, button_height2)
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)

    gun1 = get_component_button(screen_width, screen_height, 'P90', -270)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    # Проверка есть оружие или нет
    if res[0][2] == 1:
        if res2[0][0] == 2:
            yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
        else:
            yst = get_component_button(screen_width, screen_height, 'Взять', 200, 1, 300)
    else:
        yst = get_component_button(screen_width, screen_height, '3000 Zom', 200, 1, 300)
    # return (text_surface, text_rect, button_rect)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
                    if yst[2].collidepoint(mouse_pos):
                        if res[0][2] == 1:
                            if yst[3] == 'Взять':
                                yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
                                cur.execute('UPDATE person SET gun = 3')
                                con.commit()
                                con.close()
                        else:
                            if res2[0][1] >= 3000:
                                yst = get_component_button(screen_width, screen_height, 'Взять', 200, 50, 300)
                                summ = res2[0][1] - 3000
                                cur.execute(f'UPDATE person SET coins = {summ}')
                                cur.execute('UPDATE weapons SET open = 1 WHERE gun == "P90"')
                                con.commit()

        # Отрисовка кнопок
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon4():
    LOADING_BG = pygame.image.load("weapon/AKR.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))
    color = (22, 26, 30)
    clock = pygame.time.Clock()
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    # Извлечение данных из бд
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 4').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:10])
    text2 = ' '.join(res[0][1].split()[10:16])
    text3 = ' '.join(res[0][1].split()[16:])
    # Добавление переменных и осуществление "общего" вида игрового окна
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

    # Создание кнопок
    text_surface = font.render(text1, True, (255, 255, 255))
    button_width = text_surface.get_width() + 20
    button_height = text_surface.get_height() + 20
    button_x = 10
    button_y = 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)

    text_surface1 = font.render(text2, True, (255, 255, 255))
    button_width1 = text_surface1.get_width() + 20
    button_height1 = text_surface1.get_height() + 20
    button_x1 = 10
    button_y1 = 90
    button_rect1 = pygame.Rect(button_x1, button_y1, button_width1, button_height1)
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)

    text_surface2 = font.render(text3, True, (255, 255, 255))
    button_width2 = text_surface2.get_width() + 20
    button_height2 = text_surface2.get_height() + 20
    button_x2 = 10
    button_y2 = 130
    button_rect2 = pygame.Rect(button_x2, button_y2, button_width2, button_height2)
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)

    gun1 = get_component_button(screen_width, screen_height, 'AKR', -270)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    if res[0][2] == 1:
        if res2[0][0] == 2:
            yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
        else:
            yst = get_component_button(screen_width, screen_height, 'Взять', 200, 1, 300)
    else:
        yst = get_component_button(screen_width, screen_height, '4500 Zom', 200, 1, 300)
    # return (text_surface, text_rect, button_rect)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
                        # Проверка есть оружие или нет
                    if yst[2].collidepoint(mouse_pos):
                        if res[0][2] == 1:
                            if yst[3] == 'Взять':
                                yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
                                cur.execute('UPDATE person SET gun = 4')
                                con.commit()
                                con.close()
                        else:
                            if res2[0][1] >= 4500:
                                yst = get_component_button(screen_width, screen_height, 'Взять', 200, 50, 300)
                                summ = res2[0][1] - 4500
                                cur.execute(f'UPDATE person SET coins = {summ}')
                                cur.execute('UPDATE weapons SET open = 1 WHERE gun == "AKR"')
                                con.commit()

        # Отрисовка кнопок
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon5():
    LOADING_BG = pygame.image.load("weapon/M4.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))
    color = (22, 26, 30)
    clock = pygame.time.Clock()
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    # Извлечение данных из бд
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 5').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:10])
    text2 = ' '.join(res[0][1].split()[10:16])
    text3 = ' '.join(res[0][1].split()[16:])
    # Добавление переменных и осуществление "общего" вида игрового окна
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

    # Создание кнопок
    text_surface = font.render(text1, True, (255, 255, 255))
    button_width = text_surface.get_width() + 20
    button_height = text_surface.get_height() + 20
    button_x = 10
    button_y = 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)

    text_surface1 = font.render(text2, True, (255, 255, 255))
    button_width1 = text_surface1.get_width() + 20
    button_height1 = text_surface1.get_height() + 20
    button_x1 = 10
    button_y1 = 90
    button_rect1 = pygame.Rect(button_x1, button_y1, button_width1, button_height1)
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)

    text_surface2 = font.render(text3, True, (255, 255, 255))
    button_width2 = text_surface2.get_width() + 20
    button_height2 = text_surface2.get_height() + 20
    button_x2 = 10
    button_y2 = 130
    button_rect2 = pygame.Rect(button_x2, button_y2, button_width2, button_height2)
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)

    gun1 = get_component_button(screen_width, screen_height, 'M4', -270)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    if res[0][2] == 1:
        if res2[0][0] == 2:
            yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
        else:
            yst = get_component_button(screen_width, screen_height, 'Взять', 200, 1, 300)
    else:
        yst = get_component_button(screen_width, screen_height, '6000 Zom', 200, 1, 300)
    # return (text_surface, text_rect, button_rect)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
                    # Проверка есть ли оружие или нет
                    if yst[2].collidepoint(mouse_pos):
                        if res[0][2] == 1:
                            if yst[3] == 'Взять':
                                yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
                                cur.execute('UPDATE person SET gun = 5')
                                con.commit()
                                con.close()
                        else:
                            if res2[0][1] >= 6000:
                                yst = get_component_button(screen_width, screen_height, 'Взять', 200, 50, 300)
                                summ = res2[0][1] - 6000
                                cur.execute(f'UPDATE person SET coins = {summ}')
                                cur.execute('UPDATE weapons SET open = 1 WHERE gun == "M4"')
                                con.commit()

        # Отрисовка кнопок
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon6():
    LOADING_BG = pygame.image.load("weapon/M16.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))
    color = (22, 26, 30)
    clock = pygame.time.Clock()
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    # Извлечение данных из бд
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 6').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:10])
    text2 = ' '.join(res[0][1].split()[10:20])
    text3 = ' '.join(res[0][1].split()[20:])
    # Добавление переменных и осуществление "общего" вида игрового окна
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)
    # Создание кнопок
    text_surface = font.render(text1, True, (255, 255, 255))
    button_width = text_surface.get_width() + 20
    button_height = text_surface.get_height() + 20
    button_x = 10
    button_y = 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)

    text_surface1 = font.render(text2, True, (255, 255, 255))
    button_width1 = text_surface1.get_width() + 20
    button_height1 = text_surface1.get_height() + 20
    button_x1 = 10
    button_y1 = 90
    button_rect1 = pygame.Rect(button_x1, button_y1, button_width1, button_height1)
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)

    text_surface2 = font.render(text3, True, (255, 255, 255))
    button_width2 = text_surface2.get_width() + 20
    button_height2 = text_surface2.get_height() + 20
    button_x2 = 10
    button_y2 = 130
    button_rect2 = pygame.Rect(button_x2, button_y2, button_width2, button_height2)
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)

    gun1 = get_component_button(screen_width, screen_height, 'M16', -270)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    # Проверка есть ли оружие или нет
    if res[0][2] == 1:
        if res2[0][0] == 2:
            yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
        else:
            yst = get_component_button(screen_width, screen_height, 'Взять', 200, 1, 300)
    else:
        yst = get_component_button(screen_width, screen_height, '8500 Zom', 200, 1, 300)
    # return (text_surface, text_rect, button_rect)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
                    if yst[2].collidepoint(mouse_pos):
                        if res[0][2] == 1:
                            if yst[3] == 'Взять':
                                yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
                                cur.execute('UPDATE person SET gun = 6')
                                con.commit()
                                con.close()
                        else:
                            if res2[0][1] >= 8500:
                                yst = get_component_button(screen_width, screen_height, 'Взять', 200, 50, 300)
                                summ = res2[0][1] - 8500
                                cur.execute(f'UPDATE person SET coins = {summ}')
                                cur.execute('UPDATE weapons SET open = 1 WHERE gun == "M16"')
                                con.commit()

        # Отрисовка кнопок
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon7():
    LOADING_BG = pygame.image.load("weapon/AWM.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))
    color = (22, 26, 30)
    clock = pygame.time.Clock()
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    # Извлечение данных из бд
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 7').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:10])
    text2 = ' '.join(res[0][1].split()[10:18])
    text3 = ' '.join(res[0][1].split()[18:])
    # Добавление переменных и осуществление "общего" вида игрового окна
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

    # создание кнопок
    text_surface = font.render(text1, True, (255, 255, 255))
    button_width = text_surface.get_width() + 20
    button_height = text_surface.get_height() + 20
    button_x = 10
    button_y = 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)

    text_surface1 = font.render(text2, True, (255, 255, 255))
    button_width1 = text_surface1.get_width() + 20
    button_height1 = text_surface1.get_height() + 20
    button_x1 = 10
    button_y1 = 90
    button_rect1 = pygame.Rect(button_x1, button_y1, button_width1, button_height1)
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)

    text_surface2 = font.render(text3, True, (255, 255, 255))
    button_width2 = text_surface2.get_width() + 20
    button_height2 = text_surface2.get_height() + 20
    button_x2 = 10
    button_y2 = 130
    button_rect2 = pygame.Rect(button_x2, button_y2, button_width2, button_height2)
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)

    gun1 = get_component_button(screen_width, screen_height, 'AWM', -270)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    # Проверка есть ли оружие или нет
    if res[0][2] == 1:
        if res2[0][0] == 2:
            yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
        else:
            yst = get_component_button(screen_width, screen_height, 'Взять', 200, 1, 300)
    else:
        yst = get_component_button(screen_width, screen_height, '10000 Zom', 200, 1, 300)
    # return (text_surface, text_rect, button_rect)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
                    if yst[2].collidepoint(mouse_pos):
                        if res[0][2] == 1:
                            if yst[3] == 'Взять':
                                yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
                                cur.execute('UPDATE person SET gun = 7')
                                con.commit()
                                con.close()
                        else:
                            if res2[0][1] >= 10000:
                                yst = get_component_button(screen_width, screen_height, 'Взять', 200, 50, 300)
                                summ = res2[0][1] - 10000
                                cur.execute(f'UPDATE person SET coins = {summ}')
                                cur.execute('UPDATE weapons SET open = 1 WHERE gun == "AWM"')
                                con.commit()

        # Отрисовка кнопок
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def shop():
    running = True
    pygame.display.set_caption('Магазин')
    color = (22, 26, 30)
    clock = pygame.time.Clock()
    LOADING_BG = pygame.image.load("gun.jpg")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 340))
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Создание кнопок
    name = get_component_button(screen_width, screen_height, 'Оружия', -230, 100)
    gun1 = get_component_button(screen_width, screen_height, 'G22', -160, 100)
    gun2 = get_component_button(screen_width, screen_height, 'UMP', -90, 100)
    gun3 = get_component_button(screen_width, screen_height, 'P90', -20, 100)
    gun4 = get_component_button(screen_width, screen_height, 'AKR', 50, 100)
    gun5 = get_component_button(screen_width, screen_height, 'M4', 120, 100)
    gun6 = get_component_button(screen_width, screen_height, 'M16', 200, 100)
    gun7 = get_component_button(screen_width, screen_height, 'AWM', 270, 100)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if gun1[2].collidepoint(mouse_pos):
                        weapon1()
                    if gun2[2].collidepoint(mouse_pos):
                        weapon2()
                    if gun3[2].collidepoint(mouse_pos):
                        weapon3()
                    if gun4[2].collidepoint(mouse_pos):
                        weapon4()
                    if gun5[2].collidepoint(mouse_pos):
                        weapon5()
                    if gun6[2].collidepoint(mouse_pos):
                        weapon6()
                    if gun7[2].collidepoint(mouse_pos):
                        weapon7()
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
        # Отрисовка кнопок
        screen.fill((0, 0, 0))
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        screen.blit(name[0], name[1])
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, gun1[2])
        screen.blit(gun1[0], gun1[1])
        pygame.draw.rect(screen, color, gun2[2])
        screen.blit(gun2[0], gun2[1])
        pygame.draw.rect(screen, color, gun3[2])
        screen.blit(gun3[0], gun3[1])
        pygame.draw.rect(screen, color, gun4[2])
        screen.blit(gun4[0], gun4[1])
        pygame.draw.rect(screen, color, gun5[2])
        screen.blit(gun5[0], gun5[1])
        pygame.draw.rect(screen, color, gun6[2])
        screen.blit(gun6[0], gun6[1])
        pygame.draw.rect(screen, color, gun7[2])
        screen.blit(gun7[0], gun7[1])

        # обновление экрана
        clock.tick(50)
        pygame.display.flip()


def levels():
    running = True
    color = (22, 26, 30)
    clock = pygame.time.Clock()
    screen_width, screen_height = 800, 600
    pygame.display.set_caption('Уровни')
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Создание кнопок
    name = get_component_button(screen_width, screen_height, 'Уровни', -230, 100)
    lev1 = get_component_button(screen_width, screen_height, 'I', -100, 100)
    lev2 = get_component_button(screen_width, screen_height, 'II', -20, 100)
    lev3 = get_component_button(screen_width, screen_height, 'III', 60, 100)
    lev4 = get_component_button(screen_width, screen_height, 'IV', 140, 100)
    lev5 = get_component_button(screen_width, screen_height, 'V', 220, 100)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if lev1[2].collidepoint(mouse_pos):
                        a('levelex.txt', 1)
                    if lev2[2].collidepoint(mouse_pos):
                        a('levx2.txt', 2)
                    if lev3[2].collidepoint(mouse_pos):
                        a('levx3.txt', 3)
                    if lev4[2].collidepoint(mouse_pos):
                        a('levx4.txt', 3)
                    if lev5[2].collidepoint(mouse_pos):
                        a('levx5.txt', 10, 500)
                    if exitt[2].collidepoint(mouse_pos):
                        kill_all_zombie()

        # Отрисовка кнопок
        screen.fill((0, 0, 0))
        screen.blit(name[0], name[1])
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, lev1[2])
        screen.blit(lev1[0], lev1[1])
        pygame.draw.rect(screen, color, lev2[2])
        screen.blit(lev2[0], lev2[1])
        pygame.draw.rect(screen, color, lev3[2])
        screen.blit(lev3[0], lev3[1])
        pygame.draw.rect(screen, color, lev4[2])
        screen.blit(lev4[0], lev4[1])
        pygame.draw.rect(screen, color, lev5[2])
        screen.blit(lev5[0], lev5[1])

        # обновление экрана
        clock.tick(50)
        pygame.display.flip()


def a(file, All_ENEMY, HEALTH_ENEMY=100):
    # Инициализация окна
    pygame.init()
    pygame.key.set_repeat(200, 70)
    # Загрузка изабражений(анимация)
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
          'zombi\movement\enemy20.png']
    # Создание констант
    FPS = 60
    WIDTH = 800
    HEIGHT = 600
    STEP = 3
    HEALTH = 100
    SPRITE_ENEMY = ''
    GAME = True
    KOL_ENEMY = 0
    KOL_BULLET = 0
    # Подключение к бд
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    # Извлечение данных из бд
    res2 = cur.execute('SELECT gun FROM person WHERE id == 1').fetchall()
    res = cur.execute(f'SELECT health FROM weapons WHERE id == {res2[0][0]}').fetchall()
    HEALTH_BULLET = res[0][0]
    con.close()
    bullet_list = []
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    # Создание групп спрайтов
    all_sprites = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()

    # Функция "загрузки" изображения
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
    def generate_level(ALL_ENEMY, level):
        enemy_list = []
        new_player, x, y = None, None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y, tiles_group, all_sprites, tile_images, tile_width, tile_height)
                elif level[y][x] == '#':
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

    # Функция проверки столкновения врага
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
                    print(KOL_ENEMY)
                    # enemy_list.remove(i)
                    KOL_ENEMY += 1

            if Enemy.health(i) < 0:
                i.kill()
        return KOL_ENEMY

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
    player, enemy_list, level_x, level_y = generate_level(All_ENEMY, load_level(file))
    player_group.add(player)
    # Создание камеры
    pygame.display.set_caption('Уровни')
    count = 0
    running = True
    # Начало игрового цикла
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                X, Y = mouse_pos[0], mouse_pos[1]
                bullet = BulletTile('bullet', player.rect.x, player.rect.y, bullet_group, all_sprites, tile_images, X,
                                    Y)
                bullet_group.add(bullet)
                bullet_list.append(bullet)
                KOL_BULLET += 1

        # Контроль, игрок пошёл налево
        if keys[pygame.K_LEFT]:
            player.rect.x -= STEP
            player.current_animation = 'movement'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.x += STEP

        # Контроль, игрок пошёл направо
        if keys[pygame.K_RIGHT]:
            player.rect.x += STEP
            player.current_animation = 'movement'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.x -= STEP

        # Контроль, игрок пошёл вверх
        if keys[pygame.K_UP]:
            player.rect.y -= STEP
            player.current_animation = 'movement'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.y += STEP

        # Контроль, игрок пошёл вниз
        if keys[pygame.K_DOWN]:
            player.rect.y += STEP
            player.current_animation = 'movement'
            if pygame.sprite.spritecollideany(player, wall_group):
                player.rect.y -= STEP

        # Контроль, игрок стоит на месте
        if not any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]):
            player.current_animation = 'idle'

         #  ОТрисовка всех групп спрайтов и проверка пули
        tiles_group.draw(screen)
        wall_group.draw(screen)
        mouse_pos = pygame.mouse.get_pos()
        player.update(mouse_pos)
        for i in enemy_list:
            i.update(player.rect.x, player.rect.y)
        if not enemy_group:
            print(HEALTH, KOL_BULLET, KOL_ENEMY, All_ENEMY, file, HEALTH_ENEMY)
            finaly(HEALTH, KOL_BULLET, KOL_ENEMY, All_ENEMY, file, HEALTH_ENEMY)
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
            if SPRITE_ENEMY != pygame.sprite.spritecollideany(player, enemy_group):
                if GAME:
                    HEALTH -= 20
                    SPRITE_ENEMY = pygame.sprite.spritecollideany(player, enemy_group)
                    GAME = False
        else:
            SPRITE_ENEMY = ''
            GAME = True
        if HEALTH <= 0:
            finaly(HEALTH, KOL_BULLET, KOL_ENEMY, All_ENEMY, file, HEALTH_ENEMY)
        bullet_group.draw(screen)
        enemy_group.draw(screen)
        player_group.draw(screen)
        a = proverka(KOL_ENEMY)
        KOL_ENEMY = a
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


def settings(screen):
    running = True
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    color = (22, 26, 30)
    pygame.display.set_caption('Настройки')
    clock = pygame.time.Clock()

    # Задний фон
    LOADING_BG = pygame.image.load("settings.jpg")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 340))
    LOADING_BG = pygame.transform.scale(LOADING_BG, (screen_width, screen_height))
    screen.blit(LOADING_BG, (0, 0))
    pygame.display.flip()

    # Кнопочки
    game = get_component_button(screen_width, screen_height, 'Об игре', -200, 100)
    cheets = get_component_button(screen_width, screen_height, 'Читы', -100, 100)
    zvuk = get_component_button(screen_width, screen_height, 'Звук', 0, 100)
    graphik = get_component_button(screen_width, screen_height, 'Графика', 100, 100)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if game[2].collidepoint(mouse_pos):
                        Gaming()
                        screen.fill((0, 0, 0))
                    if cheets[2].collidepoint(mouse_pos):
                        Cheets()
                        screen.fill((0, 0, 0))
                    if zvuk[2].collidepoint(mouse_pos):
                        Zvuk()
                    if graphik[2].collidepoint(mouse_pos):
                        Graphik()
                        screen.fill((0, 0, 0))
                    if exitt[2].collidepoint(mouse_pos):
                        running = False

        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, game[2])
        screen.blit(game[0], game[1])
        pygame.draw.rect(screen, color, cheets[2])
        screen.blit(cheets[0], cheets[1])
        pygame.draw.rect(screen, color, zvuk[2])
        screen.blit(zvuk[0], zvuk[1])
        pygame.draw.rect(screen, color, graphik[2])
        screen.blit(graphik[0], graphik[1])

        clock.tick(50)
        pygame.display.flip()


def Gaming():
    running = True
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    color = (22, 26, 30)
    color2 = (192, 5, 248)
    pygame.display.set_caption('Наша игра')
    LOADING_BG = pygame.image.load("game_settings.jpg")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 340))
    LOADING_BG = pygame.transform.scale(LOADING_BG, (screen_width, screen_height))
    screen.blit(LOADING_BG, (0, 0))
    pygame.display.flip()

    game = get_component_button(screen_width, screen_height, 'Об игре', -200, 100)
    font = pygame.font.SysFont('comicsansms', 32)
    opis = font.render("Игра просто пушка!!!", 1, color2, color)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)

    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exitt[2].collidepoint(mouse_pos):
                        settings(screen)
                        screen.fill((0, 0, 0))

        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        screen.blit(opis, (200, 200))
        pygame.draw.rect(screen, color, game[2])
        screen.blit(game[0], game[1])

        pygame.display.update()
        pygame.display.flip()


def Cheets():
    cheets_image = pygame.image.load('cheets.png')
    cheets_rect = cheets_image.get_rect()
    width, height = screen.get_size()
    color = (22, 26, 30)
    pygame.display.set_caption('Какие тебе читы?')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] < 140 and mouse_pos[1] > height - 60:
                        settings(screen)
        screen.fill((0, 0, 0))
        screen.blit(cheets_image, (0, 0))
        pygame.draw.rect(screen, color, (10, height - 50, 130, 45))
        font = pygame.font.Font(None, 36)
        back_text = font.render("Назад", True, (255, 255, 255))
        screen.blit(back_text, (20, height - 40))

        no_cheats_text = font.render("В нашей игре нету читов!!!", True, (255, 0, 0))  # Красный цвет текста
        screen.blit(no_cheats_text, (10, 500))  # Размещаем текст под изображением

        pygame.display.flip()
    pygame.quit()


def Zvuk():
    color = (22, 26, 30)
    BLACK = (255, 255, 255)
    WHITE = (0, 0, 0)
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    pygame.display.set_caption('Управление громкостью')

    # Параметры ползунка для эффектов
    slider_x1 = 50
    slider_y1 = height // 6
    slider_width1 = 500
    slider_height1 = 20
    slider_rect1 = pygame.Rect(slider_x1, slider_y1, slider_width1, slider_height1)
    slider_color1 = (0, 128, 255)
    slider_pressed1 = False
    font = pygame.font.Font(None, 36)
    text1 = font.render('Громкость эффектов', True, BLACK)
    text_rect1 = text1.get_rect(center=(width // 4, 50))

    zv1_min = 0
    zv1_max = 100
    volume_text1 = font.render("Громкость: 0", True, BLACK)
    volume_rect1 = volume_text1.get_rect(center=(width // 2, height // 4))

    # Параметры ползунка для музыки
    slider_x2 = 50
    slider_y2 = (height // 6) * 3.5
    slider_width2 = 500
    slider_height2 = 20
    slider_rect2 = pygame.Rect(slider_x2, slider_y2, slider_width2, slider_height2)
    slider_color2 = (255, 0, 0)  # Красный цвет для отличия от первого ползунка
    slider_pressed2 = False
    text2 = font.render('Громкость музыки', True, BLACK)
    text_rect2 = text2.get_rect(center=(width // 4, (height // 6) * 2 + 100))  # Немного выше второго ползунка

    zv2_min = 0
    zv2_max = 100
    volume_text2 = font.render("Громкость: 0", True, BLACK)
    volume_rect2 = volume_text2.get_rect(center=(width // 2, (height // 6) * 2 + 200))  # Чуть ниже второго ползунка

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exitt[2].collidepoint(mouse_pos):
                        settings(screen)
                        screen.fill((0, 0, 0))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if slider_rect1.collidepoint(mouse_pos):
                        slider_pressed1 = True
                    elif slider_rect2.collidepoint(mouse_pos):
                        slider_pressed2 = True
            elif event.type == pygame.MOUSEBUTTONUP:
                slider_pressed1 = False
                slider_pressed2 = False
            elif event.type == pygame.MOUSEMOTION:
                if slider_pressed1:
                    new_x1 = min(max(event.pos[0], slider_x1), slider_x1 + slider_width1)
                    zv1 = (new_x1 - slider_x1) / slider_width1 * (zv1_max - zv1_min) + zv1_min
                    volume_text1 = font.render(f"Громкость: {int(zv1)}", True, BLACK)
                if slider_pressed2:
                    new_x2 = min(max(event.pos[0], slider_x2), slider_x2 + slider_width2)
                    zv2 = (new_x2 - slider_x2) / slider_width2 * (zv2_max - zv2_min) + zv2_min
                    volume_text2 = font.render(f"Громкость: {int(zv2)}", True, BLACK)

        screen.fill(WHITE)
        pygame.draw.rect(screen, slider_color1, slider_rect1)
        screen.blit(text1, text_rect1)
        screen.blit(volume_text1, volume_rect1)

        pygame.draw.rect(screen, slider_color2, slider_rect2)
        screen.blit(text2, text_rect2)
        screen.blit(volume_text2, volume_rect2)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])

        pygame.display.flip()

    pygame.quit()


def Graphik():
    running = True
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    color = (255, 255, 255)
    color1 = (22, 26, 30)
    color2 = (192, 5, 248)
    x, y = 200, 200
    rect_x, rect_y, rect_width, rect_height = 0, 200, 800, 20  # Параметры прямоугольника
    x_old, x_new = 0, 0
    moving = False  # Добавляем инициализацию переменной moving
    clock = pygame.time.Clock()
    min_fps, max_fps = 30, 120
    min_rect_x, max_rect_x = 50, 750
    font = pygame.font.SysFont('comicsansms', 32)
    game = font.render("Количество FPS", 1, color2, color)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
                    moving = True
                elif exitt[2].collidepoint(event.pos):
                    settings(screen)

            if event.type == pygame.MOUSEMOTION:
                if moving:
                    x_new, y_new = event.rel
                    x, y = x + x_new, y + y_new
                    if x < min_rect_x:
                        x = min_rect_x
                    elif x > max_rect_x:
                        x = max_rect_x
                    current_fps = int((x - min_rect_x) / (max_rect_x - min_rect_x) * (max_fps - min_fps) + min_fps)
                    pygame.display.set_caption(f"Current FPS: {current_fps}")
                    clock.tick(current_fps)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                moving = False

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height))
        pygame.draw.circle(screen, (0, 0, 255), (x, 200), 50)
        pygame.draw.rect(screen, color1, exitt[2])
        screen.blit(exitt[0], exitt[1])
        screen.blit(game, (300, 50))
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()


screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))


def kill_all_zombie():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Kill All Zombie')
    running = True
    clock = pygame.time.Clock()
    # Создание кнопок
    name = get_component_button(screen_width, screen_height, 'Kill all Zombie', -150)
    button = get_component_button(screen_width, screen_height, 'Играть', -20)
    button2 = get_component_button(screen_width, screen_height, 'Настройки', 120)
    button3 = get_component_button(screen_width, screen_height, 'Магазин', 50)
    button1 = get_component_button(screen_width, screen_height, 'Выход', 200)
    color = (22, 26, 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button[2].collidepoint(mouse_pos):
                        levels()
                        screen.fill((0, 0, 0))
                    if button1[2].collidepoint(mouse_pos):
                        running = False
                    if button2[2].collidepoint(mouse_pos):
                        settings(screen)
                        screen.fill((0, 0, 0))
                    if button3[2].collidepoint(mouse_pos):
                        shop()
                        screen.fill((0, 0, 0))
        # Отрисовка кнопок
        screen.blit(name[0], name[1])

        pygame.draw.rect(screen, color, button[2])
        screen.blit(button[0], button[1])

        pygame.draw.rect(screen, color, button1[2])
        screen.blit(button1[0], button1[1])

        pygame.draw.rect(screen, color, button2[2])
        screen.blit(button2[0], button2[1])

        pygame.draw.rect(screen, color, button3[2])
        screen.blit(button3[0], button3[1])

        pygame.display.flip()
        clock.tick(50)
    pygame.quit()


if __name__ == '__main__':
    kill_all_zombie()

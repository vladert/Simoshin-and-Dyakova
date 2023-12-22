import sqlite3
from main1 import loading
import pygame
from level import a

def get_component_button(screen_width, screen_height, text, step=0, x=1, stepx=0):
    font = pygame.font.Font(None, 50)
    if text == 'Kill all Zombie' or text == 'Оружия':
        font = pygame.font.Font(None, 75)
    text_surface = font.render(text, True, (255, 255, 255))
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

    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    text_rect = text_surface.get_rect(center=button_rect.center)

    return (text_surface, text_rect, button_rect, text)


def money():
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT coins FROM person').fetchall()
    font = pygame.font.Font(None, 50)
    text_surface = font.render(f'{str(res[0][0])} Zom', True, (255, 255, 255))
    button_width = text_surface.get_width() + 40
    button_height = text_surface.get_height() + 20
    button_x = screen_width - button_width
    button_y = 0
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)
    return (text_surface, text_rect, button_rect, f'{str(res[0][0])} Zom')

def weapon1():
    LOADING_BG = pygame.image.load("weapon/G22.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))

    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics FROM weapons WHERE id == 1').fetchall()
    res2 = cur.execute('SELECT gun FROM person').fetchall()
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
    gun1 = get_component_button(screen_width, screen_height, 'G22', -270)
    exitt = get_component_button(screen_width, screen_height, 'Назад', 270)
    if res2[0][0] == 1:
        yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
    else:
        yst = get_component_button(screen_width, screen_height, 'Взять', 200, 1, 300)
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
                        if yst[3] == 'Взять':
                            yst = get_component_button(screen_width, screen_height, 'Выбран', 200, 1, 300)
                            cur.execute('UPDATE person SET gun = 1')
                            con.commit()
                            con.close()

        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        a = money()
        pygame.draw.rect(screen, (0, 0, 0), a[2])
        screen.blit(a[0], a[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()



def weapon2():
    LOADING_BG = pygame.image.load("weapon/UMP.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))

    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 2').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:8])
    text2 = ' '.join(res[0][1].split()[8:16])
    text3 = ' '.join(res[0][1].split()[16:])
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

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


        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        a = money()
        pygame.draw.rect(screen, (0, 0, 0), a[2])
        screen.blit(a[0], a[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon3():
    LOADING_BG = pygame.image.load("weapon/P90.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))

    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 3').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:8])
    text2 = ' '.join(res[0][1].split()[8:16])
    text3 = ' '.join(res[0][1].split()[16:])
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

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

        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        a = money()
        pygame.draw.rect(screen, (0, 0, 0), a[2])
        screen.blit(a[0], a[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon4():
    LOADING_BG = pygame.image.load("weapon/AKR.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))

    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 4').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:10])
    text2 = ' '.join(res[0][1].split()[10:16])
    text3 = ' '.join(res[0][1].split()[16:])
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

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

        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        a = money()
        pygame.draw.rect(screen, (0, 0, 0), a[2])
        screen.blit(a[0], a[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon5():
    LOADING_BG = pygame.image.load("weapon/M4.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))

    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 5').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:10])
    text2 = ' '.join(res[0][1].split()[10:16])
    text3 = ' '.join(res[0][1].split()[16:])
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

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

        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        a = money()
        pygame.draw.rect(screen, (0, 0, 0), a[2])
        screen.blit(a[0], a[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon6():
    LOADING_BG = pygame.image.load("weapon/M16.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))

    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 6').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:10])
    text2 = ' '.join(res[0][1].split()[10:20])
    text3 = ' '.join(res[0][1].split()[20:])
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

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

        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        a = money()
        pygame.draw.rect(screen, (0, 0, 0), a[2])
        screen.blit(a[0], a[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def weapon7():
    LOADING_BG = pygame.image.load("weapon/AWM.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(300, 360))

    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 7').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    text1 = ' '.join(res[0][1].split()[:10])
    text2 = ' '.join(res[0][1].split()[10:18])
    text3 = ' '.join(res[0][1].split()[18:])
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 30)

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

        pygame.draw.rect(screen, (0, 0, 0), button_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect1)
        screen.blit(text_surface1, text_rect1)
        pygame.draw.rect(screen, (0, 0, 0), button_rect2)
        screen.blit(text_surface2, text_rect2)
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
        a = money()
        pygame.draw.rect(screen, (0, 0, 0), a[2])
        screen.blit(a[0], a[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()
    con.close()


def shop():
    running = True
    LOADING_BG = pygame.image.load("gun.jpg")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 340))
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
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
        screen.fill((0, 0, 0))
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        a = money()
        pygame.draw.rect(screen, (0, 0, 0), a[2])
        screen.blit(a[0], a[1])
        screen.blit(name[0], name[1])
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


def settings(screen):
    running = True
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    color = (22, 26, 30)

    # Задний фон
    LOADING_BG = pygame.image.load("settings.jpg")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 340))
    LOADING_BG = pygame.transform.scale(LOADING_BG, (screen_width, screen_height))
    screen.blit(LOADING_BG, (0, 0))
    pygame.display.flip()

    # Кнопочки
    game = get_component_button(screen_width, screen_height, 'Об игре', -200, 100)
    account = get_component_button(screen_width, screen_height, 'Аккаунт', -100, 100)
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
                        Game()
                        screen.fill((0, 0, 0))
                    if account[2].collidepoint(mouse_pos):
                        Account()
                        screen.fill((0, 0, 0))
                    if zvuk[2].collidepoint(mouse_pos):
                        Zvuk()
                        screen.fill((0, 0, 0))
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
        pygame.draw.rect(screen, color, account[2])
        screen.blit(account[0], account[1])
        pygame.draw.rect(screen, color, zvuk[2])
        screen.blit(zvuk[0], zvuk[1])
        pygame.draw.rect(screen, color, graphik[2])
        screen.blit(graphik[0], graphik[1])

        clock.tick(50)
        pygame.display.flip()


def Game():
    running = True
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    color = (22, 26, 30)
    color2 = (192, 5, 248)
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
                        screen.fill(0, 0, 0)

        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        screen.blit(opis, (200, 200))
        pygame.draw.rect(screen, color, game[2])
        screen.blit(game[0], game[1])

        pygame.display.update()
        pygame.display.flip()

def Account():
    ...


def Zvuk():
    ...

def Game():
    running = True
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    color = (22, 26, 30)
    color2 = (192, 5, 248)
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
                        screen.fill(0, 0, 0)

        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        screen.blit(opis, (200, 200))
        pygame.draw.rect(screen, color, game[2])
        screen.blit(game[0], game[1])

        pygame.display.update()
        pygame.display.flip()


pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
clock = pygame.time.Clock()
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
                    ...
                if button1[2].collidepoint(mouse_pos):
                    running = False
                if button2[2].collidepoint(mouse_pos):
                    settings(screen)
                    screen.fill((0, 0, 0))
                if button3[2].collidepoint(mouse_pos):
                    shop()
                    screen.fill((0, 0, 0))

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
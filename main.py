import sqlite3
import sys
import pygame
from level import a


def cost():
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT coins FROM person WHERE id == 1').fetchall()
    font = pygame.font.Font(None, 50)
    text_surface = font.render(f'{res[0][0]} zom', True, (255, 255, 255))
    button_width = text_surface.get_width() + 40
    button_height = text_surface.get_height() + 20
    button_x = screen_width - button_width
    button_y = button_height - 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect = text_surface.get_rect(center=button_rect.center)
    return (text_surface, text_rect, button_rect, f'{res[0][0]} zom')

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
        a = cost()
        pygame.draw.rect(screen, color, a[2])
        screen.blit(a[0], a[1])
        pygame.draw.rect(screen, color, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color, yst[2])
        screen.blit(yst[0], yst[1])
        pygame.draw.rect(screen, (0, 0, 0), gun1[2])
        screen.blit(gun1[0], gun1[1])
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

    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics, open FROM weapons WHERE id == 5').fetchall()
    res2 = cur.execute('SELECT gun, coins FROM person').fetchall()
    print(res2)
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
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
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
                        a()
                    if lev2[2].collidepoint(mouse_pos):
                        ...
                    if lev3[2].collidepoint(mouse_pos):
                        ...
                    if lev4[2].collidepoint(mouse_pos):
                        ...
                    if lev5[2].collidepoint(mouse_pos):
                        ...
                    if exitt[2].collidepoint(mouse_pos):
                        running = False
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

def settings(screen):
    running = True
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    color = (22, 26, 30)
    pygame.display.set_caption('Настройки')

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
    text_rect2 = text2.get_rect(center=(width // 4, (height // 6) * 2  + 100))  # Немного выше второго ползунка

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
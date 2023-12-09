import sqlite3

import pygame


def get_component_button(screen_width, screen_height, text, step=0, x=1):
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
        button_x = (screen_width - button_width) // 2
        button_y = (screen_height - button_height) // 2 + step

    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    text_rect = text_surface.get_rect(center=button_rect.center)

    return (text_surface, text_rect, button_rect)




def weapon1():
    con = sqlite3.connect('weapon.db')
    cur = con.cursor()
    res = cur.execute('SELECT gun, characteristics FROM weapons WHERE id == 2').fetchall()
    running = True
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    name = get_component_button(screen_width, screen_height, res[0][1] , -230, 100)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                exit()
        pygame.draw.rect(screen, color, name[2])
        screen.blit(name[0], name[1])
        # обновление экрана
        clock.tick(50)
        pygame.display.flip()



def weapon2():
    ...


def weapon3():
    ...


def weapon4():
    ...


def weapon5():
    ...


def weapon6():
    ...


def weapon7():
    ...


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

        screen.blit(LOADING_BG, LOADING_BG_RECT)
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
                    ...
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

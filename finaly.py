import pygame

from level import a
from main import levels


def finaly(HEALTH, KOL_BULLET, KOL_ENEMY, All_ENEMY, file, HEALTH_ENEMY=100):
    def get_component_button(screen_width, screen_height, text, step=0, x=1, stepx=0):
        font = pygame.font.Font(None, 50)
        text_surface = font.render(text, True, (255, 255, 255))
        if text == 'В главное меню':
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

    pygame.init()
    clock = pygame.time.Clock()
    running = True
    LOADING_BG = pygame.image.load("finaly_open.jpg")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 300))
    screen_width, screen_height = 800, 600
    color1 = (22, 26, 30)
    color2 = (192, 5, 248)
    screen = pygame.display.set_mode((screen_width, screen_height))
    exitt = get_component_button(screen_width, screen_height, 'В главное меню', 270)
    lev = get_component_button(screen_width, screen_height, 'Уровни', 270)
    again = get_component_button(screen_width, screen_height, 'Переиграть', 180)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exitt[2].collidepoint(mouse_pos):
                        return 0
                    if lev[2].collidepoint(mouse_pos):
                        levels()
                        screen.fill((0, 0, 0))
                    if again[2].collidepoint(mouse_pos):
                        a(file, All_ENEMY, HEALTH_ENEMY=100)
                        screen.fill((0, 0, 0))

        screen.fill((0, 0, 0))
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        pygame.draw.rect(screen, color1, exitt[2])
        screen.blit(exitt[0], exitt[1])
        pygame.draw.rect(screen, color1, lev[2])
        screen.blit(lev[0], lev[1])
        pygame.draw.rect(screen, color1, again[2])
        screen.blit(again[0], again[1])
        clock.tick(50)
        pygame.display.flip()
finaly(1, 1, 1, 1)
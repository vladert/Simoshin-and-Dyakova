import random
import sys
import pygame
import threading
import math
def loading():
    W, H = 1280, 720
    FPS = 60
    LOADING_BG = pygame.image.load("Loading Bar Background.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))
    finished = False
    progress = 0
    w = 8
    LONG = random.randint(1000000, 100000000)

    def progress_bar():
        global finished, progress, math_eq
        math_eq = 523687 / 789456 * 89456
        for i in range(LONG):
            progress = i
        pygame.mixer.music.stop()
        finished = True

    pygame.init()
    pygame.mixer.music.load("music1.mp3")
    pygame.mixer.music.play(-1)
    fon1 = pygame.image.load("zombi1.jpg")  # Загрузка изображения фона
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Loading Bar')
    FONT = pygame.font.SysFont("Roboto", 100)
    clock = pygame.time.Clock()
    loading_bar = pygame.image.load("Loading Bar.png")
    loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
    download_text = FONT.render("Подождите", True, "white")
    download_rect = download_text.get_rect(center=(640, 570))
    finished_text = FONT.render("Успешно!", True, "white")
    finished_rect = finished_text.get_rect(center=(640, 360))
    threading.Thread(target=progress_bar).start()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fon1, (0, 0))  # Использование функции blit для отображения фона
        if not finished:
            w = progress / LONG * 720
            loading_bar = pygame.transform.scale(loading_bar, (int(w), 150))
            loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
            screen.blit(LOADING_BG, LOADING_BG_RECT)
            screen.blit(loading_bar, loading_bar_rect)
            screen.blit(download_text, download_rect)
        else:
            screen.blit(finished_text, finished_rect)
            running = False

        pygame.display.update()
        clock.tick(FPS)
    return True
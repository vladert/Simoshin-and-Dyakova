

import pygame

def finaly(HEALTH, KOL_BULLET, KOL_ENEMY, All_ENEMY):
    clock = pygame.time.Clock()
    running = True
    LOADING_BG = pygame.image.load("zombi1.jpg")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=(500, 340))
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill((0, 0, 0))
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        clock.tick(50)
        pygame.display.flip()
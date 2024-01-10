import math

import pygame.sprite


# Класс игрока
class Enemy(pygame.sprite.Sprite):
    def __init__(self, images, params):
        super().__init__()
        self.cur_frame = 0
        self.images = images
        print(self.images)

        self.current_animation = 'idle'
        self.image = self.images[self.current_animation][0]
        self.rect = self.image.get_rect().move(params['tile_width'] * params['pos_x'] + 15,
                                               params['tile_height'] * params['pos_y'] + 5)

    def rotate_enemy_towards_mouse(self, x, y):
        dx = x - self.rect.centerx
        dy = y - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx))
        rotated_player = pygame.transform.rotate(self.image, angle)
        new_rect = rotated_player.get_rect(center=self.rect.center)
        return rotated_player, new_rect

    def update(self, x, y):
        self.cur_frame = (self.cur_frame + 1) % len(self.images[self.current_animation])
        self.image = self.images[self.current_animation][self.cur_frame]

        self.image, self.rect = self.rotate_enemy_towards_mouse(x, y)


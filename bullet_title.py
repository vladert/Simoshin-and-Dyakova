import pygame


class BulletTile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, bullet_group, all_sprites, tile_images, X, Y):
        super().__init__(bullet_group, all_sprites)
        self.X = X
        self.Y = Y
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(pos_x, pos_y)
    def upp(self):
        return self.X, self.Y
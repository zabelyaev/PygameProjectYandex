import math

from pygame import transform
from pygame.sprite import Sprite

from constansts import TILE_WIDTH, TILE_HEIGHT, TILE_IMAGES, PLAYER_IMAGE
from player import Player


class Tile(Sprite):
    def __init__(self, tile_image, pos, no_rect=False, *groups):
        super().__init__(*groups)

        self.no_rect = no_rect

        self.image = tile_image
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(TILE_WIDTH * pos[0], TILE_HEIGHT * pos[1])


class Coin(Tile):
    def __init__(self, tile_image, pos, *groups):
        super().__init__(tile_image, pos, *groups)
        self.scale_factor = 1.2
        self.is_scale = True
        self.original_image = self.image
        self.original_center = self.rect.center
        self.original_rect = self.rect
        self.scale_time = 0

    def update(self):
        self.scale_time += 1

        if self.scale_time == 20:
            self.scale_time = 1
            self.is_scale = not self.is_scale

        if self.is_scale:
            scaled_image = transform.scale(self.image,
                                           (self.rect.w * self.scale_factor, self.rect.h * self.scale_factor))

            self.image = scaled_image
        else:
            self.image = self.original_image






class Score:
    def __init__(self):
        self.score = 0

    def increase_score(self, level_increase):
        self.score += level_increase
        print(self.score)


def generate_level(level, all_sprites, tiles_group, walls_group, player_group, coins_group):
    new_player, x, y = None, None, None

    for y in range(len(level)):
        for x in range(len(level[y])):
            level_point = level[y][x]
            if level_point == '.':
                Tile(TILE_IMAGES['empty'], (x, y), all_sprites, tiles_group)
            elif level_point == '#':
                Tile(TILE_IMAGES['wall'], (x, y), False, all_sprites, tiles_group, walls_group)
            elif level_point == '@':
                Tile(TILE_IMAGES['empty'], (x, y), False, all_sprites, tiles_group)
                new_player = Player(PLAYER_IMAGE, (x, y), all_sprites, player_group)
            elif level_point == '0':
                Tile(TILE_IMAGES['empty'], (x, y), False, all_sprites, tiles_group)
                Coin(TILE_IMAGES['coin'], (x, y), all_sprites, tiles_group, coins_group)
            elif level_point == '*':
                Tile(TILE_IMAGES['wall'], (x, y), True, all_sprites, tiles_group, walls_group)

    return new_player, x, y


def load_next_level(level):
    pass

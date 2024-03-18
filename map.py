import os
import sys

import pygame.mixer
from pygame import transform
from pygame.sprite import Sprite

from constansts import TILE_WIDTH, TILE_HEIGHT, TILE_IMAGES, PLAYER_IMAGE, SOUNDS
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
        self.scale_time = 0

        self.score = 1
        self.drop_sound = SOUNDS['coin']

    def get_score(self) -> int:
        return self.score

    def get_sound(self) -> pygame.mixer.Sound:
        return self.drop_sound

    def update(self) -> None:
        # анимация
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


class Artefact(Coin):
    def __init__(self, tile_image, pos, *groups):
        super().__init__(tile_image, pos, *groups)

        self.score = 10
        self.drop_sound = SOUNDS['artefact']


class Score:
    def __init__(self):
        self.score = 0

    def increase_score(self, level_increase: int) -> None:
        self.score += level_increase

    def get_score(self) -> int:
        return self.score

    def reset(self) -> None:
        self.score = 0


def load_level(filename: str) -> list:
    fullname = check_map_exist(filename)

    with open(fullname, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def check_map_exist(filename: str) -> str:
    fullname = os.path.join('data', 'maps', filename + '.txt')

    if not os.path.isfile(fullname):
        print(f'Файлы с картой {fullname} не найден!')
        sys.exit()

    return fullname


def generate_level(level: list, all_sprites, tiles_group, walls_group, player_group, coins_group) -> Player:
    new_player = None

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
            elif level_point == '!':
                Tile(TILE_IMAGES['empty'], (x, y), False, all_sprites, tiles_group)
                Artefact(TILE_IMAGES['artefact'], (x, y), all_sprites, tiles_group, coins_group)

    return new_player

import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'sprites', name)

    if not os.path.isfile(fullname):
        print(f'Файлы с изображанием {fullname} не найден!')
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()

    return image


def load_sounds(filename):
    fullname = os.path.join('data', 'sounds', filename)

    if not os.path.isfile(fullname):
        print(f'Файлы со звуком {fullname} не найден!')
        sys.exit()

    return pygame.mixer.Sound(fullname)


def load_level(filename):
    fullname = check_map_exist(filename)

    with open(fullname, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def check_map_exist(filename):
    fullname = os.path.join('data', 'maps', filename + '.txt')

    if not os.path.isfile(fullname):
        print(f'Файлы с картой {fullname} не найден!')
        sys.exit()

    return fullname

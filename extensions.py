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

import pygame

from extensions import load_sounds, load_image

pygame.init()

FPS = 50
WIDTH = 700
HEIGHT = 600

TILE_WIDTH = 50
TILE_HEIGHT = 50

SOUNDS = {
    'background': 'data/sounds/background_sound.mp3',
    'coin': load_sounds('drop_coin.wav'),
    'artefact': load_sounds('drop_artefact.mp3'),
    'end': load_sounds('end_game.mp3')
}

TILE_IMAGES = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png'),
    'coin': load_image('coin.png'),
    'artefact': load_image('artefact.png'),
}

PLAYER_IMAGE = load_image('player.png')

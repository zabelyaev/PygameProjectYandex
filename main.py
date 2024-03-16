import sys

import pygame.mixer

from extensions import load_level
from map import generate_level, Score
from screens import *

from constansts import *


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    # начальные настройки
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # запускаем фоновую музыку
    pygame.mixer.music.load('data/sounds/Background Sound.mp3')
    pygame.mixer.music.play(loops=-1)

    # группы спрайтов
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    walls_group = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    player = None
    score = Score()  # счетчик монет

    pygame.display.flip()

    # основной игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and not player:
                player, level_x, level_y = generate_level(load_level('map'), all_sprites, tiles_group,
                                                          walls_group,
                                                          player_group, coins_group)
            elif event.type == pygame.KEYDOWN:
                player.move(event, walls=walls_group)

        if not player:
            start_screen(screen)
        else:
            if len(coins_group) == 0:
                for sprite in all_sprites:
                    sprite.kill()
                pygame.display.flip()

                player, level_x, level_y = generate_level(load_level('map2'), all_sprites, tiles_group,
                                                          walls_group,
                                                          player_group, coins_group)
            screen.fill((0, 0, 0))

        # отрисывываем все спрайты
        tiles_group.draw(screen)
        player_group.draw(screen)
        coins_group.update()

        # при столкновении с монеткой увеличиваем счет
        player_group.update(coins_group, score)

        # для отрисовки
        pygame.display.flip()
        clock.tick(FPS)

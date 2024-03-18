import sys

import pygame.mixer

from map import generate_level, Score, load_level
from screens import *

from constansts import *


def terminate():
    pygame.quit()
    sys.exit()


def clear_groups(*groups):
    for group in groups:
        for sprite in group:
            sprite.kill()


if __name__ == '__main__':
    # начальные настройки
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    pygame.display.set_caption('Археолог')

    # запускаем фоновую музыку
    pygame.mixer.music.load(SOUNDS['background'])
    pygame.mixer.music.play(loops=-1)

    # группы спрайтов
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    walls_group = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    player = None
    score = Score()  # счетчик монет

    db = DBManager()
    end_game = False

    pygame.display.flip()

    # основной игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and not player and not end_game:
                if db.fetch_current_level()[1]:
                    db.start_new_game()
                end_game = False
                player = generate_level(load_level(db.fetch_current_level()[0]), all_sprites,
                                        tiles_group,
                                        walls_group,
                                        player_group, coins_group)
            elif event.type == pygame.KEYDOWN:
                if player:
                    player.move(event, walls=walls_group)

        if end_game:
            end_screen(screen)
        elif not end_game and not player:
            start_screen(screen)
        else:
            if len(coins_group) == 0:
                player = None
                clear_groups(all_sprites, tiles_group, walls_group, coins_group, player_group)
                pygame.display.flip()

                db.increase_score(score.get_score())
                score.reset()

                if db.increase_level():
                    player = generate_level(load_level(db.fetch_current_level()[0]), all_sprites,
                                            tiles_group,
                                            walls_group,
                                            player_group, coins_group)
                else:
                    end_game = True
                    db.end_game(end_game)
                    pygame.mixer.music.stop()
                    SOUNDS['end'].play()

        # отрисывываем все спрайты
        tiles_group.draw(screen)  # отрисывываем тайлы
        player_group.draw(screen)  # затем игрока
        coins_group.update()

        # при столкновении с монеткой увеличиваем счет
        player_group.update(coins_group, score)

        # для отрисовки
        pygame.display.flip()
        clock.tick(FPS)

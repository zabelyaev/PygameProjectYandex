import pygame
from pygame import K_LEFT, K_UP, K_RIGHT, K_DOWN
from pygame.sprite import Sprite

from constansts import TILE_HEIGHT, TILE_WIDTH, HEIGHT, WIDTH, SOUNDS


class Player(Sprite):
    def __init__(self, player_image, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.image = player_image
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(TILE_WIDTH * pos[0] + 15, TILE_HEIGHT * pos[1] + 5)

        self.step_x = 0
        self.step_y = 0

        self.image_left = self.image
        self.image_right = pygame.transform.flip(self.image, True, False)

    def update(self, coin_groups, score):
        if pygame.sprite.spritecollide(self, coin_groups, dokill=True):
            SOUNDS['coin'].play()
            score.increase_score(level_increase=1)

    def move(self, events, walls=None):
        if events.key == K_LEFT:
            self.step_x = -TILE_WIDTH
            self.step_y = 0
            self.image = self.image_left
        elif events.key == K_RIGHT:
            self.step_x = TILE_WIDTH
            self.step_y = 0
            self.image = self.image_right
        if events.key == K_UP:
            self.step_y = -TILE_HEIGHT
            self.step_x = 0
        elif events.key == K_DOWN:
            self.step_y = TILE_HEIGHT
            self.step_x = 0

        if walls:
            move_rect = self.rect.move(self.step_x, self.step_y)
            can_move = True

            if 0 < move_rect.x <= WIDTH and 0 < move_rect.y <= HEIGHT:
                for wall in walls:
                    if move_rect.colliderect(wall.rect) and not wall.no_rect:
                        can_move = False
                        break
                if can_move:
                    self.rect = self.rect.move(self.step_x, self.step_y)

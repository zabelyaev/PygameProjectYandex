import pygame

from constansts import HEIGHT, WIDTH
from extensions import load_image


def start_screen(screen):
    intro_text = ["2D GAME", "",
                  "Правила игры",
                  "Перемещение на стрелки",
                  "Сквозь предметы проходить нельзя"
                  ]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = HEIGHT // 2 - len(intro_text) * 10 - 10

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect(center=(WIDTH // 2, 0))
        text_coord += 10
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def loading_screen(screen):
    intro_text = ["Введите название карты в консоль.", "",
                  "Не вводите расширение, все карты имеют формат",
                  "txt.",
                  "Доступные карты:",
                  "map",
                  "map1",
                  "map2"
                  ]

    font = pygame.font.Font(None, 30)
    text_coord = 50

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def end_screen(screen):
    intro_text = ["Введите название карты в консоль.", "",
                  "Не вводите расширение, все карты имеют формат",
                  "txt.",
                  "Доступные карты:",
                  "map",
                  "map1",
                  "map2"
                  ]

    font = pygame.font.Font(None, 30)
    text_coord = 50

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def show_quest(screen, texts, time=10):
    intro_text = texts
    while True:
        time -= 1
        if time < 0:
            break
        print(time)

    font = pygame.font.Font(None, 30)
    text_coord = 0
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect(center=(WIDTH // 2, 0))
        text_coord += 10
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        pygame.draw.rect(screen, (255, 0, 0), intro_rect, 0)
        screen.blit(string_rendered, intro_rect)

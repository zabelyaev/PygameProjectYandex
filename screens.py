import pygame

from constansts import HEIGHT, WIDTH
from dbmanager import DBManager
from extensions import load_image


def draw_text(screen, texts: list, font_family=None, font_size=30) -> None:
    font = pygame.font.Font(font_family, font_size)
    text_coord = HEIGHT // 2 - len(texts) * 10 - 10

    for line in texts:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect(center=(WIDTH // 2, 0))
        text_coord += 10
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def start_screen(screen) -> None:
    intro_text = ["2D GAME", "",
                  "Правила игры",
                  "Перемещение на стрелки",
                  "Через некоторые ящики можно пройти",
                  "Нажмите любую кнопку, чтобы начать"
                  ]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    draw_text(screen, intro_text)


def end_screen(screen) -> None:
    screen.fill(0)

    end_score = DBManager().fetch_score()

    intro_text = ["Поздравляем, вы победили!", "",
                  f"Текущий счет: {end_score}!",
                  'Перезапустите игру, чтобы начать сначала!'
                  ]

    draw_text(screen, intro_text)

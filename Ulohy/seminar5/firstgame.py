import pygame
from pygame.locals import *
import sys
import random

# Create the constants (go ahead and experiment with different values)
TILE_SIZE = 80
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
BLANK = None

# Colours are coded as tuples in form of (Red, Green, Blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHT_BLUE = (0, 50, 255)
DARK_TURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

BG_COLOR = DARK_TURQUOISE
TILE_COLOR = GREEN
TEXT_COLOR = WHITE
BORDER_COLOR = BRIGHT_BLUE
BASIC_FONT_SIZE = 20

BUTTON_COLOR = WHITE
BUTTON_TEXT_COLOR = BLACK
MESSAGE_COLOR = WHITE

# constants for all four movement directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# global variable to be used in multiple functions, default value is None
FPS_CLOCK = None
DISPLAY_SURFACE = None
BASIC_FONT = None
BUTTONS = None

class Board:
    def __init__(self):
        self.board = []
        self.board_width = 4
        self.board_height = 4
        self.difficulty = 10
        self.x_margin = int((WINDOW_WIDTH - (TILE_SIZE * self.board_width + (self.board_width - 1))) / 2)
        self.y_margin = int((WINDOW_HEIGHT - (TILE_SIZE * self.board_height + (self.board_height - 1))) / 2)
        self.highest_tile = self.board_width * self.board_height - 1
    
    def generate_board(self):
        self.board = [[Tile(i + 1, x, y) for x, i in enumerate(range(row * self.board_width, (row + 1) * self.board_width))]
                    for y, row in enumerate(range(self.board_height))]
        self.board[-1][-1] = BLANK
        return self.board


class Tile:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.number == other.number
        return False
    
    def __str__(self):
        return str(self.number)

def main():
    global FPS_CLOCK, DISPLAY_SURFACE, BASIC_FONT, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Slide Puzzle')
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)
    pygame. display.update()
    FPS_CLOCK.tick(FPS)
    game_board = Board()
    mouse_coordinates = 0, 0
    
    draw_tile(Board(), Tile(3, 2, 1))
    solved_board = Board()
    solved_board.generate_board()
    draw_board(solved_board, "Message")
    while True:
        pygame.display.update()
        FPS_CLOCK.tick(FPS)

        mouse_clicked = False
        for event in pygame.event.get():
            if (event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()

def terminate():
    pygame.quit()
    sys.exit()

def get_left_top_of_tile(board: Board, tile: Tile):
    if tile.number == BLANK:
        return (None, None)
    else:
        x, y = tile[0], tile[1]
        left = x * (TILE_SIZE + x - 1) + board.xmargin
        top = y * (TILE_SIZE + y - 1) + board.ymargin
        return left, top

def draw_tile(board: Board, tile: Tile, adj_x = 0, adj_y = 0):
    tile_x = (WINDOW_WIDTH // 2) - (TILE_SIZE // 2) + adj_x
    tile_y = (WINDOW_HEIGHT // 2) - (TILE_SIZE // 2) + adj_y
    rect = (tile_x, tile_y, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(DISPLAY_SURFACE, TILE_COLOR, rect)
    text_surf = BASIC_FONT.render(f"{tile.__str__()}", True, WHITE)
    text_rect = text_surf.get_rect(center=(tile_x + TILE_SIZE // 2, tile_y + TILE_SIZE // 2))
    DISPLAY_SURFACE.blit(text_surf, text_rect)

def make_text(text, color, bg_color, top, left):
    text_surf = BASIC_FONT.render(text, True, color, bg_color)
    text_rect = text_surf.get_rect(topleft=(top, left))
    return text_surf, text_rect

def draw_board(board: Board, message):
    DISPLAY_SURFACE.fill(BG_COLOR)
    text_surf, text_rect = make_text(message, WHITE, BG_COLOR, 2, 2)
    DISPLAY_SURFACE.blit(text_surf, text_rect)
    for y in range(0, board.board_height-1):
        for x in range(0, board.board_width-1):
            tile = board.board[y][x]
            if tile is not BLANK:
                draw_tile(board, tile, x * TILE_SIZE, y * TILE_SIZE)

if __name__ == '__main__':
    main()
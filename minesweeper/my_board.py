import enum
import random

import pygame as pg

from board import Board

CLOSED = -1
MINE = 10
FLAG = 100
QUESTION = 200


class Status(enum.Enum):
    NOT_INITIALIZED = 0
    PLAYING = 1
    WINNING = 2
    LOSING = 3


class Minesweeper(Board):
    """
    0       - 0 мин вокруг (открытая клетка)
    1..8    - 1-8 мин вокруг (открытая клетка)
    -1      - закрытая клетка (не мина)
    10      - мина
    +100    - флажок
    +200    - вопрос
    """

    CELL_COLOR = pg.Color('#818181')

    def __init__(self, width: int, height: int, count_mines: int):
        super().__init__(width, height, initial_value=CLOSED)
        self._count_mines = count_mines
        self._status = Status.NOT_INITIALIZED
        self._show_mines = True     # TODO: вернуть на False

    def draw_cell(self, screen: pg.Surface, row: int, col: int, rect: pg.Rect) -> None:
        cell = self._board[row][col]
        if cell == MINE and self._show_mines:
            pg.draw.rect(screen, 'red', rect)

    def on_click(self, row: int, col: int) -> None:
        if self._status == Status.NOT_INITIALIZED:
            self._initial(row, col)
            return
        # TODO

    def _initial(self, row: int, col: int) -> None:
        n = 0
        assert self._count_mines < self._width * self._height
        while n < self._count_mines:
            x = random.randrange(self._width)
            y = random.randrange(self._height)
            if (y, x) != (row, col) and self._board[y][x] == CLOSED:
                self._board[y][x] = MINE
                n += 1

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
        self._show_mines = True  # TODO: вернуть на False
        self._no_mines = self._width * self._height - count_mines
        font = pg.font.Font(None, round(self._cell_size * 1.2))
        self._DIGITS = [
            font.render(str(i), True, color)
            for i, color in enumerate([
                'black', 'blue', 'green', 'orange', 'black', 'darkviolet', 'saddlebrown', 'maroon', 'red'
            ])
        ]

    def draw_cell(self, screen: pg.Surface, row: int, col: int, rect: pg.Rect) -> None:
        cell = self._board[row][col]
        if cell == MINE and self._show_mines:
            pg.draw.rect(screen, 'red', rect)
        elif cell == CLOSED or cell == MINE and not self._show_mines:
            pg.draw.rect(screen, '#505050', rect)
        elif 0 < cell <= 8:
            digit = self._DIGITS[cell]
            screen.blit(digit, (
                rect.centerx - digit.get_width() // 2,
                rect.centery - digit.get_height() // 2
            ))

    def on_click(self, row: int, col: int) -> None:
        if self._status == Status.WINNING or self._status == Status.LOSING:
            return
        if self._status == Status.NOT_INITIALIZED:
            self._initial(row, col)
        if self._board[row][col] == MINE:
            self._lose()
        if self._board[row][col] == CLOSED:
            self._no_mines -= 1
            self._board[row][col] = self._get_neighbours(row, col)
            if self._no_mines == 0:
                self._win()

    def _get_neighbours(self, row: int, col: int) -> int:
        result = 0
        for x in range(col - 1, col + 2):
            for y in range(row - 1, row + 2):
                if self.get_cell(y, x) == MINE:
                    result += 1
        return result

    def _win(self) -> None:
        self._status = Status.WINNING
        print('win')

    def _lose(self) -> None:
        self._status = Status.LOSING
        self._show_mines = True
        print('lose')

    def _initial(self, row: int, col: int) -> None:
        self._status = Status.PLAYING
        n = 0
        assert self._count_mines < self._width * self._height
        while n < self._count_mines:
            x = random.randrange(self._width)
            y = random.randrange(self._height)
            if (y, x) != (row, col) and self._board[y][x] == CLOSED:
                self._board[y][x] = MINE
                n += 1

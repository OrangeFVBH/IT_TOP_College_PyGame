import random

import pygame as pg

from .utils import load_image
from .kuplich import Kuplich


class Coin(pg.sprite.Sprite):
    IMG  = pg.transform.smoothscale(
        load_image('coin.png'),
        (30, 30))
    SPEED = 8
    MASK = pg.mask.from_surface(IMG)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = self.IMG
        self.rect = self.IMG.get_rect()
        self.rect.bottom = 0
        self.rect.left = random.randrange(0, 800 - self.rect.width)
        self.mask = self.MASK

    def update(self, events):
        self.rect.y += self.SPEED
        if self.rect.top > 600:
            self.kill()
            Kuplich.get_instance().damage()

import random

import pygame as pg

from utils import load_image


class Kuplich(pg.sprite.Sprite):
    IMG = pg.transform.smoothscale(
        load_image('kuplich.png'),
        (300, 300))
    IMG_FLIPPED = pg.transform.flip(IMG, True, False)
    MASK = pg.mask.from_surface(IMG)
    MASK_FLIPPED = pg.mask.from_surface(IMG_FLIPPED)
    STEP = 5

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = self.IMG
        self.mask = self.MASK
        self.rect = self.IMG.get_rect()

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key in (pg.K_LEFT, pg.K_a):
                    self.image = self.IMG_FLIPPED
                    self.mask = self.MASK_FLIPPED
                elif event.key in (pg.K_RIGHT, pg.K_d):
                    self.image = self.IMG
                    self.mask = self.MASK

        keyboard = pg.key.get_pressed()
        if (keyboard[pg.K_a] or keyboard[pg.K_LEFT]) and self.rect.left > 0:
            self.rect.move_ip(-self.STEP, 0)
        if (keyboard[pg.K_d] or keyboard[pg.K_RIGHT]) and self.rect.right < 800:
            self.rect.move_ip(self.STEP, 0)


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

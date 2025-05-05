import random

import pygame as pg

pg.init()
SIZE = WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode(SIZE)

from src.kyle import Kyle, RKN, Chips
from src.cartman import Cartman
from src.utils import load_image

FPS = 60
BACKGROUND = pg.transform.smoothscale(load_image('background.png'), SIZE)

clock = pg.time.Clock()
running = True

all_sprites = pg.sprite.Group()
items_group = pg.sprite.Group()
player = Cartman(all_sprites)
player.rect.bottom = HEIGHT
player.rect.centerx = WIDTH / 2

font = pg.font.Font('data/Segoe UI Symbol.ttf', 50)

while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    screen.blit(BACKGROUND, (0, 0))
    if random.random() < 0.02:
        Kyle(all_sprites, items_group)
    if random.random() < 0.005:
        RKN(all_sprites, items_group)
    if random.random() < 0.002:
        Chips(all_sprites, items_group)
    all_sprites.draw(screen)
    all_sprites.update(events)
    player.collide(items_group)

    screen.blit(font.render(player.coins, True, '#E5B700'), (10, 10))
    screen.blit(font.render(player.health, True, '#E5000A'), (10, 60))

    pg.display.flip()
    clock.tick(FPS)
pg.quit()

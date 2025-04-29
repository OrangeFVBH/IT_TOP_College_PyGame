import random

import pygame as pg
import pygame.sprite

pg.init()
SIZE = WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode(SIZE)

from my_sprite import Kuplich, Coin

FPS = 60
BACKGROUND_COLOR = (0, 0, 0)

clock = pg.time.Clock()
running = True

all_sprites = pg.sprite.Group()
coins_group = pg.sprite.Group()
player = Kuplich(all_sprites)
player.rect.bottom = HEIGHT
player.rect.centerx = WIDTH / 2

while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)
    # if random.random() < 0.2:
    for _ in range(100):
        Coin(all_sprites, coins_group)
    all_sprites.draw(screen)
    all_sprites.update(events)
    collided = pygame.sprite.spritecollide(player, coins_group, True, pg.sprite.collide_mask)


    pg.display.flip()
    clock.tick(FPS)
pg.quit()

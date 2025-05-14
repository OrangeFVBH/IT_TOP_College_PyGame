import pygame as pg

from config import Config
import src.utils as utils

pg.init()
screen = pg.display.set_mode(Config.SIZE)


def main(screen: pg.Surface):
    clock = pg.time.Clock()
    background = 'black'

    images = utils.load_many_images('player.png', 4, 3, None)
    i = 0

    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        screen.fill(background)
        i += 1
        img = pg.transform.scale(images[i // 10 % 3], (235, 150))
        screen.blit(img, (0, 0))

        pg.display.flip()
        clock.tick(Config.FPS)


if __name__ == '__main__':
    main(screen)
    pg.quit()
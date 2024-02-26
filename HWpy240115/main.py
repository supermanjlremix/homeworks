import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(0, 0, 0)
    pg.display.update()
pg.quit()

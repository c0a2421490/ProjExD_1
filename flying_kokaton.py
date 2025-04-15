import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    kk_img = pg.image.load("fig/3.png")#2
    kk_img = pg.transform.flip(kk_img, True, False)
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    tmr = 0
    kk_rect =kk_img.get_rect()
    kk_rect.center = 300, 200
    while True:
        x = 0
        y = 0
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            x = 0
            y = -1
        if key_lst[pg.K_DOWN]:
            x = 0
            y = 1
        if key_lst[pg.K_LEFT]:
            x = -1
            y = 0
        if key_lst[pg.K_RIGHT]:
            x = 2
            y = 0

        kk_rect.move_ip((x-1, y))

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])
        screen.blit(kk_img, kk_rect)
        #screen.blit(kk_img, [300, 200])#4

        pg.display.update()
        tmr += 1        
        clock.tick(200)#5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((700, 500))
pg.display.set_caption("Доганялки")
background = pg.transform.scale(pg.image.load('assets\\background.png'), (700, 500))
pg.display.set_icon(pg.image.load('assets\\icon.png'))

SCALE = (50, 100)

sprite1 = pg.transform.scale(pg.image.load('assets\\sprite1.png'), SCALE)
sprite2 = pg.transform.scale(pg.image.load('assets\\sprite2.png'), SCALE)

clock = pg.time.Clock()
FPS = 60

def main(running):
    x1 = 100
    y1 = 100
    vy1 = 0
    on_ground1 = True

    x2 = 500
    y2 = 100
    vy2 = 0
    on_ground2 = True

    while running:
        screen.blit(background, (0, 0))
        screen.blit(sprite1, (x1, y1))
        screen.blit(sprite2, (x2, y2))
        keys_pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()

        if keys_pressed[pg.K_a] and x1 > 5:
            x1 -= 5
            
        if keys_pressed[pg.K_d] and x1 < 650:
            x1 += 5
            
        if keys_pressed[pg.K_w] and on_ground1:
            vy1 = -20
            on_ground1 = False
            pg.mixer.Sound('assets\\jump.wav').play()
        
        if keys_pressed[pg.K_LEFT] and x2 > 5:
            x2 -= 5
            
        if keys_pressed[pg.K_RIGHT] and x2 < 650:
            x2 += 5
            
        if keys_pressed[pg.K_UP] and on_ground2:
            vy2 = -20
            on_ground2 = False
            pg.mixer.Sound('assets\\jump.wav').play()
            
        vy1 += 1
        y1 += vy1
        if y1 > 256:
            y1 = 256
            on_ground1 = True

        vy2 += 1
        y2 += vy2
        if y2 > 256:
            y2 = 256
            on_ground2 = True
            
        pg.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main(True)
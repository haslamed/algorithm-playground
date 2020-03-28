import pygame as pg

def render_avatar(x,y):
    display.blit(avatar, (x,y))

width,height = 800,600
avatar = pg.image.load('images/avatar.png')

pg.init()

display = pg.display.set_mode((width,height))
clock = pg.time.Clock()

valid_exit_events = [pg.QUIT]

x,y = 1,1
xinc,yinc = 1,1

while True:
    exit_events = [True for event in pg.event.get() if event in valid_exit_events]

    if len(exit_events) > 0:
        break

    if not 0<x<width:
        xinc *= -1
    if not 0<y<height:
        yinc *= -1
    
    x += xinc
    y += yinc

    display.fill(pg.color.THECOLORS['white'])
    render_avatar(x,y)
    
    pg.display.update()
    clock.tick(60)    

pg.quit()

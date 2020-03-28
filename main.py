import pygame as pg
from collections import OrderedDict

def add_avatar_tracks(objects):
    a_coords,a_image = objects['avatar']
    bg_coords,bg_image = objects['bg']

    bg.blit(track,a_coords)

    return (bg_coords,bg_image)

def get_avatar(objects, speed=2):
    (a_x, a_y),a_image = objects['avatar']

    if 'target' in objects:
        (t_x, t_y),_ = objects['target']
        hyp_len = ((t_x-a_x)**2 + (t_y-a_y)**2)**0.5

        if hyp_len<1:
            new_a_x = a_x
            new_a_y = a_y
        else:
            new_a_x = a_x + (t_x-a_x)/hyp_len*speed
            new_a_y = a_y + (t_y-a_y)/hyp_len*speed
    else:
        new_a_x = a_x
        new_a_y = a_y

    if 'obstacle' in objects:
        (o_x,o_y),o_image = objects['obstacle']
        o_w,o_h = o_image.get_width(),o_image.get_height()
        a_w,a_h = a_image.get_width(),a_image.get_height()

        a_points = [(new_a_x,new_a_y),(new_a_x+a_w,new_a_y),
                    (new_a_x,new_a_y+a_h),(new_a_x+a_w,new_a_y+a_h)]

        for x,y in a_points:
            if o_x<x<o_x+o_w and o_y<y<o_y+o_h:
                new_a_x = a_x
                new_a_y = a_y
                break
                
    return ((new_a_x,new_a_y),a_image)

width,height = 800,600

exit_event_types = [pg.QUIT]

avatar = pg.image.load('images/avatar.png')
target = pg.image.load('images/target.png')
obstacle = pg.image.load('images/obstacle.png')
track = pg.image.load('images/track.png')
bg = pg.Surface((width,height))
bg.fill(pg.color.THECOLORS['white'])

pg.init()

display = pg.display.set_mode((width,height))
clock = pg.time.Clock()

objects = OrderedDict({'bg':((0,0),bg), 'avatar':((1,1),avatar), 'obstacle':((400,300),obstacle)})

exit_game = False

while not exit_game:
    for event in pg.event.get():
        if event.type in exit_event_types:
            exit_game = True
        if event.type == pg.MOUSEBUTTONUP:
            mouse_x,mouse_y = pg.mouse.get_pos()
            objects['target'] = ((mouse_x,mouse_y),target)

    objects['avatar'] = get_avatar(objects)
    objects['bg'] = add_avatar_tracks(objects)

    for _,((x,y),image) in objects.items():
        display.blit(image,(round(x),round(y)))
    
    pg.display.update()
    clock.tick(60)    

pg.quit()

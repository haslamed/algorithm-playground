import pygame as pg

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
    
    return ((new_a_x,new_a_y),a_image)

width,height = 800,600

exit_event_types = [pg.QUIT]

avatar = pg.image.load('images/avatar.png')
target = pg.image.load('images/target.png')

pg.init()

display = pg.display.set_mode((width,height))
clock = pg.time.Clock()

objects = {'avatar':((1,1),avatar)}

exit_game = False

while not exit_game:
    for event in pg.event.get():
        if event.type in exit_event_types:
            exit_game = True
        if event.type == pg.MOUSEBUTTONUP:
            mouse_x,mouse_y = pg.mouse.get_pos()
            objects['target'] = ((mouse_x,mouse_y),target)

    objects['avatar'] = get_avatar(objects)

    display.fill(pg.color.THECOLORS['white'])

    for _,((x,y),image) in objects.items():
        display.blit(image,(round(x),round(y)))
    
    pg.display.update()
    clock.tick(60)    

pg.quit()

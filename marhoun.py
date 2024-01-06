import pygame as pg
import random
from PIL import Image
from itertools import cycle
from Duck import Duck

pic_world = Image.open('Sprites/world.png').convert('RGBA')
pixels = pic_world.load()
for i in range(pic_world.size[0]):
    for j in range(pic_world.size[1]):
        if (i + j) % 2 == 0:
            pixels[i, j] = 0, 0, 0, 0
pic_world.save('Sprites/world.png')

pg.init()

WIDTH, HEIGHT = 1400, 700

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('FREE FOR URSA')
# screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)


clock = pg.time.Clock()
FPS = 60
background = (0, 0, 0)

pg.mouse.set_visible(False)
crosshair = pg.image.load('Sprites/crosshair.png')
crosshair = pg.transform.scale(crosshair, (32, 32))

glasses = pg.image.load('Sprites/glasses.png')
glasses = pg.transform.scale(glasses, (WIDTH + 100, HEIGHT + 40))

world = pg.image.load('Sprites/world.png')
world = pg.transform.scale(world, (WIDTH + 400, HEIGHT))

running = True
starting = [-200, 0]

# Ducks mechanic
CREATE_DUCK_EVENT = pg.USEREVENT + 1
CREATE_FLY_EVENT = pg.USEREVENT + 2
CREATE_SHOT_EVENT = pg.USEREVENT + 3
pg.time.set_timer(CREATE_DUCK_EVENT, 600)
pg.time.set_timer(CREATE_FLY_EVENT, 200)
pg.time.set_timer(CREATE_SHOT_EVENT, 150)
Duck = Duck(screen)
classic = -200

# Kill mechanic
shot_animation = []
for i in range(1, 18):
    sprite = pg.image.load(f'Sprites/shot/shot{i}.png').convert_alpha()
    sprite = pg.transform.scale(sprite, (90, 80))
    shot_animation.append(sprite)
dead_ducks = []

while running:
    screen.fill(background)
    screen.blit(world, starting)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                crosshair = pg.image.load('Sprites/crosshair_hit.png')
                mouse_x, mouse_y = pg.mouse.get_pos()
                for i in range(len(Duck.ducks)):
                    if Duck.ducks[i][0].x + 30 <= mouse_x <= Duck.ducks[i][0].x + 150 and \
                            Duck.ducks[i][0].y - 30 <= mouse_y <= Duck.ducks[i][0].y + 60:
                        dead_ducks.append([Duck.ducks[i][0].x, Duck.ducks[i][0].y, 0])
                        Duck.death(i)
                        break
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                crosshair = pg.image.load('Sprites/crosshair.png')
        if event.type == CREATE_DUCK_EVENT:
            if len(Duck.ducks) != 5:
                Duck.create_new_duck(random.choice([True, False]))
        if event.type == CREATE_FLY_EVENT:
            for i in range(len(Duck.ducks)):
                Duck.ducks[i][1] = Duck.ducks[i][1][1:] + [Duck.ducks[i][1][0]]
        if event.type == CREATE_SHOT_EVENT:
            to_del = []
            for i in range(len(dead_ducks)):
                if dead_ducks[i][2] < 4:
                    dead_ducks[i][2] += 1
                else:
                    to_del.append(i)
            for i in to_del:
                dead_ducks.pop(i)
    for i in dead_ducks:
        screen.blit(shot_animation[i[2]], (i[0], i[1]))
    res = Duck.moving(classic, starting[0])
    classic = res
    Duck.flying()

    # Проблемы с мастшабом
    if pg.mouse.get_pos()[0] <= 10 and starting[0] < 0:
        starting[0] += 4
    elif pg.mouse.get_pos()[0] >= WIDTH - 50 and starting[0] > -350:
        starting[0] -= 4

    cursor_xy = list(pg.mouse.get_pos())
    if cursor_xy[0] > 1367:
        cursor_xy[0] = 1367
    if cursor_xy[1] > 671:
        cursor_xy[1] = 671

    screen.blit(glasses, (-50, -20))

    # Battery mechanic
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(10, 10, 130, 2))


    screen.blit(crosshair, cursor_xy)
    pg.display.flip()
    pg.display.update()
    clock.tick(FPS)

pg.quit()

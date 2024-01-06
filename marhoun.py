import pygame as pg
import random
from PIL import Image
from itertools import cycle
from Duck import Duck

pic_world = Image.open('Sprites/world.png').convert('RGBA')
pixels = pic_world.load()
for k in range(pic_world.size[0]):
    for l in range(pic_world.size[1]):
        if (k + l) % 2 == 0:
            pixels[k, l] = 0, 0, 0, 0
pic_world.save('Sprites/world.png')

pg.init()
pg.display.set_caption('FREE FOR URSA')


class Game:
    def __init__(self, goal, width=1400, height=700):
        self.WIDTH, self.HEIGHT = width, height
        self.goal = goal
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.background = (0, 0, 0)
        # UI
        self.crosshair = pg.image.load('Sprites/crosshair.png')
        self.crosshair = pg.transform.scale(self.crosshair, (32, 32))
        self.glasses = pg.image.load('Sprites/glasses.png')
        self.glasses = pg.transform.scale(self.glasses, (self.WIDTH + 100, self.HEIGHT + 40))
        self.world = pg.image.load('Sprites/world.png')
        self.world = pg.transform.scale(self.world, (self.WIDTH + 400, self.HEIGHT))
        self.starting = [-200, 0]
        self.CREATE_DUCK_EVENT = pg.USEREVENT + 1
        self.CREATE_FLY_EVENT = pg.USEREVENT + 2
        self.CREATE_SHOT_EVENT = pg.USEREVENT + 3
        pg.time.set_timer(self.CREATE_DUCK_EVENT, 600)
        pg.time.set_timer(self.CREATE_FLY_EVENT, 200)
        pg.time.set_timer(self.CREATE_SHOT_EVENT, 150)
        # Duck mechanic
        self.Duck = Duck(self.screen)
        self.classic = -200
        # Kill mechanic
        self.shot_animation = []
        for i in range(1, 18):
            sprite = pg.image.load(f'Sprites/shot/shot{i}.png').convert_alpha()
            sprite = pg.transform.scale(sprite, (90, 80))
            self.shot_animation.append(sprite)
        self.dead_ducks = []
        # Battery mechanic
        self.battery = [True, True, True, True]
        self.battery_index = 3
        # White noise mechanic
        self.WHITE_NOISE_EVENT = pg.USEREVENT + 4
        self.WHITE_NOISE_ANIMATION_EVENT = pg.USEREVENT + 5
        pg.time.set_timer(self.WHITE_NOISE_EVENT, 2000)
        pg.time.set_timer(self.WHITE_NOISE_ANIMATION_EVENT, 200)
        self.step1 = pg.image.load('Sprites/white noise/steps/first.png').convert_alpha()
        self.step1 = pg.transform.scale(self.step1, (1400, 700))
        self.step2 = pg.image.load('Sprites/white noise/steps/second.png').convert_alpha()
        self.step2 = pg.transform.scale(self.step2, (1400, 700))
        self.step3 = pg.image.load('Sprites/white noise/steps/third.png').convert_alpha()
        self.step3 = pg.transform.scale(self.step3, (1400, 700))
        self.step4 = pg.image.load('Sprites/white noise/steps/fourth.png').convert_alpha()
        self.step4 = pg.transform.scale(self.step4, (1400, 700))
        self.white_noise_animation = False
        self.wn1 = pg.image.load('Sprites/white noise/wn1.png').convert_alpha()
        self.wn1 = pg.transform.scale(self.wn1, (1400, 700))
        self.wn2 = pg.image.load('Sprites/white noise/wn2.png').convert_alpha()
        self.wn2 = pg.transform.scale(self.wn2, (1400, 700))
        self.wn3 = pg.image.load('Sprites/white noise/wn3.png').convert_alpha()
        self.wn3 = pg.transform.scale(self.wn3, (1400, 700))
        self.wn4 = pg.image.load('Sprites/white noise/wn4.png').convert_alpha()
        self.wn4 = pg.transform.scale(self.wn4, (1400, 700))
        self.wn_animation = [self.wn1, self.wn2, self.wn3, self.wn4]
        self.do_animation = False
        self.running = True

    def play(self):
        pg.mouse.set_visible(False)

        while self.running:
            self.screen.fill(self.background)
            self.screen.blit(self.world, self.starting)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.crosshair = pg.image.load('Sprites/crosshair_hit.png')
                        mouse_x, mouse_y = pg.mouse.get_pos()
                        for i in range(len(self.Duck.ducks)):
                            if self.Duck.ducks[i][0].x + 30 <= mouse_x <= self.Duck.ducks[i][0].x + 150 and \
                                    self.Duck.ducks[i][0].y - 30 <= mouse_y <= self.Duck.ducks[i][0].y + 60:
                                self.dead_ducks.append([self.Duck.ducks[i][0].x, self.Duck.ducks[i][0].y, 0])
                                self.Duck.death(i)
                                break
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.crosshair = pg.image.load('Sprites/crosshair.png')
                if event.type == self.CREATE_DUCK_EVENT:
                    if len(self.Duck.ducks) != 5:
                        self.Duck.create_new_duck(random.choice([True, False]))
                if event.type == self.CREATE_FLY_EVENT:
                    for i in range(len(self.Duck.ducks)):
                        self.Duck.ducks[i][1] = self.Duck.ducks[i][1][1:] + [self.Duck.ducks[i][1][0]]
                if event.type == self.CREATE_SHOT_EVENT:
                    to_del = []
                    for i in range(len(self.dead_ducks)):
                        if self.dead_ducks[i][2] < 4:
                            self.dead_ducks[i][2] += 1
                        else:
                            to_del.append(i)
                    for i in to_del:
                        self.dead_ducks.pop(i)
                if event.type == self.WHITE_NOISE_EVENT:
                    self.battery[self.battery_index] = False
                    if self.battery_index > 0:
                        self.battery_index -= 1
                    else:
                        self.white_noise_animation = True
                if event.type == self.WHITE_NOISE_ANIMATION_EVENT and self.white_noise_animation:
                    self.do_animation = True

            for i in self.dead_ducks:
                self.screen.blit(self.shot_animation[i[2]], (i[0], i[1]))
            res = self.Duck.moving(self.classic, self.starting[0])
            self.classic = res
            self.Duck.flying()

            # Проблемы с мастшабом
            if pg.mouse.get_pos()[0] <= 10 and self.starting[0] < 0:
                self.starting[0] += 4
            elif pg.mouse.get_pos()[0] >= self.WIDTH - 50 and self.starting[0] > -350:
                self.starting[0] -= 4

            cursor_xy = list(pg.mouse.get_pos())
            if cursor_xy[0] > 1367:
                cursor_xy[0] = 1367
            if cursor_xy[1] > 671:
                cursor_xy[1] = 671

            if not self.battery[0]:
                self.screen.blit(self.step4, (0, 0))
            elif not self.battery[1]:
                self.screen.blit(self.step3, (0, 0))
            elif not self.battery[2]:
                self.screen.blit(self.step2, (0, 0))
            elif not self.battery[3]:
                self.screen.blit(self.step1, (0, 0))

            if self.do_animation:
                self.screen.blit(self.wn_animation[0], (0, 0))
                self.wn_animation = self.wn_animation[1:] + [self.wn_animation[0]]
                self.do_animation = False
            elif not self.do_animation and self.white_noise_animation:
                self.screen.blit(self.wn_animation[0], (0, 0))

            self.screen.blit(self.glasses, (-50, -20))

            # Battery mechanic
            pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(10, 10, 130, 2))
            pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(10, 10, 2, 60))
            pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(10, 70, 132, 2))
            pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(140, 10, 2, 60))
            pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(140, 31, 5, 20))
            if self.battery[0]:
                pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(14, 14, 29, 54))
            if self.battery[1]:
                pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(45, 14, 29, 54))
            if self.battery[2]:
                pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(76, 14, 29, 54))
            if self.battery[3]:
                pg.draw.rect(self.screen, (255, 255, 255), pg.Rect(107, 14, 29, 54))

            self.screen.blit(self.crosshair, cursor_xy)
            pg.display.flip()
            pg.display.update()
            self.clock.tick(self.FPS)


game = Game(10)
game.play()
pg.quit()

import pygame as pg
import random


class Bear:
    def __init__(self, surface):
        self.screen = surface
        self.bears = []
        self.positions = [(i[1], i[0]) for i in
                          [(450, 150), (450, 550), (450, 850), (450, 1150), (450, 1350)]]

    def create(self):
        if len(self.bears) < 5:
            position = random.choice(list(set(self.positions).symmetric_difference([i[0] for i in self.bears])))
            bear = pg.Rect(position[0], position[1], 50, 80)
            # Bear sprites
            spr1 = pg.transform.scale(pg.image.load('Sprites/bear/bear1.png').convert_alpha(), (50, 80))
            spr2 = pg.transform.scale(pg.image.load('Sprites/bear/bear2.png').convert_alpha(), (50, 80))
            spr3 = pg.transform.scale(pg.image.load('Sprites/bear/bear3.png').convert_alpha(), (50, 80))
            spr4 = pg.transform.scale(pg.image.load('Sprites/bear/bear4.png').convert_alpha(), (50, 80))
            spr5 = pg.transform.scale(pg.image.load('Sprites/bear/bear5.png').convert_alpha(), (50, 80))
            spr6 = pg.transform.scale(pg.image.load('Sprites/bear/bear6.png').convert_alpha(), (50, 80))
            spr7 = pg.transform.scale(pg.image.load('Sprites/bear/bear7.png').convert_alpha(), (50, 80))
            bear_animation = [spr1, spr2, spr3, spr4, spr5, spr6, spr7]
            self.bears.append([position, bear, bear_animation])

    def update(self):
        for i in self.bears:
            self.screen.blit(i[2][0], i[0])

    def death(self, index):
        if index < len(self.bears):
            self.bears.pop(index)

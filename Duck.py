import pygame as pg
import random
from itertools import cycle
import time


class Duck:
    def __init__(self, surface):
        self.screen = surface
        self.ducks = []

    def create_new_duck(self, right=True):
        available_coords = [i[0].y for i in self.ducks]
        coord = random.choice(list({100, 150, 200, 250, 300}.symmetric_difference(set(available_coords))))
        duck = pg.Rect(0, coord, 50, 50) if right else pg.Rect(1250, coord, 50, 50)
        if right:
            duck_sprite = pg.image.load('Sprites/duck/duck_default.png').convert_alpha()
            duck_sprite = pg.transform.scale(duck_sprite, (150, 100))
            duck_sprite1 = pg.image.load('Sprites/duck/duck1.png').convert_alpha()
            duck_sprite1 = pg.transform.scale(duck_sprite1, (150, 100))
            duck_sprite2 = pg.image.load('Sprites/duck/duck2.png').convert_alpha()
            duck_sprite2 = pg.transform.scale(duck_sprite2, (150, 100))
            duck_animation = [duck_sprite, duck_sprite1, duck_sprite2]
        else:
            duck_sprite = pg.image.load('Sprites/duckl/duck_default.png').convert_alpha()
            duck_sprite = pg.transform.scale(duck_sprite, (150, 100))
            duck_sprite1 = pg.image.load('Sprites/duckl/duck1.png').convert_alpha()
            duck_sprite1 = pg.transform.scale(duck_sprite1, (150, 100))
            duck_sprite2 = pg.image.load('Sprites/duckl/duck2.png').convert_alpha()
            duck_sprite2 = pg.transform.scale(duck_sprite2, (150, 100))
            duck_animation = [duck_sprite, duck_sprite1, duck_sprite2]
        self.ducks.append([duck, duck_animation, right])

    def moving(self, classic_x, starting_x):
        ducks_to_delete = []
        for i in range(len(self.ducks)):
            if self.ducks[i][2]:
                offset = abs(abs(classic_x) - abs(starting_x))
                if starting_x < classic_x:
                    offset *= -1
                if self.ducks[i][0].x < 1400 - 40:
                    self.ducks[i][0] = self.ducks[i][0].move(5 + offset, 0)
                else:
                    ducks_to_delete.append(i)
            else:
                offset = abs(abs(classic_x) - abs(starting_x))
                if starting_x > classic_x:
                    offset *= -1
                if self.ducks[i][0].x > 5:
                    self.ducks[i][0] = self.ducks[i][0].move(-5 - offset, 0)
                else:
                    ducks_to_delete.append(i)
        for i in ducks_to_delete:
            self.ducks.pop(i)
        return starting_x

    def flying(self):
        for i in range(len(self.ducks)):
            # pg.draw.rect(self.screen, (255, 255, 255), self.ducks[i][0])
            self.screen.blit(self.ducks[i][1][0], (self.ducks[i][0].x, self.ducks[i][0].y))

    def death(self, index):
        if self.ducks[index]:
            self.ducks.pop(index)

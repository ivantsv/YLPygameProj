import pygame as pg
from Tutorial import Tutorial
from marhoun import Game, EndGame, EndLevel
from final_boss import GuitarHero
from broken_glasses import Point

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption('Kill them all')
    tutorial = Tutorial()
    tutorial.play(Game(1, 5, Game(1, 10, Game(1, 15, Game(1, 20, Point())))))
    pg.quit()

import pygame as pg
from Tutorial import Tutorial
from marhoun import Game, EndGame, EndLevel
from final_boss import GuitarHero
from broken_glasses import Point

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption('Kill them all')
    tutorial = Tutorial()
    lvl1 = Game(10, 5)
    lvl2 = Game(20, 10)
    lvl3 = Game(30, 15)
    lvl4 = Game(40, 20)
    lvl5 = Game(50, 25)
    br = Point()
    final = GuitarHero()

    tutorial.play()
    lvl1.play()
    lvl2.play()
    lvl3.play()
    lvl4.play()
    lvl5.play()
    br.play()
    final.play(25)
    pg.quit()

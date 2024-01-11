import pygame as pg
import random

pg.init()

WIDTH, HEIGHT = 400, 700

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Guitar Hero')

clock = pg.time.Clock()
FPS = 60

running = True

stack_1 = []
stack_2 = []
stack_3 = []
stack_4 = []
level = [stack_1, stack_2, stack_3, stack_4]

background = (116, 237, 194)

CREATE_BLOCK_EVENT = pg.USEREVENT + 1
pg.time.set_timer(CREATE_BLOCK_EVENT, 600)

FONT = pg.font.SysFont('Comic Sans', 28)


def deleting_blocks(screen):
    global level, stack_1, stack_2, stack_3, stack_4
    for i in range(len(level)):
        for j in range(len(level[i])):
            block = level[i][j]
            if block.y >= 626:
                if i == 0:
                    stack_1.remove(block)
                elif i == 1:
                    stack_2.remove(block)
                elif i == 2:
                    stack_3.remove(block)
                elif i == 3:
                    stack_4.remove(block)


def moving_blocks(screen):
    global level, stack_1, stack_2, stack_3, stack_4
    for i in range(len(level)):
        for j in range(len(level[i])):
            block = level[i][j]
            if block.y >= 626:
                if i == 0:
                    stack_1 = stack_1[:-1]
                elif i == 1:
                    stack_2 = stack_2[:-1]
                elif i == 2:
                    stack_3 = stack_3[:-1]
                elif i == 3:
                    stack_4 = stack_4[:-1]
                level = [stack_1, stack_2, stack_3, stack_4]
            else:
                pg.draw.rect(screen, (81, 166, 136), block)
                level[i][j] = block.move(0, 2)


score = 0

while running:
    screen.fill(background)

    # Edges
    pg.draw.rect(screen, (81, 166, 136), pg.Rect(0, 0, 2, 700))
    pg.draw.rect(screen, (81, 166, 136), pg.Rect(99, 0, 2, 700))
    pg.draw.rect(screen, (81, 166, 136), pg.Rect(199, 0, 2, 700))
    pg.draw.rect(screen, (81, 166, 136), pg.Rect(299, 0, 2, 700))
    pg.draw.rect(screen, (81, 166, 136), pg.Rect(398, 0, 2, 700))
    pg.draw.rect(screen, (81, 166, 136), pg.Rect(0, 648, 400, 2))
    pg.draw.rect(screen, (81, 166, 136), pg.Rect(0, 0, 400, 50))
    score_text = FONT.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, (400 / 2 - score_text.get_rect().w / 2, 50 / 2 - score_text.get_rect().h / 2))

    # Buttons
    pg.draw.rect(screen, (61, 199, 115), pg.Rect(29, 655, 40, 40))
    pg.draw.rect(screen, (61, 199, 115), pg.Rect(129, 655, 40, 40))
    pg.draw.rect(screen, (61, 199, 115), pg.Rect(229, 655, 40, 40))
    pg.draw.rect(screen, (61, 199, 115), pg.Rect(329, 655, 40, 40))
    letter_W = FONT.render('W', True, (255, 255, 255))
    letter_A = FONT.render('A', True, (255, 255, 255))
    letter_S = FONT.render('S', True, (255, 255, 255))
    letter_D = FONT.render('D', True, (255, 255, 255))

    screen.blit(letter_W, (38, 658))
    screen.blit(letter_A, (140, 658))
    screen.blit(letter_S, (240, 658))
    screen.blit(letter_D, (340, 658))

    moving_blocks(screen)

    for event in pg.event.get():
        distance1 = 1000
        distance2 = 1000
        distance3 = 1000
        distance4 = 1000
        if event.type == pg.QUIT:
            running = False
        elif event.type == CREATE_BLOCK_EVENT:
            print('User Event')
            index = random.choice([0, 1, 2, 3])
            if index == 0:
                block = pg.Rect(25, 5, 50, 30)
                stack_1 = [block] + stack_1
            elif index == 1:
                block = pg.Rect(125, 5, 50, 30)
                stack_2 = [block] + stack_2
            elif index == 2:
                block = pg.Rect(225, 5, 50, 30)
                stack_3 = [block] + stack_3
            elif index == 3:
                block = pg.Rect(325, 5, 50, 30)
                stack_4 = [block] + stack_4
            level = [stack_1, stack_2, stack_3, stack_4]
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key in [pg.K_w, pg.K_a, pg.K_s, pg.K_d]:
                if pg.K_w and stack_1:
                    distance1 = 648 - stack_1[-1].y
                if pg.K_a and stack_2:
                    distance2 = 648 - stack_2[-1].y
                if pg.K_s and stack_3:
                    distance3 = 648 - stack_3[-1].y
                if pg.K_d and stack_4:
                    distance4 = 648 - stack_4[-1].y
                level = [stack_1, stack_2, stack_3, stack_4]
                print((distance1, distance2, distance3, distance4))
                if distance1 <= 80:
                    score += 10
                elif 80 < distance1 < 150:
                    score += 5
                elif distance2 <= 80:
                    score += 10
                elif 80 < distance2 < 150:
                    score += 5
                elif distance3 <= 80:
                    score += 10
                elif 80 < distance3 < 150:
                    score += 5
                elif distance4 <= 80:
                    score += 10
                elif 80 < distance4 < 150:
                    score += 5

    pg.display.update()
    clock.tick(FPS)

pg.quit()
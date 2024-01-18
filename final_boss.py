import pygame as pg
import random
from marhoun import EndGame


class GuitarHero:

    def __init__(self):
        self.WIDTH, self.HEIGHT = 1400, 700

        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Guitar Hero')

        self.clock = pg.time.Clock()
        self.FPS = 60

        self.running = True

        self.stack_1 = []
        self.stack_2 = []
        self.stack_3 = []
        self.stack_4 = []
        self.level = [self.stack_1, self.stack_2, self.stack_3, self.stack_4]

        self.background = (219, 124, 112)

        self.CREATE_BLOCK_EVENT = pg.USEREVENT + 1
        pg.time.set_timer(self.CREATE_BLOCK_EVENT, 600)

        self.FONT = pg.font.SysFont('Comic Sans', 28)

        self.level_of_fight = 1

    def create_aims(self):
        match self.level_of_fight:
            case 1:
                aims = []
                used_poses = []
                for _ in range(3):
                    pos_x = random.randint(401, 1300)
                    pos_y = random.randint(100, 600)
                    # comparsion = any(
                    #     [False if ((abs(pos_x - i[0]) > 50) and (abs(pos_y - i[1]) > 50)) else True for i in used_poses])
                    while (pos_x, pos_y) in used_poses:
                        pos_x = random.randint(401, 1300)
                        pos_y = random.randint(100, 600)
                    aim = pg.Rect(pos_x, pos_y, 100, 100)
                    used_poses.append((pos_x, pos_y))
                    aims.append(aim)
            case 2:
                aims = []
                used_poses = []
                for _ in range(5):
                    pos_x = random.randint(401, 1300)
                    pos_y = random.randint(100, 600)
                    while (pos_x, pos_y) in used_poses:
                        pos_x = random.randint(401, 1300)
                        pos_y = random.randint(100, 600)
                    aim = pg.Rect(pos_x, pos_y, 100, 100)
                    used_poses.append((pos_x, pos_y))
                    aims.append(aim)
            case 3:
                aims = []
                used_poses = []
                for _ in range(8):
                    pos_x = random.randint(401, 1300)
                    pos_y = random.randint(100, 600)
                    while (pos_x, pos_y) in used_poses:
                        pos_x = random.randint(401, 1300)
                        pos_y = random.randint(100, 600)
                    aim = pg.Rect(pos_x, pos_y, 100, 100)
                    used_poses.append((pos_x, pos_y))
                    aims.append(aim)
            case 4:
                aims = []
                used_poses = []
                for _ in range(10):
                    pos_x = random.randint(401, 1300)
                    pos_y = random.randint(100, 600)
                    while (pos_x, pos_y) in used_poses:
                        pos_x = random.randint(401, 1300)
                        pos_y = random.randint(100, 600)
                    aim = pg.Rect(pos_x, pos_y, 100, 100)
                    used_poses.append((pos_x, pos_y))
                    aims.append(aim)

            case 5:
                aims = []
                used_poses = []
                for _ in range(15):
                    pos_x = random.randint(401, 1300)
                    pos_y = random.randint(100, 600)
                    while (pos_x, pos_y) in used_poses:
                        pos_x = random.randint(401, 1300)
                        pos_y = random.randint(100, 600)
                    aim = pg.Rect(pos_x, pos_y, 100, 100)
                    used_poses.append((pos_x, pos_y))
                    aims.append(aim)

        return aims

    def moving_blocks(self, screen):
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                block = self.level[i][j]
                if block.y >= 626:
                    if i == 0:
                        self.stack_1 = self.stack_1[:-1]
                    elif i == 1:
                        self.stack_2 = self.stack_2[:-1]
                    elif i == 2:
                        self.stack_3 = self.stack_3[:-1]
                    elif i == 3:
                        self.stack_4 = self.stack_4[:-1]
                    self.level = [self.stack_1, self.stack_2, self.stack_3, self.stack_4]
                else:
                    pg.draw.rect(screen, (181, 77, 63), block)
                    self.level[i][j] = block.move(0, 3)

    def create_boss(self):
        match self.level_of_fight:
            case 1:
                df1 = pg.transform.scale(pg.image.load('Sprites/boss/level1/default.png').convert_alpha(),
                                         (500, 500))
                df2 = pg.transform.scale(pg.image.load('Sprites/boss/level1/default2.png').convert_alpha(),
                                         (500, 500))
                dmg = pg.transform.scale(pg.image.load('Sprites/boss/level1/damage.png').convert_alpha(),
                                         (500, 500))
            case 2:
                df1 = pg.transform.scale(pg.image.load('Sprites/boss/level2/default.png').convert_alpha(),
                                         (500, 500))
                df2 = pg.transform.scale(pg.image.load('Sprites/boss/level2/default2.png').convert_alpha(),
                                         (500, 500))
                dmg = pg.transform.scale(pg.image.load('Sprites/boss/level2/damage.png').convert_alpha(),
                                         (500, 500))
            case 3:
                df1 = pg.transform.scale(pg.image.load('Sprites/boss/level3/default.png').convert_alpha(),
                                         (500, 500))
                df2 = pg.transform.scale(pg.image.load('Sprites/boss/level3/default2.png').convert_alpha(),
                                         (500, 500))
                dmg = pg.transform.scale(pg.image.load('Sprites/boss/level3/damage.png').convert_alpha(),
                                         (500, 500))
            case 4:
                df1 = pg.transform.scale(pg.image.load('Sprites/boss/level4/default.png').convert_alpha(),
                                         (500, 500))
                df2 = pg.transform.scale(pg.image.load('Sprites/boss/level4/default2.png').convert_alpha(),
                                         (500, 500))
                dmg = pg.transform.scale(pg.image.load('Sprites/boss/level4/damage.png').convert_alpha(),
                                         (500, 500))
            case 5:
                df1 = pg.transform.scale(pg.image.load('Sprites/boss/level5/default.png').convert_alpha(),
                                         (500, 500))
                df2 = pg.transform.scale(pg.image.load('Sprites/boss/level5/default2.png').convert_alpha(),
                                         (500, 500))
                dmg = pg.transform.scale(pg.image.load('Sprites/boss/level5/damage.png').convert_alpha(),
                                         (500, 500))

        boss_animation = [df1, df2, dmg]
        return boss_animation

    def play(self, goal):
        score = 0
        aims = self.create_aims()
        pg.mouse.set_visible(False)
        crosshair = pg.transform.scale(pg.image.load('Sprites/crosshair.png').convert_alpha(), (32, 32))
        pg.mixer.Channel(0).play(pg.mixer.Sound('Music/final_fight.wav'), -1)
        bg = pg.transform.scale(pg.image.load('Sprites/background_final_fight.png').convert_alpha(), (1000, 700))

        change_boss = pg.USEREVENT + 2
        pg.time.set_timer(change_boss, 400)
        boss_animation = self.create_boss()
        df1 = boss_animation[0]
        df2 = boss_animation[1]
        dmg = boss_animation[2]

        final_animation = False

        while self.running:
            self.screen.fill(self.background)
            self.screen.blit(bg, (401, 0))

            # Edges
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(0, 0, 2, 700))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(99, 0, 2, 700))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(199, 0, 2, 700))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(299, 0, 2, 700))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(398, 0, 2, 700))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(0, 648, 400, 2))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(0, 0, 400, 50))
            score_text = self.FONT.render(str(score), True, (255, 255, 255))
            self.screen.blit(score_text, (400 / 2 - score_text.get_rect().w / 2, 50 / 2 - score_text.get_rect().h / 2))

            # Buttons
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(29, 655, 40, 40))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(129, 655, 40, 40))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(229, 655, 40, 40))
            pg.draw.rect(self.screen, (181, 77, 63), pg.Rect(329, 655, 40, 40))
            letter_W = self.FONT.render('W', True, (255, 255, 255))
            letter_A = self.FONT.render('A', True, (255, 255, 255))
            letter_S = self.FONT.render('S', True, (255, 255, 255))
            letter_D = self.FONT.render('D', True, (255, 255, 255))

            self.screen.blit(letter_W, (38, 658))
            self.screen.blit(letter_A, (140, 658))
            self.screen.blit(letter_S, (240, 658))
            self.screen.blit(letter_D, (340, 658))

            self.screen.blit(boss_animation[0], (700, 100))

            if score < goal:
                for event in pg.event.get():
                    distance1 = 1000
                    distance2 = 1000
                    distance3 = 1000
                    distance4 = 1000
                    if event.type == pg.QUIT:
                        self.running = False
                    if event.type == self.CREATE_BLOCK_EVENT:
                        index = random.choice([0, 1, 2, 3])
                        if index == 0:
                            block = pg.Rect(25, 5, 50, 30)
                            self.stack_1 = [block] + self.stack_1
                        elif index == 1:
                            block = pg.Rect(125, 5, 50, 30)
                            self.stack_2 = [block] + self.stack_2
                        elif index == 2:
                            block = pg.Rect(225, 5, 50, 30)
                            self.stack_3 = [block] + self.stack_3
                        elif index == 3:
                            block = pg.Rect(325, 5, 50, 30)
                            self.stack_4 = [block] + self.stack_4
                        self.level = [self.stack_1, self.stack_2, self.stack_3, self.stack_4]
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.running = False
                        elif event.key in [pg.K_w, pg.K_a, pg.K_s, pg.K_d]:
                            if event.key == pg.K_w and self.stack_1:
                                distance1 = 648 - self.stack_1[-1].y
                            if event.key == pg.K_a and self.stack_2:
                                distance2 = 648 - self.stack_2[-1].y
                            if event.key == pg.K_s and self.stack_3:
                                distance3 = 648 - self.stack_3[-1].y
                            if event.key == pg.K_d and self.stack_4:
                                distance4 = 648 - self.stack_4[-1].y
                            self.level = [self.stack_1, self.stack_2, self.stack_3, self.stack_4]
                            if distance1 <= 80:
                                pg.mixer.Channel(1).play(pg.mixer.Sound('Music/button_true.wav'), 0)
                                score += 10
                            elif 80 < distance1 < 150:
                                pg.mixer.Channel(1).play(pg.mixer.Sound('Music/button_true.wav'), 0)
                                score += 5
                            elif distance2 <= 80:
                                pg.mixer.Channel(1).play(pg.mixer.Sound('Music/button_true.wav'), 0)
                                score += 10
                            elif 80 < distance2 < 150:
                                pg.mixer.Channel(1).play(pg.mixer.Sound('Music/button_true.wav'), 0)
                                score += 5
                            elif distance3 <= 80:
                                pg.mixer.Channel(1).play(pg.mixer.Sound('Music/button_true.wav'), 0)
                                score += 10
                            elif 80 < distance3 < 150:
                                pg.mixer.Channel(1).play(pg.mixer.Sound('Music/button_true.wav'), 0)
                                score += 5
                            elif distance4 <= 80:
                                pg.mixer.Channel(1).play(pg.mixer.Sound('Music/button_true.wav'), 0)
                                score += 10
                            elif 80 < distance4 < 150:
                                pg.mixer.Channel(1).play(pg.mixer.Sound('Music/button_true.wav'), 0)
                                score += 5

                    if event.type == change_boss:
                        if boss_animation[0] != dmg:
                            boss_animation = [boss_animation[1], boss_animation[0], boss_animation[2]]
                        else:
                            boss_animation = [df1, df2, dmg]

                self.moving_blocks(self.screen)

            if score >= goal and aims:
                cr_x, cr_y = pg.mouse.get_pos()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            crosshair = pg.transform.scale(
                                pg.image.load('Sprites/crosshair_hit.png').convert_alpha(), (32, 32))
                            pg.mixer.Channel(1).play(pg.mixer.Sound('Music/rifle.wav'), 0)
                            boss_animation = [dmg, df1, df2]
                            for aim in aims:
                                if aim.x <= cr_x + 16 <= aim.x + 100 and aim.y <= cr_y + 16 <= aim.y + 100:
                                    aims.remove(aim)

                    if event.type == pg.MOUSEBUTTONUP:
                        if event.button == 1:
                            crosshair = pg.transform.scale(pg.image.load('Sprites/crosshair.png').convert_alpha(),
                                                           (32, 32))

                    if event.type == change_boss:
                        if boss_animation[0] != dmg:
                            boss_animation = [boss_animation[1], boss_animation[0], boss_animation[2]]
                        else:
                            boss_animation = [df1, df2, dmg]

                aim_image = pg.transform.scale(pg.image.load('Sprites/aim.png').convert_alpha(), (100, 100))
                for aim in aims:
                    # pg.draw.rect(self.screen, (255, 255, 255), aim)
                    self.screen.blit(aim_image, (aim.x, aim.y))

                if not aims:
                    if self.level_of_fight < 5:
                        self.level_of_fight += 1
                        boss_animation = self.create_boss()
                        df1 = boss_animation[0]
                        df2 = boss_animation[1]
                        dmg = boss_animation[2]
                    else:
                        self.running = False
                        final_animation = True
                    aims = self.create_aims()
                    score = 0
                    goal *= 2

                if cr_x < 401:
                    cr_x = 401
                if cr_x > 1367:
                    cr_x = 1367
                if cr_y > 671:
                    cr_y = 671
                self.screen.blit(crosshair, (cr_x, cr_y))

            pg.display.update()
            self.clock.tick(self.FPS)

        if final_animation:
            e = EndGame()
            e.play()

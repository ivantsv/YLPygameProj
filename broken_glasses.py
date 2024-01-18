import pygame as pg
from Button import Button
from marhoun import Game
from final_boss import GuitarHero


class Point:
    def __init__(self, width=1400, height=700):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.running = True
        # Background
        bg1 = pg.transform.scale(pg.image.load('Sprites/point/background/st1.png'), (1400, 700))
        bg2 = pg.transform.scale(pg.image.load('Sprites/point/background/default.png'), (1400, 700))
        bg3 = pg.transform.scale(pg.image.load('Sprites/point/background/duck_on_head.png'), (1400, 700))
        self.bg_animation = [bg1, bg2, bg3]
        # Agent
        ag_open = pg.transform.scale(pg.image.load('Sprites/point/agent/agent_mouth_open.png'), (300, 300))
        ag_close = pg.transform.scale(pg.image.load('Sprites/point/agent/agent_mouth_close.png'), (300, 300))
        self.agent_animation = [ag_open, ag_close]
        # Dialogues
        self.dialogue1 = [pg.transform.scale(pg.image.load(f'Sprites/point/dialogue/dialogue1/{i}.png'), (200, 200)) for
                          i in
                          range(9)]
        self.dialogue2 = [pg.transform.scale(pg.image.load(f'Sprites/point/dialogue/dialogue2/{i}.png'), (200, 200)) for
                          i in
                          range(1, 8)]
        # Glasses
        self.glasses = pg.image.load('Sprites/glasses.png')
        self.glasses = pg.transform.scale(self.glasses, (self.width + 100, self.height + 40))
        # White noise
        self.WHITE_NOISE_ANIMATION_EVENT = pg.USEREVENT + 1
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
        # Buttons
        button_image = pg.transform.scale(pg.image.load('Sprites/next_level_button.png').convert_alpha(),
                                          (500, 200))
        self.button_restart = Button(button_image, (350, 350), 'Restart', pg.font.SysFont('Fonts/font2.ttf', 48),
                                     (255, 255, 255), (155, 155, 155))
        self.button_turn_off = Button(button_image, (1070, 350), 'Turn Off', pg.font.SysFont('Fonts/font2.ttf', 48),
                                      (255, 255, 255), (155, 155, 155))

    def play(self):
        # change_animation_event = pg.USEREVENT + 1
        # pg.time.set_timer(change_animation_event, 1500)
        pg.mixer.music.load('Music/horror.wav')
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
        bg_slide = 0
        dialogue1_slide = 0
        dialogue_2_slide = 0
        agent_animation = None
        cur_animation_bg = self.bg_animation[bg_slide]
        cur_animation_dg = None
        show_agent = False
        infinity_mode = False
        final_fight = False

        while self.running:
            mouse_clicked = False

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_clicked = True
                    if bg_slide < 2:
                        bg_slide += 1
                        cur_animation_bg = self.bg_animation[bg_slide]
                    else:
                        show_agent = True
                        if dialogue1_slide < 9:
                            cur_animation_dg = self.dialogue1[dialogue1_slide]
                            dialogue1_slide += 1
                        else:
                            if dialogue_2_slide < 7:
                                cur_animation_dg = self.dialogue2[dialogue_2_slide]
                                dialogue_2_slide += 1
                            else:
                                cur_animation_dg = None
                                show_agent = False
                                self.white_noise_animation = True
                        if show_agent:
                            agent_animation = self.agent_animation[0]
                            self.agent_animation = self.agent_animation[::-1]
                if event.type == self.WHITE_NOISE_ANIMATION_EVENT and self.white_noise_animation:
                    self.wn_animation = self.wn_animation[1:] + [self.wn_animation[0]]

            self.screen.blit(cur_animation_bg, (0, 0))
            if show_agent:
                self.screen.blit(agent_animation, (1000, 200))
                self.screen.blit(cur_animation_dg, (900, 100))

            if self.white_noise_animation:
                self.screen.blit(self.wn_animation[0], (0, 0))
                self.button_restart.update(self.screen)
                self.button_turn_off.update(self.screen)
                self.button_restart.changeColor(pg.mouse.get_pos())
                self.button_turn_off.changeColor(pg.mouse.get_pos())
                if mouse_clicked:
                    if self.button_restart.checkForInput(pg.mouse.get_pos()):
                        infinity_mode = True
                        self.running = False
                    if self.button_turn_off.checkForInput(pg.mouse.get_pos()):
                        final_fight = True
                        pg.mixer.music.stop()
                        self.running = False

            self.screen.blit(self.glasses, (-50, -20))
            pg.display.update()
            self.clock.tick(self.FPS)

        if infinity_mode:
            g = Game(-1, 15, None)
            g.play()
        if final_fight:
            fb = GuitarHero()
            fb.play(25)

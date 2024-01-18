import pygame as pg


class Tutorial:
    def play(self, next_stage, width=1400, height=700):
        pg.mixer.music.load('Music/tutorial.mp3')
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
        tutorial_animation = []
        # change_sprite_event = pg.USEREVENT + 1
        # pg.time.set_timer(change_sprite_event, 500)
        running = True
        screen = pg.display.set_mode((width, height))
        clock = pg.time.Clock()
        fps = 60

        for i in range(1, 38):
            sprite = pg.transform.scale(pg.image.load(f'Sprites/frames/{i}.png').convert_alpha(), (1400, 700))
            tutorial_animation.append(sprite)

        pg.mouse.set_visible(True)

        start_first_level = False

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if len(tutorial_animation) >= 2:
                            tutorial_animation = tutorial_animation[1:]
                        else:
                            running = False
                            start_first_level = True

            screen.blit(tutorial_animation[0], (0, 0))
            pg.display.flip()
            pg.display.update()
            clock.tick(fps)

        if start_first_level:
            pg.mixer.music.stop()
            next_stage.play()

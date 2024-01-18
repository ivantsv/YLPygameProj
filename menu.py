import pygame
import sys
from Button import Button
from Tutorial import Tutorial
from marhoun import Game, EndGame, EndLevel
from final_boss import GuitarHero
from broken_glasses import Point

pygame.init()
SCREEN = pygame.display.set_mode((1400, 700))
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Background.jpeg")
BG = pygame.transform.scale(BG, (1400, 700))



def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        game_mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")
        play_text = get_font(45).render("Game is gonna be here soon.", True, "White")
        play_rect = play_text.get_rect(center=(700, 350))
        SCREEN.blit(play_text, play_rect)
        play_back = Button(image=None, pos=(700, 550),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        play_back.changeColor(game_mouse_pos)
        play_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(game_mouse_pos):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(700, 200),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(700, 500),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [play_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    pygame.display.set_caption('Kill them all')
                    tutorial = Tutorial()
                    tutorial.play(Game(1, 5, Game(1, 10, Game(1, 15, Game(1, 20, Point())))))
                    pygame.quit()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()

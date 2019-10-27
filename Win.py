import pygame, time
import threading
import sp_mp, Settings

def CreateGameWindow(width, height):
    pygame.display.set_caption("Checkers !")
    gameWindow = pygame.display.set_mode((width, height))
    return gameWindow

def WriteText(text, text_pos_x, text_pos_y, text_size):
    text_font = pygame.font.SysFont(None, text_size)
    text_render = text_font.render(text, True, Black)
    gameWindow.blit(text_render, (text_pos_x, text_pos_y))

class CreateButton():
    def layout(self,button):
        pygame.draw.rect(gameWindow, button[4], (button[0], button[1], button[2], button[3]))

    def text(self, button, space_x, space_y):
        WriteText(button[5], button[0] + space_x, button[1] + space_y, button[6])

    def Animate(self, button, actual_color, animate_color):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= button[0] and mouse_y >= button[1] and mouse_x <= button[0] + button[2] and mouse_y <= button[1] + button[3]:
            button[7] += 1
            if button[7] == 1:
                button[6] += 1
            button[4] = animate_color
        else:
            button[4] = actual_color
            button[6] = 30
            button[7] = 0

#Colors:
White = (255,255,255)
Black = (0,0,0)
Gray = (128,128,128)
LightWhite = (160,160,160)
LightGreen = (0,210,0)
BrightGreen = (0,255,0)
LightRed = (150,0,0)
BrightRed = (255,0,0)
LightBlue = (0,0,200)
BrightBlue = (0,0,255)

#Dimensions:
gameWindow_width = 680
gameWindow_height = 680

gameWindow = CreateGameWindow(gameWindow_width,gameWindow_height)

def ShowWinner(Player):
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        gameWindow.fill(Gray)

        player_details = [250, gameWindow_height/2 - 100, 260 ,500, LightGreen, Player, 30, 0]

        createButton = CreateButton()
        #createButton.layout(player_details)
        createButton.text(player_details, 56, 20)

        pygame.display.update()

        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()

ShowWinner('player 1')
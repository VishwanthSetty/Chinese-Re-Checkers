import pygame, time
import virtual_start_page
import two_players

def CreateGameWindow(width, height):
    pygame.display.set_caption("Checkers !")
    gamewindow = pygame.display.set_mode((width, height))
    return gamewindow

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

pygame.init()

#Colors:
White = (255,255,255)
LightWhite = (200,200,200)
Black = (0,0,0)
Gray = (128,128,128)
LightGreen = (0,200,0)
BrightGreen = (0,255,0)
LightBlue = (0,0,200)
BrightBlue = (0,0,255)

#Dimensions:
gameWindow_width = 680
gameWindow_height = 680

#-------------Lists of properties of Buttons------
twoPlayers = [gameWindow_width/4 - 60, gameWindow_height/3 + 60 , 200, 50, LightGreen, "Two Players", 30, 0]
team_play = [gameWindow_width/4 + 270 - 80, gameWindow_height/3 + 60, 200, 50, LightGreen, "Team Play", 30, 0]
back = [10, gameWindow_height - 80, 160, 50, Black, "Back", 30, 0]

gameWindow = CreateGameWindow(gameWindow_width, gameWindow_height)
#pygame.display.set_caption("Checkers")
#gameWindow = pygame.display.set_mode((gameWindow_width,gameWindow_height))

def Run_Game():
    End = False

    while not End:
        gameWindow.fill(LightWhite)

        WriteText("PLAY", 210, 100, 150)

        createButton = CreateButton()

        createButton.layout(twoPlayers)
        createButton.text(twoPlayers, 36, 16)
        createButton.Animate(twoPlayers, LightGreen, BrightGreen)

        createButton.layout(team_play)
        createButton.text(team_play, 45, 16)
        createButton.Animate(team_play, LightGreen, BrightGreen)

        createButton.layout(back)
        createButton.text(back, 55, 16)
        createButton.Animate(back, LightWhite, Gray)

        #On_Click_Back_Button(back)

        for key in pygame.event.get():
            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_ESCAPE:
                    End = True
                    pygame.quit()

            if key.type == pygame.QUIT:
                pygame.quit()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if key.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= back[0] and mouse_y >= back[1] and mouse_x <= back[0] + back[2] and mouse_y <= back[1] + back[3]:
                    return

                if mouse_x >= twoPlayers[0] and mouse_y >= twoPlayers[1] and mouse_x <= twoPlayers[0] + twoPlayers[2] \
                    and mouse_y <= twoPlayers[1] + twoPlayers[3]:
                    two_players.StartSinglePlayer(0, 0, 0)

        pygame.display.update()

#Run_Game()

#pygame.quit()
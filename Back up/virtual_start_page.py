import pygame, time
import sp_mp

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

class CreateImage():
    def play(self, image):
        pygame.draw.rect(gameWindow, image[0][4], (image[0][0], image[0][1], image[0][2], image[0][3]))
        pygame.draw.rect(gameWindow, image[1][4], (image[1][0], image[1][1], image[1][2], image[1][3]))
        pygame.draw.polygon(gameWindow, image[2][3], (image[2][0], image[2][1], image[2][2]))

    def Animate(self, image, button, actual_color1, actual_color2, actual_color3, animate_color1, animate_color2, animate_color3):
        for mouse in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #if mouse.type == pygame.MOUSEBUTTONDOWN:
            if mouse_x >= image[0][0] and mouse_y >= image[0][1] and mouse_x <= image[0][0] + image[0][2] and mouse_y <= image[0][1] + image[0][2]\
                    or mouse_x >= button[0] and mouse_y >= button[1] and mouse_x <= button[0] + button[2] and mouse_y <= button[1] + button[3]:
                image[0][4] = animate_color1
                image[1][4] = animate_color2
                image[2][3] = animate_color3
                button[7] += 1
                if button[7] == 1:
                    button[6] += 1
                button[4] = animate_color1
            else:
                image[0][4] = actual_color1
                image[1][4] = actual_color2
                image[2][3] = actual_color3
                button[4] = actual_color1
                button[6] = 30
                button[7] = 0

pygame.init()

#Colors:
White = (255,255,255)
Black = (0,0,0)
Gray = (128,128,128)
LightWhite = (160,160,160)
LightGreen = (0,200,0)
BrightGreen = (0,255,0)
LightRed = (150,0,0)
BrightRed = (255,0,0)
LightBlue = (0,0,200)
BrightBlue = (0,0,255)

#Dimensions:
gameWindow_width = 680
gameWindow_height = 680

#---------------Lists of Properties of all buttons--------------
play = [60, gameWindow_height/3 + 130, 200 ,60, LightGreen, "Play", 30, 0]
play_image = [[5, gameWindow_height/3 + 119, 78, 78, LightGreen, BrightGreen, 0], [12, gameWindow_height / 3 + 126, 64, 64, LightWhite, Gray],
              [(20, gameWindow_height / 3 + 132), (66, gameWindow_height / 3 + 158), (20, gameWindow_height / 3 + 183), LightGreen, BrightGreen]]
settings = [60, gameWindow_height/3 + 80 + 130, 200 ,60, LightBlue, "Settings", 30, 0]
quit = [60, gameWindow_height/3 + 160 + 130, 200 ,60, LightRed, "Quit Game", 30, 0]


gameWindow = CreateGameWindow(gameWindow_width,gameWindow_height)

def start_game():
    End = False

    while not End:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        gameWindow.fill(Gray)

        #-----------Classes Assignment--------
        createButton = CreateButton()
        createImage = CreateImage()

        #-----------Creating Play Button------
        createButton.layout(play)
        createButton.text(play, 79, 20)
        createImage.play(play_image)
        createImage.Animate(play_image, play, LightGreen, LightWhite, LightGreen, BrightGreen, White, BrightGreen)

        createButton = CreateButton()
        createButton.layout(settings)
        createButton.text(settings, 56, 20)

        createButton = CreateButton()
        createButton.layout(quit)
        createButton.text(quit, 49, 20)

        for key in pygame.event.get():

            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_ESCAPE:
                    End = True
                    pygame.quit()

            if key.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= play[0] and mouse_y >= play[1] and mouse_x <= play[0] + play[2] and mouse_y <= play[1] + play[3]:
                    #play_button_pos_y += 100
                    #import sp_mp
                    sp_mp.Run_Game()
                    #End = True

                if mouse_x >= settings[0] and mouse_y >= settings[1] and mouse_x <= settings[0] + settings[2] and mouse_y <= settings[1] + settings[3]:
                    #End = True
                    import Settings

                if mouse_x >= quit[0] and mouse_y >= quit[1] and mouse_x <= quit[0] + quit[2] and mouse_y <= quit[1] + quit[3]:
                    # quit_button_pos_y += 100
                    End = True
                    pygame.quit()

    #------------------------------  Play Button Animation----------------------

            #createButton.Animate(play, LightGreen, BrightGreen)

    # -------------------------------- Settings Button Animation------------------

            createButton.Animate(settings, LightBlue, BrightBlue)

    # ----------------------------------------------------------------------------
    # ------------------------------  Quit Button Animation----------------------

            createButton.Animate(quit, LightRed, BrightRed)

    #----------------------------------------------------------------------------

        pygame.display.update()

#pygame.quit()
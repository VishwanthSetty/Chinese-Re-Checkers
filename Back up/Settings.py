import pygame, random
import virtual_start_page

def CreateGameWindow(width, height):
    pygame.display.set_caption("Checkers !")
    gameWindow = pygame.display.set_mode((width, height))
    return gameWindow

def WriteText(text, text_pos_x, text_pos_y, text_size):
    text_font = pygame.font.SysFont(None, text_size)
    text_render = text_font.render(text, True, Black)
    gameWindow.blit(text_render, (text_pos_x, text_pos_y))

#def Get_Default_Values():

def RestoreDefaults(create_value_Button):
    volume_settings[5] = default_volume_value
    create_value_Button.Set_Value(volume_settings)


class CreateGif():
    def volume(self,gif):
        x = 5
        dx = gif[2]/60
        #pygame.draw.rect(gameWindow, gif[4], (gif[0], gif[1], gif[2], -gif[3]))
        while x <= gif[2]:
            pygame.draw.rect(gameWindow, gif[4], (x, gif[1] + gif[3], dx, -(random.randint(5,60))))
            x += dx

    def brightness(self, gif):
        x = 5
        dx = gif[2]/60
        color = [255,255,255]
        while color[0] > 0 or x < gif[2] - 90:
            pygame.draw.rect(gameWindow, color, (x, gif[1] + gif[3], dx, -gif[3]))
            color[0] -= 4.4
            color[1] -= 4.4
            color[2] -= 4.4
            x += dx

    def text(self, gif, space_x, space_y):
        WriteText(gif[5], gif[0] + space_x, gif[1] + space_y, gif[6])

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

class Create_Value_Button():
    def layout(self, button):
        pygame.draw.line(gameWindow, LightWihte, (button[0], button[1] + button[3]/2 + 10), (button[0] + button[2], button[1] + button[3]/2 + 10))

    def Set_Value(self, button):
        pygame.draw.rect(gameWindow, Black, (button[5], ((button[1] + button[3] + 5) - button[1] + button[3]/2 + 16 + (button[5] - button[0])/10) + 8, 10, -(button[5] - button[0])/5))


def get_user_desired_value(setting):
    for mouse in pygame.event.get():
        if mouse.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= setting[0] and mouse_y >= setting[1] and mouse_x <= setting[0] + setting[2] and mouse_y <= setting[1] + setting[3]:
                volume_value = mouse_x

def On_Click_Back_Button(back_button, end):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.event.get() == pygame.MOUSEBUTTONDOWN:
        if mouse_x >= back_button[0] and mouse_y >= back_button[1] and mouse_x <= back_button[0] + back_button[2] and mouse_y <= back_button[1] + back_button[3]:
            import startpage
            end = True

        else:
            end = False
    return end


pygame.init()

#Colors:
White = (255,255,255)
LightWihte = (200,200,200)
Gray = (128,128,128)
Black =(0,0,0)

#Dimensions:
gameWindow_width = 680
gameWindow_height = 680

#Default_Values:
default_volume_value = 500

#-------------------Lists of Properties of all buttons---------
volume = [10, gameWindow_height/10, gameWindow_width/3 + 50, 60, LightWihte, "Volume", 30, 0]
volume_settings = [volume[2] + 80, volume[1], volume[2] + 30, 50, Black, 500]
brightness = [10, gameWindow_height/10 + 120, gameWindow_width/3 + 50, 60, LightWihte, "Brightness", 30, 0]
restore = [gameWindow_width - 220, gameWindow_height - 80, 210, 50, Black, "Restore Defaults", 30, 0]
back = [10, gameWindow_height - 80, 160, 50, Black, "Back", 30, 0]


gameWindow = CreateGameWindow(gameWindow_width,gameWindow_height)

def Run_settings():
    End = False

    while not End:
        gameWindow.fill(Gray)
        #------Declarartion of classes-----
        createGif = CreateGif()
        create_value_Button = Create_Value_Button()
        createButton = CreateButton()

        #------Creating Volume Gifs--------
        createGif.volume(volume)
        createGif.text(volume, 100, 20)

        #get_user_desired_value(volume)

        create_value_Button.layout(volume_settings)
        create_value_Button.Set_Value(volume_settings)

        #------Creating brightness Gifs------
        createGif.brightness(brightness)
        createGif.text(brightness, 80, 20)

        #---------Creating Back Button-------
        createButton.layout(back)
        createButton.text(back, 60, 15)
        createButton.Animate(back, LightWihte, White)

        #---------Creating Restore Defaults Button---------
        createButton.layout(restore)
        createButton.text(restore, 22, 15)
        createButton.Animate(restore, LightWihte, White)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for key in pygame.event.get():

            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_ESCAPE:
                    End = True

            if key.type == pygame.QUIT:
                End = True

            if key.type == pygame.MOUSEBUTTONDOWN:

                # --------On Click Back Button-------
                if mouse_x >= back[0] and mouse_y >= back[1] and mouse_x <= back[0] + back[2] and mouse_y <= back[1] + back[3]:
                    virtual_start_page.start_game()

                # --------On Click Restore Button-------
                if mouse_x >= restore[0] and mouse_y >= restore[1] and mouse_x <= restore[0] + restore[2] and mouse_y <= restore[1] + restore[3]:
                    RestoreDefaults(create_value_Button)

                #---------Changing volume------------
                if mouse_x >= volume_settings[0] and mouse_y >= volume_settings[1] and mouse_x <= volume_settings[0] + volume_settings[2] - 4 and mouse_y <= volume_settings[1] + volume_settings[3]:
                    volume_settings[5] = mouse_x

        #End = On_Click_Back_Button(back, End)

        pygame.display.update()

#Run_settings()
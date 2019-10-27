import pygame
import sp_mp
import two_players

def create_game_window(width, height):
    pygame.display.set_caption("Type your name ")
    gameWindow = pygame.display.set_mode((width, height))
    return gameWindow

def mouse_pos_on_butt(button):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x >= button[0] and mouse_x <= button[0] + button[2] and mouse_y >= button[1] and mouse_y <= button[1] + button[3]:
        return 1
    else:
        return 0

def WriteText(text):
    text_font = pygame.font.SysFont(None, text[2])
    text_render = text_font.render(text[3], True, text[4])
    game_window.blit(text_render, (text[0], text[1]))

class create_buttons():
    def create_button(self, button, button_text):
        pygame.draw.rect(game_window, button[4], (button[0], button[1], button[2], button[3]))
        WriteText(button_text)

    def button_animation(self, button, actual_color, animate_color):
        if mouse_pos_on_butt(button):
            button[4] = animate_color
        else:
            button[4] = actual_color

def create_name_box():
    pygame.draw.rect(game_window, name_box[4], (name_box[0] - 1, name_box[1] - 1, name_box[2] + 2, name_box[3] + 2))
    pygame.draw.rect(game_window, name_box[5], (name_box[0], name_box[1], name_box[2], name_box[3]))

def typing():
    pygame.draw.rect(game_window, type_blink[4], (type_blink[0], type_blink[1], type_blink[2], type_blink[3]))

def type_name():
    for key in pygame.event.get():
        if key.type == pygame.KEYDOWN:
            if key.key == pygame.K_RETURN:
                print(name[3])
                name[3] = ''

            if key.unicode in alphabets:
                name[3] += key.unicode
                type_blink[0] += 13
            else:
                if key.key == pygame.K_BACKSPACE:
                    if name[3] != '':
                        type_blink[0] -= 13
                        name[3] = name[3][:-1]

#Colors:
White = (255, 255, 255)
LightBlack = (50, 50, 50)
Black = (0, 0, 0)
LightWhite = (200, 200, 200)
Gray = (128, 128, 128)
LightGray = (100, 100, 100)
Red = (255, 0, 0)
Blue = (0, 0, 255)
LightBlue = (0, 0, 200)
LightGreen = (0, 200, 0)
Green = (0, 220, 0)
LightRed = (150, 0, 0)

#Lists of Details:
game_window_width = 680
game_window_height = 680
name_box = [200, 300, 300, 40, Black, White]
back_button = [30, 615, 135, 45, LightGreen]
confirm_button = [590, 620, 100, 35, LightGreen]
name_x = 208
name_y = 303
name = [name_x, name_y, 30, '', Black]
type_blink = [208, 303, 1, 34, Black]
blink = 0
type = 1

#Texts:
back_text = [68, 625, 35, "Back", LightWhite]
confirm_text = [600, 625, 30, "Confirm", LightWhite]
alphabets = []
for i in range(65, 91):
    alphabets.append(chr(i))
for i in range(97, 123):
    alphabets.append(chr(i))

print(alphabets)

pygame.init()

game_window = create_game_window(game_window_width, game_window_height)

def start_typing_name(blink, type):
    while True:
        game_window.fill(LightWhite)

        create_name_box()

        if type == 1:
            typing()
            type_name()

        WriteText(name)

        #------------------------Declaring classes-----------
        create_button = create_buttons()

        #-----------------------Creating buttons-------------
        create_button.create_button(back_button, back_text)

        #-----------------------Creating animations----------
        create_button.button_animation(back_button, LightGreen, Green)

        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()

            if key.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_on_butt(name_box):
                    type = 1
                else:
                    type = 0

        pygame.display.update()

start_typing_name(blink, type)
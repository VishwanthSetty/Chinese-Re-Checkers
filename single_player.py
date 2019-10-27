import pygame, random

def sqrt(x):
    return x ** (1/2)

def create_game_window(width, height):
    pygame.display.set_caption("Game!")
    window = pygame.display.set_mode((width, height))
    return window

class create_obj():
    def layout(self, obj_back):
        pygame.draw.circle(game_window, obj_back[4], (obj_back[0], obj_back[1]), obj_back[2])
        pygame.draw.circle(game_window, obj_back[5], (obj_back[0], obj_back[1]), obj_back[3])

    def Animate(self, i, actual_color1, actual_color2, animate_color1, animate_color2):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if sqrt((game_objs[i][0] - mouse_x) ** 2 + (game_objs[i][1] - mouse_y) ** 2) <= game_objs[i][2]:
            game_objs[i][4] = animate_color1
            game_objs[i][5] = animate_color2

        else:
            game_objs[i][4] = actual_color1
            game_objs[i][5] = actual_color2


def make_animation(k, animate_color1, animate_color2):
    game_objs[k][4] = animate_color1
    game_objs[k][5] = animate_color2

def remove_animation(k):
    game_objs[k][4] = LightBlack
    game_objs[k][5] = LightGray

def on_click_animate(k, animate_color1, animate_color2, count):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if sqrt((game_objs[k][0] - mouse_x) ** 2 + (game_objs[k][1] - mouse_y) ** 2) <= game_objs[k][2]:
        count = k
        #if k >= 1:
        if k % 12 != 0:
            make_animation(k - 1, animate_color1, animate_color2)
        #make_animation(k, animate_color1, animate_color2)
        if (k + 1) % 12 != 0:
            make_animation(k + 1, animate_color1, animate_color2)
        #if (k+12) % 11 != 0:
        make_animation(k + 12, animate_color1, animate_color2)
        #if k % 12 != 0:
        make_animation(k - 12, animate_color1, animate_color2)
        if k % 12 != 0:
            make_animation(k + 11, animate_color1, animate_color2)
        if (k+13) % 12 != 0:
            make_animation(k + 13, animate_color1, animate_color2)
        if (k-11) % 12 != 0:
            make_animation(k - 11, animate_color1, animate_color2)
        if k % 12 != 0:
            make_animation(k - 13, animate_color1, animate_color2)

def on_click_obj():
    count = 0
    for k in range(0, 144):
        on_click_animate(k, Red, Blue, count)

def add_coins():
    for i in range(0,24):
        game_objs[i][5] = Blue

#Colors:
White = (255,255,255)
LightBlack = (50,50,50)
Black = (0,0,0)
LightWhite = (200,200,200)
Gray = (128,128,128)
LightGray = (100, 100 ,100)
Red = (255,0,0)
Blue = (0,0,255)

#Dimensions:
game_window_width = 600
game_window_height = 600
game_obj_back = [30, 30, 20, Gray]
game_obj_front = [30, 30, 15, Black]
game_objs = []
x_init = 30
y_init = 30

#--------------------------Creating List of Game Objects-----

for i in range(0, 144):
    x = x_init
    for j in range(0, 12):
        game_objs.append([x_init, y_init, 20, 15, LightBlack, LightGray])
        x_init += 49
    x_init = x
    y_init += 49

#------------------------------------------------------------

#add_coins()

var = 0

pygame.init()

game_window = create_game_window(game_window_width, game_window_height)

def StartSinglePlayer(var):
    while True:
        game_window.fill(LightWhite)

        #--------------Declaring class---------------
        createobj = create_obj()

        #--------------Creating Objects--------------
        for i in range(0, 144):
            createobj.layout(game_objs[i])

        #--------------------------------------------

        #--------------Mouseover Animation-----------
        if var == 0:
            for i in range(0, 144):
                createobj.Animate(i, LightBlack, LightGray, Black, Gray)

        #--------------------------------------------

        for key in pygame.event.get():
            #------------------Animation on click object--------------
            if key.type == pygame.MOUSEBUTTONDOWN:
                if var == 1:
                    var = 0
                else:
                    var = 1
                on_click_obj()

            #---------------------------------------------------------

            #if key.type == pygame.MOUSEBUTTONUP:
             #   var = 0

            #-----------------Exiting Condition-----------------------
            if key.type == pygame.QUIT:
                pygame.quit()

            #---------------------------------------------------------

        pygame.display.update()

#StartSinglePlayer(var)
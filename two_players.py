import pygame
import sp_mp
#import leaderboard.py

def sqrt(x):
    return x ** (1/2)

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def create_game_window(width, height):
    pygame.display.set_caption("Game!")
    window = pygame.display.set_mode((width, height))
    return window

def WriteText(text):
    text_font = pygame.font.SysFont(None, text[2])
    text_render = text_font.render(text[3], True, text[4])
    game_window.blit(text_render, (text[0], text[1]))

class create_obj():
    def layout(self, obj_back):
        pygame.draw.circle(game_window, obj_back[4], (obj_back[0], obj_back[1]), obj_back[2])
        pygame.draw.circle(game_window, obj_back[5], (obj_back[0], obj_back[1]), obj_back[3])

    def Animate(self, i, actual_color1, actual_color2, animate_color1, animate_color2):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if distance(game_objs[i][0], game_objs[i][1], mouse_x, mouse_y) <= game_objs[i][2]:
            game_objs[i][4] = animate_color1
            game_objs[i][5] = animate_color2

        else:
            game_objs[i][4] = actual_color1
            game_objs[i][5] = actual_color2

class create_margins():
    def horizantal(self):
        pygame.draw.line(game_window, horizantal_margin[2], horizantal_margin[0], horizantal_margin[1])

    def vertical(self):
        pygame.draw.line(game_window, vertical_margin[2], vertical_margin[0], vertical_margin[1])

class create_buttons():
    def replay_back(self):
        pygame.draw.circle(game_window, replay_button[4], (replay_button[0], replay_button[1]), replay_button[2])
    
    def replay_front(self):
        pygame.draw.circle(game_window, replay_button[5], (replay_button[0], replay_button[1]), replay_button[2] - 8)

    def replay_triangle(self):
        pygame.draw.polygon(game_window, replay_button[4], (replay_button[3][0], replay_button[3][1], replay_button[3][2]))

    def replay_correct(self):
        pygame.draw.circle(game_window, replay_button_cover[3], (replay_button_cover[0], replay_button_cover[1]), replay_button_cover[2])

    def score(self,player1,player2):
        WriteText([400,game_window_height-60,30,'Player 1 score:' + str(player1),Blue])
        WriteText([400,game_window_height-30,30,'player 2 score:'+str(player2),Blue])

    def pause_button(self):
        pygame.draw.rect(game_window, pause_button[4], (pause_button[0], pause_button[1], pause_button[2], pause_button[3]))
        pygame.draw.rect(game_window, pause_button[4], (pause_button[0] + 29, pause_button[1], pause_button[2], pause_button[3]))

    def pause_board(self):
        pygame.draw.rect(game_window, pause_board[4], (pause_board[0] - 3, pause_board[1] - 0.5, pause_board[2] + 4, pause_board[3] + 3.5))
        pygame.draw.rect(game_window, pause_board[5], (pause_board[0], pause_board[1], pause_board[2], pause_board[3]))

    def quit_button(self):
        pygame.draw.polygon(game_window, quit_button[2], (quit_button[0][0], quit_button[0][1], quit_button[0][2], quit_button[0][3]))
        pygame.draw.polygon(game_window, quit_button[2], (quit_button[1][0], quit_button[1][1], quit_button[1][2], quit_button[1][3]))

    def quit_board(self):
        pygame.draw.rect(game_window, quit_board[4], (quit_board[0] - 3, quit_board[1] - 0.5, quit_board[2] + 4, quit_board[3] + 3.5))
        pygame.draw.rect(game_window, quit_board[5], (quit_board[0], quit_board[1], quit_board[2], quit_board[3]))

    def yes_button(self):
        pygame.draw.rect(game_window, yes_button[4], (yes_button[0], yes_button[1], yes_button[2], yes_button[3]))

    def no_button(self):
        pygame.draw.rect(game_window, no_button[4], (no_button[0], no_button[1], no_button[2], no_button[3]))

    def PlayerTurn(self,player_no):
        if(player_no == 1):
            WriteText([100, game_window_height - 60, 45, 'Player 1\'s Turn', Blue])
        else:
            WriteText([100, game_window_height - 60, 45, 'Player 2\'s Turn', Yellow])

    def resume_button(self):
        pygame.draw.rect(game_window, resume_button[4], (resume_button[0], resume_button[1], resume_button[2], resume_button[3]))

    def replay_Animate(self, actual_color, animate_color):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if distance(replay_button[0], replay_button[1], mouse_x, mouse_y) <= replay_button[2]:
            replay_button[4] = animate_color
        else:
            replay_button[4] = actual_color

    def pause_Animate(self, actual_color, animate_color):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= pause_button[0] - 12 and mouse_x <= pause_button[0] + 41 and mouse_y >= pause_button[1] - 8 and mouse_y <= pause_button[1] + 58:
            pause_button[4] = animate_color
        else:
            pause_button[4] = actual_color

    def quit_animate(self, actual_color, animate_color):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= 600 and mouse_x <= 655 and mouse_y >= 605 and mouse_y <= 650:
            quit_button[2] = animate_color
        else:
            quit_button[2] = actual_color

    def button_animate(self, button):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= button[0] and mouse_x <= button[0] + button[2] and mouse_y >= button[1] and mouse_y <= button[1] + button[3]:
            pygame.draw.rect(game_window, LightGray, (button[0] - 1.5, button[1] + 1.5, button[2], button[3] + 1.5))
            pygame.draw.rect(game_window, button[4], (button[0], button[1], button[2], button[3]))

def create_game_objs_list(x_init, y_init):
    for i in range(0, 144):
        if i % 12 == 0:
            x = x_init
            y = y_init
        if i in player1_pos:
            game_objs.append([x_init, y_init, 20, 15, LightBlack, LightBlue])
        else:
            if i in player2_pos:
                game_objs.append([x_init, y_init, 20, 15, LightBlack, Yellow])
            else:
                game_objs.append([x_init, y_init, 20, 15, LightBlack, LightGray])
        x_init += 49
        if (i + 1) % 12 == 0:
            x_init = x
            y_init += 49

def create_player1_pos():
    for i in range(0, 24):
        player1_pos.append(i)

def create_player2_pos():
    for i in range(120, 144):
        player2_pos.append(i)

def mouse_click_on_obj():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(0, 144):
        if distance(game_objs[i][0], game_objs[i][1], mouse_x, mouse_y) <= game_objs[i][2]:
            return 1, i
    return -1, -1

def make_animation(k, animate_color1, animate_color2):
    game_objs[k][4] = animate_color1
    game_objs[k][5] = animate_color2

def remove_animation(k):
    game_objs[k][4] = LightBlack
    game_objs[k][5] = LightGray

def on_click_animate(k, animate_color1, animate_color2, player_pos, opponent_pos):
    #Left
    if k % 12 != 0 and (k - 1) >= 0 and (k - 1) not in player_pos:
        if (k - 1) in opponent_pos:
            #make_animation(k - 1, animate_color1, Red)
            #opponents.append(k - 1)
            if k-1 %12 != 0 and (k-2) >= 0 and (k-2) not in player1_pos and (k-2) not in player2_pos:
                make_animation(k - 2, animate_color1, animate_color2)
                make_animation(k - 1, animate_color1, Red)
                opponents.append(k - 1)
                game_obj_possible_pos.append(k - 2)
        else:
            make_animation(k - 1, animate_color1, animate_color2)
            game_obj_possible_pos.append(k-1)
    #Right
    if (k + 1) % 12 != 0 and (k + 1) <= 143 and (k + 1) not in player_pos:
        if (k + 1) in opponent_pos:
            #make_animation(k + 1, animate_color1, Red)
            #opponents.append(k + 1)
            if k+2 % 12 != 0 and k+2 <= 143 and (k+2) not in player2_pos and (k+2) not in player1_pos:
                make_animation(k + 2, animate_color1, animate_color2)
                make_animation(k + 1, animate_color1, Red)
                opponents.append(k + 1)
                game_obj_possible_pos.append(k + 2)
        else:
            make_animation(k + 1, animate_color1, animate_color2)
            game_obj_possible_pos.append(k + 1)
    #Down
    if (k + 12) <= 143 and (k + 12) not in player_pos:
        if (k + 12) in opponent_pos:
            #make_animation(k + 12, animate_color1, Red)
            #opponents.append(k + 12)
            if k + 24 <= 143 and (k + 24) not in player1_pos and (k+24) not in player2_pos:
                make_animation(k + 12, animate_color1, Red)
                opponents.append(k + 12)
                game_obj_possible_pos.append(k + 24)
                make_animation(k + 24, animate_color1, animate_color2)
        else:
            make_animation(k + 12, animate_color1, animate_color2)
            game_obj_possible_pos.append(k + 12)
    #Up
    if (k - 12) >= 0 and (k - 12) not in player_pos:
        if (k - 12) in opponent_pos:
            #make_animation(k - 12, animate_color1, Red)
            #opponents.append(k - 12)
            if k-24 >= 0 and (k-24) not in player2_pos and (k-24) not in player1_pos:
                make_animation(k - 12, animate_color1, Red)
                opponents.append(k - 12)
                make_animation(k - 24, animate_color1, animate_color2)
                game_obj_possible_pos.append(k - 24)
        else:
            make_animation(k - 12, animate_color1, animate_color2)
            game_obj_possible_pos.append(k - 12)
    #DownLeft
    if k % 12 != 0 and (k + 11) <= 143 and (k + 11) not in player_pos:
        if (k + 11) in opponent_pos:
            #make_animation(k + 11, animate_color1, Red)
            #opponents.append(k + 11)
            if k-1 % 12 != 0 and (k+22) <=143 and (k+22) not in player1_pos and (k+22) not in player2_pos:
                make_animation(k + 11, animate_color1, Red)
                opponents.append(k + 11)
                make_animation(k + 22, animate_color1, animate_color2)
                game_obj_possible_pos.append(k + 22)
        else:
            make_animation(k + 11, animate_color1, animate_color2)
            game_obj_possible_pos.append(k + 11)
    #DownRight
    if (k + 13) % 12 != 0 and (k + 13) <= 143 and (k + 13) not in player_pos:
        if (k + 13) in opponent_pos:
            #make_animation(k + 13, animate_color1, Red)
            #opponents.append(k + 13)
            if k+2 % 12 != 0 and k+26 <= 143 and (k+26) not in player2_pos and (k+26) not in player1_pos:
                make_animation(k + 13, animate_color1, Red)
                opponents.append(k + 13)
                make_animation(k + 26, animate_color1, animate_color2)
                game_obj_possible_pos.append(k + 26)
        else:
            make_animation(k + 13, animate_color1, animate_color2)
            game_obj_possible_pos.append(k + 13)
    #UpRight
    if (k - 11) % 12 != 0 and (k - 11) >= 0 and (k - 11) not in player_pos:
        if (k - 11) in opponent_pos:
            #make_animation(k - 11, animate_color1, Red)
            #opponents.append(k - 11)
            if k+2 % 12 != 0 and (k-22) >= 0 and (k-22) not in player1_pos and (k-22) not in player2_pos:
                make_animation(k - 11, animate_color1, Red)
                opponents.append(k - 11)
                make_animation(k - 22, animate_color1, animate_color2)
                game_obj_possible_pos.append(k - 22)
        else:
            make_animation(k - 11, animate_color1, animate_color2)
            game_obj_possible_pos.append(k - 11)
    #UpLeft
    if k % 12 != 0 and (k - 13) >= 0 and (k - 13) not in player_pos:
        if (k - 13) in opponent_pos:
            #make_animation(k - 13, animate_color1, Red)
            #opponents.append(k - 13)
            if k-12 != 0 and (k-26) >= 0 and (k-26) not in player2_pos and (k-26) not in player1_pos:
                make_animation(k - 13, animate_color1, Red)
                opponents.append(k - 13)
                make_animation(k - 26, animate_color1, animate_color2)
                game_obj_possible_pos.append(k - 26)
        else:
            make_animation(k - 13, animate_color1, animate_color2)
            game_obj_possible_pos.append(k - 13)


def on_click_obj(k,pl_t):
    """
    if k in player1_pos:
        on_click_animate(k, Blue, Green, player1_pos, player2_pos)
    else:
        if k in player2_pos:
            on_click_animate(k, Blue, Green, player2_pos, player1_pos)
        else:
            return 0
    return 1
    """
    if pl_t == 1:
        if k in player1_pos:
            on_click_animate(k, Blue, Green, player1_pos, player2_pos)
    else:
        if k in player2_pos:
            on_click_animate(k, Blue, Green, player2_pos, player1_pos)
    return 1

def GetOpPos(i,pos):
    if pos-i == 2 or i-pos == 2 or pos-i == 24 or i-pos == 24:
        return int((pos+i)/2)
    if pos-i == 26:
        return pos-13
    if pos-i == 22:
        return pos-11
    if i-pos == 26:
        return pos+13
    if i-pos == 22:
        return pos+11

def move_on_click(pos,player_score):
    for i in game_obj_possible_pos:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if distance(game_objs[i][0], game_objs[i][1], mouse_x, mouse_y) <= game_objs[i][2]:
            if pos in player1_pos:
                for pos_pos in range(0, len(player1_pos)):
                    if player1_pos[pos_pos] == pos:
                        player1_pos.pop(pos_pos)
                        break
                """
                if i in opponents:
                    for i_pos in range(0, len(player2_pos)):
                        if player2_pos[i_pos] == i:
                            player2_pos.pop(i_pos)
                            break
                """
                pl_turn[0] = 2
                if i-pos not in [1,-1,12,-12,11,-11,13,-13]:
                    op_pos = GetOpPos(i,pos)
                    player2_pos.remove(op_pos)
                    player_score[0] += 1
                    #pl_turn[0] = 1

                del opponents[:len(opponents)]
                player1_pos.append(i)
            else:
                if pos in player2_pos:
                    for pos_pos in range(0, len(player2_pos)):
                        if player2_pos[pos_pos] == pos:
                            player2_pos.pop(pos_pos)
                            break
                    """
                    if i in opponents:
                        for i_pos in range(0, len(player1_pos)):
                            if player1_pos[i_pos] == i:
                                player1_pos.pop(i_pos)
                                break
                    """
                    pl_turn[0] = 1
                    if i - pos not in [1, -1, 12, -12, 11, -11, 13, -13]:
                        op_pos = GetOpPos(i, pos)
                        player1_pos.remove(op_pos)
                        player_score[1] += 1
                        #pl_turn[0] = 2

                    del opponents[:len(opponents)]
                    player2_pos.append(i)


    """
    if pl_turn == 1:
        pl_turn = 2
    else:
        pl_turn = 1"""

def on_click_replay(mouse_x, mouse_y):
    #mouse_x, mouse_y = pygame.mouse.get_pos()
    if distance(replay_button[0], replay_button[1], mouse_x, mouse_y) <= replay_button[2]:
        del player1_pos[0:len(player1_pos)]
        create_player1_pos()
        del player2_pos[0:len(player2_pos)]
        create_player2_pos()

def on_click_pause():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x >= pause_button[0] - 12 and mouse_x <= pause_button[0] + 41 and mouse_y >= pause_button[1] - 8 and mouse_y <= pause_button[1] + 58:
        return 1
    else:
        return 0

def on_click_quit():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x >= 600 and mouse_x <= 655 and mouse_y >= 605 and mouse_y <= 650:
        return 1
    else:
        return 0

def on_click_yes():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x >= yes_button[0] and mouse_x <= yes_button[0] + yes_button[2] and mouse_y >= yes_button[1] and mouse_y <= yes_button[1] + yes_button[3]:
        sp_mp.Run_Game()

def on_click_no():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x >= no_button[0] and mouse_x <= no_button[0] + no_button[2] and mouse_y >= no_button[1] and mouse_y <= no_button[1] + no_button[3]:
        return 0
    else:
        return 1

def on_click_resume():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x >= resume_button[0] and mouse_x <= resume_button[0] + resume_button[2] and mouse_y >= resume_button[1] and \
            mouse_y <= resume_button[1] + resume_button[3]:
        return 0
    else:
        return 1

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
LightYellow = (250, 250, 210)
Gold = (255, 215, 0)
Yellow = (255, 255, 0)


#Colors for pause:
Light_Light_Blue = (0, 0, 160)
Light_LightGreen = (0, 160, 0)

#Lists of Details:
game_window_width = 680
game_window_height = 680
game_obj_back = [30, 30, 20, Gray]
game_obj_front = [30, 30, 15, Black]
game_objs = []
x_init = 30
y_init = 30


#game_obj_adjs = []
game_obj_possible_pos = []
replay_button = [635, 54, 28, [(635, 26), (618, 20), (629, 45)], LightGreen, LightWhite]
replay_button_cover = [646, 36, 11, LightWhite]
pause_button = [617, 120, 10, 50, LightGreen]
pause_board = [115, 170, 460, 200, LightGray, LightWhite]
resume_button = [250, 350, 200, 50, LightGreen]
quit_button = [[(605, 610), (615, 610), (650, 645), (640, 645)], [(650, 610), (640, 610), (605, 645), (615, 645)], LightRed]
quit_board = [50, 170, 580, 220, LightGray, LightWhite]
yes_button = [190, 370, 100, 40, LightGreen]
no_button = [390, 370, 100, 40, LightGreen]
vertical_margin = [(595, 20), (595, 650), Black]
horizantal_margin = [(20, 597), (650, 597), Black]

#Texts:
game_pause = [210, 240, 60, "Game Paused", LightRed]
resume = [300, 362, 40, "Resume", LightWhite]
yes = [217, 378, 37, "Yes", LightWhite]
no = [424, 378, 37, "No", LightWhite]
confirm_quit = [70, 260, 40, "Are you sure you want to quit the game?", LightRed]

#-------------------------Player positions-------------------

player1_pos = []
create_player1_pos()
player2_pos = []
create_player2_pos()
pl1_opponent_pos = []
pl2_opponent_pos = []
opponents = []

#------------------------------------------------------------

#add_coins()

var = 0
pl_turn = [1]
pause = 0
quit = 0

pygame.init()

game_window = create_game_window(game_window_width, game_window_height)

def StartSinglePlayer(var, pause, quit):
    player_score = [0,0]
    while True:
        game_window.fill(LightWhite)
        # --------------Declaring class---------------
        createobj = create_obj()
        create_button = create_buttons()
        create_margin = create_margins()

        #------------------------If game is continued--------------------
        if pause == 0 and quit == 0:
            #--------------Creating Game Objects Details List------------
            create_game_objs_list(30, 30)

            #--------------Creating Margins--------------
            create_margin.horizantal()
            create_margin.vertical()

            #--------------Creating Objects--------------
            for i in range(0, 144):
                createobj.layout(game_objs[i])

            create_button.replay_back()
            create_button.replay_front()
            create_button.replay_triangle()
            create_button.replay_correct()
            create_button.pause_button()
            create_button.quit_button()
            create_button.score(player_score[0],player_score[1])
            create_button.PlayerTurn(pl_turn[0])
            #--------------------------------------------

            #--------------Mouseover Animation-----------
            if var == 0:

                for i in range(0, 144):
                    if i in player1_pos:
                        createobj.Animate(i, LightBlack, LightBlue, Black, Blue)
                    else:
                        if i in player2_pos:
                            createobj.Animate(i, LightBlack, Yellow, Black, Gold)
                        else:
                            createobj.Animate(i, LightBlack, LightGray, Black, Gray)



            create_button.replay_Animate(LightGreen, Green)
            create_button.pause_Animate(LightGreen, Green)
            create_button.quit_animate(LightRed, Red)

        #--------------------------------------------

            for key in pygame.event.get():
                #------------------Animation on click object--------------
                if key.type == pygame.MOUSEBUTTONDOWN:
                    quit = on_click_quit()
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if var == 1:
                        true, pos_1 = mouse_click_on_obj()
                        if true == 1:
                            move_on_click(pos,player_score)
                            del game_obj_possible_pos[0:len(game_obj_possible_pos)]
                            del game_objs[0:len(game_objs)]
                            var = 0
                            if player1_pos == None:
                                leaderboard.ShowScore(player_score[1],'player 2')

                            if player2_pos == None:
                                leaderboard.ShowScore(player_score[0],'player 1')
                    else:
                        true, pos = mouse_click_on_obj()
                        print(pos)
                        if true == 1:
                            var = on_click_obj(pos,pl_turn[0])

                    if distance(replay_button[0], replay_button[1], mouse_x, mouse_y) <= replay_button[2]:
                        player_score = [0,0]
                        var = 0
                        on_click_replay(mouse_x, mouse_y)

                    pause = on_click_pause()


                #---------------------------------------------------------

                #-----------------Exiting Condition-----------------------
                if key.type == pygame.QUIT:
                    pygame.quit()

                #---------------------------------------------------------
            #-----------------------------------------------------------------
        else:
            #-----------------------If game is paused----------------
            if pause == 1 and quit == 0:
                create_button.pause_board()
                create_button.resume_button()
                WriteText(game_pause)

                create_button.button_animate(resume_button)
                WriteText(resume)

                for key in pygame.event.get():
                    if key.type == pygame.QUIT:
                        pygame.quit()

                    if key.type == pygame.MOUSEBUTTONDOWN:
                        pause = on_click_resume()

            #--------------------------------------------------------

            #-------------------------On Click Quit------------------
            else:
                if quit == 1:
                    create_button.quit_board()
                    create_button.yes_button()
                    create_button.no_button()

                    WriteText(confirm_quit)

                    create_button.button_animate(yes_button)
                    create_button.button_animate(no_button)
                    WriteText(yes)
                    WriteText(no)

                    for key in pygame.event.get():
                        if key.type == pygame.QUIT:
                            pygame.quit()

                        if key.type == pygame.MOUSEBUTTONDOWN:
                            if on_click_yes():
                                return


        pygame.display.update()


#StartSinglePlayer(0, 0, 0)
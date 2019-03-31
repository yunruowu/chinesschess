import pygame
import pygame.font
import sys
import traceback
from pygame.locals import *

pygame.font.init()
pygame.init()

SCREEN_SIZE = (750, 620)
# screen = pygame.display.set_mode([640,480])
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("中国象棋")
screen.fill([255, 255, 255])

color_RECT = [220, 120, 130]
color_line = [191, 77, 83]
global a
global length
a = 50
length = 50


def draw_aboard():
    rec_length = 8 * length
    rec_width = 9 * length
    position = [a, a]
    my_RECT = [a, a, rec_length, rec_width]
    my_bod = [a - 4, a - 4, rec_length + 8, rec_width + 8]
    pygame.draw.rect(screen, (255, 1, 1), my_bod, 1)
    pygame.draw.rect(screen, color_RECT, my_RECT, 2)
    # pygame.display.flip()

    for i in range(1, 8):
        pygame.draw.line(screen, color_line, (a + i * length, a), (a + i * length, a + 4 * length), 2)
        pygame.draw.line(screen, color_line, (a + i * length, a + 5 * length), (a + i * length, a + 9 * length), 2)

    for i in range(1, 10):
        pygame.draw.line(screen, color_line, (a, i * length + a), (a + 8 * length, i * length + a), 2)
    # pygame.display.flip()

    # 士气的路线
    m = 15
    for i in range(1, 2 * length, m):
        pygame.draw.line(screen, color_line, (a + 3 * length + i, a + i), (a + 3 * length + i + m / 2, a + i + m / 2))
        pygame.draw.line(screen, color_line, (a + 3 * length + i, a + 7 * length + i),
                         (a + 3 * length + i + m / 2, a + 7 * length + i + m / 2))
        pygame.draw.line(screen, color_line, (a + 3 * length + i, a + 2 * length - i),
                         (a + 3 * length + i + m / 2, a + 2 * length - i - m / 2))
        pygame.draw.line(screen, color_line, (a + 3 * length + i, a + 9 * length - i),
                         (a + 3 * length + i + m / 2, a + 9 * length - i - m / 2))

    color_aaline = [255, 1, 1]
    for i in range(0, 4):
        for j in range(1, 3):
            pygame.draw.aalines(screen, color_aaline, False,
                                [(a + i * 2 * length + 3, a + j * 3 * length - 15),
                                 (a + i * 2 * length + 3, a + j * 3 * length - 3),
                                 (a + i * 2 * length + 15, a + j * 3 * length - 3)], 1)
            pygame.draw.aalines(screen, color_aaline, False,
                                [(a + i * 2 * length + 3, a + j * 3 * length + 15),
                                 (a + i * 2 * length + 3, a + j * 3 * length + 3),
                                 (a + i * 2 * length + 15, a + j * 3 * length + 3)], 1)
    for i in range(1, 5):
        for j in range(1, 3):
            pygame.draw.aalines(screen, color_aaline, False,
                                [(a + i * 2 * length - 15, a + j * 3 * length - 3),
                                 (a + i * 2 * length - 3, a + j * 3 * length - 3),
                                 (a + i * 2 * length - 3, a + j * 3 * length - 15)], 1)
            pygame.draw.aalines(screen, color_aaline, False,
                                [(a + i * 2 * length - 3, a + j * 3 * length + 15),
                                 (a + i * 2 * length - 3, a + j * 3 * length + 3),
                                 (a + i * 2 * length - 15, a + j * 3 * length + 3)], 1)

    # 炮
    for i in range(0, 2):
        for j in range(0, 2):
            pygame.draw.aalines(screen, color_aaline, False,
                                [
                                    (a + length + i * 6 * length + 3, a + 2 * length + j * 5 * length - 15),
                                    (a + length + i * 6 * length + 3, a + 2 * length + j * 5 * length - 3),
                                    (a + length + i * 6 * length + 15, a + 2 * length + j * 5 * length - 3),
                                ], 1)
            pygame.draw.aalines(screen, color_aaline, False,
                                [
                                    (a + length + i * 6 * length + 3, a + 2 * length + j * 5 * length + 15),
                                    (a + length + i * 6 * length + 3, a + 2 * length + j * 5 * length + 3),
                                    (a + length + i * 6 * length + 15, a + 2 * length + j * 5 * length + 3),
                                ], 1)
            pygame.draw.aalines(screen, color_aaline, False,
                                [
                                    (a + length + i * 6 * length - 3, a + 2 * length + j * 5 * length - 15),
                                    (a + length + i * 6 * length - 3, a + 2 * length + j * 5 * length - 3),
                                    (a + length + i * 6 * length - 15, a + 2 * length + j * 5 * length - 3),
                                ], 1)
            pygame.draw.aalines(screen, color_aaline, False,
                                [
                                    (a + length + i * 6 * length - 3, a + 2 * length + j * 5 * length + 15),
                                    (a + length + i * 6 * length - 3, a + 2 * length + j * 5 * length + 3),
                                    (a + length + i * 6 * length - 15, a + 2 * length + j * 5 * length + 3),
                                ], 1)
    pygame.display.flip()

    ZiTiDuiXiang = pygame.font.SysFont('SimHei', 32)
    WenBenKuangDuiXiang = ZiTiDuiXiang.render("楚河", True, (255, 0, 0))
    hanjie = ZiTiDuiXiang.render("汉界", True, (255, 0, 0))
    qq = hanjie.get_rect()
    KuangDuiXiang = WenBenKuangDuiXiang.get_rect()
    KuangDuiXiang.center = (a + length + 50, a + 4 * length + 25)
    qq.center = (a + 5 * length + 50, a + 4 * length + 25)
    screen.blit(WenBenKuangDuiXiang, KuangDuiXiang)
    screen.blit(hanjie, qq)
    pygame.display.update()


def draw_chessonboard():
    draw_aboard()
    for chess in red_chess.keys():
        draw_chess(screen, chess[0], red_chess[chess]['color'], red_chess[chess]['coordinate'][0],
                   red_chess[chess]['coordinate'][1])
    for chess in black_chess.keys():
        draw_chess(screen, chess[0], black_chess[chess]['color'], black_chess[chess]['coordinate'][0],
                   black_chess[chess]['coordinate'][1])
    global position


red_color = (250, 0, 0)
black_color = (0, 0, 0)


def Draw_cir(x, y):
    r = int(a / 2) - 2
    pygame.draw.circle(screen, (12, 12, 0), (x, y), r)
    pygame.draw.circle(screen, (255, 255, 255), (x, y), r - 1)
    pygame.draw.circle(screen, (205, 124, 71), (x, y), r - 3)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), r - 5)
    pygame.draw.circle(screen, (198, 175, 125), (x, y), r - 6)
    pygame.display.flip()


# draw_aboard()

def draw_chess(screen, chess, color, x, y):
    # 画圆
    x = a + x * length
    y = a + y * length
    Draw_cir(x, y)
    Font_chess = pygame.font.SysFont('SimHei', 30)
    if color == 'red':
        txt = Font_chess.render(chess, True, red_color)

    else:
        txt = Font_chess.render(chess, True, black_color)
    screen.blit(txt, (x - 15, y - 15))
    pygame.display.update()


def get_red_chess(pos):
    global red_chess
    for chess in red_chess.keys():
        if (red_chess[chess]['coordinate'] == pos):
            print(chess)
            return chess


def get_black_chess(pos):
    global black_chess
    for chess in black_chess.keys():
        if (black_chess[chess]['coordinate'] == pos):
            print(chess)
            return chess


def move(p,s_pos, e_pos, chess):
    position[e_pos[1]][e_pos[0]] = position[s_pos[1]][s_pos[0]]
    position[s_pos[1]][s_pos[0]] = 0
    if p ==1:
        red_chess[chess]['coordinate'] = e_pos
    else:
        black_chess[chess]['coordinate'] = e_pos
    draw_chessonboard()


def way(people, s_pos, e_pos):
    if people == 0:  # 红棋
        chess = get_red_chess(s_pos)
        if chess[0] == '将':
            if e_pos[0] in range(3, 6) and e_pos[1] in range(0, 3):
                if (abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 0) or \
                        (abs(s_pos[0] - e_pos[0]) == 0 and abs(s_pos[1] - e_pos[1]) == 1):
                    print(s_pos, e_pos)

                    move(1,s_pos, e_pos, chess)
                else:
                    print("ERROR!")
            else:
                print("ERROR!")
        if chess[0] == '士':
            if e_pos[0] in range(3, 6) and e_pos[1] in range(0, 3):
                if (abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1) or \
                        (abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1):

                    print(s_pos, e_pos)
                    move(1,s_pos, e_pos, chess)

                else:
                    print("ERROR!")
            else:
                print("ERROR!")
        if chess[0] == '相':
            if e_pos[0] in range(0, 9) and e_pos[1] in range(0, 5):
                if (abs(s_pos[0] - e_pos[0]) == 2 and abs(s_pos[1] - e_pos[1]) == 2) or \
                        (abs(s_pos[0] - e_pos[0]) == 2 and abs(s_pos[1] - e_pos[1]) == 2):
                    print(s_pos, e_pos)

                    move(1,s_pos, e_pos, chess)
                else:
                    print("ERROR!")
            else:
                print("ERROR!")
        if chess[0] == '马':
            if abs(e_pos[0] - s_pos[0]) == 1 and abs(e_pos[1] - s_pos[1]) == 2:
                if position[int((e_pos[1] + s_pos[1]) / 2)][s_pos[0]] == 0:
                    move(1,s_pos, e_pos, chess)
                else:
                    print("error1")
            elif abs(e_pos[0] - s_pos[0]) == 2 and abs(e_pos[1] - s_pos[1]) == 1:
                if position[s_pos[1]][int((e_pos[0] + s_pos[0]) / 2)] == 0:
                    move(1,s_pos, e_pos, chess)
                else:
                    print("error2")
            else:
                print("error3")
        if chess[0] == '車':
            act = 1
            if (s_pos[0] - e_pos[0]) == 0:
                if s_pos[1] < e_pos[1]:
                    for i in range(s_pos[1] + 1, e_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error1")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[1] > e_pos[1]:
                    for i in range(e_pos[1] + 1, s_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error2")
                            act = 0
                            break
                # move(s_pos, e_pos,chess)
            elif (s_pos[1] - e_pos[1]) == 0:
                if s_pos[0] < e_pos[0]:
                    for i in range(s_pos[0] + 1, e_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error3")
                            act = 0
                            break
                    # move(s_pos,e_pos,chess)
                if s_pos[0] > e_pos[0]:
                    for i in range(e_pos[0] + 1, s_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error4")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[0] == e_pos[0]:
                    print("error5")
                    act = 0
            else:
                print("error6")
                act = 0
            if (act == 1):
                move(1,s_pos, e_pos, chess)
            else:
                pass
        if chess[0] == '炮':

            act = 1
            if (s_pos[0] - e_pos[0]) == 0:
                if s_pos[1] < e_pos[1]:
                    for i in range(s_pos[1] + 1, e_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error1")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[1] > e_pos[1]:
                    for i in range(e_pos[1] + 1, s_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error2")
                            act = 0
                            break
                # move(s_pos, e_pos,chess)
            elif (s_pos[1] - e_pos[1]) == 0:
                if s_pos[0] < e_pos[0]:
                    for i in range(s_pos[0] + 1, e_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error3")
                            act = 0
                            break
                    # move(s_pos,e_pos,chess)
                if s_pos[0] > e_pos[0]:
                    for i in range(e_pos[0] + 1, s_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error4")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[0] == e_pos[0]:
                    print("error5")
                    act = 0
            else:
                print("error6")
                act = 0
            if (act == 1):
                move(1,s_pos, e_pos, chess)
            else:
                pass
        if chess[0] == '兵':
            if s_pos[1]<5:
                if s_pos[0]==e_pos[0] and e_pos[1]-s_pos[1]==1:
                    move(1,s_pos,e_pos,chess)
                else:
                    print("error1!")
            else:
                if ((s_pos[0] == e_pos[0]) and (e_pos[1] - s_pos[1] == 1)) \
                        or ((s_pos[1] - e_pos[1] == 0
                            ) and (abs(s_pos[0] - e_pos[0] )== 1)):
                    move(1,s_pos,e_pos,chess)
                else:
                    print("error2!")
    if people == 1:  # 黑棋
        print("dsdfsdfsdfs")
        chess = get_black_chess(s_pos)
        if chess[0] == '将':
            if e_pos[0] in range(3, 6) and e_pos[1] in range(7, 10):
                if (abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 0) or \
                        (abs(s_pos[0] - e_pos[0]) == 0 and abs(s_pos[1] - e_pos[1]) == 1):
                    print(s_pos, e_pos)

                    move(0,s_pos, e_pos, chess)
                else:
                    print("ERROR!")
            else:
                print("ERROR!")
        if chess[0] == '仕':
            if e_pos[0] in range(3, 6) and e_pos[1] in range(7, 10):
                if (abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1) or \
                        (abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1):

                    print(s_pos, e_pos)
                    move(1,s_pos, e_pos, chess)

                else:
                    print("ERROR!")
            else:
                print("ERROR!")
        if chess[0] == '象':
            if e_pos[0] in range(0, 9) and e_pos[1] in range(5, 10):
                if (abs(s_pos[0] - e_pos[0]) == 2 and abs(s_pos[1] - e_pos[1]) == 2) or \
                        (abs(s_pos[0] - e_pos[0]) == 2 and abs(s_pos[1] - e_pos[1]) == 2):
                    print(s_pos, e_pos)

                    move(0,s_pos, e_pos, chess)
                else:
                    print("ERROR!")
            else:
                print("ERROR!")
        if chess[0] == '马':
            if abs(e_pos[0] - s_pos[0]) == 1 and abs(e_pos[1] - s_pos[1]) == 2:
                if position[int((e_pos[1] + s_pos[1]) / 2)][s_pos[0]] == 0:
                    move(0,s_pos, e_pos, chess)
                else:
                    print("error1")
            elif abs(e_pos[0] - s_pos[0]) == 2 and abs(e_pos[1] - s_pos[1]) == 1:
                if position[s_pos[1]][int((e_pos[0] + s_pos[0]) / 2)] == 0:
                    move(0,s_pos, e_pos, chess)
                else:
                    print("error2")
            else:
                print("error3")
        if chess[0] == '車':
            act = 1
            if (s_pos[0] - e_pos[0]) == 0:
                if s_pos[1] < e_pos[1]:
                    for i in range(s_pos[1] + 1, e_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error1")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[1] > e_pos[1]:
                    for i in range(e_pos[1] + 1, s_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error2")
                            act = 0
                            break
                # move(s_pos, e_pos,chess)
            elif (s_pos[1] - e_pos[1]) == 0:
                if s_pos[0] < e_pos[0]:
                    for i in range(s_pos[0] + 1, e_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error3")
                            act = 0
                            break
                    # move(s_pos,e_pos,chess)
                if s_pos[0] > e_pos[0]:
                    for i in range(e_pos[0] + 1, s_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error4")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[0] == e_pos[0]:
                    print("error5")
                    act = 0
            else:
                print("error6")
                act = 0
            if (act == 1):
                move(0
                     ,s_pos, e_pos, chess)
            else:
                pass
        if chess[0] == '炮':

            act = 1
            if (s_pos[0] - e_pos[0]) == 0:
                if s_pos[1] < e_pos[1]:
                    for i in range(s_pos[1] + 1, e_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error1")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[1] > e_pos[1]:
                    for i in range(e_pos[1] + 1, s_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error2")
                            act = 0
                            break
                # move(s_pos, e_pos,chess)
            elif (s_pos[1] - e_pos[1]) == 0:
                if s_pos[0] < e_pos[0]:
                    for i in range(s_pos[0] + 1, e_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error3")
                            act = 0
                            break
                    # move(s_pos,e_pos,chess)
                if s_pos[0] > e_pos[0]:
                    for i in range(e_pos[0] + 1, s_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error4")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[0] == e_pos[0]:
                    print("error5")
                    act = 0
            else:
                print("error6")
                act = 0
            if (act == 1):
                move(0,s_pos, e_pos, chess)
            else:
                pass
        if chess[0] == '卒':
            if s_pos[1]>4:
                if s_pos[0]==e_pos[0] and e_pos[1]-s_pos[1]==-1:
                    move(0,s_pos,e_pos,chess)
                else:
                    print("error1!")
            else:
                if ((s_pos[0] == e_pos[0]) and (e_pos[1] - s_pos[1] == -1)) \
                        or ((s_pos[1] - e_pos[1] == 0
                            ) and (abs(s_pos[0] - e_pos[0] )== 1)):
                    move(0,s_pos,e_pos,chess)
                else:
                    print("error2!")


def chess_move():
    global begin
    global master
    if begin == True:  # 选择第一个棋子
        position_x, position_y = pygame.mouse.get_pos()
        if (position_x < a + 8 * length + length / 2) and (position_y < a + 9 * length + length / 2) and (
                position_x > a - length / 2) and (position_y > a - length / 2):
            x = int((position_x - a + length / 2) / length)
            y = int((position_y - a + length / 2) / length)
            print(x, y, "qi")
            if master == True:#红方
                if position[y][x] == 0 or position[y][x] > 7:  # 选择了红棋
                    print("请选择一个己方棋子！！！")
                else:
                    chess = position[y][x]

                    start_pos = [x, y]
            else:#黑方
                if position[y][x] == 0 or position[y][x] < 8:
                    print("请选择一个己方棋子！！！")
                else:
                    chess = position[y][x]

                    start_pos = [x, y]

                    #  print("ewwe")


        else:
            print("请选择正确的位置！！！")
            pass

        # 终点
    if begin == False:  # 选择落子的位置
        position_x, position_y = pygame.mouse.get_pos()
        if (position_x < a + 8 * length + length / 2) and (position_y < a + 9 * length + length / 2) and (
                position_x > a - length / 2) and (position_y > a - length / 2):
            x = int((position_x - a + length / 2) / length)
            y = int((position_y - a + length / 2) / length)
            print(x, y)
            end_pos = [x, y]
            print(begin)
            # print("dsd")

            if position[y][x] == 0:  # 位置为空
                global start_pos, chess,master
                if master==True:
                    way(0, start_pos, end_pos)
                    master = not master
                else:
                    way(1,start_pos,end_pos)
                    master = not master

            else:
                print("zijide qi")
        else:
            print("请选择正确的位置！！！")
            pass
    begin = not begin





"""def black_move():
    global begin
    if begin == True:
        position_x, position_y = pygame.mouse.get_pos()
        if (position_x < a + 8 * length + length / 2) and (position_y < a + 9 * length + length / 2) and (
                position_x > a - length / 2) and (position_y > a - length / 2):
            x = int((position_x - a + length / 2) / length)
            y = int((position_y - a + length / 2) / length)
            print(x, y, "qi")

            if position[y][x] == 0 or position[y][x] > 7:
                print("请选择一个棋子！！！")
            else:
                chess = position[y][x]

                start_pos = [x, y]
                begin = not begin

                #  print("ewwe")


        else:
            print("请选择正确的位置！！！")
            pass

    # 终点
    if  begin == False:
        position_x, position_y = pygame.mouse.get_pos()
        if (position_x < a + 8 * length + length / 2) and (position_y < a + 9 * length + length / 2) and (
                position_x > a - length / 2) and (position_y > a - length / 2):
            x = int((position_x - a + length / 2) / length)
            y = int((position_y - a + length / 2) / length)
            print(x, y)
            end_pos = [x, y]
            print(begin)
            # print("dsd")
            begin = not begin
            if position[y][x] == 0:
                global start_pos, chess,master
                if master==True:
                    way(1, start_pos, end_pos)
                else:
                    way(0,start_pos,end_pos)
            else:
                print("zijide qi")
        else:
            print("请选择正确的位置！！！")
            pass
    global master
    master = not master
"""
def main():
    global red_chess
    global black_chess
    print("we")
    red_chess = {
        '将': {'color': 'red', 'position': [a + 4 * length, a], 'coordinate': [4, 0]},
        '士1': {'color': 'red', 'position': [a + 3 * length, a], 'coordinate': [3, 0]},
        '士2': {'color': 'red', 'position': [a + 5 * length, a], 'coordinate': [5, 0]},
        '相1': {'color': 'red', 'position': [a + 2 * length, a], 'coordinate': [2, 0]},
        '相2': {'color': 'red', 'position': [a + 6 * length, a], 'coordinate': [6, 0]},
        '马1': {'color': 'red', 'position': [a + 1 * length, a], 'coordinate': [1, 0]},
        '马2': {'color': 'red', 'position': [a + 7 * length, a], 'coordinate': [7, 0]},
        '車1': {'color': 'red', 'position': [a + 0 * length, a], 'coordinate': [0, 0]},
        '車2': {'color': 'red', 'position': [a + 8 * length, a], 'coordinate': [8, 0]},
        '炮1': {'color': 'red', 'position': [a + 1 * length, a + 2 * length], 'coordinate': [1, 2]},
        '炮2': {'color': 'red', 'position': [a + 7 * length, a + 2 * length], 'coordinate': [7, 2]},
        '兵1': {'color': 'red', 'position': [a + 0 * length, a + 3 * length], 'coordinate': [0, 3]},
        '兵2': {'color': 'red', 'position': [a + 2 * length, a + 3 * length], 'coordinate': [2, 3]},
        '兵3': {'color': 'red', 'position': [a + 4 * length, a + 3 * length], 'coordinate': [4, 3]},
        '兵4': {'color': 'red', 'position': [a + 6 * length, a + 3 * length], 'coordinate': [6, 3]},
        '兵5': {'color': 'red', 'position': [a + 8 * length, a + 3 * length], 'coordinate': [8, 3]},
    }
    black_chess = {
        '将': {'color': 'black', 'position': [a + 4 * length, a + 9 * length], 'coordinate': [4, 9]},
        '仕1': {'color': 'black', 'position': [a + 3 * length, a + 9 * length], 'coordinate': [3, 9]},
        '仕2': {'color': 'black', 'position': [a + 5 * length, a + 9 * length], 'coordinate': [5, 9]},
        '象1': {'color': 'black', 'position': [a + 2 * length, a + 9 * length], 'coordinate': [2, 9]},
        '象2': {'color': 'black', 'position': [a + 6 * length, a + 9 * length], 'coordinate': [6, 9]},
        '马1': {'color': 'black', 'position': [a + 1 * length, a + 9 * length], 'coordinate': [1, 9]},
        '马2': {'color': 'black', 'position': [a + 7 * length, a + 9 * length], 'coordinate': [7, 9]},
        '車1': {'color': 'black', 'position': [a + 0 * length, a + 9 * length], 'coordinate': [0, 9]},
        '車2': {'color': 'black', 'position': [a + 8 * length, a + 9 * length], 'coordinate': [8, 9]},
        '炮1': {'color': 'black', 'position': [a + 1 * length, a + 7 * length], 'coordinate': [1, 7]},
        '炮2': {'color': 'black', 'position': [a + 7 * length, a + 7 * length], 'coordinate': [7, 7]},
        '卒1': {'color': 'black', 'position': [a + 0 * length, a + 6 * length], 'coordinate': [0, 6]},
        '卒2': {'color': 'black', 'position': [a + 2 * length, a + 6 * length], 'coordinate': [2, 6]},
        '卒3': {'color': 'black', 'position': [a + 4 * length, a + 6 * length], 'coordinate': [4, 6]},
        '卒4': {'color': 'black', 'position': [a + 6 * length, a + 6 * length], 'coordinate': [6, 6]},
        '卒5': {'color': 'black', 'position': [a + 8 * length, a + 6 * length], 'coordinate': [8, 6]},
    }
    draw_chessonboard()

    global position
    position = [
        [5, 4, 3, 2, 1, 2, 3, 4, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 6, 0],
        [7, 0, 7, 0, 7, 0, 7, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [14, 0, 14, 0, 14, 0, 14, 0, 14],
        [0, 13, 0, 0, 0, 0, 0, 13, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, 11, 10, 9, 8, 9, 10, 11, 12]
    ]

    global begin,master
    begin = True
    master = True
    start_pos = (0, 0)
    end_pos = (0, 0)
    chess = 0
    who = 0
    while True:
        for event in pygame.event.get():
            # print(pygame.event.__sizeof__())
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                chess_move()


        screen.fill([255, 255, 255])


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
import pygame
import pygame.font
import sys
import traceback
from pygame.locals import *

pygame.font.init()
pygame.init()

SCREEN_SIZE = (750,620)
#screen = pygame.display.set_mode([640,480])
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
pygame.display.set_caption("中国象棋")
screen.fill([255,255,255])

color_RECT = [220, 120, 130]
color_line = [191, 77, 83]
global a
global length
a = 50
length = 50


def draw_aboard():
    rec_length = 8*length
    rec_width = 9*length
    position = [a,a]
    my_RECT = [a,a,rec_length,rec_width]
    my_bod = [a-4,a-4,rec_length+8,rec_width+8]
    pygame.draw.rect(screen,(255,1,1),my_bod,1)
    pygame.draw.rect(screen,color_RECT,my_RECT,2)
    #pygame.display.flip()

    for i in range(1,8):
        pygame.draw.line(screen,color_line,(a+i*length,a),(a+i*length,a+4*length),2)
        pygame.draw.line(screen,color_line,(a+i*length,a+5*length),(a+i*length,a+9*length),2)

    for i in range(1,10):
        pygame.draw.line(screen,color_line,(a,i*length+a),(a+8*length,i*length+a),2)
    #pygame.display.flip()

    #士气的路线
    m = 15
    for i in range(1,2*length,m):
        pygame.draw.line(screen,color_line,(a+3*length+i,a+i),(a+3*length+i+m/2,a+i+m/2))
        pygame.draw.line(screen,color_line,(a+3*length+i,a+7*length+i),(a+3*length+i+m/2,a+7*length+i+m/2))
        pygame.draw.line(screen,color_line,(a+3*length+i,a+2*length-i),(a+3*length+i+m/2,a+2*length-i-m/2))
        pygame.draw.line(screen,color_line,(a+3*length+i,a+9*length-i),(a+3*length+i+m/2,a+9*length-i-m/2))

    color_aaline =[255,1,1]
    for i in range(0,4):
        for j in range(1,3):
            pygame.draw.aalines(screen, color_aaline, False,
                                [(a+i*2*length+3,a+j*3*length-15), (a+i*2*length+3,a+j*3*length-3),
                                    (a+i*2*length+15,a+j*3*length-3)], 1)
            pygame.draw.aalines(screen, color_aaline, False,
                                [(a+i*2*length+3,a+j*3*length+15), (a+i*2*length+3,a+j*3*length+3),
                                    (a+i*2*length+15,a+j*3*length+3)], 1)
    for i in range(1,5):
        for j in range(1,3):
            pygame.draw.aalines(screen,color_aaline,False,
                               [(a+i*2*length-15,a+j*3*length-3), (a+i*2*length-3,a+j*3*length-3),
                                    (a+i*2*length-3,a+j*3*length-15)],1)
            pygame.draw.aalines(screen, color_aaline, False,
                                [(a+i*2*length-3,a+j*3*length+15), (a+i*2*length-3,a+j*3*length+3),
                                 (a+i*2*length-15,a+j*3*length+3)], 1)

    #炮
    for i in range(0,2):
        for j in range(0,2):
            pygame.draw.aalines(screen,color_aaline,False,
                                [
                                    (a+length+i*6*length+3,a+2*length+j*5*length-15),
                                    (a+length+i*6*length+3,a+2*length+j*5*length-3),
                                    (a+length+i*6*length+15,a+2*length+j*5*length-3),
                                ],1)
            pygame.draw.aalines(screen,color_aaline,False,
                                [
                                    (a+length+i*6*length+3,a+2*length+j*5*length+15),
                                    (a+length+i*6*length+3,a+2*length+j*5*length+3),
                                    (a+length+i*6*length+15,a+2*length+j*5*length+3),
                                ],1)
            pygame.draw.aalines(screen,color_aaline,False,
                                [
                                    (a+length+i*6*length-3,a+2*length+j*5*length-15),
                                    (a+length+i*6*length-3,a+2*length+j*5*length-3),
                                    (a+length+i*6*length-15,a+2*length+j*5*length-3),
                                ],1)
            pygame.draw.aalines(screen,color_aaline,False,
                                [
                                    (a+length+i*6*length-3,a+2*length+j*5*length+15),
                                    (a+length+i*6*length-3,a+2*length+j*5*length+3),
                                    (a+length+i*6*length-15,a+2*length+j*5*length+3),
                                ],1)
    pygame.display.flip()

    ZiTiDuiXiang=pygame.font.SysFont('SimHei',32)
    WenBenKuangDuiXiang=ZiTiDuiXiang.render("楚河",True, (255,0,0))
    hanjie=ZiTiDuiXiang.render("汉界",True, (255,0,0))
    qq = hanjie.get_rect()
    KuangDuiXiang=WenBenKuangDuiXiang.get_rect()
    KuangDuiXiang.center=(a+length+50,a+4*length+25)
    qq.center=(a+5*length+50,a+4*length+25)
    screen.blit(WenBenKuangDuiXiang,KuangDuiXiang)
    screen.blit(hanjie,qq)
    pygame.display.update()
draw_aboard()

red_color = (250,0,0)
black_color = (0,0,0)
def Draw_cir(x,y):
    r = int (a/2)-2
    pygame.draw.circle(screen,(12,12,0),(x,y),r)
    pygame.draw.circle(screen,(255,255,255),(x,y),r-1)
    pygame.draw.circle(screen,(205, 124, 71),(x,y),r-3)
    pygame.draw.circle(screen,(0,0,0),(x,y),r-5)
    pygame.draw.circle(screen,(198, 175, 125),(x,y),r-6)
    pygame.display.flip()
#draw_aboard()

def draw_chess(screen,chess,color,x,y):
    #画圆
    Draw_cir(x,y)
    Font_chess = pygame.font.SysFont('SimHei',30)
    if color == 'red':
        txt = Font_chess.render(chess,True,red_color)

    else:
        txt = Font_chess.render(chess,True,black_color)
    screen.blit(txt, (x - 15, y - 15))
    pygame.display.update()


def way(people,chess,s_pos,e_pos):
    if people == 0:#红棋
        if chess == 1:
            #way_jiang(p)
            print(s_pos,e_pos)
def red_move():
    start_pos = (0, 0)
    end_pos = (0, 0)
    chess = 0

    for event in pygame.event.wait():
       # print(pygame.event.__sizeof__())
        if event.type == QUIT:
            sys.exit()
        print(begin)
        #起始位置
        if event.type == MOUSEBUTTONDOWN and begin == True:
            position_x, position_y = pygame.mouse.get_pos()
            if (position_x < a + 8 * length + length / 2) and (position_y < a + 9 * length + length / 2) and (
                    position_x > a - length / 2) and (position_y > a - length / 2):
                x = int((position_x - a + length / 2) / length)
                y = int((position_y - a + length / 2) / length)
                print(x, y,"qi")

                if position[y][x] == 0:
                    print("请选择一个棋子！！！")
                else:
                    chess = position[y][x]

                    start_pos = [x,y]
                    begin = not begin
                    continue
                  #  print("ewwe")
                    #way(1,chess,start_pos,end_pos)
            else:
                print("请选择正确的位置！！！")
                pass


        #终点
        if event.type == MOUSEBUTTONDOWN and begin == False:
            position_x, position_y = pygame.mouse.get_pos()
            if (position_x < a + 8 * length + length / 2) and (position_y < a + 9 * length + length / 2) and (
                    position_x > a - length / 2) and (position_y > a - length / 2):
                x = int((position_x - a + length / 2) / length)
                y = int((position_y - a + length / 2) / length)
                print(x, y,"sds")
                end_pos = [x,y]
                print(begin)
                print("dsd")
                begin = not begin

                continue
            else:
                print("请选择正确的位置！！！")
                pass



def black_move():
    a=1






def main():
    global red_chess
    global black_chess
    print("we")
    red_chess={
        '将': {'color': 'red', 'position': [a + 4 * length, a]},
        '士1': {'color': 'red', 'position': [a + 3 * length, a]},
        '士2': {'color': 'red', 'position': [a + 5 * length, a]},
        '相1': {'color': 'red', 'position': [a + 2 * length, a]},
        '相2': {'color': 'red', 'position': [a + 6 * length, a]},
        '马1': {'color': 'red', 'position': [a + 1 * length, a]},
        '马2': {'color': 'red', 'position': [a + 7 * length, a]},
        '車1': {'color': 'red', 'position': [a + 0 * length, a]},
        '車2': {'color': 'red', 'position': [a + 8 * length, a]},
        '炮1': {'color': 'red', 'position': [a + 1 * length, a + 2 * length]},
        '炮2': {'color': 'red', 'position': [a + 7 * length, a + 2 * length]},
        '兵1': {'color': 'red', 'position': [a + 0 * length, a + 3 * length]},
        '兵2': {'color': 'red', 'position': [a + 2 * length, a + 3 * length]},
        '兵3': {'color': 'red', 'position': [a + 4 * length, a + 3 * length]},
        '兵4': {'color': 'red', 'position': [a + 6 * length, a + 3 * length]},
        '兵5': {'color': 'red', 'position': [a + 8 * length, a + 3 * length]},
    }
    black_chess = {
        '将': {'color': 'black', 'position': [a + 4 * length, a + 9 * length]},
        '仕1': {'color': 'black', 'position': [a + 3 * length, a + 9 * length]},
        '仕2': {'color': 'black', 'position': [a + 5 * length, a + 9 * length]},
        '象1': {'color': 'black', 'position': [a + 2 * length, a + 9 * length]},
        '象2': {'color': 'black', 'position': [a + 6 * length, a + 9 * length]},
        '马1': {'color': 'black', 'position': [a + 1 * length, a + 9 * length]},
        '马2': {'color': 'black', 'position': [a + 7 * length, a + 9 * length]},
        '車1': {'color': 'black', 'position': [a + 0 * length, a + 9 * length]},
        '車2': {'color': 'black', 'position': [a + 8 * length, a + 9 * length]},
        '炮1': {'color': 'black', 'position': [a + 1 * length, a + 7 * length]},
        '炮2': {'color': 'black', 'position': [a + 7 * length, a + 7 * length]},
        '卒1': {'color': 'black', 'position': [a + 0 * length, a + 6 * length]},
        '卒2': {'color': 'black', 'position': [a + 2 * length, a + 6 * length]},
        '卒3': {'color': 'black', 'position': [a + 4 * length, a + 6 * length]},
        '卒4': {'color': 'black', 'position': [a + 6 * length, a + 6 * length]},
        '卒5': {'color': 'black', 'position': [a + 8 * length, a + 6 * length]},
    }
    for chess in red_chess.keys():
        draw_chess(screen,chess[0],red_chess[chess]['color'],red_chess[chess]['position'][0],red_chess[chess]['position'][1])
    for chess in black_chess.keys():
        draw_chess(screen,chess[0],black_chess[chess]['color'],black_chess[chess]['position'][0],black_chess[chess]['position'][1])
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


    while True:
        who = 0
        if who == 0:
            red_move()
            who = not who
        if  who == 1:
            black_move()
            who = not who
        screen.fill([255,255,255])

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
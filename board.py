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


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

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
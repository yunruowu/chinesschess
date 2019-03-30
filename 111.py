import pygame
import pygame.font
import sys
import traceback
import copy
from math import sqrt
from pygame.locals import *

pygame.font.init()
pygame.init()

i = 50  # 一格的距离
r = 25  # 棋子半径


# 绘制棋盘
def Draw_qipan(screen):
    # 棋盘背景色
    screen.fill((200, 200, 200))
    # 画外框
    color1 = (100, 100, 100)
    pygame.draw.rect(screen, color1, [40, 40, 420, 470], 5)
    # 画行和列
    color2 = (0, 0, 0)
    for i in range(1, 11):
        pygame.draw.line(screen, color2, (50, 50 * i), (450, 50 * i))
    for i in (1, 9):
        pygame.draw.line(screen, color2, (50 * i, 50), (50 * i, 500))
    for i in range(2, 9):
        pygame.draw.line(screen, color2, (50 * i, 50), (50 * i, 250))
        pygame.draw.line(screen, color2, (50 * i, 300), (50 * i, 500))
    # 画‘士’路线
    color3 = (0, 0, 0)
    pygame.draw.line(screen, color3, (200, 50), (300, 150))
    pygame.draw.line(screen, color3, (200, 150), (300, 50))
    pygame.draw.line(screen, color3, (200, 500), (300, 400))
    pygame.draw.line(screen, color3, (200, 400), (300, 500))
    # 画‘悔棋’，‘重新开始’，‘退出’，‘楚河汉界’
    color4 = (100, 100, 100)
    pygame.draw.rect(screen, color4, [500, 200, 120, 40], 3)
    pygame.draw.rect(screen, color4, [500, 300, 120, 40], 3)
    pygame.draw.rect(screen, color4, [500, 400, 120, 40], 3)
    font1 = pygame.font.Font('C:\Windows\Fonts\STXINGKA.TTF', 20)
    font2 = pygame.font.Font('C:\Windows\Fonts\STXINGKA.TTF', 30)
    text1 = font1.render("悔    棋", True, color4)
    text2 = font1.render("重新开始", True, color4)
    text3 = font1.render("退出游戏", True, color4)
    text4 = font2.render("楚 河         汉 界", True, color4)
    screen.blit(text1, (520, 210))
    screen.blit(text2, (520, 310))
    screen.blit(text3, (520, 410))
    screen.blit(text4, (150, 260))


# 绘制棋子
def Draw_qizi(screen, color, qizi, x, y):
    red_color = (255, 0, 0)
    black_color = (0, 0, 0)
    pygame.draw.circle(screen, (128, 64, 0), (x, y), 25)
    pygame.draw.circle(screen, (255, 255, 128), (x, y), 20)
    font1 = pygame.font.Font('C:\Windows\Fonts\STHUPO.TTF', 32)
    if color == 'red':
        q_color = red_color
    elif color == 'black':
        q_color = black_color
    screen.blit(font1.render(qizi[0], True, q_color), (x - 16, y - 16))


# 绘制带有棋盘的棋子
def Draw_qipan_with_qizi(screen):
    Draw_qipan(screen)
    for qizi in hongqi.keys():
        Draw_qizi(screen, hongqi[qizi]['color'], qizi, hongqi[qizi]['weizhi'][0], hongqi[qizi]['weizhi'][1])
    for qizi in heiqi.keys():
        Draw_qizi(screen, heiqi[qizi]['color'], qizi, heiqi[qizi]['weizhi'][0], heiqi[qizi]['weizhi'][1])


# 通过位置寻找棋子
def find(x, y):
    for qizi in hongqi.keys():
        if sqrt((hongqi[qizi]['weizhi'][0] - x) ** 2 + (hongqi[qizi]['weizhi'][1] - y) ** 2) < r:
            return [True, qizi, 'red']
    for qizi in heiqi.keys():
        if sqrt((heiqi[qizi]['weizhi'][0] - x) ** 2 + (heiqi[qizi]['weizhi'][1] - y) ** 2) < r:
            return [True, qizi, 'black']
    return [False]


# 判断该位置有无棋子
def weizhi_panduan(x, y):
    for qizi in hongqi.keys():
        if [x, y] == hongqi[qizi]['weizhi']:
            return True
    for qizi in heiqi.keys():
        if [x, y] == heiqi[qizi]['weizhi']:
            return True
    return False


# 棋子移动的规则
def move_rules(qizi, color, x, y):
    can_move = []
    if qizi == '将' or qizi == '帅':
        can_move += [[x + i, y], [x - i, y], [x, y + i], [x, y - i]]
        count = 0
        if qizi == '将':
            if hongqi['帅']['weizhi'][0] == x:
                weizhicha = y - hongqi['帅']['weizhi'][1]
                for j in range(50, weizhicha, 50):
                    if weizhi_panduan(x, hongqi['帅']['weizhi'][1] + j):
                        count += 1
                if count == 0:
                    can_move.append(hongqi['帅']['weizhi'])
        if qizi == '帅':
            if heiqi['将']['weizhi'][0] == x:
                weizhicha = heiqi['将']['weizhi'][0] - y
                for j in range(50, weizhicha, 50):
                    if weizhi_panduan(x, y + j):
                        count += 1
                if count == 0:
                    can_move.append(heiqi['将']['weizhi'])
    elif qizi[0] == '士':
        can_move += [[x + i, y + i], [x - i, y - i], [x - i, y + i], [x + i, y - i]]
    elif qizi[0] == '相' or qizi[0] == '象':
        can_move += [[x + 2 * i, y + 2 * i], [x - 2 * i, y - 2 * i], [x - 2 * i, y + 2 * i], [x + 2 * i, y - 2 * i]]
    elif qizi[0] == '马':
        can_move += [[x + i, y + 2 * i], [x + 2 * i, y + i], [x - i, y - 2 * i], [x - 2 * i, y - i], [x + i, y - 2 * i],
                     [x + 2 * i, y - i], [x - i, y + 2 * i], [x - 2 * i, y + i]]
    elif qizi[0] == '车' or qizi[0] == '炮':
        for m in range(1, 10):
            can_move.append([x, y + m * i])
            can_move.append([x, y - m * i])
            can_move.append([x + m * i, y])
            can_move.append([x - m * i, y])
    elif qizi[0] == '兵':
        if color == 'red':
            if i <= y <= 5 * i:
                can_move += [[x, y + i]]
            else:
                can_move += [[x + i, y], [x - i, y], [x, y + i]]
        elif color == 'black':
            if 6 * i <= y <= 10 * i:
                can_move += [[x, y - i]]
            else:
                can_move += [[x - i, y], [x + i, y], [x, y - i]]
    return can_move


# 判断棋子是否可以走该位置
def weizhi_able(qizi, color, x, y, d_x, d_y):
    can_move = move_rules(qizi, color, x, y)
    if [d_x, d_y] in can_move:
        if qizi == '将' or qizi == '帅' or qizi[0] == '士':
            if ((i <= d_y <= 3 * i and 4 * i <= d_x <= 6 * i) or (8 * i <= d_y <= 10 * i and 4 * i <= d_x <= 6 * i)):
                return True
        elif qizi[0] == '相':
            if (i <= d_y <= 5 * i):
                if weizhi_panduan(x - i, y - i) and [d_x, d_y] == [x - 2 * i, y - 2 * i]:
                    return False
                elif weizhi_panduan(x + i, y - i) and [d_x, d_y] == [x + 2 * i, y - 2 * i]:
                    return False
                elif weizhi_panduan(x + i, y + i) and [d_x, d_y] == [x + 2 * i, y + 2 * i]:
                    return False
                elif weizhi_panduan(x - i, y + i) and [d_x, d_y] == [x - 2 * i, y + 2 * i]:
                    return False
                else:
                    return True
        elif qizi[0] == '象':
            if (6 * i <= d_y <= 10 * i):
                if weizhi_panduan(x - i, y - i) and [d_x, d_y] == [x - 2 * i, y - 2 * i]:
                    return False
                elif weizhi_panduan(x + i, y - i) and [d_x, d_y] == [x + 2 * i, y - 2 * i]:
                    return False
                elif weizhi_panduan(x + i, y + i) and [d_x, d_y] == [x + 2 * i, y + 2 * i]:
                    return False
                elif weizhi_panduan(x - i, y + i) and [d_x, d_y] == [x - 2 * i, y + 2 * i]:
                    return False
                else:
                    return True
        elif qizi[0] == '马':
            if weizhi_panduan(x, y - i) and ([d_x, d_y] == [x - i, y - 2 * i] or [d_x, d_y] == [x + i, y - 2 * i]):
                return False
            elif weizhi_panduan(x + i, y) and ([d_x, d_y] == [x + 2 * i, y - i] or [d_x, d_y] == [x + 2 * i, y + i]):
                return False
            elif weizhi_panduan(x, y + i) and ([d_x, d_y] == [x - i, y + 2 * i] or [d_x, d_y] == [x + i, y + 2 * i]):
                return False
            elif weizhi_panduan(x - i, y) and ([d_x, d_y] == [x - 2 * i, y - i] or [d_x, d_y] == [x - 2 * i, y + i]):
                return False
            else:
                return True
        elif qizi[0] == '兵':
            return True
        elif qizi[0] == '车':
            count = 0
            if d_y == y:
                weizhicha = abs(d_x - x)
                for j in range(50, weizhicha, 50):
                    if weizhi_panduan(min(d_x, x) + j, y):
                        count += 1
                if count == 0 and weizhi_panduan(d_x, d_y) and find(d_x, d_y)[2] != color:
                    return True
                elif count == 0 and not weizhi_panduan(d_x, d_y):
                    return True
                else:
                    return False
            elif d_x == x:
                weizhicha = abs(d_y - y)
                for j in range(50, weizhicha, 50):
                    if weizhi_panduan(x, min(d_y, y) + j):
                        count += 1
                if count == 0 and weizhi_panduan(d_x, d_y) and find(d_x, d_y)[2] != color:
                    return True
                elif count == 0 and not weizhi_panduan(d_x, d_y):
                    return True
                else:
                    return False
        elif qizi[0] == '炮':
            count = 0
            if d_y == y:
                weizhicha = abs(d_x - x)
                for j in range(50, weizhicha, 50):
                    if weizhi_panduan(min(d_x, x) + j, y):
                        count += 1
                if count == 1 and weizhi_panduan(d_x, d_y) and find(d_x, d_y)[2] != color:
                    return True
                elif count == 0:
                    if weizhi_panduan(d_x, d_y):
                        return False
                    else:
                        return True
                else:
                    return False
            elif d_x == x:
                weizhicha = abs(d_y - y)
                for j in range(50, weizhicha, 50):
                    if weizhi_panduan(x, min(d_y, y) + j):
                        count += 1
                if count == 1 and weizhi_panduan(d_x, d_y) and find(d_x, d_y)[2] != color:
                    return True
                elif count == 0:
                    if weizhi_panduan(d_x, d_y):
                        return False
                    else:
                        return True
                else:
                    return False
    else:
        return False


# 绘制提示器
def Tishi(screen, s):
    font1 = pygame.font.Font('C:\Windows\Fonts\STXINWEI.TTF', 30)
    text = font1.render(s, True, (100, 100, 100))
    screen.blit(text, (500, 100))
    pygame.display.flip()


# 绘制选棋提示器
def Qizi_tishi(screen, x, y):
    color = (100, 100, 100)
    pygame.draw.aalines(screen, color, False, [(x - 15, y - 25), (x - 25, y - 25), (x - 25, y - 15)], 3)
    pygame.draw.aalines(screen, color, False, [(x + 15, y - 25), (x + 25, y - 25), (x + 25, y - 15)], 3)
    pygame.draw.aalines(screen, color, False, [(x - 15, y + 25), (x - 25, y + 25), (x - 25, y + 15)], 3)
    pygame.draw.aalines(screen, color, False, [(x + 15, y + 25), (x + 25, y + 25), (x + 25, y + 15)], 3)


def main():
    global hongqi, heiqi, i, r
    screen = pygame.display.set_mode([640, 560])  # 创建一个窗口
    pygame.display.set_caption("中国象棋")  # 设置窗口标题
    # 棋子初始位置
    hongqi = {'帅': {'color': 'red', 'weizhi': [250, 50]},
              '士1': {'color': 'red', 'weizhi': [200, 50]},
              '士2': {'color': 'red', 'weizhi': [300, 50]},
              '相1': {'color': 'red', 'weizhi': [150, 50]},
              '相2': {'color': 'red', 'weizhi': [350, 50]},
              '马1': {'color': 'red', 'weizhi': [100, 50]},
              '马2': {'color': 'red', 'weizhi': [400, 50]},
              '车1': {'color': 'red', 'weizhi': [50, 50]},
              '车2': {'color': 'red', 'weizhi': [450, 50]},
              '炮1': {'color': 'red', 'weizhi': [100, 150]},
              '炮2': {'color': 'red', 'weizhi': [400, 150]},
              '兵1': {'color': 'red', 'weizhi': [50, 200]},
              '兵2': {'color': 'red', 'weizhi': [150, 200]},
              '兵3': {'color': 'red', 'weizhi': [250, 200]},
              '兵4': {'color': 'red', 'weizhi': [350, 200]},
              '兵5': {'color': 'red', 'weizhi': [450, 200]}
              }
    heiqi = {'将': {'color': 'black', 'weizhi': [250, 500]},
             '士1': {'color': 'black', 'weizhi': [200, 500]},
             '士2': {'color': 'black', 'weizhi': [300, 500]},
             '象1': {'color': 'black', 'weizhi': [150, 500]},
             '象2': {'color': 'black', 'weizhi': [350, 500]},
             '马1': {'color': 'black', 'weizhi': [100, 500]},
             '马2': {'color': 'black', 'weizhi': [400, 500]},
             '车1': {'color': 'black', 'weizhi': [50, 500]},
             '车2': {'color': 'black', 'weizhi': [450, 500]},
             '炮1': {'color': 'black', 'weizhi': [100, 400]},
             '炮2': {'color': 'black', 'weizhi': [400, 400]},
             '兵1': {'color': 'black', 'weizhi': [50, 350]},
             '兵2': {'color': 'black', 'weizhi': [150, 350]},
             '兵3': {'color': 'black', 'weizhi': [250, 350]},
             '兵4': {'color': 'black', 'weizhi': [350, 350]},
             '兵5': {'color': 'black', 'weizhi': [450, 350]}
             }
    # 用来存储所有棋子信息
    b = []
    print(hongqi.keys())
    b0 = copy.deepcopy([hongqi, heiqi])
    b.append(b0)
    print(b)
    # 定义两个存储棋子现在的状态
    b1 = []
    b2 = []
    working = True  # 用于游戏结束后停止棋子操作
    order = True  # 用于控制顺序
    running = True  # 用与选棋与落棋
    Draw_qipan_with_qizi(screen)
    while True:
        # 对局提示
        if working:  # 对局未结束
            if order:
                color = 'red'
                Tishi(screen, '红棋落子')
            else:
                color = 'black'
                Tishi(screen, '黑棋落子')
        else:  # 对局结束
            if '帅' not in hongqi.keys():
                Tishi(screen, '黑棋胜利！')
            if '将' not in heiqi.keys():
                Tishi(screen, '红棋胜利！')
        # 监听所有事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击x则关闭窗口
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:  # 点击窗口内则完成相应指令
                if event.button == 1:
                    x, y = event.pos[0], event.pos[1]
                    if working:  # 对局未结束
                        if running:  # running == True 时选棋
                            x, y = event.pos[0], event.pos[1]
                            if find(x, y)[0]:  # 判断是否选择棋子
                                if find(x, y)[2] == 'red':  # 选择棋子为红色时
                                    b1 = [find(x, y)[1], hongqi[find(x, y)[1]]]
                                    Qizi_tishi(screen, b1[1]['weizhi'][0], b1[1]['weizhi'][1])
                                    running = not running
                                else:  # 选择棋子为黑色时
                                    b2 = [find(x, y)[1], heiqi[find(x, y)[1]]]
                                    Qizi_tishi(screen, b2[1]['weizhi'][0], b2[1]['weizhi'][1])
                                    running = not running
                        else:  # not running == True 时落棋
                            if r < event.pos[0] < 450 + r and r < event.pos[1] < 500 + r:
                                x = (event.pos[0] + r) // 50 * 50
                                y = (event.pos[1] + r) // 50 * 50
                                if b1:  # 红棋
                                    if weizhi_able(b1[0], b1[1]['color'], b1[1]['weizhi'][0], b1[1]['weizhi'][1], x,
                                                   y) and order:  # 判断是否符合走棋规则
                                        if weizhi_panduan(x, y):  # 所走位置有棋子
                                            if b1[1]['color'] != find(x, y)[1]:  # 判断是否为敌方棋子
                                                heiqi.pop(find(x, y)[1])
                                                hongqi[b1[0]]['weizhi'] = [x, y]
                                                b0 = copy.deepcopy([hongqi, heiqi])
                                                b.append(b0)
                                                order = not order
                                        else:  # 所走位置没有棋子
                                            hongqi[b1[0]]['weizhi'] = [x, y]
                                            b0 = copy.deepcopy([hongqi, heiqi])
                                            b.append(b0)
                                            order = not order
                                    b1 = []
                                    running = not running
                                    if '将' not in heiqi.keys():
                                        working = False
                                elif b2:  # 黑棋
                                    if weizhi_able(b2[0], b2[1]['color'], b2[1]['weizhi'][0], b2[1]['weizhi'][1], x,
                                                   y) and not order:  # 判断是否符合走棋规则
                                        if weizhi_panduan(x, y):  # 所走位置有棋子
                                            if b2[1]['color'] != find(x, y)[2]:  # 判断是否为敌方棋子
                                                hongqi.pop(find(x, y)[1])
                                                heiqi[b2[0]]['weizhi'] = [x, y]
                                                b0 = copy.deepcopy([hongqi, heiqi])
                                                b.append(b0)
                                                order = not order
                                        else:  # 所走位置没有棋子
                                            heiqi[b2[0]]['weizhi'] = [x, y]
                                            b0 = copy.deepcopy([hongqi, heiqi])
                                            b.append(b0)
                                            order = not order
                                    b2 = []
                                    running = not running
                                    if '帅' not in hongqi.keys():
                                        working = False
                            else:
                                if b1:
                                    b1 = []
                                    running = not running
                                elif b2:
                                    b2 = []
                                    running = not running
                            Draw_qipan_with_qizi(screen)
                    if 500 < x < 620 and 300 < y < 340:  # 点击‘重新开始’
                        main()
                    elif 500 < x < 620 and 400 < y < 440:  # 点击‘退出游戏’
                        pygame.quit()
                        sys.exit()
                    elif 500 < x < 620 and 200 < y < 240 and len(b) > 1:  # 点击‘悔棋’
                        del b[len(b) - 1]
                        hongqi = copy.deepcopy(b[-1][0])
                        heiqi = copy.deepcopy(b[-1][1])
                        Draw_qipan_with_qizi(screen)
                        working = True  # 在游戏结束时可以悔棋
                        order = not order  # 切换顺序
                        x, y = 0, 0  # 悔棋完成，阻止再次悔棋


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()

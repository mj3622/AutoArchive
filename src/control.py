import os
import time
from src import vision

right_top_point = [1880, 30]
left_mid_point = [80, 600]
right_down_point = [1720, 1010]


# 跳过进入游戏前的界面
def clickBeginMenu():
    # 每3s进行一次检测，循环检测30次
    # 假如检测到内容，则进行点击开始并且等待20s加载时间
    # 假如检测失败，则结束并报错
    for i in range(30):
        if vision.checkContext('MENU', 30, 920, 140, 85):
            clickMouse(right_top_point[0], right_top_point[1])
            time.sleep(20)
            return
        else:
            time.sleep(3)
    print('Out of times, pls try again')
    exit(0)


# 返回游戏主界面
def backMainPage():
    while not vision.isMainPage():
        clickMouse(right_top_point[0], right_top_point[1])
        time.sleep(1)

    clickMouse(left_mid_point[0], left_mid_point[1])

    time.sleep(0.5)


# 跳过进入游戏后的签到、活动通知等内容
def passFirstInfo():
    while not vision.checkContext('内川', 1390, 930, 360, 65):
        clickMouse(left_mid_point[0], left_mid_point[1])
    clickMouse(left_mid_point[0], left_mid_point[1])
    time.sleep(2)
    clickMouse(left_mid_point[0], left_mid_point[1])


# 进入工作页面
def enterWorkPage():
    backMainPage()

    # 进入工作界面
    clickMouse(1780, 850)

    # 检测是否到达工作界面，循环判断直到确认到达
    for i in range(10):
        if vision.checkContext('お仕事', 145, 5, 150, 60):
            return
        clickMouse(1780, 850)
        time.sleep(0.4)
    print('out of time in entering work page, pls try again')
    backMainPage()
    exit(0)


# 跳过领取奖励后出现的动画只对“报酬获取”
def skipRewardEffect():
    # 检测是否弹出窗口（双重判断，防止出现识别错误）
    for i in range(5):
        if vision.checkContext('報', 700, 170, 525, 150) or vision.checkContext('得', 700, 170, 525, 150):
            break

    # 跳过动画
    clickMouse(right_down_point[0], right_down_point[1])
    time.sleep(0.3)


# 在编队界面时点击右下角的出击
def goAttack():
    while not vision.checkContext('出撃', 1680, 950, 270, 120):
        pass
    clickMouse(1750, 1000)


# 控制鼠标点击(x,y)
def clickMouse(x, y):
    os.system('adb -s 127.0.0.1:16384 shell input tap ' + str(x) + ' ' + str(y))


# 按下esc键
def clickESC():
    os.system('adb -s 127.0.0.1:16384 shell input keyevent 111')


# 滑动屏幕，从(fx,fy)->(dx,dy)
def scrollScreen(fx, fy, dx, dy):
    os.system('adb -s 127.0.0.1:16384 shell input swipe ' + str(fx) + ' ' + str(fy) + ' ' + str(dx) + ' ' + str(dy))


# 点击弹出的Ok
def clickOK():
    clickMouse(1150, 750)


# 扫荡结束前后都将停留在扫荡画面(0代表MAX)
def sweepMission(cnt):
    time.sleep(0.5)
    # 确定刷取次数
    if cnt > 0:
        for i in range(cnt - 1):
            clickMouse(1525, 445)
            time.sleep(0.1)
    else:
        clickMouse(1620, 450)
        time.sleep(1)

    # 确认扫荡
    clickMouse(1400, 600)
    time.sleep(0.5)
    clickOK()

    while not vision.checkContext('掃', 850, 115, 210, 65):
        pass

    # 退出奖励界面
    for i in range(5):
        clickMouse(208, 566)
        time.sleep(0.1)

    time.sleep(2)

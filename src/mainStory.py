import time

import control
import vision


# 进入主线界面
def enterMainStory():
    control.enterWorkPage()
    control.clickMouse(1222, 400)
    time.sleep(2)


# 前往特定区域
def goArea(des):
    now = getNowChapter()
    dif = abs(des - now)
    for i in range(dif):
        if des - now > 0:
            goNextChapter()
        else:
            goPreChapter()


# 获取当前处于的章节，若识别失败会往后走一章
def getNowChapter():
    temp = vision.getContext(155, 233, 117, 105)
    if len(temp) > 1:
        return int(temp[1])
    else:
        goNextChapter()
        return getNowChapter()


# 去下一章
def goNextChapter():
    control.clickMouse(1868, 537)
    time.sleep(0.2)


# 去上一章
def goPreChapter():
    control.clickMouse(48, 540)
    time.sleep(0.2)


# 扫荡普通图
def sweepNormal(area, mission, cnt):
    # 选择normal模式
    control.clickMouse(1200, 240)
    time.sleep(0.5)

    # 前往对应区域
    goArea(area)

    # 向下拉列表，保证坐标不乱
    control.scrollScreen(1300, 350, 1300, 800)

    # 进入选择的mission
    control.clickMouse(1670, 340 + (mission - 1) * 149)

    # 开始扫荡
    control.sweepMission(cnt)

    # 推出扫荡界面
    control.clickESC()
    time.sleep(1)


# 扫荡困难图
def sweepHard(area, mission, cnt):
    # 选择hard模式
    control.clickMouse(1600, 240)
    time.sleep(0.5)

    # 前往对应区域
    goArea(area)

    # 进入选择的mission
    control.clickMouse(1670, 375 + (mission - 1) * 170)

    # 开始扫荡
    control.sweepMission(cnt)

    # 推出扫荡界面
    control.clickESC()
    time.sleep(1)

import time

from src import control, vision


# 进入课程表界面（外部不要调用）
def enterSchedule():
    # 返回主界面
    control.backMainPage()

    # 进入课程表界面
    control.clickMouse(310, 990)
    time.sleep(2)


# 获取剩余的次数
def getLeftChance():
    text = vision.getContext(285, 120, 70, 60)
    return int(text[0][0])


# 进入特定的地区（共9个，从上到下为1~9）
def enterArea(number):
    # 进入界面
    enterSchedule()
    # 向上滑动，确保在最顶端
    control.scrollScreen(1350, 220, 1350, 1000)
    time.sleep(0.2)

    # 上下两栏的偏移量
    dy = 160

    # 若为前五个学院则位于第一页，否则要进行翻页操作
    if number <= 5:
        control.clickMouse(1350, 285 + (number - 1) * dy)
    else:
        control.scrollScreen(1350, 1000, 1350, 220)
        time.sleep(1)
        control.clickMouse(1350, 285 + (number - 5) * dy)

    # 进入后等待加载
    time.sleep(2)


# 选择课程上课从左到右，从上到下，number分别为1~9
def takeClass(number):
    # 检测是否位于选课界面
    while not isSelectClassPage():
        control.clickMouse(1750, 1000)
        time.sleep(2)

    # 选择对应课程
    control.clickMouse(600 + ((number - 1) % 3) * 500, 360 + ((number - 1) // 3) * 220)
    time.sleep(2)

    # 进行上课
    control.clickMouse(947, 843)
    time.sleep(2)


# 检查是否位于课程表界面
def isSchedulePage():
    return vision.checkContext('スケ', 150, 5, 256, 55)


# 检测是否位于选课界面（九宫格）
def isSelectClassPage():
    return vision.checkContext('すべて', 730, 145, 460, 65)

import time

from src import control


# 进入子工作区域，即指名手配、特别依赖、学园交流会
def enterSubWorkPage(number):
    control.enterWorkPage()
    control.clickMouse(1100, 640 + 125 * (number - 1))
    time.sleep(2)


# 选择要进入的Location/Request/Academy (1,2,3分别表示从上到下的三个/两个)
def selectLRA(num):
    control.clickMouse(1345, 300 + (num - 1) * 165)
    time.sleep(1)


# 刷取 学院n 素材 cnt次(都是刷最高难度)
def getAcademyMaterial(number, cnt):
    # 选择区域
    selectLRA(number)

    # 进入关卡
    control.clickMouse(1675, 950)
    time.sleep(1)

    # 开始扫荡
    control.sweepMission(cnt)

    # 返回到选择区域的界面
    control.clickESC()
    time.sleep(2)
    control.clickESC()
    time.sleep(1.5)


# 刷取 专武n 素材 cnt次(都是刷最高难度)
def getWeaponMaterial(number, cnt):
    # 选择区域
    selectLRA(number)

    # 进入关卡
    control.clickMouse(1666, 730)
    time.sleep(1)

    # 开始扫荡
    control.sweepMission(cnt)

    # 返回到选择区域的界面
    control.clickESC()
    time.sleep(2)
    control.clickESC()
    time.sleep(1.5)

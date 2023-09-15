# 检测是否满足收取钻石的条件
import time

from src import vision, control


def isReceiveDiamond():
    rank = getRank()
    if rank == 1 or getLeftChance() == 0:
        return True
    elif rank > 4:
        return False
    else:
        attackPlayer(1)
        return True


# 获取当前排名
def getRank():
    text = vision.getContext(190, 435, 120, 75)
    # 获取排名
    return int(text[0][0:-1])


# 检测剩余挑战次数
def getLeftChance():
    text = vision.getContext(300, 711, 70, 45)
    # 获取次数
    return int(text[0][0])


# 攻击玩家1/2/3
def attackPlayer(number):
    # 选择挑战对手
    control.clickMouse(1000, 350 + (number - 1) * 250)

    # 进入挑战界面
    while not vision.checkContext('相手', 850, 120, 210, 65):
        pass

    # 开始作战
    control.clickMouse(960,860)
    time.sleep(1)
    control.goAttack()

    # 确认作战结果
    while not vision.checkContext('確認', 890, 760, 140, 80):
        pass
    control.clickMouse(960,790)

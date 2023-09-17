import time
from src import vision, pvp
from src.control import backMainPage, clickMouse, enterWorkPage, skipRewardEffect


# 用于领取完成日常任务的奖励
def receiveMissionReward():
    backMainPage()

    # 进入任务面板
    clickMouse(95, 350)

    # 等待加载时间
    time.sleep(2)

    # 领取任务奖励（一键领取）
    clickMouse(1720, 1010)
    time.sleep(2)
    clickMouse(1720, 1010)

    time.sleep(2)

    # 领取一次领取完后出现的第二次奖励
    clickMouse(1720, 1010)
    time.sleep(2)
    clickMouse(1720, 1010)

    # 缓冲时间
    time.sleep(2)

    # 领取20石头
    clickMouse(1450, 1000)
    time.sleep(2)
    clickMouse(1450, 1000)

    backMainPage()


# 领取咖啡厅的奖励
def receiveCoffeeReward():
    backMainPage()

    # 进入咖啡厅
    clickMouse(135, 985)
    time.sleep(3)

    # 进入领取界面
    while not vision.checkContext('受取', 900, 750, 120, 70):
        clickMouse(1722, 972)
        time.sleep(1)

    # 领取奖励
    clickMouse(955, 780)

    backMainPage()


# 领取邮箱中的奖励
def receiveMailReward():
    backMainPage()

    # 进入邮箱
    clickMouse(1750, 55)
    time.sleep(2)

    # 领取奖励
    clickMouse(1720, 1010)

    # 返回主界面
    backMainPage()


# 领取社团奖励
def receiveCircleReward():
    backMainPage()

    # 进入社团界面
    clickMouse(840, 975)
    time.sleep(2)

    # 自动领取完毕返回主界面
    backMainPage()


# 领取PVP奖励
def receivePVPReward():
    backMainPage()

    # 进入工作界面
    enterWorkPage()

    # 进入PVP界面
    clickMouse(1622, 876)
    while not vision.checkContext('戦術対抗戦', 145, 5, 530, 60):
        pass

    # 领取信用点奖励
    clickMouse(532, 583)
    skipRewardEffect()

    # 检查是否是可以领取钻石（是第一位 或 还有剩余攻击次数， 如果满足条件则领取
    if pvp.isReceiveDiamond():
        clickMouse(532, 709)
        skipRewardEffect()

    # 返回主界面
    backMainPage()

import time

from src import control


def enterShop():
    control.backMainPage()

    # 进入商店界面
    control.clickMouse(1190, 980)

    # 等待加载
    time.sleep(2)


# 购买经验书
def buyLevelBook():
    chooseFilter(1)

    # 选择商品
    for i in range(4):
        control.clickMouse(1050 + i * 230, 380)
        time.sleep(0.2)

    # 点击购买
    control.clickMouse(1760, 1000)
    time.sleep(0.5)

    # 确认购买
    control.clickMouse(1150, 730)
    control.skipRewardEffect()


# 购买欧帕兹
def buyMaterial():
    chooseFilter(3)

    # 选择商品
    for i in range(4):
        control.clickMouse(1050 + i * 230, 380)
        time.sleep(0.2)

    # 点击购买
    control.clickMouse(1760, 1000)
    time.sleep(0.5)

    # 确认购买
    control.clickMouse(1150, 730)
    control.skipRewardEffect()


# 买强化珠
def buyEquipmentBall():
    chooseFilter(2)

    # 选择商品
    for i in range(4):
        control.clickMouse(1050 + i * 230, 380)
        time.sleep(0.2)

    control.scrollScreen(1340, 840, 1340, 290)
    time.sleep(0.5)

    for i in range(4):
        control.clickMouse(1050 + i * 230, 330)
        time.sleep(0.2)

    for i in range(4):
        control.clickMouse(1050 + i * 230, 770)
        time.sleep(0.2)

    # 点击购买
    control.clickMouse(1760, 1000)
    time.sleep(0.5)

    # 确认购买
    control.clickMouse(1150, 730)
    control.skipRewardEffect()


# 进行商店中的内容过滤 1-经验书，2-强化珠，3-材料
def chooseFilter(num):
    # 进行过滤
    control.clickMouse(1735, 125)
    time.sleep(1)

    # 重置选择
    control.clickMouse(1660, 250)
    time.sleep(0.5)

    # 选择需要购买的过滤
    control.clickMouse(435 + 345 * (num - 1), 400)
    time.sleep(0.5)

    # 确认选择
    control.clickMouse(1120, 900)
    time.sleep(1)


# 购买体力
def buyAP(num):
    # 进入购买AP页面
    control.clickMouse(150, 765)
    time.sleep(1)

    # 进行过滤
    chooseFilter(2)

    for i in range(2):
        control.clickMouse(1050 + i * 230, 380)
        time.sleep(0.2)

    # 点击购买
    control.clickMouse(1760, 1000)
    time.sleep(0.5)

    # 确认购买
    control.clickMouse(1150, 730)
    control.skipRewardEffect()

    if num > 1:
        control.clickMouse(1760, 1000)
        time.sleep(0.5)
        control.clickMouse(1150, 730)
        buyAP(num-1)
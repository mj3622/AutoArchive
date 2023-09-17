import control
import mainStory
import pvp
import reward
import schedule
import shop
import vision
import work


# 每日商店的技能书，欧帕兹和体力
def dailyShop():
    shop.enterShop()

    shop.buyLevelBook()
    shop.buyMaterial()

    shop.buyAP(4)

    control.backMainPage()


# 每日的困难刷图
def dailyHard():
    mainStory.enterMainStory()
    mainStory.sweepHard(14, 3, 0)


# 每日最后领取奖励并更新数据
def dailyFinalRecord():
    reward.receiveMissionReward()
    vision.renewCurrency()


# 每日的咖啡厅日常
def dailyCoffee():
    reward.receiveCoffeeReward()


# 每日社团+邮箱
def dailyReceive():
    reward.receiveCircleReward()
    reward.receiveMailReward()


# 每日PVP
def dailyPVP():
    reward.receivePVPReward()


# 每日工作日常
def dailyWork():
    # 刷武器素材
    work.enterSubWorkPage(3)
    work.getWeaponMaterial(1, 0)

    # 刷学院素材
    work.enterSubWorkPage(1)
    work.getAcademyMaterial(1, 6)
    work.getAcademyMaterial(2, 6)
    work.getAcademyMaterial(3, 6)


# 每日课程表
def dailySchedule():
    schedule.enterArea(4)
    schedule.takeClass(6)
    schedule.takeClass(7)
    schedule.takeClass(8)

    schedule.enterArea(7)
    schedule.takeClass(7)

    schedule.enterArea(8)
    schedule.takeClass(7)

    schedule.enterArea(9)
    schedule.takeClass(7)
    schedule.takeClass(6)
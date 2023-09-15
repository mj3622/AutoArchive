import data
import os
import control
from src import vision, reward

# 用于存储任务队列
tasks = list()


def init():
    # 防止adb出问题
    os.system('adb kill-server')
    os.system('adb start-server')

    # 连接adb
    os.system('adb.exe connect 127.0.0.1:16384')

    # 初始化数据库
    data.initDatabase()

    # 打开游戏
    os.system('MuMuManager.exe api -v 0 launch_app com.YostarJP.BlueArchive')


def begin():
    # 过开始界面
    control.clickBeginMenu()

    # 跳过公告、签到等一系列弹窗
    control.passFirstInfo()

    reward.receiveCoffeeReward()
    reward.receiveMailReward()
    reward.receiveCircleReward()
    reward.receivePVPReward()
    reward.receiveMissionReward()


if __name__ == '__main__':
    init()
    begin()
    for task in tasks:
        pass

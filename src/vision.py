import os
import cv2
import easyocr
from src import data

image_path = '../source/temp.png'


def renewCurrency():
    getPic()

    # 创建一个识别器进行识别
    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(resizePic(1000, 20, 600, 70), detail=0)

    # 取出识别结果：信用点 钻石
    money = results[0]
    diamond = results[1]

    # 更新到数据库中去
    data.updateCurrency(money, diamond)


# 检测在区域[x,y,width,height]中是否存在text内容
def checkContext(text, x, y, width, height):
    # 获取图片
    getPic()

    # 进行OCR识别，读取图片中的内容
    reader = easyocr.Reader(['en', 'ja'], gpu=False)
    result = reader.readtext(resizePic(x, y, width, height), detail=0)
    print(result)
    return len([item for item in result if text in item])


# 识别对应区域的内容
def getContext(x, y, width, height):
    # 获取图片
    getPic()

    # 进行OCR识别，读取图片中的内容
    reader = easyocr.Reader(['en', 'ja'], gpu=False)
    return reader.readtext(resizePic(x, y, width, height), detail=0)


# 检测是否位于主界面
def isMainPage():
    return checkContext("カフ", 90, 1010, 100, 50)


# 截取模拟器当前的显示图片并储存为temp.png
def getPic():
    os.system(r'adb -s 127.0.0.1:16384 exec-out screencap -p > ../source/temp.png')


# 裁切图片尺寸
def resizePic(x, y, width, height):
    return cv2.imread(image_path)[y:y + height, x:x + width]


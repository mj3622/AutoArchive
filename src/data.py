# 指定数据库文件路径
import os
import sqlite3
from datetime import date

db_file_path = '../source/archiveData.db'


def initDatabase():
    # 检测数据库文件是否存在
    if not os.path.exists(db_file_path):
        # 创建数据库连接
        conn = sqlite3.connect(db_file_path)
        # 创建游标对象
        cursor = conn.cursor()

        # 创建currency表
        cursor.execute('''
            CREATE TABLE currency (
                key INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                money INTEGER,
                diamond INTEGER
            )
        ''')

        # 提交事务
        conn.commit()

        # 关闭游标和连接
        cursor.close()


def updateCurrency(money, diamond):
    # 创建数据库连接
    conn = sqlite3.connect(db_file_path)

    # 创建游标对象
    cursor = conn.cursor()

    # 插入数据
    cursor.execute("INSERT INTO currency (date, money, diamond) VALUES (?, ?, ?)",
                   (str(date.today()), int(money.replace(",", "")), int(diamond.replace(",", ""))))

    # 提交事务
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()

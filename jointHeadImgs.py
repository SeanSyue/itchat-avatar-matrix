# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# __author__='阳光流淌007'
# __date__ = '2018-03-06'
"""
https://zhuanlan.zhihu.com/p/34290391
"""
import os
from math import sqrt
from PIL import Image

PATH = './avatars'  # 存放好友头像图的文件夹的路径
SIZE = 128  # 每个头像图的大小

# 获取好友头像图的位置
pathList = [os.path.join(PATH, imgPath) for imgPath in os.listdir(PATH) if imgPath.endswith('.jpg')]

total = len(pathList)  # total是好友头像图片总数
line = int(sqrt(total))  # line是拼接图片的行数（即每一行包含的图片数量）
x = y = 0

NewImage = Image.new('RGB', (SIZE * line, SIZE * line))
for item in pathList:
    try:
        img = Image.open(item)
        img = img.resize((SIZE, SIZE), Image.ANTIALIAS)
        NewImage.paste(img, (x * SIZE, y * SIZE))
        x += 1
    except IOError:
        print("第%d行,%d列文件读取失败！IOError:%s" % (y, x, item))
        x -= 1
    if x == line:
        x = 0
        y += 1
    if (x + line * y) == line * line:
        break
NewImage.save("final.jpg")

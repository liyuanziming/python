# -*- coding: UTF-8 -*-
#实验效果：控制掌控板板载RGB灯
#接线：使用windows或linux电脑连接一块掌控板主控板

import time
import random
from pinpong.board import Board
from pinpong.extension.handpy import *

#Board("handpy").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("handpy","COM36").begin()   #windows下指定端口初始化
Board("handpy","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("handpy","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化
while True:
    i=random.randint(100,255)
    j=random.randint(200,255)
    k=random.randint(100,255)
    rgb[0] = (i,j,k)  # 设置为红色，全亮度
    rgb.write()
    time.sleep(0.1)
    rgb[1] = (i,j,k)  # 设定为绿色，一半亮度
    rgb.write()
    time.sleep(0.1)
    rgb[2] = (i,j,k)   # 设置为蓝色，四分之一亮度
    rgb.write()
    time.sleep(0.1)
    i=random.randint(0,100)
    j=random.randint(0,50)
    k=random.randint(0,100)
    rgb[2] = (i,j,k)  # 设置为红色，全亮度
    rgb.write()
    time.sleep(0.1)
    rgb[1] = (i,j,k)  # 设定为绿色，一半亮度
    rgb.write()
    time.sleep(0.1)
    rgb[0] = (i,j,k)   # 设置为蓝色，四分之一亮度
    rgb.write()
    time.sleep(0.1)

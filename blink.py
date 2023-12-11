# -*- coding: UTF-8 -*-
#实验效果：控制arduino UNO板载LED灯一秒闪烁一次
#接线：使用windows或linux电脑连接一块arduino主控板
import time
from pinpong.board import Board,Pin

   #windows下指定端口初始化
Board("uno","/dev/ttyACM0").begin() #linux下指定端口初始化
#Board("uno","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化


led = Pin(Pin.D4, Pin.OUT) #引脚初始化为电平输出

while True:
  #led.value(1) #输出高电平 方法1
  led.write_digital(1) #输出高电平 方法2
  print("1") #终端打印信息
  time.sleep(1) #等待1秒 保持状态

  #led.value(0) #输出低电平 方法1
  led.write_digital(0) #输出低电平 方法2
  print("0") #终端打印信息
  time.sleep(1) #等待1秒 保持状态

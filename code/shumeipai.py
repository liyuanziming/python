import RPi.GPIO as GPIO # 导入Rpi.GPIO库函数命名为GPIO

import time # 导入计时time函数



GPIO.setmode(GPIO.BOARD) #将GPIO编程方式设置为BOARD模式

GPIO.setup(4, GPIO.OUT) #设置物理引脚11负责输出电压



while True: #条件符合，执行以下程序循环

    GPIO.output(11, GPIO.HIGH) #11号引脚输出高电平

    time.sleep(0.5) #计时0.5秒

    GPIO.output(11, GPIO.LOW) #11号引脚输出低电平

    time.sleep(1) #计时1秒

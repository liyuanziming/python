from utils.detect_face import *
from utils.hat import *
import time

for i in range(1,15):
    url = "face/"+str(i)+".jpg" # 指定图像路径
    img = get_image(url) # 获取路径url下的图像，并将图像存储在变量中

    gender, age = predict_age_and_gender(img) # 获取指定图像中人的性别，年龄，使用变量gender、age接收
    print(f"图像中人脸的性别为：{gender}") # 输出gender变量的值
    print(f"图像中人脸的年龄段为：{age}") # 输出age变量的值

    # 根据年龄采用分支结构进行推荐
    if gender == 'Male': # 如果性别为男，属于规则1
        hat_recommend(img, "8.jpg") # 推荐编号为"8.jpg"的帽子
    else:
        hat_recommend(img, "62.jpg")
        time.sleep(3)

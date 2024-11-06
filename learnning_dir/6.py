#输入三维空间两点坐标（x,y,z），计算两点之间的距离并输出。

x1,y1,z1 = map(float,input().split())
x2,y2,z2 = map(float,input().split())
print("{:.2f}".format(pow((x1-x2)**2+(y1-y2)**2+(z1-z2)**2,0.5)))

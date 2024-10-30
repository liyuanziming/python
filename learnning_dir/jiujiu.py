import time
for i in range(1,10):
    j = 1
    while j <= i:
        print("%d*%d=%2d" %(j,i,i*j),end = " ")
        j +=1
        time.sleep(0.8)
    print()
    time.sleep(1)

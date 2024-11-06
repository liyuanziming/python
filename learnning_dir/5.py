#输入正整数N, 求N的平方根X。如果N不是一个完美的平方，输出floor(X)
import math
N = int(input())

x = math.sqrt(N)

if x * x !=N:
    print(int(math.floor(x)))
else:
    pring(int(x))


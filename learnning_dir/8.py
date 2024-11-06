#给定一个正整数n，求满足floor（n/x）=y的x和y (x和y是正整数)。比如输入5，则(x, y)的组合可以有:(1, 5), (2, 2), (3, 1), (4, 1), (5, 1)。不考虑负数，0或者其他特殊情况。

import math
N = int(input())

for x in range(1,N+1):
    print("%d %d" %(x,math.floor(N/x)))

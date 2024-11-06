#给定一个正整数n，求满足floor（n/x）=y的x和y的乘积之和 (x和y是正整数)。比如输入5，则(x, y)的组合可以有:(1, 5), (2, 2), (3, 1), (4, 1), (5, 1)，那么， 1 * 5 + 2 * 2 + 3 * 1 + 4 * 1 + 5 * 1 = 5 + 4 + 3 + 4 + 5 = 21。不考虑负数，0或者其他特殊情况。

import math
N = int(input())

sum =0

for x in range(1,N+1):
    sum += x*math.floor(N/x) 
print(sum)

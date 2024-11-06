#输入正整数N，求N的立方根。向下取整后输出，输出最小列宽为3列。

import math
N = int(input())

print("{:>3d}".format(int(N**(1/3))))

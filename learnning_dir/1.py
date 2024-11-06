#在一条直线上点上N(N>=1)个点可以把这条直线分成多少条射线？
#以一个点为端点向一个方向无限延伸的线叫做射线。
  # 接着考虑直线上点的情况：
  # 当直线上有1个点时，以这个点为端点向左右两个方向各能形成一条射线，共2条射线。
  # 当直线上有2个点时，以这两个点为端点分别向左右两个方向形成射线，每个点对应条射线，共4条射线。
  # 当直线上有3个点时，每个点同样对应条射线，共6条射线。
  # 最后得出结论：
  # 可以发现，直线上有N（N >=1）个点时，以每个点为端点都能向左右两个方向形成条射线，所以一共有2N条射线。
  # 综上，在一条直线上点上N个点可以把这条直线分成2N条射线

n = int(input())

print(n)

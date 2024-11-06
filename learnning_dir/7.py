#假定幸运数是只包含4或7的正整数，如7、47。判断一个正整数n是不是一个幸运数。是则输出YES，否则输出NO。不考虑负数，0或者其他特殊情况。不考虑溢出或者超出整型范围的情况。

str1 = input()
flag ="YES"

for s in str1:
    if s =="4" or s =="7":
        continue
    else:
        flag = "NO"
        break

print(flag)

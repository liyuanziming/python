#水仙花數
for number in range(100,1000):
    str_num = str(number)

    one_n=int(str_num[-1])
    ten_n=int(str_num[-2])
    hundred_n=int(str_num[-3])

    if (number == one_n**3 + ten_n**3 +hundred_n**3):
        print("     ",number)


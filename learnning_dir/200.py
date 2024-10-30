#四葉玫瑰花數

def is_rose_num(num):
    str_num = str(num)

    sum_of_powers = sum(int(digit) ** 4 for digit in str_num)

    return num == sum_of_powers

for i in range(1000,10000):
    if is_rose_num(i):
        print("      ",i)

#倒轉數字

def reverse_number(number:int):
    c_whole = 0
    
    while(number >0):
        c = number % 10 
        print(c,end = "**-**")
        c_whole = c_whole * 10 + c
        number = number // 10

    return c_whole
n = 456545

print("\nFirst way:\n",reverse_number(n))


s_n = str(n)[::-1]
print("Second way:\n",int(s_n))


def change(n,k):
    s=""
    if k ==8:
        while n >0:
            s=s+(str(n%k))
            n=n//k
        return s
    elif k == 16:
        while n >0:
            l = n%k
            if l <=9:
                s=s+(str(n%k))
                n=n//k
            elif l ==10:
                s=s+"A"
                n=n//k
            elif l == 11:
                s=s+"B"
                n=n//k
            elif l ==12:
                s=s+"C"
                n=n//k
            elif l ==13:
                s=s+"D"
                n=n//k
            elif l ==14:
                s=s+"E"
                n=n//k
            elif l ==15:
                s=s+"F"
                n=n//k
        return s
        
def main():
    #code here
    s1_8 = change(202,8)
    s1_16 = change(202,16)

    s2_8 = change(117,8)
    s2_16 = change(117,16)

    s3_8 = change(70,8)
    s3_16 = change(70,16)

    s4_8 = change(130,8)
    s4_16 = change(130,16)

    print(202,end =" ")
    print("0"+str(s1_8)[::-1],end =" ")
    print("0X"+str(s1_16)[::-1])

    print(117,end =" ")
    print("0"+str(s2_8)[::-1],end =" ")
    print("0X"+str(s2_16)[::-1])

    print(70,end =" ")
    print("0"+str(s3_8)[::-1],end =" ")
    print("0X"+str(s3_16)[::-1])

    print(130,end =" ")
    print("0"+str(s4_8)[::-1],end =" ")
    print("0X"+str(s4_16)[::-1])





if __name__ == '__main__':
    main();

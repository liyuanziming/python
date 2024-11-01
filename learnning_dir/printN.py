def printN1(n):
    if(n):
        printN1(n-1)
        print(n,end =" ")

def printN2(n):
    for i in range(n):
        print(i,end = " ")


while True:
    n =int(input())
    printN1(n)
    print("*******************************")
    printN2(n)
    print("*******************************")

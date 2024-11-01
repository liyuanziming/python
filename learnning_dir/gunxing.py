
def main():
    #code here
    R,H=map(float,input().split(" "))
    C = 2*(H*(2*R-H))**0.5

    print("{:.2f}".format(C))


if __name__ == '__main__':
    main();

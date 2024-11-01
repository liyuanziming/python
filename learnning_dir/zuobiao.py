
import math
def main():
    #code here
    PI=3.1415926
    x,y = map(float,input().split(" "))
    r = (x**2+y**2)**0.5
    theta= math.degrees(math.atan(y/x))

    print('{:.1f} {:.1f}'.format(r,theta))
    


if __name__ == '__main__':
    
    main();

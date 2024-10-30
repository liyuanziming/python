pi = 3.1415926
R,h = map(float,input().split(' '))
C = 2*R*pi
S = pi*R**2
Q = 4*pi*R**2
QT = (4/3) * pi*R**3
Z = h *pi*R**2
print('{:.2f}'.format(C))
print('{:.2f}'.format(S))
print('{:.2f}'.format(Q))
print('{:.2f}'.format(QT))
print('{:.2f}'.format(Z))

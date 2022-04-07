import math
A,B=map(int, input().split())
C=math.sqrt(A**2+B**2)
x=A/C
y=B/C
print(x," ",y)

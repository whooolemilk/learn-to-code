n=int(input())
XY=[]
for i in range(n):
  x,y=map(int,input().split())
  XY.append([x,y])
s=input()

L,R={},{}
for i in range(n):
  if s[i]=="L":
    if XY[i][1]not in L:
      L[XY[i][1]]=XY[i][0]
    else:
      L[XY[i][1]]=max(L[XY[i][1]],XY[i][0])
  if s[i]=="R":
    if XY[i][1] not in R:
      R[XY[i][1]]=XY[i][0]
    else:
      R[XY[i][1]]=min(R[XY[i][1]],XY[i][0])

for i in R.keys():
  if i in L and L[i]>R[i]:
    print("Yes")
    exit()
print("No")

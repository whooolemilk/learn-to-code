N=int(input())
A=list(map(int,input().split()))

num=0
while num<=2000:
  if num in A:
    num+=1
  else:
    print(num)
    break

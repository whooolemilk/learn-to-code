L = int(input())
n = int(input())
x = list(map(int,input().split()))

# 最大の時間の計算
maxT = 0
for i in range(n):
  maxT = max([maxT, max([x[i], L-x[i]])])

# 最少の時間の計算
minT = 0
for i in range(n):
  minT = max([minT, min([x[i], L-x[i]])])

# 答え
print(maxT)
print(minT)


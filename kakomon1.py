# input
from multiprocessing.connection import answer_challenge


N=int(input())
FX={}
for i in range(N):
  f, x = input().split()
  FX.setdefault(f,[]).append(int(x))

ans={}
for key in FX.keys():
  X=key
  L=min(FX[key])
  H=max(FX[key])
  M=sum(FX[key])//len(FX[key])
  ans[X]=[L,H,M]

sorted_ans=sorted(ans.items())

# output
print(sorted_ans)


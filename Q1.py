def Solve (N):
  factor=[]
  for i in range(1, N):
    if N % i==0:
      factor.append(i)
  s=0
  ans="NO"
  for i in factor:
    s+=i
    if s==N:
      ans="YES"
      break
    else:
      ans="NO"
  return ans

T = int(input())
for _ in range(T):
    N = int(input())
    out_ = Solve(N)
    print (out_)

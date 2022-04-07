def solve():
  n=int(input())
  ans={}
  for i in range(n):
    f,x=input().split()
    ans.setdefault(f,[]).append(int(x))
  return ans

t=int(input())

for i in range(t):
  ans = solve()
  sorted_ans=sorted(ans)
  for i in sorted_ans:
    print(i," ", min(ans[i]), max(ans[i]), sum(ans[i])//len(ans[i]))






  
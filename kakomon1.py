def solve(): # 解決処理
  N=int(input()) # F,Xの入力回数
  FX={}
  for i in range(N):
    f, x = input().split()
    FX.setdefault(f,[]).append(int(x)) # keyが同じなら追加で値が格納される
  sorted_ans=sorted(FX.items()) # keyをアルファベット順に並べる
  return sorted_ans

T=int(input()) # caseの数
for X in range(T):
  ans=solve()
  print("Case #{}".format(X+1)) # format関数
  for i in ans:
    print (i[0]," ",min(i[1])," ",max(i[1])," ",(sum(i[1])//len(i[1])))

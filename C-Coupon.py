n,k,x=map(int, input().split())
a=list(map(int,input().split()))

# xの値がn個並ぶ長さのリスト
y=[x]*n
# a//yのリストを返す
# それぞれの商品に-０円にならない範囲で最高でも何枚クーポン適用できるか
d=list(map(lambda i,j:i//j,a,y))

# n個の商品、k枚のクーポン、１枚x円
if sum(d) >= k: # クーポンが足りないとき
    ttl = sum(a) - k*x # 全額-全クーポン代を引く
elif k-sum(d) >= n: # 商品の数以上にクーポンが余っているとき
    ttl=0 # 0円
else:
    e=sorted(list(map(lambda i,j,k:i-j*k, a,d,y)), reverse=True)
    print(e)
    ttl = sum(a) - sum(d)*x - sum(e[0:k-sum(d)])
print(ttl)

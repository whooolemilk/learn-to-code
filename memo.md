### format

```py
"Case #{}".format(X+1)

"名前{myname}です。{myold}歳です。".format(myname="Yamada", myold=18)
```

{}部分に値が入ってくる！

### lambda

無名関数を作成する

```py
def add_def(a, b=1):
    return a + b

add_lambda = lambda a, b=1: a + b

print(add_def(3, 4))
# 7

print(add_def(3))
# 4

print(add_lambda(3, 4))
# 7

print(add_lambda(3))
# 4
```

### map 関数に lambda 式を適用

```py
l = [-2, -1, 0]
print(list(map(lambda x: x**2, l)))
# [4, 1, 0]
```

#### 複数のイテラブルを引数に指定

```py
l = [-2, -1, 0]
print(list(map(lambda x: x**2, l)))
# [4, 1, 0]

l_3 = [100, 200, 300, 400]
print(list(map(lambda x, y, z: x * y * z, l_1, l_2, l_3)))
# [1000, 8000, 27000]
```

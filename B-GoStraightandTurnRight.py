n=int(input())
t=str(input())

#n, e, s, w
x=0
y=0
c="e"
for i in range(len(t)):
  if t[i]=="S":
    if c=="n":
      y+=1
    elif c=="e":
      x+=1
    elif c=="s":
      y-=1
    else:
      x-=1
  else:
    if c=="n":
      c="e"
    elif c=="e":
      c="s"
    elif c=="s":
      c="w"
    else:
      c="n"

print(x,y)


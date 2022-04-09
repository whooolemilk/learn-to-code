from audioop import reverse
import collections
def Circular_str (N, S1, M, S2):
    # Write your code here
    s1=[]
    s2=[]
    for i in range(N):
        s1.append(S1[i])
    for i in range(M):
        s2.append(S2[i])
    pass
    xlist=[]
    l=[]
    for i in s2:
      if i not in s1:
        l.append(i)
      else:
        if l!=[]:
          xlist.append(l)
          l=[]
    if l!=[]:
      xlist.append(l)
    if s2[0] not in s1 and s2[-1] not in s1:
      xlist.append(xlist[0]+xlist[-1])

    l=[]        
    for i in xlist:
      maxlen=0
      m=[]
      if maxlen<len(i):
        maxlen=len(i)
        m=i
    t=s1+m
    t.sort(reverse=True)
    ans="".join(t)
    
    return ans

N = int(input())
S1 = input()
M = int(input())
S2 = input()

out_ = Circular_str(N, S1, M, S2)
print (out_)

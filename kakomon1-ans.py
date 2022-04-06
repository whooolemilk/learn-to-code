def solve():
    N=int(input())
    mat = []
    for i in range(N):
        matrix = input().split(" ")
        mat.append(matrix)

    dictx={mat[0][0]:[int(mat[0][1])]}

    for i in range (1,len(mat)):
        if mat[i][0] in dictx:
            dictx[mat[i][0]].append(int(mat[i][1]))
        else:
            dictx.update({mat[i][0]:[int(mat[i][1])]})
    return dictx    

T=int(input())
for X in range(T):
    dictx=solve()
    print("Case #{}".format(X+1))
    for i in dictx:
        print (i," ",min(dictx[i])," ",max(dictx[i])," ",(sum(dictx[i])/len(dictx[i])))

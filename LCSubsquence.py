def LCSsubs(s1, s2):
    m=len(s1)
    n=len(s2)
    
    # for i in range(m+1):
    #     for j in range(n+1):
    #         L[i][j]=None
    L = [[None]*(n+1) for i in range(m+1)]
    print(L)
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0 
            elif s1[i-1]==s2[j-1]:
                L[i][j]=L[i-1][j-1]+1 
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
  
    return L[m][n]

s1="harsh"
s2="bhardwaj"
print(LCSsubs(s1,s2))
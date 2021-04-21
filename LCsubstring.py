class soln:
    def lcsubstring(self,s1,s2):
        m=len(s1)
        n=len(s2)
        res=-1
        L = [[None]*(n+1) for i in range(m+1)]
        print(L)
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    L[i][j]=0 
                elif s1[i-1]==s2[j-1]:
                    L[i][j]=L[i-1][j-1]+1
                    res=max(L[i][j],res)
                else:
                    L[i][j]=0 
        print(L)
        return res

X = 'harsh'
Y = 'harshvs'
s=soln()
print(s.lcsubstring(X,Y))
ls=[-1,1,1,2,-2,3,3,-3]
ls.sort(reverse=True)
dic={}
for i in ls:
    if i<0:
        if i in dic:
            dic[abs(i)]=0
        else:
            dic[-1*i]=1 
    else:
        if i not in dic:  
            dic[i]=1
        else:
             dic[i]=dic.get(i,0)+1
for i in dic:
    if dic[i]==0: 
        print(i)

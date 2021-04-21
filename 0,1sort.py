ls=[1,1,0,0,1,1,0]
n=ls.count(0)

for i in range(n):
    ls[i]=0
for i in range(n,len(ls)):
    ls[i]=1 
print(ls)
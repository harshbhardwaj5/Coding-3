def even(n,s=0):
    
    if n==0:
       return s
    k=n%10
    if k%2==0:
        s+=k
       
    return even(n-1,s)

print(even(3))
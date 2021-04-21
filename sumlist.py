def maxx(arr,i,n,s):
    # print(s)
    if i>n:
        return s
    else:
        s+=arr[i]
    return maxx(arr,i+1,n,s)
    
print(maxx([1,2,3,4,5],0,4,0))
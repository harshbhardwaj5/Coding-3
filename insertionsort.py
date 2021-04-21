arr=list(map(int,input().split()))
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while(j>=0 and arr[j]>key):     #key hi use hoga cuz the value ai arr[i] has been changed
        arr[j+1]=arr[j]
        j=j-1 
    arr[j+1]=key 

print("sorted array is->"+ " ".join(map(str,arr)) )


def bubblesort(arr):
    for  i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

                swapped=True                             #swapped bubble sort
        if swapped==False:
            break
    return arr

print(bubblesort([1,2,3,2,1]))
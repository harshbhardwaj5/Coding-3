def mergeSort(nums):
   if len(nums)>1:
        mid=len(nums)//2 
        l=nums[:mid]
        r=nums[mid:]
        mergeSort(l)
        mergeSort(r)

        i=j=k=0 
        while(i<len(l) and j<len(r)):
            if l[i]<r[j]:
               nums[k]=l[i]
               i+=1
            else:
                nums[k]=r[j]
                j+=1 
            k+=1 
        while(i<len(l)):
            nums[k]=l[i]
            i+=1 
            k+=1
        while(j<len(r)):
             nums[k]=r[j]
             j+=1 
             k+=1 
        
            
        


myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)
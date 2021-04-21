def partition(arr,low,high):
	j=low-1 
	pi=arr[high]
	for i in range(low,high):
    		if arr[i]<=pi:
    				j+=1
    				arr[j],arr[i]=arr[i],arr[j]
	arr[j+1],arr[high]=arr[high],arr[j+1]
	return j+1
    
        
def quick(arr,low,high) :
	if len(arr)==1:
		return arr
	if low<high:
		pi=partition(arr,low,high)   # pi-1 and pi+1 cuz pivot not include cuz it is already in its correct position
		quick(arr,low,pi-1)
		quick(arr,pi+1,high) 
		
ls= [10, 7, 8, 9, 1, 5]
n = len(ls)
print(quick(ls, 0, n-1))
print("Sorted array is:")
print(ls)
  
ls=[1,3,4,5,6,39,9]



# kth smallest largest---
# # This function returns k'th smallest element
# # in arr[l..r] using QuickSort based method.
# # ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
# import sys

# def kthSmallest(arr, l, r, k):

# 	# If k is smaller than number of
# 	# elements in array
# 	if (k > 0 and k <= r - l + 1):
	
# 		# Partition the array around last
# 		# element and get position of pivot
# 		# element in sorted array
# 		pos = partition(arr, l, r)

# 		# If position is same as k
# 		if (pos - l == k - 1):
# 			return arr[pos]
# 		if (pos - l > k - 1): # If position is more,
# 							# recur for left subarray
# 			return kthSmallest(arr, l, pos - 1, k)

# 		# Else recur for right subarray
# 		return kthSmallest(arr, pos + 1, r,
# 							k - pos + l - 1)

# 	# If k is more than number of
# 	# elements in array
# 	return sys.maxsize

# # Standard partition process of QuickSort().
# # It considers the last element as pivot and
# # moves all smaller element to left of it
# # and greater elements to right
# def partition(arr, l, r):

# 	x = arr[r]
# 	i = l
# 	for j in range(l, r):
# 		if (arr[j] <= x):
# 			arr[i], arr[j] = arr[j], arr[i]
# 			i += 1
# 	arr[i], arr[r] = arr[r], arr[i]
# 	return i

# # Driver Code
# if __name__ == "__main__":
	
# 	arr = [12, 3, 5, 7, 4, 19, 26]
# 	n = len(arr)
# 	k = 3;
# 	print("K'th smallest element is",
# 		kthSmallest(arr, 0, n - 1, k))

# # This code is contributed by ita_c

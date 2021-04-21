
# def findMaxRec(A, n):

# 	# if n = 0 means whole array
# 	# has been traversed
# 	if (n == 1):
# 		return A[0]
# 	return max(A[n - 1], findMaxRec(A, n - 1))

# # Driver Code
# if __name__ == "__main__":
	
# 	A = [1, 4, 45, 6, -50, 10, 2]
# 	n = len(A)
# 	print(findMaxRec(A, n))


# # Recursive python 3 program to
# # find minimum

# # function to print Minimum element
# # using recursion
# def findMinRec(A, n):
	
# 	# if size = 0 means whole array
# 	# has been traversed
# 	if (n == 1):
# 		return A[0]
# 	return min(A[n - 1], findMinRec(A, n - 1))

# # Driver Code
# if __name__ == '__main__':
# 	A = [1, 4, 45, 6, 50, 10, 2]
# 	n = len(A)
# 	print(findMinRec(A, n))

# # This code is contributed by
# # Shashank_Sharma



def maxx(arr,i,max1):
    if i=len(arr):
        return max1
    
    if arr[i]>max1:
         max1=arr[i]
    maxx(arr,i+1,max1)

print(maxx([1,2,3],0,-1))
def SubArraySum(arr, n ):
	result = 0
	for i in range(0, n):
		result += (arr[i] * (i+1) * (n-i))

	return result
arr = [1, 2, 3]
n = len(arr)
print ("Sum of SubArray : ",
	SubArraySum(arr, n))

 

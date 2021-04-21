#sum of all unique subarray sum
#very easy very 

def findSubarraySum(arr, n):

	res = 0

	# Go through all subarrays, compute sums
	# and count occurrences of sums.
	m = dict()
	for i in range(n):
		Sum = 0
		for j in range(i, n):
			Sum += arr[j]
			m[Sum] = m.get(Sum, 0) + 1
		
	# Print all those Sums that appear
	# once.
	for x in m:
		if m[x] == 1:
			res += x

	return res

# Driver code
arr = [3, 2, 3, 1, 4]
n = len(arr)
print(findSubarraySum(arr, n))



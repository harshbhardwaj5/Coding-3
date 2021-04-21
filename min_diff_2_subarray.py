# Python3 program for the above approach
import sys
# bro bahut simple h bro bahut karke dhekna logic 
# Function to return minimum difference
# between sum of two subarrays
def minDiffSubArray(arr, n):
	
	# To store total sum of array
	total_sum = 0

	# Calculate the total sum
	# of the array
	for i in range(n):
		total_sum += arr[i]

	# Stores the prefix sum
	prefix_sum = 0

	# Stores the minimum difference
	minDiff = sys.maxsize

	# Traverse the given array
	for i in range(n - 1):
		prefix_sum += arr[i]

		# To store minimum difference
		diff = abs((total_sum -prefix_sum) -prefix_sum)

		# Update minDiff
		if (diff < minDiff):
			minDiff = diff

	# Return minDiff
	return minDiff

# Driver code
	
# Given array
arr = [ 7, 9, 5, 10 ]

# Length of the array
n = len(arr)

print(minDiffSubArray(arr, n))

# This code is contributed by code_hunt

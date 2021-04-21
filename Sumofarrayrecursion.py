# Python program to find sum of array
# elements using recursion.


def _findSum(arr):
	if len(arr)== 1:
		return arr[0]
	else:
		return arr[0]+_findSum(arr[1:])

arr =[]
# input values to list
arr = [1, 2, 3, 4, 5]

N = len(arr)

ans =_findSum(arr)
print (ans)


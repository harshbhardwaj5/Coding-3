# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
	largest = i # Initialize largest as root
	# print(arr[i])
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)




def heapSort(arr):
	n = len(arr)
	# Build a maxheap.
	for i in range(n//2 - 1, -1, -1):
    		
		heapify(arr, n, i)
	
	# One by one extract elements
	
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)
	


class Solution:
  
        def heapify(arr,n,i):
            lar=i 
            l=2*i+1 
            r=2*i+2 

            if l<n and arr[l]>arr[lar]:
                lar=l 
            if r<n and arr[r]>arr[lar]:
                lar=r 
            if lar!=i :
                arr[lar],arr[i]=arr[i],arr[lar]
                heapify(arr,n,lar)

        def heapsort(arr):	
            n=len(arr)
            for i in range(n//2 - 1, -1, -1):
                 heapify(arr, n, i)
            for j in range(n-1, 0, -1):
                arr[0],arr[j]=arr[j],arr[0]
                heapify(arr, j, 0)
            return arr
       		 
# Driver code
arr = [ 1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17 ]
heapSort(arr)
n = len(arr)
print("Sorted array is")

for i in range(n):
	print("%d" % arr[i]),


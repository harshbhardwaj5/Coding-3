def isSubsetSum(set, n, sum):
	
	
	subset =([[False for i in range(sum + 1)]
			for i in range(n + 1)])
	
	                                        
	for i in range(n + 1):              # If sum is 0, then answer is true
		subset[i][0] = True
		
                                           
	for i in range(1, sum + 1):              # If sum is not 0 and set is empty,
                                            # then answer is false
		subset[0][i]= False
			
	
	for i in range(1, n + 1):
		for j in range(1, sum + 1):
			if j<set[i-1]:
				subset[i][j] = subset[i-1][j]
			if j>= set[i-1]:
				subset[i][j] = (subset[i-1][j] or subset[i - 1][j-set[i-1]])
	
	# uncomment this code to print table
	# for i in range(n + 1):
	#     for j in range(sum + 1):
	#         print (subset[i][j], end =" ")
	#         print()
	return subset[n][sum]
		

if __name__=='__main__':
	set = [3, 34, 4, 12, 5, 2]
	sum = 9
	n = len(set)
	if (isSubsetSum(set, n, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")


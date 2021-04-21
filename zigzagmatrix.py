# Program to print matrix in Zig-zag pattern

matrix =[
			[ 1, 2, 3,],
			[ 4, 5, 6 ],
			[ 7, 8, 9 ],
		]
rows=3
columns=3
	
solution=[[] for i in range(rows+columns-1)]

for i in range(rows):
	for j in range(columns):
		sum=i+j
		if(sum%2 ==0):

			#add at beginning
            
			solution[sum].insert(0,matrix[i][j])    #explained in video first insert [1]->[2,1]->[3,2,1]
            
		else:

			#add at end of the list
			solution[sum].append(matrix[i][j])     #explained in video at last insert [1]->[1,2]->[1,2,3]
		
print(solution)			
# print the solution as it as
for i in solution:
	for j in i:
		print(j,end=" ")
		

	

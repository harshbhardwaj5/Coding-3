# tower of hanoi

def TowerOfHanoi(n , source, destination, auxiliary):             #https://www.youtube.com/watch?v=q6RicK1FCUs
	if n==1:
		print ("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
		
#sd->sa->ad

n = 4
TowerOfHanoi(n,'A','B','C')


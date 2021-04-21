# Python3 program to find the maximum depth of tree
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node
def maxDepth(node):
	if node is None:
		return 0 ;            #not 1 bro zero try recuring it has to zero

	return 1+max(maxDepth(node.left),maxDepth(node.right))


root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print ("Height of tree is %d" %(maxDepth(root)))


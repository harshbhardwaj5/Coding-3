# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert
# a new node with the given key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	
	return root

# A utility function to do inorder tree traversal
# A utility function to search a given key in BST
def search(root,key):
	
	# Base Cases: root is null or key is present at root
	if root is None or root.val == key:
		return root

	# Key is greater than root's key
	if root.val < key:
		return search(root.right,key)

	# Key is smaller than root's key
	return search(root.left,key)
def minnode(n):
    while n.left!=None:
        n=n.left 
    return n

def deletenode(root,key):
        if root==None:
            return root 
        
        if root.val>key:
            root.left=deletenode(root.left,key)
        elif root.val<key:
            root.right=deletenode(root.right,key)
        
        else:
            if root.left==None:
                temp=root.right
                root.right=None
                return temp 
            elif root.right==None:
                temp=root.left
                root.left=None
                return temp 
            temp=minnode(root.right)
            root.val=temp.val
            root.right=deletenode(root.right,temp.val)

   


            # temp=minnode(root.right)
            # root.val=temp.val

            # deletenode(root.right,temp.key)
        # return root

def sumleavenode(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return root.val
    else:
       
        return sumleavenode(root.left)+sumleavenode(root.right)  #for counting and summation of leaf node
      
        # print(leavenode(root.left))                     #for printing leaf nodes
        # print(leavenode(root.right))
            
def zigzagLevelOrder( root) :
        res = []
        q = []
        level = 0
        if not root:
            return res
        q.append(root)
        
        while q:
            size = len(q)
            sublist = []
            for i in range(size):
                node = q[i]
                sublist.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
               
                if level % 2 != 0:
                    sublist.reverse()
                
                for i in range(len(sublist)):
                        res.append(sublist[i])
                 
            # res.append(sublist)
            level += 1
            
            q = q[size:]
            
        return res
     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
           
        
    #     if p.val > root.val and q.val > root.val:
    #        return  self.lowestCommonAncestor(root.right, p, q)
                
    #     if p.val < root.val and q.val < root.val:
    #      return self.lowestCommonAncestor(root.left, p, q)
        
    #     return root
    									
def bstfromarr(arr):
    if not arr:
        return None

    mid=len(arr)//2
    root=Node(arr[mid])

    root.left=bstfromarr(arr[:mid])
    root.right=bstfromarr(arr[mid+1:])

    return root

def maxheight(root) :      
    if root==None:          
        return 0
    return 1+max(maxheight(root.left),maxheight(root.right))
        
        
def levelOrder(root):
        
        queue = []
        queue.append(root)
        while(len(queue)>0):
            node = queue.pop(0)
            print( node.info),
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)          


# def invert(root):
#             if root==None:
#                 return root
#             invert(root.left)
#             invert(root.right)
            
#             root.left,root.right=root.right,root.left
            
            
            
#         invert(root)
#         return root
        
def inorder(root,maxx=0):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
# 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80

r = Node(30) 

 
 
r = insert(r, 40)

r = insert(r, 20)



# inorder(r)
b=(search(r,30))

deletenode(r,4)

print("ZIg Zag Traversal is",zigzagLevelOrder(r))

rr=bstfromarr([1,2,3,4,5])
inorder(rr)
print("The max depth of b tree is ",maxheight(r))
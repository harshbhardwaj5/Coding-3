def check_binary_search_tree_(root):
    if root==None:
        return
    if root.left!=None:
        if root.left.data>root.data :
            return False
    if root.right!=None:
        if root.right.data<root.data:
            return False 
    return  check_binary_search_tree_(root.left)
    return  check_binary_search_tree_(root.right)
    return True
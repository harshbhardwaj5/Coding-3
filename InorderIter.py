def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root,ls):
            stack=[]
            
            curr=root
            
            while True:
                if curr!=None:
                    stack.append(curr)
                    curr=curr.left
                elif curr==None and stack:
                    
                    curr=stack.pop()
                    ls.append(curr.val)
                    curr=curr.right
                else:
                    break
            return ls  
        return inorder(root,[])


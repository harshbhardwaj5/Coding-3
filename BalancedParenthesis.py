if 2>1:
            stack = []
    
        # Traversing the Expression
            for char in s:
                if char in ["(", "{", "["]:

                    # Push the element in the stack
                    stack.append(char)
                    
                else:
                    if not stack: # or if stack==[] we can also write
                        return False
                    s=stack.pop()
                    if s=='(' and char!=')' or s=='{' and char!='}' or s=="[" and char!="]":
                            return False
                        
            if stack:
                return False  #stack is still filled
            return True    #now stack is empty
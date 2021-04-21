class Node:
    def __init__(self,data):
        self.data=data 
        self.right=None
        self.left=None 


class dll:
    def __init__(self):
        self.head=None 




    def addbeg(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode 
        else:
            
            newnode.right=self.head 
            self.head.left=newnode
            self.head=newnode



    def addend(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode 
        else:
            n=self.head 
            while(n.right!=None):
                n=n.right 
            n.right=newnode 
            newnode.left=n



    def print_LL(self):
            if self.head is None:
                 print("Linked List is empty!")
            else:
                n = self.head
                while n is not None:
                    print(n.data)
                    n = n.right



    def anyloc(self,data,x):
        n=self.head 
       
        while n.data!=x  :
            n=n.right 
        newnode=Node(data)
        newnode.right=n.right
        n.right.left=newnode 
        newnode.left=n
        
        n.right=newnode
        






c=dll()
h=dll()
h.addbeg(4)
h.addbeg(9)
h.addend(5)
h.anyloc(0,9)
h.print_LL()


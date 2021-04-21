class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 

class linkedlist:
    def __init__(self):
        self.head=None 
        self.next=None
    def printll(self):
        if self.head==None:
            print("empty linked list")

        else:
            print("Our L. List is----")
            c=0
            n=self.head
            while n is not None:
                if c%2==0:
                    print(n.data)
                c+=1
                n=n.next 

    def addbeg(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    

    def addend(self,data):
        newnode=node(data)

        if self.head==None:
            self.head=newnode 
        else:
            n=self.head
            while n.next!=None:   #this is imp n.next not ( n )
                n=n.next 
            n.next=newnode 
    
    def addmiddle(self,data,x):
        n=self.head 
        while n.data!=x  :
            n=n.next 
        newnode=node(data)
        newnode.next=n.next 
        n.next=newnode


    def looplinkedlist(self):
        slow=self.head
        fast=self.head
        while(slow and fast and fast.next):
            slow=slow.next 
            fast=fast.next.next 
            if slow==fast:
                return True
        return False
    #     # slow=self.head
    #     # fast=self.head 
        # while(slow and fast and fast.next):
        #     slow=slow.next 
        #     fast=fast.next.next 
        #     if slow==fast:        
        #         slow=self.head
        #         while(slow!=fast):
        #             slow=slow.next
        #             fast=fast.next 
        #         return slow
        # return False 
     
        
   

    def reversell(self):     #O(n)
        curr=self.head
        prev=None
        while curr!=None:
            nex=curr.next
            curr.next=prev 
            prev=curr 
            curr=nex
        self.head=prev 

    def lllenght(self):                 #go till last node and add values 
        n=self.head 
        c=0
        while n!=None:
            c+=1 
            n=n.next
        return c

    def lldeleteend(self):
        n=self.head 
        while n.next!=None:
            if n.next.next==None:
                n.next=None
            else:
                n=n.next 
                
            
    def isPalindrome(self):
        fast = slow = self.head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        n=self.head
        
        while node: # while node and head:
            if node.data != n.data:
                return False
            node = node.next
            n = n.next
        return True

    def llmiddlefind(self):
        slow=fast=self.head 
        while fast and  fast.next:
            fast=fast.next.next
            slow=slow.next 
        return slow.data


    def removeNthFromNth(self,n):
        dummyhead=node(0)
        dummyhead.next=self.head
        fast=dummyhead
        slow=dummyhead
        for i in range(n):
            fast=fast.next
          
        while(fast.next !=None):
            fast=fast.next 
            slow=slow.next
        slow.next=slow.next.next
        return dummyhead.next

     
    def mergeTwoLists(self, l1, l2):         #O(m+n) time complexity & space also due to rec call satck
     
        ## Base cases aka stop condition       #https://www.youtube.com/watch?v=bdWOmYL5d1g for refrence 
        
        if not l1 and not l2:
            # both l1 and l2 are empty list
            return None
        
        elif not l1:
            # l1 is empty, directly return l2
            return l2
        
        elif not l2:
            # l2 is empty, directly return l1
            return l1
        
        
        ## General cases
        # Compare node value and merge
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


n=linkedlist()
n.addbeg(1)

n.addbeg(1)
n.addbeg(2)
# n.head.next.next = n.head
p=linkedlist()

# n.reversell()
# n.printll()
# print("middle element is ->" +str (n.llmiddlefind()))

# #print(n.lllenght())
print(n.isPalindrome())
print("------------enter the position from end to remove----")

n.printll()

class stack:
    def __init__(self):
        self.top=-1 
        self.stack=[0]*3



    def push(self,val):
       self.top+=1 
      
       self.stack[self.top]=val

    def pop(self):
        s=self.stack[self.top]
        self.top=self.top-1 
        return s


def push(val,stack1):
        stack1.append(val)
def pop1(stack1,stack2):
    for i in stack1[::-1]:
        stack2.append(i)
    print(stack1.pop())
           
def queueusingstack(val):
        stack1=[]
        stack2=[]
       
        push(val,stack1)
        pop1(stack1,stack2)



s=stack()

s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
print(s.pop())

queueusingstack(2)
queueusingstack(3)
queueusingstack(4)
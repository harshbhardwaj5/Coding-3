# The Stock Span Problem 

# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate 
# span of stock’s price for all n days. 
# The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day,
#  for which the price of the stock on the current day is less than or equal to its price on the given day. 
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
#  then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6} 


class StockSpanner(object):
    
    def __init__(self):
        self.stack = [] 
        self.ls=[]
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while self.stack and self.stack[-1][0] <= price:
           res+= self.stack.pop()[1]
                                             #[1] means index will pop off if stack[0] means if [100,2] 100 will pop of stack[1]->2 will pop off
        self.stack.append([price, res])
        self.ls.append(res)
       # print(self.stack)
        return res


s=StockSpanner()
for i in [100, 80, 60, 70, 60, 75, 85]:
    print(s.next(i))
print(s.ls)
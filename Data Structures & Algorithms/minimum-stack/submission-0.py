class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        #.minimum=float("inf")

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

        #self.stack.append("null")
        
    def pop(self):
        self.min_stack.pop()
        self.stack.pop()


    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
#obj = MinStack()
#for 
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
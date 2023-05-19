# approach: maintain an adjacent stack that stores the mins at each node
# in the stack

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        if self.stack:
            if val < self.mins[-1]:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)
        
        self.stack.append(val)
        
    def pop(self):
        """
        :rtype: None
        """
        
        self.stack.pop()
        self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
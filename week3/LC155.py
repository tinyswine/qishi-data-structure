class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = []
        self.min_container = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.container.append(x)
        if self.min_container:
            self.min_container.append(min(self.min_container[-1], x))
        else:
            self.min_container.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.min_container.pop()
        self.container.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.container:
            return self.container[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_container:
            return self.min_container[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
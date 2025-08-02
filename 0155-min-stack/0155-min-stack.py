class MinStack:

    def __init__(self):
        self.res=[]
        self.min=[] 
    def push(self, val: int) -> None:
        self.res.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
    def pop(self) -> None:
        val = self.res.pop()
        if val == self.min[-1]:
            self.min.pop()
    def top(self) -> int:
        num = len(self.res)
        return self.res[num-1]
    def getMin(self) -> int:
        return self.min[-1]
    
        # self.push = push(val)
        # self.pop = pop()
        # self.top = top()
        # self.getMin = getMin()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
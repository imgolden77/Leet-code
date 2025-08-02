class MinStack:

    def __init__(self):
        self.res=[]
        self.output=[]
    def push(self, val: int) -> None:
        self.res.append(val)
        # self.output.append("null")
    def pop(self) -> None:
        self.res.pop()
        # self.output.append("null")
    def top(self) -> int:
        num = len(self.res)
        return self.res[num-1]
    def getMin(self) -> int:
        return min(self.res)
    
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
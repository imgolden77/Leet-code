class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        res= [0]*len(temperatures)
        for i in range(len(temperatures)):  
            if stack == []:
                stack.append(i)
            elif temperatures[i]<= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]]= i-stack[-1]
                    stack.pop()
                    if stack ==[]:
                        break
                stack.append(i)
        return res

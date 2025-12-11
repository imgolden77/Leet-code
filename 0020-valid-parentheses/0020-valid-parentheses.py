class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        former= ['(', '{', '[']
        
        for i in s:
            if i in former:
                stack.append(i)
            elif i == ')':
                if stack== []:
                    return False
                elif stack[-1]== '(':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if stack== []:
                    return False
                elif stack[-1]== '{':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                print(stack)
                if stack == []:
                    return False
                elif stack[-1]== '[':
                    stack.pop()
                else:
                    return False
            
        
        if stack == []:
            return True
        else:
            return False